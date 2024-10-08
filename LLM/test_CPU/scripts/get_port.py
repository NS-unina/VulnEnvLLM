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
        if e["Transport Protocol"] == "":
            port_numbers += f"{e['Port Number']} "
        else:
            port_numbers += f"{e['Port Number']}/{e['Transport Protocol']} "
    return port_numbers


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
    "kubernetes": ["6443/tcp"],
    "grafana": ["3000/tcp"],
    "smb": ["445/tcp"],
    "samba": ["445/tcp"],
    "git": ["22/tcp", "80/tcp", "443/tcp", "9418/tcp"],
    "jenkins": ["8080", "8443"],
    "nagios": ["80", "443"],
    "radius": ["1812/udp", "1813/udp"],
    "rails": ["3001/tcp"],
    "graphql": ["8080/tcp"],
    "prometheus": ["9090/tcp"],
    "consul": ["8500/tcp"],
    "vault": ["8200/tcp"],
    "etcd": ["2379/tcp"],
    "minio": ["9000/tcp"],
    "cassandra": ["7000/tcp"],
    "couchdb": ["5984/tcp"],
    "neo4j": ["7474/tcp"],
    "hadoop": ["50070/tcp"],
    "spark": ["7077/tcp"],
    "hbase": ["16010/tcp"],
    "hive": ["10000/tcp"],
    "flume": ["44444/tcp"],
    "kibana": ["5601/tcp"],
    "logstash": ["5044/tcp"],
    "filebeat": ["5044/tcp"],
    "beats": ["5044/tcp"],
    "splunk": ["8000/tcp"],
    "graylog": ["9000/tcp"],
    "zabbix": ["10050/tcp"],
    "nifi": ["8080/tcp"],
    "druid": ["8082/tcp"],
    "superset": ["8088/tcp"],
    "airflow": ["8080/tcp"],
    "presto": ["8080/tcp"],
    "kong": ["8000/tcp"],
    "traefik": ["80/tcp"],
    "haproxy": ["80/tcp"],
    "jboss": ["8080/tcp"],
    "jetty": ["8080/tcp"],
    "weblogic": ["7001/tcp"],
    "websphere": ["9060/tcp"],
    "jira": ["8080/tcp"],
    "confluence": ["8090/tcp"],
    "gitlab": ["80/tcp", "443/tcp"],
    "sonarqube": ["9000/tcp"],
    "nexus": ["8081/tcp"],
    "artifactory": ["8081/tcp"],
    "harbor": ["80/tcp", "443/tcp"],
    "portainer": ["9000/tcp"],
    "rancher": ["80/tcp", "443/tcp"],
    "wordpress": ["80/tcp", "443/tcp"],
    "drupal": ["80/tcp", "443/tcp"],
    "magento": ["80/tcp", "443/tcp"],
    "prestashop": ["80/tcp", "443/tcp"],
    "opencart": ["80/tcp", "443/tcp"],
    "odoo": ["8069/tcp"],
    "redmine": ["3000/tcp"],
    "moodle": ["80/tcp"],
}
