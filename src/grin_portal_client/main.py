#!/usr/bin/env python3
# coding: utf-8
from grin_portal_client.Question import Question
from grin_portal_client.ShinySolver import ShinySolver, NotSolvable


def main():
    question = Question("NM_000834.5*", "GRIN2B", "c.1176dupA")
    try:
        answer = ShinySolver(question).solve()
        print(f"Answer: {answer}")
    except NotSolvable:
        print("Question was not solvable")
