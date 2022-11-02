import csv
import json
import pandas as pd


def make_json(csvFilePath, jsonFilePath):
    data = {}

    keys = ['Series Number', 'Filename', 'UUID']
    results = pd.read_csv("Allteams2.csv")
    print(results)

    with open('Allteams2.csv', encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        for row in csv_reader:
            for content in row:
                lst = []
                lst.append(content)
                # temp = list(lst.split(' '))
            for  key in keys:
                i = 0
                data[key] = lst[i]
                i += 1
                
    with open('newoutput.json','w',  encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'Allteams2.csv'
jsonFilePath = r'newoutput.json'
make_json(csvFilePath, jsonFilePath)