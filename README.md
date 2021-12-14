# awesome2csv

*Note: Nothing to see here yet. Move along...*

python3 script to parse Awesome list-style Markdown files and create a CSV file including meta data from it as a database.
Please hand in any issues you encounter using this script. Pull requests or feature ideas and any constructive feedback are welcome as well.

## What will it do?

Look in the given directory for a Markdown (.md) file.
Make some assumptions about that files structure.
The assumptions are based on the rules the [Linter for Awesome lists](https://github.com/sindresorhus/awesome-lint).

Check the file structure for already existing database.

Detect categories and assign them based on the category the links are found in.

On a rerun, only check for changes in the database and add those accordingly.

## Usage

Install some dependencies (that you might already have):

...

Run:

```
`python3 awesome2csv.py`
```

To print the help information, run:

```
`python3 awesome2csv.py -h`
```

To hand over a file from a specific location, run:
```
`python3 awesome2csv.py /path/to/that/file`
```

