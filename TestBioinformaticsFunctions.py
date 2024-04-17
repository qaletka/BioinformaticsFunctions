from gc_content import gc_content
from transcribe_dna_to_rna import transcribe_dna_to_rna
from translate_rna_to_protein import translate_rna_to_protein
from levenshtein_distance import levenshtein_distance

import unittest


class TestBioinformaticsFunctions(unittest.TestCase):

    def test_gc_content(self):
        seq1 = "ATGCATGC"
        seq2 = "AAAAAA"
        self.assertEqual(gc_content(seq1), 50.0)
        self.assertEqual(gc_content(seq2), 0.0)

    def test_transcribe_dna_to_rna(self):
        dna_seq = "ATGCATGC"
        self.assertEqual(transcribe_dna_to_rna(dna_seq), "AUGCAUGC")

    def test_translate_rna_to_protein(self):
        rna_seq = "AUGCAUGC"
        self.assertEqual(translate_rna_to_protein(rna_seq), "MHX")

    def test_levenshtein_distance(self):
        seq1 = "kitten"
        seq2 = "sitting"
        self.assertEqual(levenshtein_distance(seq1, seq2), 3)


if __name__ == '__main__':
    unittest.main()
