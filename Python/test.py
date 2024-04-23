import requests
from bs4 import BeautifulSoup

searchUrl = input("Movie Name: ")

searchUrl = searchUrl.replace(" ","+")

print(searchUrl)

URL = f"https://ww1.moviesm4u.org/search?q={searchUrl}"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")
#variableDeclaring
i = 0
Dict = {}

# Now you can navigate and search the parse tree
# For example, find all links on the page:
for a in soup.find_all('h3'):
    link = a.find('a', href = True)
    if link:
        i += 1
        Dict[i] = link['href']
        print(f"{i} {link.text}")


