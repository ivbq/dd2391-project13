import os
import json
import itertools
from playwright.sync_api import sync_playwright

# Possible values for browser settings
user_agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
]

locales = [
    "ar-SA",
    "bn-BD",
    "bn-IN",
    "cs-CZ",
    "da-DK",
    "de-DE",
    "el-GR",
    "en-AU",
    "en-CA",
    "en-GB",
    "es-ES",
    "es-MX",
    "es-US",
    "fi-FI",
    "fr-BE",
    "fr-CA",
    "fr-CH",
    "fr-FR",
    "nl-BE",
    "nl-NL",
    "no-NO",
    "sv-SE"
]

timezones = [
    "America/New_York",
    "America/Los_Angeles",
    "America/Chicago",
    "America/Sao_Paulo",
    "America/Argentina/Buenos_Aires",
    "Europe/London",
    "Europe/Paris",
    "Europe/Berlin",
    "Europe/Stockholm",
    "Europe/Moscow",
    "Europe/Istanbul",
    "Asia/Kolkata",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Asia/Seoul",
    "Australia/Sydney",
    "Pacific/Auckland",
    "Pacific/Honolulu"
]

permissions = [
    "background-sync",
    "camera",
    "clipboard-read",
    "clipboard-write",
    "geolocation",
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
                cookies = None
                try:
                    page = browser.new_page(user_agent=ua, locale=lc, timezone_id=tz, permissions=[perms])
                    page.goto("file://" + html_path)
                    page.wait_for_selector("#fingerprint")
                    res = page.locator("#fingerprint").text_content()
                    cookies = page.locator("#cookies").text_content()
                except Exception as e:
                    print(f"Error: {e}")
                finally:
                    page.close()
                    f.write(json.dumps({"user_agent": ua, "locale" : lc, "timezone": tz,"permissions": perms, "cookies": cookies, "hash": res})+ '\n')
            browser.close()


if __name__ == "__main__":
    main()