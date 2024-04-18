from get_port import get_ports
from get_from_docker import get_ubuntu_version, get_official_image
from replace_directive import remove_useless_directive, clean_output

def generate_constraints(prompt: str) -> list:
    """
    Generate the constraint list from the input string.
    Args:
        input (str): The LLM request string.
    Returns:
        list: The constraint list containing in order the image name and version.
    """
    try:
        package_info = prompt.split("Generate a dockerfile of ")[1].split()
        package_name = package_info[0]
        package_version = package_info[1]     

    except IndexError:
        package_name = ""
        package_version = ""
        
    finally:
        image = get_official_image(package_name)
        if image == "":
            image: str = get_ubuntu_version(package_name, package_version)
        port_numbers: str = get_ports(package_name)
        return [image, port_numbers]

def improve_result(output: str) -> str:
    """
    Improve the result by adjusting the right Ubuntu versions and the right exposed port number.
    Args:
        prompt (str): The original prompt formatted as "Generate a dockerfile of <package_name> <package_version> ...".
        output (str): The original output which is actually a dockerfile.
    Returns:
        str: The improved dockerfile.
    """
    output = remove_useless_directive(output)
    output = clean_output(output)
    
    return output


if __name__ == "__main__":
    prompt = "Generate a dockerfile of openssh-client 1:8.2p1-4ubuntu0.11"
    output = 'FROM ubuntu:20.04\nCOPY example2.txt /run/var/example.txt\nADD https://example.com/test.txt ./test.txt\nRUN apt-get update && apt-get install -y openssh-client\nADD example.conf ./example.conf\nCMD ["bash"]'
    improved_output = improve_result(prompt, output)
    print(improved_output)
