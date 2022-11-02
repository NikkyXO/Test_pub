import csv
import json
import pandas as pd


def make_json(csvFilePath, jsonFilePath):
    data = {}

    keys = ['Series Number', 'UUID']
    # results = pd.read_csv("Allteams2.csv")
    # print(results)

    with open('Allteams2.csv', encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        data = {}
        
        for row in csv_reader:
            i += 0
            for key in keys:
                temp = row.split(",")
                
                data[key] = temp[i]
                i += 1

                
    with open('newoutput.json','w',  encoding='utf-8') as jsonf:
        json.dump(data, jsonf)
        # jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'Allteams2.csv'
jsonFilePath = r'newoutput.json'
make_json(csvFilePath, jsonFilePath)