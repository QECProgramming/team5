from bs4 import BeautifulSoup
import urllib2
import requests
import ssl
import re
import numpy as np


def cleanMe(html):
    soup = BeautifulSoup(html,'html.parser') 
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text



def getPrice(testURL):

    p = requests.get(testURL)
    data = p.text

    soup = BeautifulSoup(data, 'html.parser')

    text = cleanMe(data)
    indOfPizza = 0
    #print text
    for i in range(0,len(text)):
        indOfPizza = text.find('Pizza',indOfPizza+1)
        if indOfPizza == -1:
            break
        if indOfPizza == text.find('Pizza Sub',indOfPizza -1):
            continue


        indOfPrice = text.find('$',indOfPizza,len(text))
        indOfSpace = text.find(' ',indOfPrice,len(text))
        i = indOfPizza+1
        return text[indOfPrice:indOfPrice+6]
        
    


test = 'http://www.bubbas.ca'
r = requests.get(test)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

result_array = np.array([])
priceArray = np.array([])


for link in soup.find_all('a'):
    check = 0
    for i in range(0,len(result_array)):
        if link == result_array[i]:
            check = 1
    if check == 0:
        result_array = np.append(result_array,link.get('href'))
    
for i in range(0, result_array.size):
    string1 = str(result_array[i])
    if string1.startswith("http"):
        priceArray = np.append(priceArray, getPrice(result_array[i]))
    elif string1.startswith("/"):
        priceArray = np.append(priceArray, getPrice(test+string1))

print priceArray
    
