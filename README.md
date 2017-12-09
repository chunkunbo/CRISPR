# CRISPR
Description

The CRISPR/Cas system is a bacteria immune system protecting cells from foreign genetic elements. One version that attracted special interest is CRISPR/Cas9, because it can be modified to edit genomes at targeted locations. However, the risk of binding and damaging off-target locations limits its power. Identifying all these potential off-target sites is thus important for users to effectively use the system to edit genomes. This process is computationally expensive, especially when one allows more differences in gRNA targeting sequences. 
We can model the process as an approximate matching problem and use automata to identify these off-targets. Each automaton recognizes each gRNA targeting sequence and we can process a huge number of gRNA targeting sequences simultaneously. For current design, we focus on Hamming distance, but the design can be easily extended to Edit distance or other user-specified distance.
