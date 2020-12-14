from lxml import etree as et
import pandas as pd
import numpy as np
import re
import os

#ключевые фразы по которым происходит поиск данных
key_words = ["Дата поступления в приемное отделение", "Время поступления в приемное отделение",
             "Дата поступления", "Время поступления", "Пребывание в отделении реанимации"]

def etree2df(tree):
     index = -1 #номер п.п пациента в файле
     root = tree.getroot()
     data = [[" - "]*5 for i in range(len(root))] #количество элемнтов в руте - количество пациентов
     tags = []
     for elem in root:
         tags.append(str(elem.tag)) #сохраняем тэги соответсвующие пациентам
     for elem in tree.iter():
         line = str(elem.text) #считываем строку и выполняем в ней поиск необходимой информации
         if str(elem.tag) in tags: index+= 1
         if data[index][0] == " - " and key_words[0] in line:
            data[index][0] = (".".join(re.findall("\d+", line)))
            continue
         if data[index][1] == " - " and key_words[1] in line:
            data[index][1] = (":".join(re.findall("\d+", line)))
            continue
         if data[index][2] == " - " and key_words[2] in line:
            data[index][2] = (".".join(re.findall("\d+", line)))
            continue
         if data[index][3] == " - " and key_words[3] in line:
            data[index][3] = (":".join(re.findall("\d+", line)))
            continue
         if data[index][4] == " - " and key_words[4] in line:
            data[index][4] = ("".join(re.findall("\d+", line)) + " койко-дн(ей/я)")
     return pd.DataFrame(data,columns = key_words) #строим дф для всего файла

list_of_files = os.listdir("Cases_with_html")
xmlframe = pd.DataFrame(columns = key_words) #общий дф, собирается из дф всех файлов
for file in list_of_files:
    tree = et.parse(open("Cases_with_html/" + file, errors='ignore'))
    xmlframe= xmlframe.append(etree2df(tree), ignore_index = True)
with open("DataFrame.txt","w") as file:
    file.write(xmlframe.to_string())
