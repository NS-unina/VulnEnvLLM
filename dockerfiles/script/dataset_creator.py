import csv
import json
from os import remove, path, walk

def tsv_to_jsonl(tsv_folder, jsonl_filepath):
    for root, dirs, files in walk(tsv_folder):
        for file in files:
            if file.endswith(".tsv"):
                tsv_filepath = path.join(root, file)
                with open(tsv_filepath, 'r') as tsv_file, open(jsonl_filepath, 'a') as jsonl_file:
                    tsv_reader = csv.reader(tsv_file, delimiter='\t')
                    for row in tsv_reader:
                        jsonl_file.write(json.dumps({"input": row[0], "output": row[1]}) + '\n')
                        if(len(row) > 2 and row[2] != ''):
                            jsonl_file.write(json.dumps({"input": row[2], "output": row[3]}) + '\n')
                
def remove_trailing_newlines(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            file_path = path.join(root, file)
            if(file_path.endswith(".DS_Store")):
                continue
            with open(file_path, 'r') as f:
                lines = f.readlines()
            with open(file_path, 'w') as f:
                for i in range(len(lines)):
                    if i != len(lines) - 1:  # If it's not the last line
                        f.write(lines[i])
                    else:  # If it's the last line
                        f.write(lines[i].rstrip('\r\n'))

# Specifica la directory da cui iniziare la ricerca

if(path.exists('dataset.jsonl')):
    remove('dataset.jsonl')

tsv_to_jsonl('TSVs', 'dataset.jsonl')

# remove_trailing_newlines("../with-llms")
# remove_trailing_newlines("../fixed")
# remove_trailing_newlines(".")