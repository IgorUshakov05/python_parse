from bs4 import BeautifulSoup
import re
with open("index.html") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")

# Print Title
def PrintInfoTitle():
    title = soup.title
    print(title.text)

# .find()
def find():
    find = soup.find("div")
    print(find)

# .find_all()
def find_All():
    find2 = soup.find_all("div")
    print(find2)

def find_class():
    # find class
    user_name = soup.find("div", class_="user__name")
    print(user_name.text.strip())

    # find class
    user_name_top = soup.find("div", {"class" : "user__name"}).text.strip()
    print(user_name_top)


# find_perent

def find_perent():
    find_perent = soup.find("p").find_parent()
    print(find_perent)

# find_perents

def find_perents():
    find_perents = soup.find(class_="user__name").find_parents()
    print(find_perents)

# next_element

def next_element():
    next_element = soup.find(class_="user__name").next_element.next_element.next_element
    print(next_element)

# find_next_sibling

def find_next_sibling():
    find_next_sibling = soup.find(class_="user__name").find_next_sibling()
    print(find_next_sibling)

# find_previous_sibling

def find_previous_sibling():
    find_previous_sibling = soup.find(class_="user__name").find_previous_sibling()
    print(find_previous_sibling)

# Найти эллемент по тесксту

find_tetxt = soup.find("div", text=re.compile("Igor"))
print(find_tetxt)

# Найти эллементы по тесксту

find_texts = soup.find_all(text=re.compile("([Ii]gor)"))
print(find_texts)