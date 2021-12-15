from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element_by_xpath('//*[@id="post-25121"]/div/div/table[1]/tbody')
table_text = table.text
lista = table_text.split('\n')

header = browser.find_element_by_xpath('//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]').find_elements_by_tag_name('td')
header = [i.text for i in header]
dictionar = {i: [] for i in header}

for j in range(1, len(lista)-2):
    for i in range(len(header)):
        if lista[j].count(" ") == 4:
            dictionar[header[i]].append(lista[j].split(" ")[i])
        else:
            if i == 1:
                dictionar[header[i]].append(str(lista[j].split(" ")[i] + " " + lista[j].split(" ")[i+1]))
            elif i > 1:
                dictionar[header[i]].append(str(lista[j].split(" ")[i+1]))
            else:
                dictionar[header[i]].append(lista[j].split(" ")[i])

df = pd.DataFrame(dictionar)
df.to_csv("Covid_cases.xls", mode="a", encoding='utf-16', index=False)
