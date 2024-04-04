import requests
import sys

def get_ubuntu_versions(package_name, package_version):
    url = f"https://api.launchpad.net/1.0/ubuntu/+archive/primary?ws.op=getPublishedSources&source_name={package_name}&exact_match=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        versions = []
        for entry in data['entries']:
            if entry['source_package_version'] == package_version:
                versions.append("ubuntu:" + entry['distro_series_link'].rsplit("/")[-1])
        return versions
    else:
        print("Errore durante la richiesta delle informazioni.")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_ubuntu_version.py <package_name> <package_version>")
        sys.exit(1)

    package_name = sys.argv[1]
    package_version = sys.argv[2]

    ubuntu_versions = get_ubuntu_versions(package_name, package_version)

    if ubuntu_versions:
        print("Ubuntu versions compatible with {} {}: {}".format(package_name, package_version, ", ".join(ubuntu_versions)))
    else:
        print("No Ubuntu versions found for {} {}".format(package_name, package_version))
