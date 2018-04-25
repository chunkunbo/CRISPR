To use these ANML generators, users need to provide the input for them.
The input file format is as follows: gRNA target sequence followed by certain PAM sequences.
To study the performance of different platforms, we write a simple input generator to produce such files.
The gRNA target sequence is a 20-length DNA sequence randomly seleted from {A, T, G, C}.
Users need to provide the PAM sequence. 
The first parameter is the number of sequences users want to generate. The second one is the PAM sequence.
Users can speficy the output names.

### Example Usage
```
python input_generator.py 100.txt 100 agg > 100.txt
```

# CasOFFinder
One needs to provide two parameters for CasOFFinder ANML generator. The first one is the input file name, which can be generated using the input generator for CasOFFinder. The second one is the distance allowed in the gRNA targeting sequence.
### Example Usage
```
python anml_gen_casoffinder.py 100.txt 1
```

# CasOT
One needs to provide two parameters for CasOT ANML generator. The first one is the input file name, which can be generated using the input generator for CasOT. The second one is the distance allowed in the non-seed region and the third one is the distance allowed in the seed region.

### Example Usage
```
python anml_gen_casot.py 100.txt 2 3
```
