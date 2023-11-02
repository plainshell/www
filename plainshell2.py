#!/usr/bin/env python3
import os
import markdown
import re
import sys
import subprocess

# Parse README.md file and get headers and code blocks
def parse_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    md = markdown.Markdown(extensions=['fenced_code'])
    html = md.convert(text)
    code_blocks = md.parser.blockprocessors['fenced_code'].code_blocks
    return code_blocks

def check_language(lang):
    lang_check = {'python': 'python3 --version', 
              'bash': 'bash --version',
              'ruby': 'ruby --version',
              'perl': 'perl --version'}  

    if lang in lang_check:
        try:
            subprocess.check_output(lang_check[lang],shell=True)
        except Exception:
            print(f"{lang} is not installed. Do you want to install it now?")
            answer = input("Y/N: ")
            if answer.lower() == 'y':
                os.system(f"sudo apt-get install {lang}")
            else:
                print("Exitting...")
                exit(1)
        return True
    else:
        print(f"Language {lang} is not supported in this script.")
        return False

# Run code block in appropriate language
def run_code_block(code_block):
    lang, code = code_block.split("\n", 1)
    if check_language(lang):
        os.system(code)

# Main function
def main():
    filename = "README.md"
    code_blocks = parse_file(filename)

    while True:
        if len(sys.argv) == 1:
            for i, code in enumerate(code_blocks):
                print(f"{i+1} - {code[:100]}...")
            option = input("\nChoose an option (or 'q' to quit): ")
            if option.lower() == 'q':
                break
            else:
                try: 
                    index = int(option) - 1
                    if index < 0 or index >= len(code_blocks):
                        print("\nInvalid option\n")
                    else:
                        run_code_block(code_blocks[index])
                except ValueError:
                    print("\nInvalid option\n")
        else:
            index = int(sys.argv[1])
            if index < 0 or index >= len(code_blocks):
                print("\nInvalid option\n")
            else:
                run_code_block(code_blocks[index])

if __name__ == "__main__":
    main()
