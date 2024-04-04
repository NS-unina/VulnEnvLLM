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

def csv_to_dict():
    save_path = "service-names-port-numbers.csv"
    url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
    if not path.exists(save_path):
        download_csv_from_url(url, save_path)
    data_list = []
    with open("service-names-port-numbers.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trimmed_row = {key: row[key] for key in list(row.keys())[:4]}
            data_list.append(trimmed_row)
    return data_list

if __name__ == "__main__":
    data = csv_to_dict()
    for e in data:
        print(e)