#!/usr/bin/env python3
"""
自动将巴厘岛行程地点保存到 Google Maps "巴厘岛" 收藏列表
通过 CDP 连接到已运行的 Chrome（端口 9222）
"""

import time
import random
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

PLACES = [
    # D0 雅加达
    ("Digital Airport Hotel Terminal 3 Soekarno Hatta", "D0 · 胶囊酒店"),
    ("Soekarno Hatta International Airport Terminal 3", "D0 · 雅加达 T3"),
    ("Soekarno Hatta International Airport Terminal 2", "D0 · 雅加达 T2"),
    # D1 仓古
    ("Amandaya Canggu Bali",                             "D1-D4 · 入住酒店"),
    ("Batu Bolong Beach Canggu Bali",                    "D1 · 冲浪海滩"),
    ("Hungry Bird Coffee Canggu Bali",                   "D1 · 早餐咖啡"),
    ("Deus Ex Machina Canggu Bali",                      "D1 · 咖啡/摩托圣地"),
    ("Pretty Poison Canggu Bali",                        "D1 · 网红泳池酒吧"),
    ("La Brisa Bali",                                    "D1 · 海边日落餐厅"),
    ("Old Man's Canggu Bali",                            "D1 · 仓古经典酒吧"),
    ("The Lawn Canggu Beach Club",                       "D1 · 草坪沙滩俱乐部"),
    ("Tanah Lot Temple Bali",                            "D1 · 海神庙日落"),
    # D2 乌布
    ("Tegalalang Rice Terrace Ubud Bali",                "D2 · 梯田"),
    ("Tirta Empul Temple Bali",                          "D2 · 圣泉寺"),
    ("Sacred Monkey Forest Sanctuary Ubud",              "D2 · 猴林"),
    ("Ubud Royal Palace Bali",                           "D2 · 乌布王宫"),
    ("Ibu Oka Ubud Bali",                                "D2 · 烤猪饭"),
    ("Clear Cafe Ubud Bali",                             "D2 · 素食健康餐"),
    ("Warung Biah Biah Ubud",                            "D2 · 本地印尼菜"),
    # D3 乌鲁瓦图
    ("Single Fin Uluwatu Bali",                          "D3 · 悬崖餐厅酒吧"),
    ("Suluban Beach Uluwatu Bali",                       "D3 · 蓝点海滩"),
    ("Uluwatu Temple Bali",                              "D3 · 乌鲁瓦图寺"),
    ("Jimbaran Bay Seafood Bali",                        "D3 · 金巴兰海鲜"),
    # D4 仓古告别
    ("Crate Cafe Canggu Bali",                           "D4 · 早午餐"),
    ("The Slow Canggu Bali",                             "D4 · 告别晚餐"),
    ("The Shady Shack Canggu Bali",                      "D4 · 素食网红"),
    ("Bintang Supermarket Canggu Bali",                  "D4 · 纪念品超市"),
    ("Mal Bali Galeria",                                 "D4 · 购物商场"),
    ("Ngurah Rai International Airport Bali",            "D4 · 巴厘岛机场"),
    # D5 雅加达
    ("Monas National Monument Jakarta",                  "D5 · 独立纪念碑"),
    ("Grand Indonesia Mall Jakarta",                     "D5 · 购物中心"),
]

LIST_NAME = "巴厘岛"


def random_delay(min_s=2.0, max_s=4.0):
    time.sleep(random.uniform(min_s, max_s))


def wait_for_login(page, timeout_sec=120):
    """等待用户在 Chrome 窗口中完成 Google 登录"""
    print("\n🔐 请在弹出的 Chrome 窗口中登录 Google 账户...")
    print("   （脚本将等待最多 2 分钟）\n")
    page.goto("https://accounts.google.com/signin", timeout=30000)
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        time.sleep(3)
        url = page.url
        # 登录成功后会跳转到 myaccount 或 google.com
        if "myaccount.google.com" in url or (
            "google.com" in url and "signin" not in url and "accounts" not in url
        ):
            print("✅ 登录成功！")
            return True
        # 检查是否在 Google Maps 页面（直接复用了已登录状态）
        content = page.content()
        if '"isSignedIn":true' in content or 'data-email' in content:
            print("✅ 已检测到登录状态！")
            return True
    print("⚠️  等待超时，仍未检测到登录")
    return False


def save_place(page, search_query, note):
    """搜索一个地点并保存到指定收藏列表"""
    print(f"\n  🔍 {note} — {search_query}")

    try:
        encoded = search_query.replace(" ", "+")
        page.goto(f"https://www.google.com/maps/search/{encoded}", timeout=30000)
        random_delay(2.5, 4)

        # ── 寻找 Save 按钮 ──────────────────────────────────────────
        save_selectors = [
            'button[data-value="Save"]',
            'button[jsaction*="save"]',
            'button[aria-label="Save"]',
            'button[aria-label*="Save"]',
        ]

        save_btn = None
        for sel in save_selectors:
            try:
                btn = page.locator(sel).first
                btn.wait_for(timeout=5000, state="visible")
                save_btn = btn
                break
            except PWTimeout:
                continue

        if save_btn is None:
            # 尝试点击列表页第一个结果
            try:
                first = page.locator('a[href*="/maps/place/"]').first
                first.wait_for(timeout=6000)
                first.click()
                random_delay(2, 3)
                for sel in save_selectors:
                    try:
                        btn = page.locator(sel).first
                        btn.wait_for(timeout=5000, state="visible")
                        save_btn = btn
                        break
                    except PWTimeout:
                        continue
            except PWTimeout:
                pass

        if save_btn is None:
            print(f"  ⚠️  找不到 Save 按钮，跳过")
            page.screenshot(path=f"/tmp/maps_fail_{search_query[:20].replace(' ','_')}.png")
            return False

        # ── 点击 Save ───────────────────────────────────────────────
        save_btn.click()
        random_delay(1.5, 2.5)

        # ── 在对话框中找「巴厘岛」──────────────────────────────────
        list_found = False

        try:
            item = page.get_by_text(LIST_NAME, exact=True).first
            item.wait_for(timeout=5000, state="visible")
            item.click()
            list_found = True
        except PWTimeout:
            pass

        if not list_found:
            try:
                item = page.locator(f'[aria-label*="{LIST_NAME}"]').first
                item.wait_for(timeout=3000, state="visible")
                item.click()
                list_found = True
            except PWTimeout:
                pass

        if not list_found:
            page.screenshot(path=f"/tmp/maps_dialog_{search_query[:20].replace(' ','_')}.png")
            print(f"  ⚠️  找不到「{LIST_NAME}」列表，截图已保存到 /tmp/")
            page.keyboard.press("Escape")
            return False

        random_delay(1, 1.5)

        # 关闭对话框
        try:
            done = page.get_by_role("button", name="Done").first
            done.wait_for(timeout=2000, state="visible")
            done.click()
        except PWTimeout:
            try:
                page.keyboard.press("Escape")
            except Exception:
                pass

        print(f"  ✅ 已保存到「{LIST_NAME}」")
        return True

    except Exception as e:
        print(f"  ❌ 异常: {e}")
        try:
            page.keyboard.press("Escape")
        except Exception:
            pass
        return False


def main():
    saved = []
    failed = []

    with sync_playwright() as pw:
        print("🔗 通过 CDP 连接到 Chrome (localhost:9222)...")
        browser = pw.chromium.connect_over_cdp("http://localhost:9222")

        contexts = browser.contexts
        if contexts and contexts[0].pages:
            page = contexts[0].pages[0]
        else:
            context = browser.new_context()
            page = context.new_page()

        page.set_viewport_size({"width": 1280, "height": 900})

        # ── 检查登录状态 ────────────────────────────────────────────
        print("🗺  检查 Google 登录状态...")
        page.goto("https://www.google.com/maps", timeout=30000)
        random_delay(3, 4)

        # 检测是否已登录：看页面是否有账户相关元素
        logged_in = False
        try:
            # 已登录时 Maps 右上角有头像按钮
            avatar = page.locator('img[src*="googleusercontent.com"]').first
            avatar.wait_for(timeout=5000)
            logged_in = True
            print("✅ 检测到已登录 Google 账户！")
        except PWTimeout:
            pass

        if not logged_in:
            # 等待用户手动登录
            logged_in = wait_for_login(page)
            if not logged_in:
                print("❌ 未能完成登录，退出")
                return
            # 登录后返回 Maps
            page.goto("https://www.google.com/maps", timeout=30000)
            random_delay(3, 4)

        print(f"\n开始批量保存 {len(PLACES)} 个地点到「{LIST_NAME}」...\n")

        total = len(PLACES)
        for i, (query, note) in enumerate(PLACES, 1):
            print(f"[{i:02d}/{total}]", end="")
            ok = save_place(page, query, note)
            if ok:
                saved.append(f"{note}: {query}")
            else:
                failed.append(f"{note}: {query}")

            if i % 5 == 0 and i < total:
                print(f"\n  ⏸  休息 6 秒避免限流...")
                time.sleep(6)
            else:
                random_delay(1.5, 3)

        print(f"\n\n{'='*55}")
        print(f"✅ 成功保存: {len(saved)}/{total}")
        print(f"❌ 失败/跳过: {len(failed)}/{total}")
        if failed:
            print("\n❌ 失败列表（请手动在 Google Maps 添加）:")
            for f in failed:
                print(f"  - {f}")
        print(f"{'='*55}")


if __name__ == "__main__":
    main()
