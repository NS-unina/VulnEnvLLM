import csv
import sys
from requests import get
from os import path


def download_csv_from_url(url, save_path):
    response = get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
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
    with open("service-names-port-numbers.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (
                row["Service Name"] != ""
                and row["Transport Protocol"] != ""
                and row["Port Number"] != ""
            ):  # Skip rows with empty values
                trimmed_row = {
                    key: row[key] for key in list(row.keys())[:4]
                }  # Return only the first 4 columns
                data_list.append(trimmed_row)
    return data_list

def get_ports(package_name: str) -> str:
    return " ".join(common_programs.get(package_name, get_ports_csv(package_name)))
    

def get_ports_csv(package_name: str) -> str:
    csv_list: list = port_csv_to_list()
    matching_elements = [
        element for element in csv_list if element["Service Name"] in package_name
    ]
    port_numbers = ""
    for e in matching_elements:
        if e["Transport Protocol"] == "":
            port_numbers += f"{e['Port Number']} "
        else:
            port_numbers += f"{e['Port Number']}/{e['Transport Protocol']} "
    return port_numbers



if __name__ == "__main__":
    data = port_csv_to_list()
    for e in data:
        print(e)

common_programs = {
    "nginx": ["80/tcp", "443/tcp"],
    "apache": ["80/tcp", "443/tcp"],
    "ssh": ["22/tcp"],
    "openssh": ["22/tcp"],
    "openssh-client": ["22/tcp"],
    "openssh-server": ["22/tcp"],
    "mysql": ["3306/tcp"],
    "postgresql": ["5432/tcp"],
    "mongodb": ["27017/tcp"],
    "redis": ["6379/tcp"],
    "ftp": ["21/tcp"],
    "telnet": ["23/tcp"],
    "smtp": ["25/tcp"],
    "dns": ["53/tcp", "53/udp"],
    "http": ["80/tcp"],
    "pop3": ["110/tcp"],
    "imap": ["143/tcp"],
    "snmp": ["161/udp", "162/udp"],
    "https": ["443/tcp"],
    "dhcp": ["67/udp", "68/udp"],
    "oracle": ["1521/tcp"],
    "mssql": ["1433/tcp"],
    "rdp": ["3389/tcp"],
    "rabbitmq": ["5672/tcp"],
    "memcached": ["11211/tcp"],
    "ntp": ["53"],
    "docker": ["2375/tcp", "2376/tcp"],
    "elasticsearch": ["9200/tcp", "9300/tcp"],
    "kafka": ["9092/tcp"],
    "zookeeper": ["2181/tcp"],
    "tomcat": ["8080/tcp", "8443/tcp"],
    "wildfly": ["8080/tcp", "8443/tcp"],
    "glassfish": ["8080/tcp", "8181/tcp"],
    "node": ["3000/tcp"],
    "rabbitmq": ["5672/tcp", "15672/tcp"],
    "kubernetes": ["6443/tcp"],
    "grafana": ["3000/tcp"],
    "smb": ["445/tcp"],
    "samba": ["445/tcp"],
    "git": ["22/tcp", "80/tcp", "443/tcp"],
    "jenkins": ["8080", "8443"],
    "nagios": ["80", "443"],
    "ntp": ["123/udp"],
    "radius": ["1812/udp", "1813/udp"],
}
