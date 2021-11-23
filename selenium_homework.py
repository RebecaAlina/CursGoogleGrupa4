from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element_by_xpath('//*[@id="post-25121"]/div/div/table[1]/tbody')
table_text = table.text
lista = table_text.split('\n')
print(lista)

header = browser.find_element_by_xpath('//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]').find_elements_by_tag_name('td')
header = [i.text for i in header]
dictionar = {i: [] for i in header}
# print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)

# df = pd.DataFrame(dictionar)
# df.to_csv("20IANUARIE.csv")
