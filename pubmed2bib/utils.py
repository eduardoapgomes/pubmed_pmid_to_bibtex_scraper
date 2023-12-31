from pubmed_bibtex import bibtex_entry_from_pmid
from joblib import Parallel, delayed


def num_of_lines_in_file(filename):
    """
    Count the number of lines in a file.

    Args:
        filename (str): Name of the file.

    Returns:
        int: Number of lines in the file.
    """
    with open(filename, "r") as f:
        N = sum(1 for _ in f)
    return N


def write_new_bib_entry(bib_entry, fileoutname):
    """
    Write a new BibTeX entry to the output file.

    Args:
        bib_entry (str): BibTeX entry to be written.
        fileoutname (str): Name of the output file.
    """
    with open(fileoutname, 'a', encoding="utf-8") as file_out:
        file_out.write(bib_entry + '\n')


def new_bib_entry(line, k, N, fileoutname):
    """
    Process each line to generate a new BibTeX entry.
    Args:
        line (str): Line from the input file containing a PMID.
        k (int): Index of the line being processed.
        N (int): Total number of lines in the input file.
        fileoutname (str): Name of the output file.

    Returns:
        str or None: BibTeX entry if successfully generated, None otherwise.
    """
    counter = 0
    while (1):
        counter += 1
        print(f"Processing PMID {line} ({k} of {N}) - Attempt: {counter}")
        bib_entry = bibtex_entry_from_pmid(line.strip())
        if bib_entry != None:
            break
        if counter >= 10:
            print(f"PMID {line} ({k} of {N})  not found")
            return line
    write_new_bib_entry(bib_entry, fileoutname)
    pass
