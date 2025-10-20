import os
import json
import itertools
from playwright.sync_api import sync_playwright

# Possible values for browser settings
user_agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
]

locales = [
    "sv-SE"
]

timezones = [
    "Pacific/Auckland",
    "Pacific/Honolulu"
]

permissions = [
    "background-sync",
    "camera",
    "clipboard-read",
    "clipboard-write",
    "local-fonts",
    "microphone",
    "midi",
    "notifications",
    "payment-handler",
]

def main():
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
    html_path = abs_path + "/index.html"
    with open(abs_path + "testing/output.json", "w") as f:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            for i, (ua, lc, tz, perms) in enumerate(itertools.product(user_agents, locales, timezones, permissions)): 
                print("Progress: " + str(round(i/len(user_agents), 3)))
                res = None
                try:
                    page = browser.new_page(user_agent=ua, locale=lc, timezone_id=tz, permissions=[perms])
                    # print("Set configuration...")

                    page.goto("file://" + html_path)
                    # print("Going to page...")

                    page.wait_for_selector("#fingerprint")
                    # print("Select fingerprint element on page...")

                    res = page.locator("#fingerprint").text_content()
                    # print("Get fingerprint content...")

                    cookies = page.locator("#cookies").text_content()
                    # print("Get cookies...")
                except Exception as e:
                    print(f"Error: {e}")
                finally: 
                    page.close()
                    f.write(json.dumps({"user_agent": ua, "locale" : lc, "timezone": tz,"permissions": perms, "cookies": cookies, "hash": res})+ '\n')
            browser.close()


if __name__ == "__main__":
    main()