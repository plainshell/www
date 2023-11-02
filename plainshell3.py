#!/usr/bin/env python3

import os
import sys
import re
from markdown import Markdown
from io import StringIO

# Function to read README.md file
def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

# Finds code blocks, extracts, saves to list and returns
def find_code_blocks(md_file_text):
    md_to_html_converter = Markdown()
    html = md_to_html_converter.convert(md_file_text)
    code_blocks = re.findall('```(.+?)```', md_file_text, re.DOTALL)

    return code_blocks


def docker():
    # Check if Docker is installed
    if os.system("docker -v") != 0:
        print("Docker is not installed. Installing Docker...")
        os.system("curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh")
    
    # Pull Python image
    os.system("docker pull python")
    
    # Run a Python script
    os.system("docker run python python -c 'print(\"Hello, World!\")'")

def main():
    filename = "README.md"
    md_file_text = read_file(filename)
    code_blocks = find_code_blocks(md_file_text)

    while True:
        for index, code_block in enumerate(code_blocks):
            print(f'{index + 1}. {code_block[:75]}...')

        block_num_to_execute = input(f'\nEnter a block number to execute ("q" to quit program): ')

        if block_num_to_execute.lower() == 'q':
            break

        is_integer = re.match("^[1-9][0-9]*$", block_num_to_execute)
        is_in_range = is_integer and (1 <= int(block_num_to_execute) <= len(code_blocks))

        if not is_in_range:
            print(f'Invalid option; expected integer between 1 and {len(code_blocks)}\n')
            continue

        os.system(code_blocks[int(block_num_to_execute) - 1])

if __name__ == "__main__":
    docker()
    main()
