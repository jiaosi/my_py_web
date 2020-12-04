




import requests
html = requests.get("https://www.nytimes.com/")
with open('test.html','w',encoding='utf-8') as f:
 f.write(html.text)

