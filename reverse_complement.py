# Funkcja do do odwracania sekwencji DNA

def gc_content(seq):
    gc_count = seq.upper().count('G') + seq.upper().count('C')
    total_bases = len(seq)
    if total_bases == 0:
        return 0
    else:
        return (gc_count / total_bases) * 100
