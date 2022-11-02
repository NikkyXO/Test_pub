#  HNG TASK

-  Convert a CSV provided file, Generate a CHIP_0007 compatible json
-  Calculate the sha256 of the json file
-  Append it to each line in the CSV as (filename.output.csv)


## Steps taken to get task done

###  Converted a CSV provided file, Generated a CHIP_0007 compatible json

Reading of the file is done using default fs npm package

	const fs = require("fs");
	csv = fs.readFileSync("Naming - All Teams.csv")

Convert the data to String and split it in an array

	var array = csv.toString().split("\r");

All the rows of the CSV will be converted to JSON objects which will be added to result in an array

	let result = [];

The array[0] contains all the header columns so we store them in headers array

	let headers = array[0].split(", ")

Since headers are separated, we need to traverse remaining n-1 rows.

	for (let i = 1; i < array.length - 1; i++) {
  		let obj = {}

Create an empty object to later add values of the current row to it Declare string str as current array value to change the delimiter and store the generated string in a new string s

	let str = array[i]
  	let s = ''


By Default, we get the comma separated values of a cell in quotes " " so we use flag to keep track of quotes and split the string accordingly If we encounter opening quote (") then we keep commas as it is otherwise we replace them with pipe | We keep adding the characters we traverse to a String s

	let flag = 0
  	for (let ch of str) {
    	if (ch === '"' && flag === 0) {
      	flag = 1
    	}
    	else if (ch === '"' && flag == 1) flag = 0
    	if (ch === ', ' && flag === 0) ch = '|'
    	if (ch !== '"') s += ch
  	}


Split the string using pipe delimiter | and store the values in a properties array

	let properties = s.split("|")

For each header, if the value contains multiple comma separated data, then we store it in the form of array otherwise directly the value is stored


	for (let j in headers) {
		if (properties[j].includes(", ")) {
		obj[headers[j]] = properties[j]
			.split(", ").map(item => item.trim())
		}
		else obj[headers[j]] = properties[j]
	}

	

Add the generated object to our result array

	result.push(obj)


Convert the resultant array to json and generate the JSON output file.

	let json = JSON.stringify(result);
	fs.writeFileSync('output.json', json);



### Calculated the sha256 of the json file

sha-256 was created for the generated json file with the linux command
	sha256sum output.csv

### Appended it to each line in the CSV as (filename.output.csv) with a bash script

	Appending to each line in the file was done with the use of the linux stream editor. (sed) and running file command with a bash script

		sed -r 's/\r/|the_text\r/' Allteams2.csv > output.csv
	
	The \r represent EOL
	the_text: is the text to be appended

# GUIDELINES ON HOW TO USE THE SCRIPT

Input the Csv file to be read and coverted in the fs.readFileSync function in the **app.js** file and run the script

	node app.js

Result  is outputted as **output.json**

Run sha256 with output.json on command line to create the hash of file

	sha256 output.json

Then Run the bash script scriptcsv on your terminal to append the required text to each end of the line of the file, with the file input and output specified

	./scriptcsv

Thanks for taking time to go through
