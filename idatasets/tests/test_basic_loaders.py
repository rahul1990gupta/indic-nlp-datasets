import types
import os
from datasets.basic_loaders import get_data_gen


def test_data_gen(root):
    fpath = os.path.join(root, "fixture", "bar.txt.gz")
    gen = get_data_gen(fpath)
    assert isinstance(gen, types.GeneratorType)
    assert len(list(gen)) == 4
