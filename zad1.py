# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача, ровабврпы, ымер'

listi = text.split()

def text(texti):
    text = ""
    for i in listi:
        prov = True
        if len(i) >= 3:
            j = 0
            while j + 3 <= len(i):
                if i[j:3 + j:] =="абв":
                    prov = False
                j += 1
        if prov:
            text += i + " "
    print(text)
    
text(text)