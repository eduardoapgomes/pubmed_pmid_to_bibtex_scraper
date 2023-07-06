from pubmed_bibtex import bibtex_entry_from_pmid
from joblib import Parallel, delayed
from .utils import num_of_lines_in_file, write_new_bib_entry, new_bib_entry


def pmids_to_bibtex(filename, fileoutname):
    """
    Process a file containing PMIDs to generate BibTeX entries.

    Args:
        filename (str): Name of the input file containing PMIDs.
        fileoutname (str): Name of the output file for BibTeX entries.

    Returns:
        list: List of problematic PMIDs.
    """
    N = num_of_lines_in_file(filename)
    file_out = open(fileoutname, 'w', encoding="utf-8")

    # Process each PMID
    with open(filename, 'r', encoding="utf-8") as f:
        # Parallel processing of each line to generate BibTeX entries
        Bib = Parallel(n_jobs=-1,
                       verbose=100,
                       timeout=None,
                       return_as='list')(delayed(new_bib_entry)
                                         (f.readline().strip(), k, N, fileoutname)for k in range(N))
        # Retry processing files with errors
        Bib = [k for k in Bib if k is not None]
        if len(Bib) > 0:
            Bib = Parallel(n_jobs=1,
                           verbose=100,
                           timeout=None,
                           return_as='list')(delayed(new_bib_entry)
                                             (Bib[k], k, len(Bib), fileoutname)for k in range(len(Bib)))
        Bib = [k for k in Bib if k is not None]
    # Manage the PMID files with errors (not found)
    if len(Bib) > 0:
        print(f'Report of problematic pmids')
        with open('error_'+fileoutname+'.pmid', 'w', encoding="utf-8") as f:
            for pmid in Bib:
                f.write(pmid + '\n')
                print(f'{pmid}')
        return Bib
    else:
        print('All references converted without issues')
    print('done!')
    pass
