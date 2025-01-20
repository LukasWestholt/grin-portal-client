#!/usr/bin/env python3
# coding: utf-8

class Question:
    def __init__(self, transcript, gene, variant_c_dna):
        self.transcript = transcript
        self.gene = gene
        self.variant_c_dna = variant_c_dna

    def __str__(self):
        return (self.__class__.__name__, self.transcript, self.gene, self.variant_c_dna)
