import os
from .util import get_file, Bunch


URL = "www.cfilt.iitb.ac.in/iitb_parallel/iitb_corpus_download/monolingual.hi.tgz"


def get_monolingual_gen(extracted_dir):
    """
    One document at a time
    """

    for (dirpath, dirnames, filenames) in os.walk(extracted_dir):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as fopen:
                for line in fopen.readlines():
                    yield line


def load_monolingual_hi(url=URL):
    untar_path = get_file(url, untar=True)
    return Bunch(
        data=get_monolingual_gen(untar_path),
        desc="Oscar Common Crawl dataset",
        created_at="2019",
        size="17 GB", 
    )
