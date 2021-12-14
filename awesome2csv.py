# awesome2csv.py

## Dependencies

import csv      # obviously
import os       # for nice exit codes
import re       # for regex magic
from pathlib import Path  # for path handling

## Script setup

### Path to markdown file. Change it according to your file location. If non is given the script looks in the current directory.
path_to_input_file = Path("input.md")

### Path to existing database. If non is given, look in the current dir.
path_to_db = Path("")

### Path to output file
path_to_output = Path("")

### Choose what columns should be created and parsed for:
#  (or comment out by adding a '#' character at the start of the line)


## Scripty stuff, aka. what we are here for

print('\nawesome2csv.py\n')

print('Looking for...')
if not path_to_input_file.exists():
    currentDirectory = os.getcwd()
    for file in currentDirectory:
        match = re.search('\.md$', file)
        print(file)
        if match:
            print('Markdown file: found, it is: ' + str(match))
            path_to_input_file = match
        else:
            print('Markdown file: None found\n'+
                  'Put a markdown file somewhere here, or provide a path to it.\n'+
                  'Exiting.')
            os._exit(1)
else:
    print('Markdown file: found, it is: penis ' + str(Path(path_to_input_file)))
    print()




os._exit(0)
