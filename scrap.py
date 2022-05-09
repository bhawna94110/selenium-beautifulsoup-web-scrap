import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"D:/Bhawana/Scrapping Data/IndeedData"
driver = webdriver.Chrome()
driver.get("https://in.indeed.com/?from=gnav-jobsearch--jasx")
driver.implicitly_wait(30)

what = driver.find_element_by_id('text-input-what')  #class 'icl-TextInput-control icl-TextInput-control--withIconRight'
driver.implicitly_wait(30)
where = driver.find_element_by_id('text-input-where')

# try: 
#     no_button = driver.find_element_by_class_name('icl-CloseButton')
#     no_button.click()
# except:
#     print('No element with this class name found...')

# job search button class 'yosegi-InlineWhatWhere-primaryButton'
# popover-x-button-close icl-CloseButton

what.send_keys('python developer')
driver.implicitly_wait(30)
where.send_keys('work from home')

search_button = driver.find_element_by_class_name('yosegi-InlineWhatWhere-primaryButton')
search_button.click()

try: 
    no_button = driver.find_element_by_class_name('icl-CloseButton')
    no_button.click()
except:
    print('No element with this class name found...')