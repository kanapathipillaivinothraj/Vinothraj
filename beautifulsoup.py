from bs4 import BeautifulSoup
import requests
print("beautifulsoup4 is running & lxml is running & requests is running")

# with open('index.html','r') as f:
#     doc = BeautifulSoup(f, 'html.parser')
 
# print(doc.prettify()) print the all website page in html 
# title = doc.title

# print the Title eg:- <title> Vinothraj kanapathipillai </title>
# print(title) 

# print the Title eg:- Vinothraj kanapathipillai 
# print(title.string) 

# Change the Title eg:- Vinothraj kanapathipillai
# title.string = "Vinothraj"
 
# print(title.string) 

# find_all & find 
# find first a tag only
# tags_a = doc.find("a") 
# find all a tag
# tags_a = doc.find_all("a") 
# print(tags_a) 

# find first a tag
# tags_a = doc.find_all("a")[0]

# find first a tag have a span tag
# print(tags_a.find_all("span"))


# start project


url = "https://ideabeam.com/finance/rates/goldprice.php"
# url = "https://www.cbsl.gov.lk/en/rates-and-indicators/exchange-rates/daily-gold-rates"
result = requests.get(url)
# print(result.text)
doc = BeautifulSoup(result.text, 'html.parser')
# print(doc.prettify())
tags_td_title = doc.title
print(tags_td_title.string)
tags_td_pawn = doc.find_all("td")[8]
print(tags_td_pawn.string)
tags_td_price = doc.find_all("td")[9]
print(tags_td_price.string)

# with open('Gold.html','r') as f:
#     doc = BeautifulSoup(f, 'html.parser')
    
# tag_p = doc.find_all('h1')[0]
# print(tag_p)
# tag_p['class'] = 'remove' 
# tag_p.string = "gold is changed"
# print(tag_p)

# tag_p = doc.find_all(['p'], choice="Gold History")[0]
# print(tag_p)