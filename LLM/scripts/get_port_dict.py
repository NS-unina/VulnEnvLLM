import csv
import sys
from requests import get
from os import path

def download_csv_from_url(url, save_path): 
    response = get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")

import csv
from os import path

def port_csv_to_list():
    """
    Retrieves a list of port data from a CSV file.
    
    This function downloads a CSV file from a given URL if it doesn't exist locally.
    It then reads the CSV file and returns a list of dictionaries, where each dictionary
    represents a row in the CSV file with only the first 4 columns.
    
    Returns:
        A list of dictionaries representing port data.
    """
    save_path = "service-names-port-numbers.csv"
    url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
    if not path.exists(save_path):
        download_csv_from_url(url, save_path)
    data_list = []
    with open("service-names-port-numbers.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(row['Service Name'] != '' and row['Transport Protocol'] != '' and row['Port Number'] != ''): # Skip rows with empty values
                trimmed_row = {key: row[key] for key in list(row.keys())[:4]} # Return only the first 4 columns
                data_list.append(trimmed_row)
    return data_list

if __name__ == "__main__":
    data = port_csv_to_list()
    for e in data:
        print(e)