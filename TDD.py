# coding: utf-8
from timeit import timeit

from main import Sudoku, InvalidSudokuException

class TestFail(Exception): pass

sudoku = Sudoku([
    [3,1,6,5,7,8,4,9,2],
    [5,2,9,1,3,4,7,6,8],
    [4,8,7,6,2,9,5,3,1],
    [2,6,3,4,1,5,9,8,7],
    [9,7,4,8,6,3,1,2,5],
    [8,5,1,7,9,2,6,4,3],
    [1,3,8,9,4,7,2,5,6],
    [6,9,2,3,5,1,8,7,4],
    [7,4,5,2,8,6,3,1,9]
])

def test_sudoku_constructor():
    try: Sudoku([])
    except InvalidSudokuException: pass
    try: Sudoku([[1,2,3,4,5,6,7,8,9]])
    except InvalidSudokuException: pass
    try: Sudoku([[1,2,3,4,5,6,7,8]])
    except InvalidSudokuException: pass
    try: Sudoku([[1,2,3,4,5,6,7,8,9],
                 [1,2,3,4,5,6,7,8]])
    except InvalidSudokuException: pass

def test_clauses_creator():
    global sudoku

    # On prend un sudoku complet et on enlève le chiffre du milieu
    sudoku[4][4] = 0

    # On récupère sa fonction de clause
    res = sudoku.clause()

    # On initialise les valeurs de test (éléments | résultat attendu)
    test_elements_answer = [
        # Test de la 1ère et 5ᵉ ligne
        (sudoku[0], True),
        (sudoku[4], False),
        # Test de la 1ère et 5ᵉ colonne
        ([sudoku[0][i] for i in range(9)], True),
        ([sudoku[4][i] for i in range(9)], False),
        # Test de la 1ère et 5ᵉ région
        ([sudoku[i][j] for i in range(3) for j in range(3)], True),
        ([sudoku[i][j] for i in range(3,6) for j in range(3,6)], False),
    ]

    # On lance les tests
    for elements, answer in test_elements_answer:
        if res(elements) != answer:
            raise TestFail(f"Une clause n'a pas retourné {answer} (éléments: {elements})")

    # Test final sur l'entièreté du sudoku
    if sudoku.valid():
        raise TestFail(f"Le sudoku incomplet est validé")

    sudoku[4][4] = 6
    if not sudoku.valid():
        print(sudoku)
        raise TestFail(f"Le sudoku complet est invalidé")

def test_sudoku_verifier(): raise TestFail("Non implémenté")

def test_sudoku_generator(): raise TestFail("Non implémenté")

if __name__ == "__main__":
    tests = [
        test_sudoku_constructor,
        test_clauses_creator,
        test_sudoku_verifier,
        test_sudoku_generator,
    ]

    # Running tests
    for test in tests:
        try:
            print(f"Test: {test.__name__}")
            timeTaken = timeit(lambda: test(), number=1)
            print(f"✔   Durée: {timeTaken:.2f}s")
        except TestFail as fail:
            print(f"❌   Erreur: \"{fail}\"")
