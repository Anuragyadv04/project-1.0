import requests
from bs4 import BeautifulSoup
import csv

# Specify the URL of the target web page
url = 'https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
# Send an HTTP GET request to the URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the HTML content of the page
    html_content = response.text
    
    # Create a Beautiful Soup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    product_elements=soup.select('._13oc-S._1t9ceu')
    # Define the CSV file path
    csv_file = 'prodct_data.csv'

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Title', 'Price'])

        # Iterate over the product elements and extract the data
        for product in product_elements:
            title = product.select_one('.IRpwTa').text.strip()
            price = product.select_one('._30jeq3').text.strip()

        # Write the data to the CSV file
            writer.writerow([title, price])

# Print a message indicating that the data has been saved to the CSV file
    print(f"Data has been saved to {csv_file}.")
    ##Print the HTML content
    ##print(soup.prettify())
else:
    print(f"Error: Failed to fetch the page. Status code: {response.status_code}")

