# PubMed BibTeX Scraper

**PubMed BibTeX Scraper**: A web scraping tool that reads a list of PMIDs from PubMed and returns a file with corresponding BibTeX data.

Key Features:

* Efficiently reads a list of PMIDs from PubMed
* Automates the retrieval of bibliographic details
* Provides a user-friendly example to facilitate the process
* Outputs a file containing the complete BibTeX data for each article

This tool streamlines the process of gathering BibTeX information from PubMed, saving you valuable time and effort. Whether you're a researcher, academic, or anyone in need of BibTeX data, this scraper simplifies the task and enhances your workflow.

## Example of Usage

```python
import pubmed2bib.converter as converter

# Example usage
input_filename = 'sample_pmids.txt'
output_filename = 'converted_references.bib'

problematic_pmids = converter.pmids_to_bibtex(
    input_filename, output_filename)
```

## Functions

### pmid_to_bib(filename, fileoutname)

Converts PubMed identifiers (PMIDs) listed in a text file to BibTeX format and writes the converted references to an output file.

#### Parameters:

* `filename` (str): The name of the input text file containing PMIDs. Each PMID should be listed on a separate line.
* `fileoutname` (str): The name of the output file where the converted BibTeX references will be written.

#### Returns:

* `problematic_pmids` (list): A list of PMIDs that encountered issues during the conversion process. These PMIDs were not successfully converted to BibTeX format.
