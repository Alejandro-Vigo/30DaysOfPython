#Day 19: 30 Days of python programming

path = './30DaysOfPython/obama_speech.txt'
def count_lines_words (path):
    with open(path,'r') as f:
        lines = f.readlines()
        f.seek(0)
        words = f.read().split()
    return len(lines), len(words)
print(count_lines_words(path))

path='./30DaysOfPython/michelle_obama_speech.txt'
print(count_lines_words(path))


import json
path='./30DaysOfPython/countries_data.json'
def most_spoken_languages(path, top_n=10):
    with open(path, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] +=1
            else: language_count[language] = 1
    sorted_languages = sorted(language_count.items(),key=lambda item: item[1], reverse=True)
    top_languages = sorted_languages[:top_n]
    return top_languages
print(most_spoken_languages(path))

def most_populated_countries(path, top_n=10):
    with open(path, 'r', encoding='utf-8') as file:
        countries = json.load(file)
        populated_count={}
    for country in countries:
        populated_count[country['name']]=country['population']
        sorted_population = sorted(populated_count.items(),key=lambda item: item[1], reverse=True)
        top_population = sorted_population[:top_n]
    return top_population
print(most_populated_countries(path))

import re

email_path = './30DaysOfPython/email_exchanges_big.txt'

def extract_emails(email_path):
    with open (email_path,'r', encoding='utf-8') as file:
        content = file.read()
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    return emails
print(extract_emails(email_path)) 

import re
from collections import Counter

def find_most_common_words(input_text, top_n):
    if isinstance(input_text, str) and input_text.endswith('.txt'):
        with open(input_text, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = input_text
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(top_n)
    return [(count, word) for word, count in most_common]
print(find_most_common_words(email_path,10))

print(find_most_common_words('./30DaysOfPython/michelle_obama_speech.txt',10))
print(find_most_common_words('./30DaysOfPython/obama_speech.txt',10))


import re
import string
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_support_words(text, stop_words):
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity

def process_texts(input_text_one, input_text_two, stop_words):
    if isinstance(input_text_one, str) and input_text_one.endswith('.txt'):
        with open(input_text_one, 'r', encoding='utf-8') as file:
            text1 = file.read()
    else:
        text1 = input_text_one
    if isinstance(input_text_two, str) and input_text_two.endswith('.txt'):
        with open(input_text_two, 'r', encoding='utf-8') as file_two:
            text2 = file_two.read()
    else:
        text2 = input_text_two
    text1 =clean_text(text1)
    text2 =clean_text(text2)
    text1 = remove_support_words(text1,stop_words)
    text2 = remove_support_words(text2, stop_words)
    similarity_score = check_text_similarity(text1,text2)
    return similarity_score
process_texts('./30DaysOfPython/michelle_obama_speech.txt','./30DaysOfPython/melina_trump_speech.txt',stop_words)

def most_repeated_words(text, n=10):
    count_words = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word:
            count_words[word] = count_words.get(word,0)+1
    sorted_words = sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]
most_repeated_words('./30DaysOfPython/romeo_and_juliet.txt')

import csv
def count_lines(text):
    with open('./30DaysOfPython/hacker_news.csv',newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if any('python' in cell.lower() for cell in row):
             line_count +=1
        return line_count
print(count_lines('./30DaysOfPython/hacker_news.csv'))
