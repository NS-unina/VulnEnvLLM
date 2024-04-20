from get_port import get_ports
from get_from_docker import get_ubuntu_version, get_official_image
from replace_directive import replace_expose, remove_useless_directive, clean_output


def generate_constraints(prompt: str) -> str:
    """
    Generate the constraint list from the input string.
    Args:
        prompt (str): The original prompt formatted as "Generate a dockerfile of <package_name> <package_version> ...".
    Returns:
        str: The constraint string defined as base_image_name:version.
    """
    try:
        package_info = prompt.split("Generate a dockerfile of ")[1].split()
        package_name: str = package_info[0]
        package_version: str = package_info[1]

    except IndexError:
        package_name = ""
        package_version = ""

    finally:
        image = get_official_image(package_name)
        if image == "":
            return get_ubuntu_version(package_name, package_version)   
        if package_version != "":
            image += f":{package_version}"
        return image


def improve_result(prompt: str, output: str) -> str:
    """
    Improve the result by adjusting the right Ubuntu versions and the right exposed port number.
    Args:
        prompt (str): The original prompt formatted as "Generate a dockerfile of <package_name> <package_version> ...".
        output (str): The original output which is actually a dockerfile.
    Returns:
        str: The improved dockerfile.
    """
    try:
        package_info = prompt.split("Generate a dockerfile of ")[1].split()
        package_name: str = package_info[0]
        package_version: str = package_info[1]

    except IndexError:
        package_name = ""
        package_version = ""
    finally:
        port_numbers: str = get_ports(package_name)
        output = replace_expose(output, port_numbers)
        output = remove_useless_directive(output)
        output = clean_output(output)
        return output


if __name__ == "__main__":
    prompt = "Generate a dockerfile of openssh-client 1:8.2p1-4ubuntu0.11"
    output = 'FROM ubuntu:20.04\nCOPY example2.txt /run/var/example.txt\nADD https://example.com/test.txt ./test.txt\nRUN apt-get update && apt-get install -y openssh-client\nADD example.conf ./example.conf\nCMD ["bash"]'
    improved_output = improve_result(prompt, output)
    print(improved_output)
