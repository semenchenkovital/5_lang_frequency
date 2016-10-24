#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs
from collections import Counter

def load_data(filepath):
    infile=codecs.open(filepath,'r', 'utf-8-sig').read()
    return infile
def get_most_frequent_words(text):
    data = text.lower()
    spisok = ['1','2','3','4','5','6','7','8','9','0',
              '*','-','.',',','\\','/','#','_','&','}','{','[',']','?','!','"',':',';','@','&']
    for zamena in spisok:
        data = data.replace(zamena,' ')    
    data = data.split()
    data = Counter(data)
    print (data.most_common(10))
    

if __name__ == '__main__':
    file = input("Введите имя файла:")
    try:
        data = load_data(file)
    except:
        print('Некорректное имя файла или путь к файлу')
    else:
        get_most_frequent_words(data)
