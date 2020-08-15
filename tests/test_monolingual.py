from datasets.monolingual import load_monolingual_hi


def test_monolingual_hi():
    url = "https://storage.googleapis.com/rgupta-toxicity/monolingual.hi.tgz"

    hi = load_monolingual_hi(url)
    assert hasattr(hi, "data")
    gen = hi.data 
    assert len(list(gen)) == 2
