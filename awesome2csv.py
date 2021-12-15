# awesome2csv.py

## Dependencies

import csv      # obviously
import os       # for nice exit codes
import re       # for regex magic
import glob     # for globbing, might be obsolete later
from pathlib import Path  # for path handling

## Script setup

### Path to markdown file. Change it according to your file location. If non is given the script looks in the current directory.
path_to_input_file = Path("input.md")

### Path to existing database. If non is given, look in the current dir. Unsupported
#path_to_db = Path("")

### Path to output file.
output_file = Path("database.csv")

### Choose what columns should be created and parsed for:
#  (or comment out by adding a '#' character at the start of the line)
fields = ['project_name',
          'oneliner',
          'git_namespace',
          'topics'
          ] 

## Scripty stuff, aka. what we are here for

print('\nawesome2csv.py\n')


# Find a markdown file in cwd

if not path_to_input_file.exists():
    print('Looking for markdown files...')
    list_markdown_file = glob.glob('*.md')
    for i in list_markdown_file:
        if not i.startswith('README'):
            a_markdown_file = i
            print(a_markdown_file)
            if a_markdown_file:
                currentDirectory = os.getcwd()
                path_to_input_file = str(currentDirectory + '/' + a_markdown_file)
                print('File found:\n' + path_to_input_file)
            else:
                print('Markdown file: None found\n'+
                        'Put a markdown file somewhere here, or provide a path to it.\n'+
                        'Exiting.')
                os._exit(1)
else:
    print('Using given input file:\n' + str(Path(path_to_input_file)))

# Read the input file

current_topics = []
current_project = []

# Ignore lines that start with anything else but '#' or '-'
# Ignore the toc
# Write the name of headings into the 'current_topics' list
# Extract the fields from each project line and add it accordingly into the 'current_project' var
# write the extracted data into the output file
# As soon as a new heading start, add new 'current_topics' and continue until done

# Extract meta data from the links...

os._exit(0)
