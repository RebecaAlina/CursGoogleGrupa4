from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element_by_xpath('//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
# for i in lista:
#     print(i, end='\n')

header = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr').text.split('\n')
dictionar = {i: [] for i in header}
# print(header)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)

# df = pd.DataFrame(dictionar)
# df.to_csv("BNR_ALL_DATA.csv")
