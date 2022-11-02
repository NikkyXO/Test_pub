import csv
import json
 
def csv_to_json(csv_file_path, json_file_path):
    #create a dictionary
	data_dict = {}
 
    #Step 2
    #open a csv file handler
	with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
		csv_reader = csv.DictReader(csv_file_handler)
 
		for rows in csv_reader:ey
			key = rows['Serial Number']
			data_dict[key] = rows

	with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent = 4))