import os
import json
import subprocess 
from .util import Bunch, download_file

URL = "https://dumps.wikimedia.org/hiwiki/20200801/hiwiki-20200801-pages-meta-current.xml.bz2"


def extract_data(fpath, output_dir=None):
    """ Extracts wikipedia docs from the xml dump.
    """
    if not output_dir:
        dirname = os.path.dirname(fpath)
        reldir = os.path.basename(fpath).split('.')[0]
        output_dir = os.path.join(dirname, reldir)

    # Extract if directory is empty
    if len(os.listdir(output_dir)) == 0:
        subprocess.run(
            ["wikiextractor", fpath, "-o", output_dir, "--json"]
        )
    return output_dir


def get_wiki_generator(extracted_dir):
    """
    One document at a time
    """
    for (dirpath, dirnames, filenames) in os.walk(extracted_dir):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as fopen:
                for line in fopen.readlines():
                    yield json.loads(line)["text"]


def load_wikipedia():
    fpath = download_file(URL)
    extracted_dir = extract_data(fpath)
    return Bunch(
        data=get_wiki_generator(extracted_dir),
        desc="Wikipedia page artciles retrieved from dump",
        created_at="2020-08-01",
        size="443 MB",
    )


if __name__ == "__main__":
    load_wikipedia()
