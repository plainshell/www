#!/usr/bin/env python3
import os
import sys
import re
from markdown import Markdown
from io import StringIO


# Function to run bash commands
def run_bash_cmd(cmd):
    os.system(cmd)


# Function to simulate switch-case in Python
def run_code(prog):
    choices = {'python': run_bash_cmd}

    func = choices.get(prog.lower(), lambda: 'Invalid language!')
    return func


# Function to read README.md file
def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


# Finds code blocks, extracts, saves to list and returns
def find_code_blocks(md_file_text):
    md_to_html_converter = Markdown()

    html = md_to_html_converter.convert(md_file_text)

    code_block_with_breaks = re.findall('<pre><code class="(.*)">([\s\S]*?)<\/code><\/pre>', html)
    code_block_language_and_code = [(item[0].split()[0], item[1]) for item in code_block_with_breaks]

    return code_block_language_and_code


# Starts respective code block
def runner(code_language, code_text):
    lang_run_cmd = {'python': 'python'}

    check_installed_cmd = {'python': 'python --version'}

    if code_language not in lang_run_cmd or code_language not in check_installed_cmd:
        print(f'Language "{code_language}" is not supported yet, or is invalid.\n')
        return

    is_installed = os.system(check_installed_cmd[code_language])

    if is_installed != 0:
        os.system(f"apt update && apt install {code_language}")
        # TODO: add more sophisticated method of installing programming languages/tools

    os.system(lang_run_cmd[code_language])


def main():
    filename = "README.md"
    md_file_text = read_file(filename)
    code_blocks = find_code_blocks(md_file_text)

    while True:
        for index, code_block in enumerate(code_blocks):
            print(f'{index + 1}. {code_block[0]}: \t{code_block[1][:75]}...')

        block_num_to_execute = input(f'\nEnter a block number to execute ("q" to quit program): ')

        if block_num_to_execute.lower() == 'q':
            break

        is_integer = re.match("^[1-9][0-9]*$", block_num_to_execute)
        is_in_range = is_integer and (1 <= int(block_num_to_execute) <= len(code_blocks))

        if not is_in_range:
            print(f'Invalid option; expected integer between 1 and {len(code_blocks)}\n')
            continue

        runner(code_blocks[int(block_num_to_execute) - 1][0], code_blocks[int(block_num_to_execute) - 1][1])


if __name__ == "__main__":
    main()
