#!/usr/bin/env python3
# coding: utf-8

class Answer:
    def __init__(self, acmg_classification, detailed_effect, protein):
        self.acmg_classification = acmg_classification
        self.detailed_effect = detailed_effect
        self.protein = protein

    def __str__(self):
        return str((self.__class__.__name__, self.acmg_classification, self.detailed_effect, self.protein))
