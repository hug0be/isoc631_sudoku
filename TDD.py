# coding: utf-8
from timeit import timeit
import numpy as np
from main import Sudoku, InvalidSudokuException, SudokuGenerator


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
    else: raise TestFail(f"Sudoku([]) n'a pas renvoyé d'erreur")

    try: Sudoku([[1,2,3,4,5,6,7,8,9]])
    except InvalidSudokuException: pass
    else: raise TestFail(f"Sudoku([[1 ... 9]]) n'a pas renvoyé d'erreur")

    try: Sudoku([[1,2,3,4,5,6,7,8]])
    except InvalidSudokuException: pass
    else: raise TestFail(f"Sudoku([[1 ... 8]]) n'a pas renvoyé d'erreur")

    try: Sudoku([[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8]])
    except InvalidSudokuException: pass
    else: raise TestFail(f"Sudoku([[1 ... 9],[1 ... 8]) n'a pas renvoyé d'erreur")

def test_sudoku_verifier():
    global sudoku

    # On prend un sudoku complet et on enlève le chiffre du milieu
    sudoku[4][4] = 0

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
        if sudoku.clause(elements) != answer:
            raise TestFail(f"Une clause n'a pas retourné {answer} (éléments: {elements})")

    # Test final sur l'entièreté du sudoku
    if sudoku.is_valid():
        raise TestFail(f"Le sudoku incomplet est validé")

    sudoku[4][4] = 6
    if not sudoku.is_valid():
        raise TestFail(f"Le sudoku complet est invalidé")

def test_sudoku_generator():
    for _ in range(100):
        try:
            SudokuGenerator.random()
        except InvalidSudokuException as ex:
            raise TestFail(ex)

def test_random_solver():
    test_sudoku:Sudoku = Sudoku([
        [0, 1, 6, 5, 7, 8, 4, 9, 2],
        [0, 2, 9, 1, 3, 4, 7, 6, 8],
        [0, 8, 7, 6, 2, 9, 5, 3, 1],
        [0, 6, 3, 4, 1, 5, 9, 8, 7],
        [0, 7, 4, 8, 6, 3, 1, 2, 5],
        [0, 5, 1, 7, 9, 2, 6, 4, 3],
        [0, 3, 8, 9, 4, 7, 2, 5, 6],
        [0, 9, 2, 3, 5, 1, 8, 7, 4],
        [0, 4, 5, 2, 8, 6, 3, 1, 9]
    ])

    # Test si tous les éléments vides sont remplis
    for i in range(100):
        rss = test_sudoku.random_solve_attempt()
        if np.any(rss == 0): raise TestFail(f"Il reste un zéro après un RSA (essai n°{i})")

if __name__ == "__main__":
    tests = [
        test_sudoku_constructor,
        test_sudoku_verifier,
        test_sudoku_generator,
        test_random_solver
    ]

    # Running tests
    for test in tests:
        try:
            print(f"Test: {test.__name__}")
            timeTaken = timeit(lambda: test(), number=1)
            print(f"✔   Durée: {timeTaken:.2f}s")
        except TestFail as fail:
            print(f"❌   Erreur: \"{fail}\"")
