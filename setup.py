#!/usr/bin/env python
# coding: utf-8

if __name__ == "__main__":
    from setuptools import setup, find_packages

    setup(
        name="indic-nlp-datasets", 
        packages=find_packages(),
        include_package_data=True,
        install_requires=['tqdm'],
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ],
        entry_points={
            "console_scripts": [
                "wikiextractor = idatasets.vendor.WikiExtractor:main"
            ]
        },
    )
