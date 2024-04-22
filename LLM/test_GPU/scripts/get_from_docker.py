import requests


def get_ubuntu_version(package_name, package_version) -> str:
    """
    Retrieves the latest and compatible Ubuntu version for a given package.

    Args:
        package_name (str): The name of the package.
        package_version (str): The specific version of the package (optional).

    Returns:
        str: The latest and compatible Ubuntu version in the format 'ubuntu:<version>', if not found, returns 'ubuntu:20.04'.
    """
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


def get_official_image(target_image: str) -> str:
    """
    Retrieves the official Docker image from the Docker Hub API.

    Args:
        target_image (str): The name of the target image to search for.

    Returns:
        str: The lowercase name of the target image if found, otherwise an empty string.
    """
    # Start at first page
    i = 1
    # List to store official images
    official_images = []
    # Define the Docker Hub API endpoint for official images
    while True:
        endpoint = (
            f"https://hub.docker.com/v2/repositories/library/?page={i}&page_size=100"
        )
        # Send GET request to the Docker Hub API
        response = requests.get(endpoint)
        # Check if request was successful
        if response.status_code == 404:
            # No more pages available
            break
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Get list of repositories
            repositories = data.get("results", [])
            # Extract repository names
            official_images.extend([repo["name"] for repo in repositories])
            # Move to next page
            i += 1
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return ""
    if target_image.lower() in official_images:
        return target_image.lower()
    else:
        return ""
        


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
