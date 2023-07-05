from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os

# Choose a browser and set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
PATH = "C:\Users\ay912\Downloads\project\.venv\img132121"
# Navigate to the webpage containing the image
driver.get("https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
os.mkdir(PATH)
# Locate the image element
image_element = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div/div/img')
image_name = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/a[1]')


# Extract the URL of the image
image_url = image_element.get_attribute("src")
image_n =image_name.text
print (image_n)
# Download the image
urllib.request.urlretrieve(image_url, "/img132121/"+image_n +".jpg")

# Close the browser
driver.quit()
