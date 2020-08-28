[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/rahul1990gupta/indic-nlp-datasets)

## Overview
This library provides Indian regional language datasets in an easy to use sklearn.dataset API format. You are free to use it in an application intended for commercial uses. 

![indic-nlp-datasets](https://github.com/rahul1990gupta/indic-nlp-datasets/workflows/build/badge.svg)
[![Coverage](https://img.shields.io/codecov/c/github/rahul1990gupta/indic-nlp-datasets.svg?style=flat-square)](https://codecov.io/github/rahul1990gupta/indic-nlp-datasets?branch=master)

## Installation 
You can use `pip` to install this library 

```bash
pip install indic-nlp-datasets
```
To install the latest version of the datasets, use 
```bash 
pip install git+https://github.com/rahul1990gupta/indic-nlp-datasets.git@master
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
Devdas| 300 KB | `load_devdas`| hi



## Getting started
After installation, you can start by importing the dataset 
```python
from idatasets import load_devdas
devdas = load_devdas()
print(devdas.desc) # prints description of the data
print(devdas.created_at) # date/year when dataset was created
for sent in devdas.data:
    # process text chunks
```
