#!/usr/bin/env python3
import os
import markdown
import sys

# Parse README.md file and get headers and code blocks
def parse_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    md = markdown.Markdown(extensions=['meta', 'fenced_code'])
    html = md.convert(text)
    headers =  md.toc_tokens
    code_blocks = md.parser.blockprocessors['fenced_code'].code_blocks
    return headers, code_blocks

# Print help menu with headers
def print_help_menu(headers):
    for i, header in enumerate(headers):
        print(f"{i} - {header['name']}")

# Run code block in appropriate language
def run_code_block(code_block):
    lang, code = code_block.split("\n", 1)
    if lang == "python":
        os.system("pip install -r requirements.txt")
        exec(code)
    elif lang == "bash":
        os.system("bash -c '%s'" % code)
    else:
        print(f"Language {lang} not supported")
        return

# Main function
def main():
    filename = "README.md"
    headers, code_blocks = parse_file(filename)

    if len(sys.argv) == 1:
        print_help_menu(headers)
    else:
        index = int(sys.argv[1])
        if index < 0 or index >= len(code_blocks):
            print("Invalid option")
        else:
            run_code_block(code_blocks[index])

if __name__ == "__main__":
    main()
