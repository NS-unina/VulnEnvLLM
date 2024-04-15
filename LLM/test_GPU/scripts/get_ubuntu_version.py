import requests
import sys


def get_ubuntu_version(package_name, package_version) -> str:
    url = f"https://api.launchpad.net/1.0/ubuntu/+archive/primary?ws.op=getPublishedSources&source_name={package_name}&exact_match=false"
    try:
        response = requests.get(url)
    except:
        print("Connection Error")
        return "ubuntu:20.04"
    if response.status_code == 200:
        data = response.json()
        versions = []
        for entry in data["entries"]:
            if package_version is not None:  # If specific version is provided
                if (
                    entry["source_package_version"] == package_version
                ):  # Check if the version is the same
                    versions.append(entry["distro_series_link"].rsplit("/")[-1])
            else:  # If no specific version is provided
                versions.append(
                    entry["distro_series_link"].rsplit("/")[-1]
                )  # Add all versions
        if len(versions) == 0:
            return "ubuntu:20.04"
        versions = [
            version_dict.get(version)
            for version in versions
            if version_dict.get(version) is not None
        ]  # Convert the versions list to the value corresponding to version_dict
        return "ubuntu:" + str(max(versions, key=float))
    else:
        return "ubuntu:20.04"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_ubuntu_version.py <package_name> <package_version>")
        sys.exit(1)

    package_name = sys.argv[1]
    package_version = sys.argv[2]

    ubuntu_version = get_ubuntu_version(package_name, package_version)

    if ubuntu_version:
        print(
            "Latest Ubuntu version compatible with {} {}: {}".format(
                package_name, package_version, ubuntu_version
            )
        )
    else:
        print(
            "No Ubuntu versions found for {} {}".format(package_name, package_version)
        )


version_dict = {
    "precise": "12.04",
    "quantal": "12.10",
    "raring": "13.04",
    "saucy": "13.10",
    "trusty": "14.04",
    "utopic": "14.10",
    "vivid": "15.04",
    "wily": "15.10",
    "xenial": "16.04",
    "yakkety": "16.10",
    "zesty": "17.04",
    "artful": "17.10",
    "bionic": "18.04",
    "cosmic": "18.10",
    "disco": "19.04",
    "eoan": "19.10",
    "focal": "20.04",
    "groovy": "20.10",
    "hirsute": "21.04",
    "impish": "21.10",
    "jammy": "22.04",
}
