# coding: utf-8
import numpy as np

class InvalidSudokuException(Exception): pass

class SudokuGenerator:
    @staticmethod
    def random():
        """ Génère un sudoku avec des éléments aléatoires """
        return Sudoku(np.random.randint(0, 10, size=(9, 9)))

class Sudoku(np.ndarray):
    def __new__(cls, array:list[list[int]] | np.ndarray):
        Sudoku.is_sudoku(array)
        obj = np.asarray(array).view(cls)
        return obj

    def is_valid(self):
        """ Test la validité du sudoku """
        # Validation des lignes et colonnes
        for i in range(9):
            row, col = self[i, :], self[:, i]
            if not self.clause(row) or not self.clause(col):
                return False

        # Validation des régions
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = self[i:i + 3, j:j + 3]
                if not self.clause(square.flatten()):
                    return False

        return True

    def random_solve_attempt(self):
        """ Retourne une liste d'entiers aléatoires générés dans l'objectif de résoudre le Sudoku"""
        rse = np.copy(self) # rse : Randomly Solved Elements
        rse = rse[rse==0]
        rse = np.random.randint(1, 10, size=np.count_nonzero(rse == 0))
        return rse

    @staticmethod
    def clause(elements):
        """ Test la validité de 9 éléments """
        unique, counts = np.unique(elements, return_counts=True)
        return len(unique) == len(elements) - (0 in unique) and np.all(counts[1:] <= 1)

    @staticmethod
    def is_sudoku(array):
        """ Test si le tableau donné est une grille de sudoku """
        if len(array) != 9:
            raise InvalidSudokuException(f"Un sudoku doit avoir 9 lignes, ici il y en a {len(array)}")
        for i, line in enumerate(array):
            if len(line) != 9:
                raise InvalidSudokuException(f"Une ligne de sudoku doit avoir 9 éléments, ici, la ligne {i} en a {len(line)}")

if __name__ == "__main__":
    pass