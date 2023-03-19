# coding: utf-8
from random import randint

class InvalidSudokuException(Exception): pass

class SudokuGenerator:
    @staticmethod
    def random():
        """ Génère un sudoku avec des éléments aléatoires """
        return Sudoku([
            [randint(0,9) for _ in range(9)]
            for _ in range(9)
        ])

class Sudoku:
    def __init__(self, array:list[list[int]]):
        self.is_sudoku(array)
        self.array = array

    def valid(self):
        """ Valide le sudoku """
        validation_function = self.clause()

        # Validation des lignes
        for line in self.array:
            if not validation_function(line): return False

        # Validation des colonnes
        for column in zip(*self.array):
            if not validation_function(column): return False

        # Validation des régions
        for i in [1,4,7]:
            for j in [1,4,7]:
                region = [
                    self[i-1][j-1], self[i-1][j], self[i-1][j+1],
                    self[i][j-1], self[i][j], self[i][j+1],
                    self[i+1][j-1], self[i+1][j], self[i+1][j+1],
                ]
                if not validation_function(region): return False

        return True


    @staticmethod
    def clause():
        """ Retourne la fonction qui teste la validité de 9 éléments """
        """ Traduction directe de l'implémentation Isabelle/HOL """
        return lambda elements: all(
            any(
                element == digit
                for element in elements
            )
            for digit in range(1,10)
        )

    @staticmethod
    def is_sudoku(array):
        # Validation du tableau donné
        if len(array) != 9:
            raise InvalidSudokuException(f"Un sudoku doit avoir 9 lignes, ici il y en a {len(array)}")
        for i, line in enumerate(array):
            if len(line) != 9:
                raise InvalidSudokuException(
                    f"Une ligne de sudoku doit avoir 9 éléments, ici, la ligne {i} en a {len(line)}")

    def __getitem__(self, key)->list:
        if isinstance(key, int):
            return self.array[key]
        raise KeyError(f"{key.__class__.__name__} n'est pas une clé valide")

    def __str__(self):
        return self.array.__str__()

if __name__ == "__main__":
    pass