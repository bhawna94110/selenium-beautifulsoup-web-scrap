import time
import os
import pandas
from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions  


os.environ['PATH'] += r"D:/Bhawana/Scrapping Data/IndeedData"
driver = webdriver.Chrome()
driver.get("https://weworkremotely.com/remote-jobs/search?term=&button=")
driver.implicitly_wait(30)

what = driver.find_element_by_id("search--input")
what.send_keys('digital marketing')
driver.implicitly_wait(30)

search_button = driver.find_element_by_id('post-job-cta').click()
driver.implicitly_wait(30)

l_list = []
job_search = driver.find_elements_by_class_name("title")
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
for i in range(0, len(job_search)):
    try:
        if job_search[i].is_displayed():
            job_search[i].click()
            l_list.append(driver.current_url)
            driver.back()
            # print(driver.current_url)
    except exceptions.StaleElementReferenceException as e:
        # print(e)
        job_search = driver.find_elements_by_class_name("title")
        job_search[i].click()
        # print(driver.current_url)
        l_list.append(driver.current_url)
        driver.back()
        pass  
#==================================================================================================================
for i in l_list:
    source = requests.get(i).text
    soup = BeautifulSoup(source, 'lxml')

    job = soup.find('div', class_='content')
    job_title = job.h1.text
    job_description = soup.find('div', class_='listing-container').text
    job_type = soup.find('span', class_="listing-tag").text
    company_name = job.h2.a.text.replace(' ','')
    external_url = soup.find("a",{"id":"job-cta-alt"}).get("href")

    try: 
        logo = soup.find('div', class_='listing-logo').img.get('src')
    except:
        print('No element with this class name found...')
    country = soup.find('div', class_='company-card').h3.text

    with open('data.csv', 'w', newline='', encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Title', 'Description', 'Job Type', 'Company Name', 'Logo', 'Country', 'External URL'])
        for i in range(len(l_list)):
            csv_writer.writerow([job_title, job_description, job_type, company_name, logo, country, external_url])
        f.close()


