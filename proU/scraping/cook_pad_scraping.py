# coding: utf-8

from bs4 import BeautifulSoup
import requests

url = "https://cookpad.com/recipe/3672400"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.88 Safari/537.36 Vivaldi/1.7.735.46"}
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text, "html.parser")

recipe = soup.select(".clearfix")
steps = soup.select(".step")
step_texts = soup.select(".step_text")


print(recipe)
print(steps)
