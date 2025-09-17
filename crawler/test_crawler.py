# pip install playwright bs4 lxml
# python -m playwright install chromium

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time, json, re, os, sys

def scrape_cube(URL):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ))
        page = ctx.new_page()
        page.goto(URL, wait_until="networkidle")
        time.sleep(1.5)
        html = page.content()
        browser.close()
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n", strip=True)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_crawler.py $URL")
        sys.exit()
    with open("../tmp/output", "w", encoding="utf-8") as f:
        content = scrape_cube(sys.argv[1])
        f.write(content)