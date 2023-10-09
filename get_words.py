from bs4 import BeautifulSoup
import requests
import lxml
import sqlite3
URL = "https://3000mostcommonwords.com/list-of-3000-most-common-uzbek-words-in-english/"

response = requests.get(URL).text

soup = BeautifulSoup(response, "lxml")

con = sqlite3.connect("data/database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT, english TEXT, uzbek TEXT, pos TEXT, level TEXT)")
con.commit()
print("Table created")

table_datas = soup.find_all("tr")
print(len(table_datas))
for data in table_datas:
    english = data.find("td", class_="column-2")
    uzbek = data.find("td", class_="column-5")
    pos = data.find("td", class_="column-3")
    level = data.find("td", class_="column-4")

    english = str(english).replace('<td class="column-2">', '').replace('</td>', '').strip()
    uzbek = str(uzbek).replace('<td class="column-5">', '').replace('</td>', '').strip()
    pos = str(pos).replace('<td class="column-3">', '').replace('</td>','').replace('>', '').strip()
    level = str(level).replace('<td class="column-4">', '').replace('</td', '').replace('>', '').strip()
    if english != "" or uzbek!= "" or english != "None" or english != None:
        cur.execute("INSERT INTO words (english, uzbek, pos, level) VALUES (?,?,?,?)", (english, uzbek, pos, level))
        con.commit()
        print(f"{english}-{uzbek} successfully inserted")
