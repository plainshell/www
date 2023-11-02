import markdown
import re
import os
import yaml
from subprocess import call
import platform


def install(package):
    if platform.system() == 'Linux':
        try:
            distro = platform.linux_distribution()[0]
        except:
            print("Unable to determine Linux distribution")
            return
        if distro == "Ubuntu":
            call(["sudo", "apt-get", "install", "-y", package])
        elif distro == "Fedora":
            call(["sudo", "dnf", "install", "-y", package])
        elif distro == "arch":
            call(["sudo", "pacman", "-S", package])
        else:
            print(f'Unsupported Linux distribution: {distro}')
            return
    elif platform.system() == 'Darwin':
        call(["brew", "install", package])
    elif platform.system() == 'Windows':
        call(["pip", "install", package])
    else:
        print('Unsupported OS')
        return

def read_md_file(file_name):
    with open(file_name, "r") as readme_file:
        readme_content = readme_file.read()
    return readme_content

def extract_code_blocks(md_content, language):
    extracted_code = {}
    html = markdown.markdown(md_content)
    count = 1
    for match in re.finditer('<pre><code class="{}">(.*?)</code></pre>'.format(language), html, re.S):
        script = match.group(1).strip().replace('<br>', '\n').replace('&lt;', '<').replace('&gt;', '>')
        extracted_code[str(count)] = script
        count += 1
    return extracted_code

def extract_package_names(code):
    packages = []
    for line in code.split('\n'):
        if line.startswith('import'):
            packages.append(line.split(' ')[1])
    return packages

def display_menu(code_blocks):
    print("MENU: ")
    for number in code_blocks:
        print(f"{number}. Show script")
        print(f"{number}.1. Run script") 


if __name__ == "__main__":
    md_content = read_md_file("README.md")
    code_blocks = extract_code_blocks(md_content, "python")
    install("python3-pip")

    while True:
        # wywołaj funkcję wyświetlania menu
        display_menu(code_blocks)
        
        choice = input("Choose option: ")
        choice = choice.split('.')
        #script_id, action = choice.split('.')
        if len(choice) < 2:
            print("Invalid input. Please enter the script number and action (e.g. '1.1').")
            continue
        script_id, action = choice

        if script_id not in code_blocks:
            print("Invalid option. Please choose a valid script number.")
            continue

        if action == '1':
            # Uruchom skrypt
            exec(code_blocks[script_id])
        else:
            # Wyświetl skrypt
            print(code_blocks[script_id])
            packages = extract_package_names(code_blocks[script_id])
            for package in packages:
                call(["pip3", "install", package], shell=True)
