import os
from idatasets.datasets.util import download_file 


def test_download_file():
    occ_an_url = "https://oscar-public.huma-num.fr/shuffled/an.txt.gz"
    fpath = download_file(occ_an_url)
    assert os.path.exists(fpath)
    os.remove(fpath)
    assert not os.path.exists(fpath)

