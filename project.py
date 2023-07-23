

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

product_search = input("what do you want to search:")


source1 = "https://www.flipkart.com/"
source2 = "https://www.amazon.in"
source3 = "https://www.croma.com/"


wait_imp = 0
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
CO.add_argument('log-level=3')  
wd = webdriver.Chrome(options=CO)

print("***************************************************************************")
print("                     Starting Program, Please wait .....")
print("***************************************************************************\n")



print("Connecting to Amazon")
wd.get(source2)

search_input = wd.find_element(By.ID, "twotabsearchtextbox")


search_input.send_keys(product_search)


search_input.send_keys(Keys.ENTER)


search_results = wd.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")
first_result_url = search_results.get_attribute("href")


wd.get(first_result_url)
wd.implicitly_wait(wait_imp)
a_price = wd.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[11]/div[17]/div[3]/div[1]/span[2]/span[2]/span[2]")
pr_name = wd.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[3]/div[11]/div[3]/div/h1/span")
product_amazon = pr_name.text
raw_p = a_price.text
print(" ---> Successfully retrieved the price from Amazon \n")
time.sleep(0)



print("Connecting to Flipkart")
wd.get(source1)

try:
    close_button = wd.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
    close_button.click()
except:
    pass

search_box = wd.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys(product_search)
search_box.submit()

wait = WebDriverWait(wd, 10)
first_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='/p/']")))

first_result_url = first_result.get_attribute("href")



wd.get(first_result_url)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product_flipkart = pr_name.text
r_price = f_price.text
print(" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(0)


print("Connecting to Croma")
wd.get(source3)

wait = WebDriverWait(wd, 10)
search_input = wait.until(EC.visibility_of_element_located((By.ID, "searchV2")))
search_input.send_keys(product_search)
search_input.send_keys(Keys.ENTER)

    
first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div[1]/div[2]/div/div/div[3]/ul/li[1]/div/div[2]/div[1]/h3/a")))

first_result_url = first_result.get_attribute("href")

 
wd.get(first_result_url)

wd.implicitly_wait(wait_imp)
c_price = wd.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/div[2]/div[1]/div/span")
pr_name = wd.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/h1")
product_chroma = pr_name.text
raw_c = c_price.text
print(" ---> Successfully retrieved the price from croma \n")
time.sleep(0)

wd.quit()




print("#------------------------------------------------------------------------#")
print("Price for [{}] on flipkart,  ".format(product_flipkart))
print("Price(INR) available at Flipkart is: " + r_price[1:])
print("\n")
print("Price for [{}] on Amazon, ".format(product_amazon))
print("  Price(INR) available at Amazon is: " + raw_p[:8])
print("\n")
print("Price for [{}] on croma, ".format(product_chroma))
print("        Price available at Croma is: " + raw_c[1:7])

 
