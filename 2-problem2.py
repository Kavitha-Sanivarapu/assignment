import requests
from bs4 import BeautifulSoup
import re

# url = "https://ful.io"
# print(url)
url = input("Please enter a url: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')
# print(response.text)

all_anchors = soup.find_all('a', href=True)
# print(all_anchors)
social_links = []

social_domains = ["facebook.com", "linkedin.com", "twitter.com"]

for anchor in all_anchors:
    link = anchor.attrs['href']
    # print(link)
    for domain in social_domains:
        if domain in link:
            social_links.append(link)

# Social links
print()
print("Social links:")
for link in social_links:
    print(link)
print()

# Emails
emails = list(set(re.findall(
    "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", response.text)))

print("Emails: ")
for link in emails:
    print(link)
print()

# PhoneNumbers
phone_numbers = []
for anchor in all_anchors:
    link = anchor.attrs['href']
    if "tel:" in link:
        phone_numbers.append(link.replace("tel:", ""))

print("Contacts:")
for link in phone_numbers:
    print(link)
print()
