import os
import json
from playwright.sync_api import sync_playwright
from itertools import combinations

def main():
    #sub_sets_of_perms = []
    #for i in range(len(permissions) + 1):
    #    t = combinations(permissions, i)
    #    for item in t:
    #        sub_sets_of_perms.append(list(item))

    i = 0
    with open("output.json", "x") as f:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            for ua in user_agents:
                i += 1
                print("Progress: " + str(round(i/len(user_agents), 3)))
                for lc in locales:
                    for perms in permissions:
                        res = None
                        try:
                            page = browser.new_page(user_agent=ua, locale=lc, permissions=[perms])
                            page.goto("file://" + abs_path)
                            page.wait_for_selector("#fingerprint")
                            res = page.locator("#fingerprint").text_content()
                        except:
                            pass
                        finally: 
                            f.write(json.dumps({"user_agent": ua, "locale" : lc, "permissions":perms, "hash": res})+ '\n')
            browser.close()

abs_path = os.path.abspath("../index.html")
    
        



#-----------------------------------------
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
"screen-wake-lock",
"top-level-storage-access",
"window-management"
]


if __name__ == "__main__":
    main()