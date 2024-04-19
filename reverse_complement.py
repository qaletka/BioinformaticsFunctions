# Funkcja do do odwracania sekwencji DNA

def reverse_complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse_complement_sequence = ''.join(complement_dict[base] for base in reversed(dna_sequence))
    return reverse_complement_sequence
