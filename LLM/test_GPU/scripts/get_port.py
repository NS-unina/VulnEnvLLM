import csv
from requests import get
from os import path, chdir


def download_csv_from_url(url, save_path):
    response = get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")


def port_csv_to_list():
    """
    Retrieves a list of port data from a CSV file.

    This function downloads a CSV file from a given URL if it doesn't exist locally.
    It then reads the CSV file and returns a list of dictionaries, where each dictionary
    represents a row in the CSV file with only the first 4 columns.

    Returns:
        A list of dictionaries representing port data.
    """
    # Change the current directory to the script's directory
    chdir(path.dirname(path.realpath(__file__)))
    save_path = "service-names-port-numbers.csv"
    url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
    if not path.exists(save_path):
        download_csv_from_url(url, save_path)
    data_list = []
    with open(save_path, "r", newline="") as file:
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
    return " ".join(common_programs.get(package_name.lower(), get_ports_csv(package_name)))


def get_ports_csv(package_name: str) -> str:
    csv_list: list = port_csv_to_list()
    matching_elements = [
        element for element in csv_list if element["Service Name"] in package_name
    ]
    port_numbers = ""
    for e in matching_elements:
        port_numbers += f"{e['Port Number']} "
    return port_numbers


common_programs = {
    "nginx": ["80", "443"],
    "apache": ["80", "443"],
    "ssh": ["22"],
    "openssh": ["22"],
    "openssh-client": ["22"],
    "openssh-server": ["22"],
    "mysql": ["3306"],
    "postgresql": ["5432"],
    "mongodb": ["27017"],
    "redis": ["6379"],
    "ftp": ["21"],
    "telnet": ["23"],
    "smtp": ["25"],
    "dns": ["53"],
    "http": ["80"],
    "pop3": ["110"],
    "imap": ["143"],
    "snmp": ["161", "162"],
    "https": ["443"],
    "dhcp": ["67", "68"],
    "oracle": ["1521"],
    "mssql": ["1433"],
    "rdp": ["3389"],
    "rabbitmq": ["5672"],
    "memcached": ["11211"],
    "ntp": ["53"],
    "docker": ["2375", "2376"],
    "elasticsearch": ["9200", "9300"],
    "kafka": ["9092"],
    "zookeeper": ["2181"],
    "tomcat": ["8080", "8443"],
    "wildfly": ["8080", "8443"],
    "glassfish": ["8080", "8181"],
    "node": ["3000"],
    "kubernetes": ["6443"],
    "grafana": ["3000"],
    "smb": ["445"],
    "samba": ["445"],
    "git": ["22", "80", "443", "9418"],
    "jenkins": ["8080", "8443"],
    "nagios": ["80", "443"],
    "radius": ["1812", "1813"],
    "rails": ["3001"],
    "graphql": ["8080"],
    "prometheus": ["9090"],
    "consul": ["8500"],
    "vault": ["8200"],
    "etcd": ["2379"],
    "minio": ["9000"],
    "cassandra": ["7000"],
    "couchdb": ["5984"],
    "neo4j": ["7474"],
    "hadoop": ["50070"],
    "spark": ["7077"],
    "hbase": ["16010"],
    "hive": ["10000"],
    "flume": ["44444"],
    "kibana": ["5601"],
    "logstash": ["5044"],
    "filebeat": ["5044"],
    "beats": ["5044"],
    "splunk": ["8000"],
    "graylog": ["9000"],
    "zabbix": ["10050"],
    "nifi": ["8080"],
    "druid": ["8082"],
    "superset": ["8088"],
    "airflow": ["8080"],
    "presto": ["8080"],
    "kong": ["8000"],
    "traefik": ["80"],
    "haproxy": ["80"],
    "jboss": ["8080"],
    "jetty": ["8080"],
    "weblogic": ["7001"],
    "websphere": ["9060"],
    "jira": ["8080"],
    "confluence": ["8090"],
    "gitlab": ["80", "443"],
    "sonarqube": ["9000"],
    "nexus": ["8081"],
    "artifactory": ["8081"],
    "harbor": ["80", "443"],
    "portainer": ["9000"],
    "rancher": ["80", "443"],
    "wordpress": ["80", "443"],
    "drupal": ["80", "443"],
    "magento": ["80", "443"],
    "prestashop": ["80", "443"],
    "opencart": ["80", "443"],
    "odoo": ["8069"],
    "redmine": ["3000"],
    "moodle": ["80"],
}
