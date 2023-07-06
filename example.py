# The pubmed2bib.convert module provides functionality to convert PubMed identifiers (PMIDs) to BibTeX format. This documentation will describe the usage and available functions of this module.

import pubmed2bib.converter as converter

# Example usage
input_filename = 'sample_pmids.txt'
output_filename = 'converted_references.bib'

problematic_pmids = converter.pmids_to_bibtex(
    input_filename, output_filename)
