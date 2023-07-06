##
from pubmed_bibtex import bibtex_entry_from_pmid
from joblib import Parallel, delayed


def num_of_lines_in_file(filename):
    with open(filename, "r") as f:
        N = sum(1 for _ in f)
    return N


def write_new_bib_entry(bib_entry, fileoutname):
    with open(fileoutname+'.bib', 'a', encoding="utf-8") as file_out:
        file_out.write(bib_entry + '\n')


filename = 'sample_big.txt'
fileoutname = 'references2'
N = num_of_lines_in_file(filename)
file_out = open(fileoutname+'.bib', 'w', encoding="utf-8")
index = 0
with open(filename, 'r', encoding="utf-8") as f:
    def new_bib_entry(line, k, N):
        # return line
        counter = 0
        while (1):
            counter += 1
            bib_entry = bibtex_entry_from_pmid(line.strip())
            if bib_entry != None:
                break
            if counter >= 10:
                return line
        write_new_bib_entry(bib_entry, fileoutname)
        pass
    # Parallel
    Bib = Parallel(n_jobs=-1,
                   verbose=100,
                   timeout=None,
                   return_as='list')(delayed(new_bib_entry)
                                     (f.readline().strip(), k, N)for k in range(N))
    # Try again the files with error (series)
    Bib = [k for k in Bib if k is not None]
    if len(Bib) > 0:
        Bib = Parallel(n_jobs=1,
                       verbose=100,
                       timeout=None,
                       return_as='list')(delayed(new_bib_entry)
                                         (Bib[k], k, len(Bib))for k in range(len(Bib)))
    Bib = [k for k in Bib if k is not None]
if len(Bib) > 0:
    print(f'Report of problematic pmids')
    with open('error_'+fileoutname+'.pmid', 'w', encoding="utf-8") as f:
        for pmid in Bib:
            f.write(pmid + '\n')
            print(f'{pmid}')
else:
    print('All references converted without issues')
print('done!')
