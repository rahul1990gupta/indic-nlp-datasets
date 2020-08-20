from os import path 
from .util import Bunch
from typing import Iterator, Dict


BASEPATH = path.dirname(path.abspath(__file__))
TXT_FILE_PATH = path.join(BASEPATH, "devdas.txt")


def get_devdas_gen() -> Iterator:
    with open(TXT_FILE_PATH, encoding="utf-8") as fh:
        text = fh.read()
        for paragraph in text.split('\n'):
            if paragraph.strip() != "":
                yield paragraph

def load_devdas() -> Dict:
    return Bunch(
        data=get_devdas_gen(),
        size="300 KB",
        desc="A love triangle novel by Sharatchandra written in 1920."\
            "where Devdas is the lead male character",
        created_at="2020" 
    )
