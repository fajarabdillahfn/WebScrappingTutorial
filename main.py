import requests
import bs4

print('''========================================================
Hello! This is my documentation on learning web scrapping using python from "2021 Complete Python Bootcamp From Zero to Hero in Python" on Section 15
========================================================
''')

print("\n+++++++++++++++++++++++++++++++++++++++++++++")
print("Video 118. Web Scrapping - Grabbing a Title")
print("+++++++++++++++++++++++++++++++++++++++++++++")
result = requests.get("http://www.example.com")

print("\n==> Implementing 'requests' library <==")
#check the data type of result 
print("\nresult data type: " + str(type(result)))

#check the content of the website
print("\n-----------------------------------------------")
print("Below is the content of the website (same as if you do inspect element on the website)")
print("-----------------------------------------------")
print(result.text)

print("\n==> Implementing 'BeautifulSoup4' or 'bs4' library <==")
print("\n-----------------------------------------------")
print("Below is the content of the website (same as if you do inspect element on the website) using BeautifulSoup4")
print("-----------------------------------------------")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

print("\n-----------------------------------------------")
print("Grab the elements using 'select()' method")
print("=> returns a list of all elements")
print("-----------------------------------------------")

print("\n> Grab <title> element(s)")
site_titles=soup.select('title')
print(site_titles)

print("\n> Grab <h1> element(s)")
site_heading1=soup.select('h1')
print(site_heading1)

print("\n> Grab <p> element(s)")
site_paragraphs=soup.select('p')
print(site_paragraphs)

print("\n+++++++++++++++++++++++++++++++++++++++++++++")
print("Video 119. Web Scrapping - Grabbing a Class")
print("+++++++++++++++++++++++++++++++++++++++++++++")

print("\n==> Grab the website from Wikipedia - Grace Hopper <==")
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# uncomment the print command below if you want to see the html of the webpage
# print(soup)

print("\n==> Grab a class and its content from the website <==")
print("> Grab a 'toctext' class from the website as an example")
# we know that the website has a class named 'toctext' from inspecting the element of the website
site_toctext_class=soup.select('.toctext')
print(f"The contents of 'toctext' class are:\n{site_toctext_class}")

print("\n> Get the first item of the toctext class content")
first_item=site_toctext_class[0]
print(f"The first content of 'toctext' class is:\n{first_item}")

print("\n> Get the text of the first toctext class content")
first_text=first_item.text
print(f"Text only of the first content of 'toctext' class is: {first_text}")

print("\n> Get all of text of the toctext class content")
text_content=[]
for text_item in site_toctext_class:
  text_content.append(text_item.text)
print(f"Text only of the all content in 'toctext' class are:\n{text_content}")

print("\n+++++++++++++++++++++++++++++++++++++++++++++")
print("Video 120. Web Scrapping - Grabbing an Image")
print("+++++++++++++++++++++++++++++++++++++++++++++")

print("\n==> Grab the website from Wikipedia - Deep Blue (Chess Computer) <==")
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
# uncomment the print command below if you want to see the html of the webpage
# print(soup)

print("\n==> Grab the Blue Computer Image on the website <==")

print("\n> Try to grabbing <img> element as it's where the image belong")
image=soup.select('img')
print(image)
print("!! It returns too many list of image element, we need to specify !!")

print("\n> Try to grabbing <.image> class as it's where the image belong")
image=soup.select('.image')[0]
print(image)

print("\n> Grab the image link add the 'https:' attribute to make the url be able to open on browser")
image_link="https:" + image.select('img')[0]['src']
print(image_link)