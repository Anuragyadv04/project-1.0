from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os
import csv


browser = webdriver.Chrome()


url_2 ='https://www.amazon.in/Titan-Economy-Analog-Dial-Watch-1802SL06/dp/B083ZJGV67/ref=sr_1_1_sspa?keywords=watch&qid=1688066672&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
csv_file = 'product_data_a.csv'
PATH = "C:\Users\ay912\Downloads\project\.venv\data"
##os.mkdir(PATH)

browser.get(url_2)


csv_file = 'product_data_a.csv'


with open(csv_file, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

       
    writer.writerow(['Title', 'Price'])

   
    
    title = browser.find_element(By.XPATH,'').text.strip()
    price = browser.find_element(By.XPATH,'').text.strip()
    image_element = browser.find_element(By.XPATH, '')
    print(title,price)
       
    writer.writerow([title, price])

image_element = browser.find_element(By.XPATH, '')
image_url = image_element.get_attribute("src")
urllib.request.urlretrieve(image_url, PATH +title +".jpg")

print(f"Data has been saved to {csv_file}.")



browser.quit()



