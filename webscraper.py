import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find_all("article")
    if not article:
        return None, None
    title = article[0].find("h1").get_text()
    paragraphs = article[0].find_all("p")
    text = ""
    for p in paragraphs:
        text += p.get_text() + "\n"
    return title, text

df = pd.read_excel("Input.xlsx")
output_df = pd.DataFrame(columns=["URL_ID", "Title", "Text"])

for index, row in df.iterrows():
    url = row["URL"]
    url_id = row["URL_ID"]
    title, text = extract_article_text(url)
    if title is None:
        print(f"No article found for URL: {url}")
        continue
    output_df = output_df.append({"URL_ID": url_id, "Title": title, "Text": text}, ignore_index=True)

output_df.to_excel("Output.xlsx", index=False)
