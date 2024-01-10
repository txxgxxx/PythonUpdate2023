from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
#browser 만들기

page = browser.new_page()
# 새 탭 실행

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")
# 첫 번째 argument가 url, positional argument를 사용한 것

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

# time.sleep(5)

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")


content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job_data = {
        "title": title,
        "company_name": company_name,
        "location": location,
        "reward": reward,
        "link": link
    }
    jobs_db.append(job_data)

print(jobs_db)
print(len(jobs_db))