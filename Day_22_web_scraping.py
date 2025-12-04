#Day 22: 30 Days of python programming

import requests
from bs4 import BeautifulSoup
import json
 
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
facts_data = {}
for section in soup.find_all(["h2", "h3"]):
    heading = section.get_text(strip=True)
    content = section.find_next_sibling("p")
    if content:
        facts_data[heading] = content.get_text(strip=True)
with open("bu_facts.json", "w", encoding="utf-8") as file:
    json.dump(facts_data, file, indent=4, ensure_ascii=False)
print(response.status_code)
print(soup.prettify()[:2000]) 
#request can't load JavaScript content, we should use Selenium

#Exercise 2
import pandas as pd

url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"border": "1"})
headers = [header.get_text(strip=True) for header in table.find_all("th")]
data = []
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if cols:
        row_data = [col.get_text(strip=True) for col in cols]
        data.append(dict(zip(headers, row_data)))
with open("uci_datasets.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

#Exercise 3
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": "wikitable"})
headers = ["No.", "Portrait", "Name", "Term", "Party", "Vice President(s)"]
data = []
for row in table.find_all("tr")[1:]:
    cols = row.find_all(["td", "th"])
    if len(cols) < 5:
        continue
    president_data = {
        "No.": cols[0].get_text(strip=True),
        "Name": cols[2].get_text(strip=True),
        "Term": cols[3].get_text(strip=True),
        "Party": cols[4].get_text(strip=True), 
        "Vice President(s)": cols[5].get_text(strip=True) if len(cols) > 5 else "N/A" 
    }
    data.append(president_data)
with open("us_presidents.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
print(table)
print("Presidents' table successfully saved as JSON!")