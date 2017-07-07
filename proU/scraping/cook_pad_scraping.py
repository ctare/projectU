# coding: utf-8

from bs4 import BeautifulSoup
import requests
import codecs

url = "https://cookpad.com/recipe/3672400"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.88 Safari/537.36 Vivaldi/1.7.735.46"}
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text, "html.parser")

recipes = soup.select(".clearfix")
# steps = soup.select(".step,.step_last")
steps = soup.select(".instruction")
step_texts = soup.select(".step_text")


f = codecs.open("steps.html", "w", "utf-8")

for i, step in enumerate(steps):
    i += 1
    f.write("<h3 id=step" + str(i) + ">step" + str(i) + "</h3>")
    f.write(str(step))
    f.write("</div>")
    f.write("<br>")
    f.write("<a href=#step" + str(i-1) + "><button type='button'>prev</button></a>")
    f.write("<a href=#step" + str(i+1) + "><button type='button'>next</button></a>")
f.close()

f = codecs.open("recipes.html", "w", "utf-8")
f.write(str(recipes[0]))
f.write("<br>")
f.close()


print(steps)
print()