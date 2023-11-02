import markdown
import re
import os
import yaml
from subprocess import call

def install(package):
    call(["sudo", "apt-get", "install", "-y", package])

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

if __name__ == "__main__":
    md_content = read_md_file("README.md")
    code_blocks = extract_code_blocks(md_content, "python")
    install("python3-pip")

    while True:
        print("MENU: ")
        for number, script in code_blocks.items():
            print(number, "Show script")
            print(number + ".1", "Run script")

        choice = input("Choose option: ")
        script_id = choice.split('.')[0]
        script = code_blocks[script_id]

        if choice.endswith('.1'):
            exec(script)
        else:
            packages = extract_package_names(script)
            for package in packages:
                call(["sudo", "pip3", "install", package])
            print(script)
