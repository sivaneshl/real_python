"""
Fetch and parse people names from IMDB

Usage:
$ python download_imdb.py
"""

import csv
import gzip
import shutil
import tempfile
import urllib.request


def main():
    print("Fetching data from IMDB...")

    with open('names.txt', 'w', encoding='utf-8') as destination:
        destination.writelines(names())

    with open('names.txt', encoding='utf-8') as source, open('sorted_names.txt', 'w', encoding='utf-8') as destination:
        destination.writelines(sorted(source.readlines()))

    print("Created 'names.txt' and 'sorted_names.txt'")


def names():
    """
    Return a generator of names with trailing new line
    """
    url = "https://datasets.imdbws.com/name.basics.tsv.gz"
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(mode='w+b') as archive:
            shutil.copyfileobj(response, archive)
            archive.seek(0)
            with gzip.open(archive, mode='rt', encoding='utf-8') as tsvfile:
                tsv = csv.reader(tsvfile, delimiter='\t')
                next(tsv)  # skip th header
                for record in tsv:
                    full_name = record[1]
                    yield f"{full_name}\n"


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Aborted')
