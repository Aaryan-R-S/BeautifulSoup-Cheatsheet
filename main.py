# Scrap any website using :
# 1. Use the API
# 2. Tools like bs4

# Refer --
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


#  ---------------Step 0 [Requirements] ----------------------------
# CMD :
#  pip install requests
#  pip install bs4
#  pip install html5lib


#  --------------Step 1 [Get the HTML]---------------------------------
import requests
from bs4 import BeautifulSoup
url = "https://www.cricbuzz.com/live-cricket-scores/35612/1st-match-indian-premier-league-2021"

response = requests.get(url)
htmlContent = response.content 
# -- OR --
# htmlContent = response.text 
# print(htmlContent)

#  -----------Step 2 [Parse the HTML]--
mySoup = BeautifulSoup(htmlContent, 'html.parser')
# print(mySoup.prettify())  # All HTML content
# --OR--
# print(mySoup.get_text())  # Get All text
# --OR--
# i=0
# for e in mySoup.stripped_strings:
#     i+=1
#     print(i, end=" ")
#     print(e)
# --OR--
print(list(mySoup.stripped_strings)[146])
print(list(mySoup.stripped_strings)[147])


# --------------Imp funcs -- ---------------------

# [.get_text() , .prettify() , .strings , .stripped_strings]
# [ .tag.name , .tag['class'] , .tag['id'] , tag.attrs , .tag.stripped_strings , .tag.previous_sibling , .tag.next_sibling , tag.parents.name]


#------------------------ Types of objects ----------------

# -- 1. Beautiful Soup --
# print(type(mySoup))

# -- 2. Tag --
# title = mySoup.title
# title = mySoup.title.name
# title = mySoup.title.strings
# print(title)
# print(type(title))
# print(mySoup.script)

# -- 3. Navigable String --
# print(title.string)
# print(type(title.string))

# -- 4. Comment --
# m = "<p><!-- This is my comment --></p>"
# mySoup2 = BeautifulSoup(m)
# print(mySoup2.p)
# print(mySoup2.p.string)
# print(type(mySoup2.p.string))
#     -- OR --
# from bs4 import Comment
# comments = mySoup.find_all(string=lambda text: isinstance(text, Comment))
# print(comments)



#  ---------------------------Step 3 [HTML Tree Traversal]-----------------------------------

#  -- General search --
# paras = mySoup.find_all('p')
# print(paras)

# -- Find All elements having attr id --
# print(mySoup.find_all(id=True))

#  -- Search by id or class --
# print(mySoup.find_all('p', class_= 'lead'))
# idTag = mySoup.find(id = 'navbarSupportedContent')
# print(idTag.prettify())
# for e in idTag.stripped_strings:
#     print(e)


# -- Complex filter --
# import re
# regx = re.compile("t$")
# for tag in mySoup.find_all(regx):
#     print(tag.name)


# -- Links --
# anchors = mySoup.find_all('a')
# print(anchors)
# s = set()
# for a in anchors:
#     if a.get('href') != '#':
#         link = "https://codewithharry.com" + a.get('href')
#         s.add(link)
# for e in s:
#     print(e)

# -- All attributes of a tag --
# inp = mySoup.input.attrs
# print(inp)
# -- or --
# p = mySoup.find('p')
# print(p)
# print(p['class'])
# print(p['id'])
# print(p['href'])


# --Get the text of p of HTML page--
# print(mySoup.find('p').get_text()
# pTags = mySoup.find_all('p')
# for e in pTags: 
#     print (e.get_text())

# -- Parents --
# print(idTag.parent)
# for e in idTag.parents:
#     print(e.name)

#  -- Siblings --
# clsTag = mySoup.find(class_='form-group')
# print(clsTag.previous_sibling.previous_sibling)
# print(" ")
# print(clsTag.next_sibling.next_sibling)


# ----Get required element---
# e = mySoup.select('p')
# e = mySoup.select('#navbarSupportedContent')
# e = mySoup.select('.form-group')
# e = mySoup.select("a#link2")
# e = mySoup.select('a[href]')  
# e = mySoup.select('a[href="http://example.com/elsie"]')  
# e = mySoup.select("html head title")  # heirarchy
# e = mySoup.select('p:nth-of-type(3)')
# print(e)
# print(e[0].get_text())

#  -- Other Imp --
# del tag['class']
# del tag['id']
# mySoup.a.append("Bar")     # bar is appended to <a>tag contents
# j = mySoup.a.insert(3, "Bar")     # bar is appended to <a>tag contents at 3 index position
# print(mySoup.a.get_text())