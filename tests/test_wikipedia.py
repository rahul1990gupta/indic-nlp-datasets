import os
import json
import types
import tempfile
from datasets.wikipedia import (
    extract_data,
    get_wiki_generator,
)


def test_extract_data(root):
    with tempfile.TemporaryDirectory() as tempdir: 
        wikidump_path = "aawiki-20200801-pages-meta-current.xml.bz2"
        fpath = os.path.join(root, "fixture", wikidump_path)    
        extracted_dir = extract_data(fpath, tempdir)
        assert "AA" in os.listdir(tempdir)
        
        fchunk_path = os.path.join(tempdir, "AA", "wiki_00")
        assert os.path.exists(fchunk_path)
        with open(fchunk_path) as fh:
            text = json.loads(fh.readline())["text"]
            assert len(text) > 0 


def test_get_wiki_generator(root):
    with tempfile.TemporaryDirectory() as tempdir: 
        wikidump_path = "aawiki-20200801-pages-meta-current.xml.bz2"
        fpath = os.path.join(root, "fixture", wikidump_path)    
        extracted_dir = extract_data(fpath, tempdir)
        gen = get_wiki_generator(extracted_dir)

        assert isinstance(gen, types.GeneratorType)
        assert len(list(gen)) == 2
