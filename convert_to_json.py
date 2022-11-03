import csv, hashlib, json

OUTPUT_FILE = 'csv/test.csv'

with open(OUTPUT_FILE, 'w') as f:

    writer = csv.writer(f)
    writer.writerow(['S/N', 'Filename','UUID', 'Output File Name'])

    with open('csv/HNG.csv', 'r') as csvFile:
        CSV_reader = csv.reader(csvFile, delimiter=',')
        
        next(CSV_reader)
        data = [m for m in CSV_reader]  
        for col in data:
            if col[1] and col[2]:
                SN = col[0]
                file_name = col[1]
                uuid = col[-1]
                nft = {
                    'format' : 'CHIP-0007',
                    'id' : uuid,
                    'name' : file_name.replace('-',' ').title(),
                    'filename': file_name,
                    'description' : '',
                    'minting_tool' : 'Matanmi SuperMint',
                    'sensitive_content' : False,
                    'series_number' : SN,
                    'series_total' : data[-1][0],
                    'collection' : {
                        'name' : 'Zuri Hng NFT Collection',
                        'id' : '24f5ff82-a2f1-494e-8be5-69f1d5e42d15'
                    }
                }
                jsonObj = json.dumps(nft, indent=4)
                with open(f'json/{file_name}.json', 'w') as output:
                    output.write(jsonObj)
                
                hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
                col.append(f'{file_name}.{hashString}.csv')
                writer.writerow(col)
