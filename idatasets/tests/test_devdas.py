from idatasets.datasets.devdas import load_devdas

def test_load_devdas():
    devdas = load_devdas()
    paras = list(devdas.data)
    assert len(paras) == 2424
    assert paras[0] == "देवदास"
        
