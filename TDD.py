# coding: utf-8
from timeit import timeit

class TestFail(Exception): pass

def test_clauses_creator(): raise TestFail("Non implémenté")

def test_sudoku_verifier(): raise TestFail("Non implémenté")

def test_sudoku_generator(): raise TestFail("Non implémenté")

if __name__ == "__main__":
    tests = [
        test_clauses_creator,
        test_sudoku_verifier,
        test_sudoku_generator,
    ]

    # Running tests
    for test in tests:
        try:
            print(f"Test: {test.__name__}")
            timeTaken = timeit(lambda: test(), number=1)
            print(f"✔   Durée: {timeTaken:.2f}s ")
        except TestFail as fail:
                print(f"❌   Erreur: \"{fail}\"")