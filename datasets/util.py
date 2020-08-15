import os
from urllib.error import URLError, HTTPError
from urllib.request import urlretrieve
import tqdm
import tarfile
import zipfile
import shutil


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_file(origin, cache_subdir="datasets"):
    fname = origin.split("/")[-1]
    datadir_base = os.path.expanduser(os.path.join("~", ".keras"))
    if not os.access(datadir_base, os.W_OK):
        datadir_base = os.path.join("/tmp", ".keras")
    datadir = os.path.join(datadir_base, cache_subdir)
    if not os.path.exists(datadir):
        os.makedirs(datadir)

    fpath = os.path.join(datadir, fname)
    if os.path.exists(fpath):
        return fpath

    global progbar
    progbar = None
    
    def dl_progress(count, block_size, total_size):
        global progbar
        if progbar is None:
            progbar = tqdm.tqdm(total=total_size)
        else:
            progbar.update(block_size)
    
    error_msg = "URL fetch failure on {}: {} -- {}"
    if not os.path.exists(fpath):
        try:
            try:
                urlretrieve(origin, fpath, dl_progress)
            except URLError as e:
                raise Exception(error_msg.format(origin, e.errno, e.reason))
            except HTTPError as e:
                raise Exception(error_msg.format(origin, e.code, e.msg))
        except (Exception, KeyboardInterrupt):
            if os.path.exists(fpath):
                os.remove(fpath)
            raise
        progbar = None
    return fpath


def get_file(origin, untar=False, unzip=False, cache_subdir="datasets"):
    """Downloads a file from a URL if it not already in the cache."""
    # https://raw.githubusercontent.com/fchollet/keras/master/keras/utils/data_utils.py
    # Copyright Francois Chollet, Google, others (2015)
    # Under MIT license
    fname = origin.split("/")[-1].split(".")[0]
    datadir_base = os.path.expanduser(os.path.join("~", ".keras"))
    if not os.access(datadir_base, os.W_OK):
        datadir_base = os.path.join("/tmp", ".keras")
    datadir = os.path.join(datadir_base, cache_subdir)
    if not os.path.exists(datadir):
        os.makedirs(datadir)
    if untar or unzip:
        untar_fpath = os.path.join(datadir, fname)
        if unzip:
            fpath = untar_fpath + ".zip"
        else:
            fpath = untar_fpath + ".tar.gz"
    else:
        fpath = os.path.join(datadir, fname)
    global progbar
    progbar = None

    def dl_progress(count, block_size, total_size):
        global progbar
        if progbar is None:
            progbar = tqdm.tqdm(total=total_size)
        else:
            progbar.update(block_size)

    error_msg = "URL fetch failure on {}: {} -- {}"
    if not os.path.exists(fpath):
        try:
            try:
                urlretrieve(origin, fpath, dl_progress)
            except URLError as e:
                raise Exception(error_msg.format(origin, e.errno, e.reason))
            except HTTPError as e:
                raise Exception(error_msg.format(origin, e.code, e.msg))
        except (Exception, KeyboardInterrupt):
            if os.path.exists(fpath):
                os.remove(fpath)
            raise
        progbar = None

    if untar:
        if not os.path.exists(untar_fpath):
            print("Untaring file...")
            tfile = tarfile.open(fpath, "r:gz")
            try:
                tfile.extractall(path=datadir)
            except (Exception, KeyboardInterrupt):
                if os.path.exists(untar_fpath):
                    if os.path.isfile(untar_fpath):
                        os.remove(untar_fpath)
                    else:
                        shutil.rmtree(untar_fpath)
                raise
            tfile.close()
        return untar_fpath
    elif unzip:
        if not os.path.exists(untar_fpath):
            print("Unzipping file...")
            with zipfile.ZipFile(fpath) as file_:
                try:
                    file_.extractall(path=datadir)
                except (Exception, KeyboardInterrupt):
                    if os.path.exists(untar_fpath):
                        if os.path.isfile(untar_fpath):
                            os.remove(untar_fpath)
                        else:
                            shutil.rmtree(untar_fpath)
                    raise
        return untar_fpath
    return fpath


class Bunch(dict):
    """Container object exposing keys as attributes
    Bunch objects are sometimes used as an output for functions and methods.
    They extend dictionaries by enabling values to be accessed by key,
    `bunch["value_key"]`, or by an attribute, `bunch.value_key`.
    Examples
    --------
    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass
