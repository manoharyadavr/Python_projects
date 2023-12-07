# import requests
# from bs4 import BeautifulSoup
# import csv
# import threading



# # URL of the search page
# url = "https://www.hopkinsmedicine.org/profiles/search?query="

# # Send an HTTP GET request
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all provider details on the page
# provider_details = []
# for provider in soup.find_all("div", class_="provider"):
#     details = {
#         "name": provider.find("span", class_="name").text.strip(),
#         "title": provider.find("span", class_="title").text.strip(),
#         "gender": provider.find("span", class_="gender").text.strip(),
#         # ... other details ...
#     }
#     provider_details.append(details)

# # Save to CSV file
# csv_filename = "provider_details.csv"
# with open(csv_filename, "w", newline="") as csvfile:
#     fieldnames = ["name", "title", "gender", ...]  # Add all field names
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for details in provider_details:
#         writer.writerow(details)
# def scrape_page(url):
#     # Your scraping code here

# # List of URLs to scrape

# urls = ["url1", "url2", ...]

# threads = []
# for url in urls:
#     thread = threading.Thread(target=scrape_page, args=(url,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()




import requests
from bs4 import BeautifulSoup
import csv

# URL of the search page
base_url = "https://www.hopkinsmedicine.org/profiles/search?query="

# Function to scrape provider details from a page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    provider_details = []
    for provider in soup.find_all("div", class_="provider"):
        details = {
            "name": provider.find("span", class_="name").text.strip(),
            "title": provider.find("span", class_="title").text.strip(),
            "gender": provider.find("span", class_="gender").text.strip(),
            # Add more details extraction here
        }
        provider_details.append(details)
    
    return provider_details

# List of URLs to scrape
search_terms = ["term1", "term2", "term3"]  # Add your search terms here
urls = [base_url + term for term in search_terms]

# Scrape provider details from all URLs
all_provider_details = []
for url in urls:
    provider_details = scrape_page(url)
    all_provider_details.extend(provider_details)

# Save to CSV file
csv_filename = "provider_details.csv"
with open(csv_filename, "w", newline="") as csvfile:
    fieldnames = ["name", "title", "gender"]  # Add more field names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for details in all_provider_details:
        writer.writerow(details)

print("Scraping and CSV creation complete.")
