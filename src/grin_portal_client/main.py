#!/usr/bin/env python3
# coding: utf-8
import argparse

from grin_portal_client.Question import Question
from grin_portal_client.ShinySolver import ShinySolver, NotSolvable


def main():

    # ArgumentParser erstellen
    parser = argparse.ArgumentParser(
        description="Ein Skript zum Verarbeiten von Transkripten, Genen und Varianten."
    )

    # Kommandozeilenargumente definieren
    parser.add_argument(
        '--transcript', '-t',
        type=str,
        required=True,
        help="Das Transkript, das verarbeitet werden soll."
    )
    parser.add_argument(
        '--gene', '-g',
        type=str,
        required=True,
        help="Das Gen, das verarbeitet werden soll."
    )
    parser.add_argument(
        '--variant_c_dna', '-d',
        type=str,
        required=True,
        help="Die cDNA-Variante, die verarbeitet werden soll."
    )

    # Argumente parsen
    args = parser.parse_args()

    # Argumente ausgeben oder weiterverarbeiten
    print(f"Transkript: {args.transcript}")
    print(f"Gen: {args.gene}")
    print(f"cDNA-Variante: {args.variant_c_dna}")

    question = Question(args.transcript, args.gene, args.variant_c_dna)
    try:
        answer = ShinySolver(question).solve()
        print(f"Answer: {answer}")
    except NotSolvable:
        print("Question was not solvable")
