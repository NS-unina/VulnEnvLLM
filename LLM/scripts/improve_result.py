from get_port_dict import port_csv_to_list
from get_ubuntu_version import get_ubuntu_version
import re

def get_ports(package_name: str) -> str:
    csv_list : list = port_csv_to_list()
    matching_elements = [element for element in csv_list if element['Service Name'] in package_name ]
    port_numbers = ""
    for e in matching_elements:
        if(e['Transport Protocol'] == ''):
            port_numbers += f"{e['Port Number']} "
        else:
            port_numbers += f"{e['Port Number']}/{e['Transport Protocol']} "
    return port_numbers

def improve_result(prompt:str, output: str) -> str:
    """
    Improve the result by adjusting the right Ubuntu versions and the right exposed port number.
    Args:
        prompt (str): The original prompt formatted as "Generate a dockerfile of <package_name> <package_version> ...".
        output (str): The original output which is actually a dockerfile. 
    Returns:
        str: The improved dockerfile.
    """
    splitted = prompt.split(" ")
    package_name = splitted[4].lower()
    package_version : str | None = splitted[5] if len(splitted) > 5 and not splitted[5].isalpha else None

    ubuntu_version : str = get_ubuntu_version(package_name, package_version)
    port_numbers: str = get_ports(package_name)

    # Find any "EXPOSE <port_number>" inside output
    expose_pattern = re.compile(r'EXPOSE \d+')
    if port_numbers != "":
        if expose_pattern.search(output):
            # Replace it with "EXPOSE " + port_numbers
            output = expose_pattern.sub(f'EXPOSE {port_numbers}', output)
        else:
            # If there is no EXPOSE command, add it at the end of the Dockerfile
            output += f'\nEXPOSE {port_numbers}'

    # Find the last occurrence of "FROM <something>" inside output
    from_pattern = re.compile(r'FROM .+')
    matches = list(from_pattern.finditer(output))
    if matches:
        last_match = matches[-1]
        # Replace it with "FROM " + ubuntu_versions
        output = output[:last_match.start()] + f'FROM {ubuntu_version}' + output[last_match.end():]

    return output
   

if __name__ == "__main__":
    prompt = "Generate a dockerfile of openssh on Ubuntu 18.04"
    output = "FROM ubuntu:18.04\nRUN apt-get update\nRUN apt-get install -y nginx\nCMD [\"nginx\"]"
    improved_output = improve_result(prompt, output)
    print(improved_output)