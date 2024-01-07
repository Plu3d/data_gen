import random
import os
from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet

class Cell:
    def __init__(self, row: int, col: int, val: float):
        self.row = row
        self.col = col
        self.val = val

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.arraySpreadsheet = []

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        if 0 <= rowIndex < self.rowNum() and 0 <= colIndex < self.colNum():
            self.arraySpreadsheet[rowIndex][colIndex] = value
            return True
        return False

    def buildSpreadsheet(self, lCells: [Cell]):
        noRows, noCols = 0, 0
        for cell in lCells:
            noRows = max(noRows, cell.row)
            noCols = max(noCols, cell.col)

        self.arraySpreadsheet = [[None] * (noCols + 1) for _ in range(noRows + 1)]

        for cell in lCells:
            self.arraySpreadsheet[cell.row][cell.col] = cell.val

def generate_cells(matrix, upper_limit_row, upper_limit_col, density_factor):
    cell_list = []
    lower_limit = 0

    for i in range(density_factor * 10 + 2):
        if random.randint(0, 9) > 4:
            temp_cell = Cell(
                random.randint(lower_limit, upper_limit_row),
                random.randint(lower_limit, upper_limit_col),
                random.randint(-100, 100)
            )
        else:
            temp_cell = Cell(
                random.randint(lower_limit, upper_limit_row),
                random.randint(lower_limit, upper_limit_col),
                round(random.uniform(-100, 100), 2)
            )

        while matrix.arraySpreadsheet[temp_cell.row - 1][temp_cell.col - 1] is not None:
            temp_cell = Cell(
                random.randint(lower_limit, upper_limit_row),
                random.randint(lower_limit, upper_limit_col),
                random.randint(-100, 100)
            ) if random.randint(0, 9) > 4 else Cell(
                random.randint(lower_limit, upper_limit_row),
                random.randint(lower_limit, upper_limit_col),
                round(random.uniform(-100, 100), 2)
            )

        cell_list.append(temp_cell)
        matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    return cell_list

def write_to_file(file_name, data):
    if os.path.exists(file_name):
        os.remove(file_name)

    with open(file_name, "x") as file:
        for cell_data in data:
            file.write(cell_data)

# Matrices for Small Size
s_upper_limit_row = 32
s_upper_limit_col = 32
s_matrix_10 = ArraySpreadsheet()
s_cell_list_10 = generate_cells(s_matrix_10, s_upper_limit_row, s_upper_limit_col, 10)
write_to_file("sampleDataSmall_10_density", [f"{s_upper_limit_row} {s_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in s_cell_list_10])

s_matrix_25 = ArraySpreadsheet()
s_cell_list_25 = generate_cells(s_matrix_25, s_upper_limit_row, s_upper_limit_col, 25)
write_to_file("sampleDataSmall_25_density", [f"{s_upper_limit_row} {s_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in s_cell_list_25])

s_matrix_50 = ArraySpreadsheet()
s_cell_list_50 = generate_cells(s_matrix_50, s_upper_limit_row, s_upper_limit_col, 50)
write_to_file("sampleDataSmall_50_density", [f"{s_upper_limit_row} {s_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in s_cell_list_50])

# Matrices for Medium Size
m_upper_limit_row = 100
m_upper_limit_col = 100
m_matrix_10 = ArraySpreadsheet()
m_cell_list_10 = generate_cells(m_matrix_10, m_upper_limit_row, m_upper_limit_col, 10)
write_to_file("sampleDataMedium_10_density", [f"{m_upper_limit_row} {m_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in m_cell_list_10])

m_matrix_25 = ArraySpreadsheet()
m_cell_list_25 = generate_cells(m_matrix_25, m_upper_limit_row, m_upper_limit_col, 25)
write_to_file("sampleDataMedium_25_density", [f"{m_upper_limit_row} {m_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in m_cell_list_25])

m_matrix_50 = ArraySpreadsheet()
m_cell_list_50 = generate_cells(m_matrix_50, m_upper_limit_row, m_upper_limit_col, 50)
write_to_file("sampleDataMedium_50_density", [f"{m_upper_limit_row} {m_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in m_cell_list_50])

# Matrices for Large Size
l_upper_limit_row = 500
l_upper_limit_col = 500
l_matrix_10 = ArraySpreadsheet()
l_cell_list_10 = generate_cells(l_matrix_10, l_upper_limit_row, l_upper_limit_col, 10)
write_to_file("sampleDataLarge_10_density", [f"{l_upper_limit_row} {l_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in l_cell_list_10])

l_matrix_25 = ArraySpreadsheet()
l_cell_list_25 = generate_cells(l_matrix_25, l_upper_limit_row, l_upper_limit_col, 25)
write_to_file("sampleDataLarge_25_density", [f"{l_upper_limit_row} {l_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in l_cell_list_25])

l_matrix_50 = ArraySpreadsheet()
l_cell_list_50 = generate_cells(l_matrix_50, l_upper_limit_row, l_upper_limit_col, 50)
write_to_file("sampleDataLarge_50_density", [f"{l_upper_limit_row} {l_upper_limit_col} {random.randint(-100, 100)}\n"] + [f"{cell.row} {cell.col} {cell.val}\n" for cell in l_cell_list_50])
