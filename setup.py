# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pubmed2bib',
    version='1.0',
    description='PubMed to BibTeX Scraper:A web scraping tool that reads a list of PMIDs from PubMed and returns a file with corresponding BibTeX data.',
    long_description=readme,
    author='Eduardo A. P Gomes',
    author_email='eng.eduardoapg@gmail.com',
    url='https://github.com/eduardoapgomes/pubmed_pmid_to_bibtex_scraper',
    license='MIT License',
    packages=find_packages(where="pubmed2bib"),
    install_requires=['joblib==1.3.1', 'pubmed-bibtex==1.0.0'],
)
