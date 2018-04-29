# CRISPR
## Description

The CRISPR/Cas system is a bacteria immune system protecting cells from foreign genetic elements. One version that attracted special interest is CRISPR/Cas9, because it can be modified to edit genomes at targeted locations. However, the risk of binding and damaging off-target locations limits its power. Identifying all these potential off-target sites is thus important for users to effectively use the system to edit genomes. This process is computationally expensive, especially when one allows more differences in gRNA targeting sequences. 

We can model the process as an approximate matching problem and use automata to identify these off-targets. Each automaton recognizes each gRNA targeting sequence and we can process a huge number of gRNA targeting sequences simultaneously. For current design, we focus on Hamming distance, but the design can be easily extended to Edit distance or other user-specified distance.

## Helpful and instructive images
![mismatch_nocount](https://user-images.githubusercontent.com/10245416/33798054-1b82ba42-dce0-11e7-8422-25638830706f.png)

The above figure shows an automaton design recognizing the sequence “TAATATAG” when the Hamming distance is shorter than 3. The STEs in the ith column store the ith character in the sequence. The odd rows store the DNA characters one wants to match. Because there is no standard for whether uppercase or lowercase letters are used, this design stores both. The even rows match on any other symbol except for the desired character, thus capturing an increase in the Hamming distance. The STEs in odd rows connect to the next STE in the same row and the next STE in the next row. The STEs in even rows connect to the next STE in the next row and the next STE in the third row below them. This allows processing to proceed whether or not the current symbol matched. The structure can be extended to recognize sequences with more mismatches, but will consume more STEs. The STEs in the last column are configured as \textit{reporting} and they will trigger a report when they are activated. This structure is used to build the automata to recognize gRNA off-target sites.

![whole_1pam](https://user-images.githubusercontent.com/10245416/33798076-66de63a6-dce0-11e7-97b6-9a19a8de39c3.png)

One example of gRNA off-target identifying automaton is shown in the above figure. This design allows the mismatch to take place in any position in the gRNA targeting sequence. The design is straightforward and we use the Hamming distance automata to match the gRNA targeting sequence with one mismatch allowed. We then connect the STEs in the last column in the gRNA targeting sequence to the start of the PAM sequence. No mismatches are allowed in the PAM sequence, so we just connect one STE to another. The STE storing the last character is the reporting STE. The STE storing “*” matches with any input symbol so we can match PAM sequences, such as “NGG” in streptococcus pyogenes, where “N” refers to any DNA character in {AaTtGgCc} in this context.
More gRNA off-target identifying autamata can be found in the paper.

## Input Genome/Chromosome
Users can use any genomes/chromosomes as input. However, there can't by any new-line symbols inside the input. Scripts that can remove new-lines symbols are provided.

## ANML Generators
The input formats for ANML generators are as follows. The first 20 characters are the gRNA targeting sequences and the following characters are the PAM sequences.
```
CTCAGGATACGCACTTTGTGagg
CTCCTCTCGTCCGCGTGCTTagg
GAATCCTCCGACGAGATTGGagg
...
```

We compare the automata-based approach with two state-of-the-art tools (CasOFFinder and CasOT), but these tools allow mismatches in different positions, leading to differnet automata designs. Therefore, we provide two differnt ANML generators for CasOFFinder and CasOT respectively. These generators are in the ANML folder.


