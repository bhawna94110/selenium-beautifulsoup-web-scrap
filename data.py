from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get('https://weworkremotely.com/remote-jobs/pixbuffer-software-inc-full-stack-developer-strong-python-and-django').text

# source = requests.get('https://weworkremotely.com/remote-jobs/opencraft-senior-open-source-developer-devops-python-django-react-aws-openstack').text

source = requests.get('https://weworkremotely.com/remote-jobs/pixbuffer-software-inc-full-stack-developer-strong-python-and-django').text


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