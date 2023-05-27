// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract mon_sudoku{
    uint8[9][9] private sudokugrid;
    uint8 private constant N = 9;

        constructor(uint8[9][9] memory _board) {
        sudokugrid = _board;
    }


    function isValid() public view returns (bool) {
        // Validation des lignes et colonnes
        for (uint8 i = 0; i < 9; i++) {
            uint8[] memory row = new uint8[](9);
            uint8[] memory col = new uint8[](9);
            
            for (uint8 j = 0; j < 9; j++) {
                row[j] = sudokugrid[i][j];
                col[j] = sudokugrid[j][i];
            }

            if (!clause(row) || !clause(col)) {
                return false;
            }
        }

        // Validation des régions
        for (uint8 i = 0; i < 9; i += 3) {
            for (uint8 j = 0; j < 9; j += 3) {
                uint8[] memory square = new uint8[](9);
                uint8 index = 0;
                for (uint8 x = i; x < i + 3; x++) {
                    for (uint8 y = j; y < j + 3; y++) {
                        square[index] = sudokugrid[x][y];
                        index++;
                    }
                }

                if (!clause(square)) {
                    return false;
                }
            }
        }

        return true;
    }

    function clause(uint8[] memory values) private pure returns (bool) {
        uint8[] memory occurrences = new uint8[](9);

        for (uint8 i = 0; i < 9; i++) {
            if (values[i] == 0) {
                return false;
            }
            if (values[i] != 0) {
                occurrences[values[i] - 1]++;
            }
        }

        for (uint8 i = 0; i < 9; i++) {
            if (occurrences[i] > 1) {
                return false;
            }
        }

        return true;
    }
}

