## Overview
This library provides Indian regional language datasets in an easy to use sklearn.dataset API format. You are free to use it in an application intended for commercial uses. 

![indic-nlp-datasets](https://github.com/rahul1990gupta/indic-nlp-datasets/workflows/build/badge.svg)
[![Coverage](https://img.shields.io/codecov/c/github/rahul1990gupta/indic-nlp-datasets.svg?style=flat-square)](https://codecov.io/github/rahul1990gupta/indic-nlp-datasets?branch=master)

## Installation 
You can use `pip` to install this library 

```bash
pip install indic-nlp-datasets
```

## Datasets Available
These are the datasets available in the library

Name | Size | submodule| language
 :-- | :---| :-----|:----
Wikipedia| 275 MB| `load_wikipedia`| hi
Oscar Common Crawl| 17 GB| `load_occ`| hi
News Crawl| 472 MB| `load_news_crawl`| hi
Monlingual | 2.45 GB| `load_monolingual`| hi
Tweet Corpus | 875 MB| `load_tweets`| hi
Hinglish Corpus | 18 MB| `load_hinglish`| hi



## Getting started
After installation, you can start by importing the dataset 
```python
from idatasets import load_hinglish
hinglish = load_hinglish()
print(hinglish.desc) # prints description of the data
print(hingligh.created_at) # date/year when dataset was created
for sent in hinglish.data:
    # process sentence
```

