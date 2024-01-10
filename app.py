from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

keywords = [
        "flutter",
        "next.js",
        "kotlin"
    ]


class JobScrap:

    all_jobs_db = []

    def __init__(self, keyword):
        self.type = keyword

    def scrap(self):
        self.jobs_db = []
        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False)
        #browser 만들기

        page = browser.new_page()
        # 새 탭 실행

        page.goto(f"https://www.wanted.co.kr/search?query={self.type}&tab=position")

        for x in range(5):
            time.sleep(5)
            page.keyboard.down("End")


        content = page.content()

        p.stop()

        soup = BeautifulSoup(content, "html.parser")

        jobs = soup.find_all("div", class_="JobCard_container__FqChn")

        
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
            self.jobs_db.append(job_data)
            JobScrap.all_jobs_db.append(job_data)
    def create_file(self):

        file = open(f"{self.type}_jobs.csv", mode="w", encoding="utf-8")

        writer = csv.writer(file)
        writer.writerow(["Title",
                        "Company", 
                        "Location", 
                        "Reward", 
                        "Link"]
                        )
        writer.writerow(["This", "is", self.type, "Jobs", len(self.jobs_db)])

        for job in self.jobs_db:
            writer.writerow(job.values())
        file.close()

    def see_all_jobs(self):
        file = open(f"all_jobs.csv", mode="w", encoding="utf-8")

        writer = csv.writer(file)
        writer.writerow(["Title",
                        "Company", 
                        "Location", 
                        "Reward", 
                        "Link"]
                        )
        writer.writerow(["This", "is", "All", "Jobs", len(JobScrap.all_jobs_db)])

        for job in JobScrap.all_jobs_db:
            writer.writerow(job.values())
        file.close()


flutter = JobScrap(keywords[0])
flutter.scrap()
flutter.create_file()

nextjs = JobScrap(keywords[1])
nextjs.scrap()
nextjs.create_file()

kotlin = JobScrap(keywords[2])
kotlin.scrap()
kotlin.create_file()

flutter.see_all_jobs()
