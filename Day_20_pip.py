#Day 20: 30 Days of python programming

import requests
import re
from collections import Counter
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
word_counts = Counter(words)
most_common = word_counts.most_common(10)
print(most_common)

import numpy as np
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    weights_metric = []
    for breed in data:
        if "weight" in breed and "metric" in breed["weight"]:
            weight_range = breed["weight"]["metric"].split(" - ")
            if len(weight_range) == 2:
                try:
                    min_w, max_w = map(float, weight_range)
                    avg_weight = (min_w + max_w) / 2  # Average of the range
                    weights_metric.append(avg_weight)
                except ValueError:
                    pass
    min_weight = np.min(weights_metric)
    max_weight = np.max(weights_metric)
    mean_weight = np.mean(weights_metric)
    median_weight = np.median(weights_metric)
    std_dev_weight = np.std(weights_metric)
    print(min_weight, max_weight, mean_weight, median_weight, std_dev_weight)

#Exercises 2
import statistics
import re
def analyze_cat_lifespans(cat_data):
    lifespans = []
    for cat in cat_data:
        if 'life_span' in cat:
            span = re.findall(r'\d+', cat['life_span'])
            if len(span) == 2:
                min_age, max_age = map(int, span)
                avg_age = (min_age + max_age) / 2
                lifespans.append(avg_age)
    if not lifespans:
        return "No valid lifespan data found."
    stats = {
        'min': min(lifespans),
        'max': max(lifespans),
        'mean': round(statistics.mean(lifespans), 2),
        'median': statistics.median(lifespans),
        'stdev': round(statistics.stdev(lifespans), 2) if len(lifespans) > 1 else 0.0}
    return stats

from collections import Counter
def country_breed_frequency(cat_data):
    country_counter = Counter()
    for cat in cat_data:
        country = cat.get('origin', 'Unknown')
        country_counter[country] += 1
    return dict(country_counter)

#Exercise 3
import requests
def get_largest_countries_by_area(top_n=10):
    url = "https://restcountries.eu/rest/v2/all"
    response = requests.get(url)
    countries = response.json()
    area_data = []
    for country in countries:
        name = country.get('name', {}).get('common', 'Unknown')
        area = country.get('area', 0)
        area_data.append((name, area))
    top_countries = sorted(area_data, key=lambda x: x[1], reverse=True)[:top_n]
    return top_countries

import requests
from collections import Counter
def get_most_spoken_languages(top_n=10):
    url = "https://restcountries.eu/rest/v2/all"
    response = requests.get(url)
    countries = response.json()
    language_counter = Counter()
    for country in countries:
        languages = country.get('languages', {})
        for lang_code, lang_name in languages.items():
            language_counter[lang_name] += 1
    top_languages = language_counter.most_common(top_n)
    return top_languages

import requests
def count_unique_languages():
    url = "https://restcountries.eu/rest/v2/all"
    response = requests.get(url)
    countries = response.json()
    languages = set()
    for country in countries:
        country_languages = country.get('languages', {})
        for lang_code, lang_name in country_languages.items():
            languages.add(lang_name.lower()) 
    return len(languages)
total_languages = count_unique_languages()
print(total_languages)

#Exercise 4
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    dataset_links = soup.find_all('a', href=True)
    datasets = []
    for link in dataset_links:
        href = link['href']
        if 'datasets/' in href:
            datasets.append(href)
    datasets = set(datasets)
    print("First 10 datasets in the UCI repository:")
    for i, dataset in enumerate(datasets):
        if i == 10:
            break
        print(f"{i+1}. {dataset.replace('/ml/datasets/', '')}")