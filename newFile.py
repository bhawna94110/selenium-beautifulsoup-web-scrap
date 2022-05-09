import time
import os
import pandas
from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r"D:/Bhawana/Scrapping Data/IndeedData"
driver = webdriver.Chrome()
driver.get("https://weworkremotely.com/remote-jobs/search?term=&button=")
driver.implicitly_wait(30)

what = driver.find_element_by_id("search--input")

what.send_keys('python developer')
driver.implicitly_wait(30)

search_button = driver.find_element_by_id('post-job-cta').click()
# search_button.click()
driver.implicitly_wait(30)

# job_search = driver.find_element_by_link_text("Full Stack Developer (strong Python and Django)").get_attribute("href")
# job_search.click()

job_search = driver.find_element_by_class_name("title")
job_search.click()
driver.current_url
# print(job_search)
# source = job_search.click()
# for c in job_search:
#     c.click()
# driver.implicitly_wait(30)

#==================================================================================================================
source = requests.get(driver.current_url).text
soup = BeautifulSoup(source, 'lxml')

# csv_file = open('data.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Title', 'Description', 'Job Type', 'Company Name', 'Website', 'Logo', 'Country', 'City', 'External URL'])

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

# logo = soup.find('div', class_='listing-logo').img.get('src')
country = soup.find('div', class_='company-card').h3.text

print(f'''
Title: {job_title}
Description: {job_description}
Job Type: {job_type}
Company Name: {company_name}
External URL: {external_url}
Logo: {logo}
Country: {country}
''')



# csv_writer.writerow([job_title, job_description, url])
# csv_file.close()

# print(job.prettify())

