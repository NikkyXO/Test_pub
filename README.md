#  HNG TASK

-  Convert a CSV provided file, Generate a CHIP_0007 compatible json
-  Calculate the sha256 of the json file
-  Append it to each line in the CSV as (filename.output.csv)


## PROCESS

-  python script "covert_to_json" Script writes key values into the first row on output file. (output.csv)

-  A variable team is initialized with an empty string

 with the "with open" statement convert_to_json reads csv file named "HNG.csv" and stores in CSV_reader


-  it skips the first line of HNG_csv with the function next



-  in the HNG.csv, it loops through each row and create a json object, and then create a sha256 hash of the json object before adding it to the end of each row of the output csv file.


# GUIDELINES ON HOW TO USE THE SCRIPT


	run	python convert_to_json.py

Thanks for taking time to go through
