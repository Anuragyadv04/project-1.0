from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os
import csv

# Initialize the WebDriver
browser = webdriver.Chrome()

# Specify the URL of the target web page
url_1 = 'https://www.flipkart.com/titan-np1802sl06-neo-economy-2019-analog-watch-men/p/itm45476b0c32b0d'
csv_file = 'product_data_a.csv'
PATH = "C:\Users\ay912\Downloads\project\.venv\data"
os.mkdir(PATH)
# Navigate to the URL
browser.get(url_1)
product_elements=soup.select('._13oc-S._1t9ceu')
    # Define the CSV file path
csv_file = 'product_data_a.csv'

    # Open the CSV file in write mode
with open(csv_file, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

        # Write the header row
    writer.writerow(['Title', 'Price'])

        # Iterate over the product elements and extract the data
    
    title = browser.find_element(By.XPATH,'').text.strip()
    price = browser.find_element(By.XPATH,'').text.strip()
    image_element = browser.find_element(By.XPATH, '')
    print(title,price)
        # Write the data to the CSV file
    writer.writerow([title, price])

image_element = browser.find_element(By.XPATH, '')
image_url = image_element.get_attribute("src")
urllib.request.urlretrieve(image_url, PATH +title +".jpg")
# Print a message indicating that the data has been saved to the CSV file
print(f"Data has been saved to {csv_file}.")
    ##Print the HTML content
    ##print(soup.prettify())
    # Define the CSV file path


browser.quit()



