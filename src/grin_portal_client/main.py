#!/usr/bin/env python3
# coding: utf-8
import argparse
import pandas as pd

from grin_portal_client.Question import Question
from grin_portal_client.ShinySolver import ShinySolver, NotSolvable

def process(transcript, gene, variant_c_dna) -> tuple[str, str, str]:
    """
    Beispiel-Funktion, die die Daten verarbeitet.
    Du kannst hier die Logik für die Verarbeitung der Zeilen hinzufügen.
    """
    question = Question(transcript, gene, variant_c_dna)
    print(f"Processed {transcript}, {gene}, {variant_c_dna}")
    try:
        answer = ShinySolver(question).solve()
        print(f"Answer: {answer}")
        answer = (answer.acmg_classification, answer.detailed_effect, answer.protein)
    except (NotSolvable, TypeError):
        print("Question was not solvable")
        answer = ("", "", "")
    return answer

def process_stack(input_file, output_file):
    # Excel-Datei einlesen
    df = pd.read_excel(input_file)
    # df = df.iloc[0:1]

    # Sicherstellen, dass die erwarteten Spalten vorhanden sind
    required_columns = ["transcript", "gene", "variant_c_dna"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Die Spalte '{col}' fehlt in der Eingabedatei.")

    df[["acmg_classification", "detailed_effect", "protein"]] = df.apply(
        lambda row: pd.Series(process(row["transcript"], row["gene"], row["variant_c_dna"])),
        axis=1
    )

    # Ergebnisse in eine neue Excel-Datei schreiben
    df.to_excel(output_file, index=False)
    print(f"Verarbeitung abgeschlossen. Ergebnisse gespeichert in '{output_file}'.")


def main():
    # ArgumentParser erstellen
    parser = argparse.ArgumentParser(
        description="Ein Skript zum Verarbeiten von Transkripten, Genen und Varianten."
    )

    # Kommandozeilenargumente definieren
    parser.add_argument(
        '--transcript', '-t',
        type=str,
        help="Das Transkript, das verarbeitet werden soll."
    )
    parser.add_argument(
        '--gene', '-g',
        type=str,
        help="Das Gen, das verarbeitet werden soll."
    )
    parser.add_argument(
        '--variant_c_dna', '-d',
        type=str,
        help="Die cDNA-Variante, die verarbeitet werden soll."
    )
    parser.add_argument(
        '--input', '-i',
        type=str,
        help="Pfad zur Eingabe-Excel-Datei."
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help="Pfad zur Ausgabe-Excel-Datei."
    )

    # Argumente parsen
    args = parser.parse_args()

    if all([args.transcript, args.gene, args.variant_c_dna]):
        process(args.transcript, args.gene, args.variant_c_dna)

    elif all([args.input, args.output]):
        process_stack(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
