from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        "linkedin_profile",
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    keywords = [
        "JAVA DEVELOPER C2C",
        "BUSINESS ANALYST C2C",
        "PROJECT MANAGER C2C",
        "DATA ANALYST C2C"
    ]

    all_data = []

    for keyword in keywords:
        print("\nSearching:", keyword)

        # Open search page
        url = "https://www.linkedin.com/search/results/content/?keywords=" + keyword.replace(" ", "%20")
        page.goto(url)

        page.wait_for_timeout(5000)

        # Click Posts filter
        try:
            page.click("text=Posts")
        except:
            print("Posts button not found, continuing anyway")

        page.wait_for_timeout(5000)

        # SCRAPING POSTS
        posts = page.locator("div.feed-shared-update-v2")
        count = posts.count()

        print("Posts found:", count)

        for i in range(count):
            post = posts.nth(i)

            try:
                text = post.inner_text()

                # extract email
                emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
                email = emails[0] if emails else None

                # extract link
                link = None
                try:
                    link = post.locator("a").first.get_attribute("href")
                except:
                    pass

                data = {
                    "keyword": keyword,
                    "text": text,
                    "email": email,
                    "link": link
                }

                all_data.append(data)

                print("\n--- POST ---")
                print("Email:", email)
                print("Link:", link)

            except:
                print("Error reading post", i)

    print("\nDONE. Total posts collected:", len(all_data))

    import pandas as pd

    df = pd.DataFrame(all_data)
    df.to_csv("linkedin_results.csv", index=False)

    print("Data saved to linkedin_results.csv")

    input("Press Enter to exit...")
    context.close()