import time
import copy
import random

class Cell:
    """Represents a single cell in a Sudoku puzzle."""

    def __init__(self, position):
        self.position = position  # (row, col, box)
        self.possible_answers = list(range(1, 10))
        self.answer = None
        self.solved = False

    def remove(self, num):
        """Removes a number from the list of possible answers."""
        if num in self.possible_answers and not self.solved:
            self.possible_answers.remove(num)
            if len(self.possible_answers) == 1:
                self.set_answer(self.possible_answers[0])

    def set_answer(self, num):
        """Sets the answer and marks the cell as solved."""
        if num in range(1, 10):
            self.answer = num
            self.possible_answers = [num]
            self.solved = True
        else:
            raise ValueError("Invalid number")

    def reset(self):
        """Resets the cell to its initial state."""
        self.possible_answers = list(range(1, 10))
        self.answer = None
        self.solved = False

    def is_solved(self):
        return self.solved

    def get_answer(self):
        return self.answer if self.solved else 0

def empty_sudoku():
    """Generates an empty Sudoku grid with initialized cells."""
    sudoku = []
    for x in range(1, 10):
        box_base = (x - 1) // 3 * 3 + 1
        for y in range(1, 10):
            box = box_base + (y - 1) // 3
            sudoku.append(Cell((x, y, box)))
    return sudoku

def print_sudoku(sudoku):
    """Prints the Sudoku grid in a readable format."""
    for i in range(0, 81, 9):
        row = [sudoku[j].get_answer() for j in range(i, i + 9)]
        print(row[:3], row[3:6], row[6:9])
        if (i // 9 + 1) % 3 == 0 and i < 72:
            print()

def update_cells(sudoku, position, value):
    """Removes a value from all cells in the same row, column, or box."""
    for cell in sudoku:
        if any(position[i] == cell.position[i] for i in range(3)):
            cell.remove(value)

def generate_sudoku():
    """Generates a valid, randomly-filled Sudoku grid."""
    sudoku = empty_sudoku()
    cells = list(range(81))

    while cells:
        cell_options = [sudoku[i].possible_answers for i in cells]
        min_options = min(len(opt) for opt in cell_options)
        candidates = [sudoku[i] for i in cells if len(sudoku[i].possible_answers) == min_options]

        selected_cell = random.choice(candidates)
        value = random.choice(selected_cell.possible_answers)
        selected_cell.set_answer(value)
        update_cells(sudoku, selected_cell.position, value)
        cells.remove(sudoku.index(selected_cell))

    return sudoku

def is_valid_sudoku(sudoku):
    """Validates that a Sudoku grid meets all constraints."""
    for i, cell1 in enumerate(sudoku):
        for j, cell2 in enumerate(sudoku):
            if i != j and cell1.get_answer() == cell2.get_answer():
                if any(cell1.position[k] == cell2.position[k] for k in range(3)):
                    return False
    return True

def generate_valid_sudoku():
    """Generates a complete and valid Sudoku grid."""
    while True:
        sudoku = generate_sudoku()
        if is_valid_sudoku(sudoku):
            return sudoku

def solve_sudoku(sudoku, depth=0):
    """Solves the Sudoku puzzle using backtracking."""
    if depth > 900:
        return False

    cells = [i for i, cell in enumerate(sudoku) if not cell.is_solved()]
    if not cells:
        return sudoku

    min_len = min(sudoku[i].lenOfPossible() for i in cells)
    candidates = [i for i in cells if sudoku[i].lenOfPossible() == min_len]

    selected = random.choice(candidates)
    for value in sudoku[selected].possible_answers:
        copied_sudoku = copy.deepcopy(sudoku)
        copied_sudoku[selected].set_answer(value)
        update_cells(copied_sudoku, copied_sudoku[selected].position, value)

        solution = solve_sudoku(copied_sudoku, depth + 1)
        if solution:
            return solution

    return False

def generate_puzzle(sudoku):
    """Generates a solvable puzzle by removing cells."""
    cells = list(range(81))
    while cells:
        copy_sudoku = copy.deepcopy(sudoku)
        random_cell = random.choice(cells)
        cells.remove(random_cell)

        copy_sudoku[random_cell].reset()
        if solve_sudoku(copy_sudoku):
            sudoku[random_cell].reset()
        else:
            break

    return sudoku

def main(level):
    """Generates and solves a Sudoku puzzle of the desired difficulty."""
    start_time = time.time()
    completed_sudoku = generate_valid_sudoku()
    puzzle = generate_puzzle(completed_sudoku)

    solution = solve_sudoku(puzzle)
    if not solution:
        print("Failed to solve the puzzle.")
        return

    print(f"Sudoku Puzzle ({level}):")
    print_sudoku(puzzle)

    print("\nSolution:")
    print_sudoku(solution)

    print(f"Time taken: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main("Medium")
