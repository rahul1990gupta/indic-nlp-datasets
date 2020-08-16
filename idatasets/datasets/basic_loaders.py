from .util import download_file, Bunch
import gzip
import bz2
import json

TWEETS_URL = "https://github.com/bedapudi6788/LOIT/releases/download/v1/lit-h.json.bz2"

# Oscar Common Crawl dats
OCC_URL = "https://oscar-public.huma-num.fr/shuffled/hi.txt.gz"

# News data
NEWS_URL = "http://data.statmt.org/news-crawl/hi/news.2019.hi.shuffled.deduped.gz"

HINGLISH_URL = "https://raw.githubusercontent.com/khyathiraghavi/multi_task_code_switched_language_modeling/master/hinglishData/"


def get_data_gen(gzip_fpath):
    with gzip.open(gzip_fpath) as fgz:
        for line in fgz:
            yield line


def load_occ():
    fpath = download_file(OCC_URL)
    return Bunch(
        data=get_data_gen(fpath),
        desc="Oscar Common Crawl dataset",
        created_at="2019",
        size="17 GB", 
    )


def load_news_crawl():
    fpath = download_file(NEWS_URL)
    return Bunch(
        data=get_data_gen(fpath),
        desc="News Crawl sentence level dataset",
        created_at="2019",
        size="472 MB", 
    )


def get_tweet_gen(tweet_fpath):
    with bz2.open(tweet_fpath) as fbz:
        for line in fbz:
            yield json.loads(line)["tweet"]


def load_tweets(url=TWEETS_URL):
    fpath = download_file(url)
    return Bunch(
        data=get_tweet_gen(fpath),
        desc="Indic Twitter dataset",
        created_at="2019",
        size="850 MB", 
    )


def get_hinglish_gen(fpaths):
    for fpath in fpaths:
        with open(fpath) as fp:
            for line in fp:
                yield line


def load_hinglish(base_url=HINGLISH_URL):
    urls = [HINGLISH_URL + t for t in ["train.txt", "valid.txt", "test.txt"]]

    fpaths = [fpath for fpath in download_file(urls)]

    return Bunch(
        data=get_hinglish_gen(fpaths),
        desc="Hinglish dataset",
        created_at="2018",
        size="20 MB", 
    )
