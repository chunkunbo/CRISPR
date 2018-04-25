The input for searching for gRNA off-target are usually genomes/chromosomes, which can be downloaded from http://hgdownload.cse.ucsc.edu/downloads.html.
This website includes various genomes from different species.
In our paper, we use human genome (hg38) as an example to study the performance (http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/), which is the most common use case in prior papers.
Users can either use genomes/chromosomes from this website or use there own DNA sequences.
However, there can't be by any new-line symbols inside the input. Users should be careful if they use their own file.
We provide the following script that can remove new-line symbols. This script will generate a new file named newfile.txt

## Example Usage
```
$ python rmnewline.py filename
```
Users then can rename the newly generated file.
