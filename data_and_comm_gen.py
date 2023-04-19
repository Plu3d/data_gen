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
            if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
                return False
            else:
                self.arraySpreadsheet[rowIndex][colIndex] = value
                return True
    
    def buildSpreadsheet(self, lCells: [Cell]):
        noRows = 0
        noCols = 0
        for cell in lCells:
            if cell.row > noRows:
                noRows = cell.row
            if cell.col > noCols:
                noCols = cell.col
        self.arraySpreadsheet = []
        for i in range(noRows + 1):
            row = []
            for j in range(noCols + 1):
                row.append(None)
            self.arraySpreadsheet.append(row)

        for cell in lCells:
            self.arraySpreadsheet[cell.row][cell.col] = cell.val
    
    def update(self, rowIndex: int, colIndex: int, value: float):

        if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
            pass
        else:
            self.arraySpreadsheet[rowIndex][colIndex] = value


s_upper_limit_col = 32
s_upper_limit_row = 32

#################################################################################################################

s_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(s_upper_limit_row, s_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
s_matrix.buildSpreadsheet(lonely_list)

s_cell_list = []
lower_limit = 0

if os.path.exists("sampleDataSmall_10_density"):
    os.remove("sampleDataSmall_10_density")
s = open("sampleDataSmall_10_density",  "x")

cell_data = str(str(s_upper_limit_row)+ " " + str(s_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
s.write(cell_data)

for i in range(102):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))
        
        while s_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))

        s_cell_list.append(temp_cell)
        s_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))

        while s_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))
        s_cell_list.append(temp_cell)
        s_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    s.write(cell_data)
s.close()

#################################################################################################################

s_matrix_2 = ArraySpreadsheet()
lonely_list_2 = []
single_cell = Cell(s_upper_limit_row, s_upper_limit_col, random.randint(-100, 100))
lonely_list_2.append(single_cell)
s_matrix_2.buildSpreadsheet(lonely_list_2)

s_cell_list_2 = []

if os.path.exists("sampleDataSmall_25_density"):
    os.remove("sampleDataSmall_25_density")
s = open("sampleDataSmall_25_density",  "x")

cell_data = str(str(s_upper_limit_row)+ " " + str(s_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
s.write(cell_data)

for i in range(255):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))
        
        while s_matrix_2.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))

        s_cell_list_2.append(temp_cell)
        s_matrix_2.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))

        while s_matrix_2.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))
        s_cell_list_2.append(temp_cell)
        s_matrix_2.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    s.write(cell_data)
s.close()

#######################################################################################################################

s_matrix_3 = ArraySpreadsheet()
lonely_list_3 = []
single_cell = Cell(s_upper_limit_row, s_upper_limit_col, random.randint(-100, 100))
lonely_list_3.append(single_cell)
s_matrix_3.buildSpreadsheet(lonely_list_3)

s_cell_list_3 = []

if os.path.exists("sampleDataSmall_50_density"):
    os.remove("sampleDataSmall_50_density")
s = open("sampleDataSmall_50_density",  "x")

cell_data = str(str(s_upper_limit_row)+ " " + str(s_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
s.write(cell_data)

for i in range(511):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))
        
        while s_matrix_3.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), random.randint(-100, 100))

        s_cell_list_3.append(temp_cell)
        s_matrix_3.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))

        while s_matrix_3.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, s_upper_limit_row), random.randint(lower_limit, s_upper_limit_col), round(random.uniform(-100, 100), 2))
        s_cell_list_3.append(temp_cell)
        s_matrix_3.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    s.write(cell_data)
s.close()

#######################################################################################################################
m_upper_limit_row = 100
m_upper_limit_col = 100
m_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(m_upper_limit_row, m_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
m_matrix.buildSpreadsheet(lonely_list)

m_cell_list = []

if os.path.exists("sampleDataMedium_10_density"):
    os.remove("sampleDataMedium_10_density")
m = open("sampleDataMedium_10_density",  "x")

cell_data = str(str(m_upper_limit_row)+ " " + str(m_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
m.write(cell_data)

for i in range(999):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))
        
        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))

        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))

        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))
        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    m.write(cell_data)
m.close()

#######################################################################################################################

m_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(m_upper_limit_row, m_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
m_matrix.buildSpreadsheet(lonely_list)

m_cell_list = []

if os.path.exists("sampleDataMedium_25_density"):
    os.remove("sampleDataMedium_25_density")
m = open("sampleDataMedium_25_density",  "x")

cell_data = str(str(m_upper_limit_row)+ " " + str(m_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
m.write(cell_data)

for i in range(2499):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))
        
        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))

        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))

        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))
        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    m.write(cell_data)
m.close()

#######################################################################################################################

m_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(m_upper_limit_row, m_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
m_matrix.buildSpreadsheet(lonely_list)

m_cell_list = []

if os.path.exists("sampleDataMedium_50_density"):
    os.remove("sampleDataMedium_50_density")
m = open("sampleDataMedium_50_density",  "x")

cell_data = str(str(m_upper_limit_row)+ " " + str(m_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
m.write(cell_data)

for i in range(4999):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))
        
        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), random.randint(-100, 100))

        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))

        while m_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, m_upper_limit_row), random.randint(lower_limit, m_upper_limit_col), round(random.uniform(-100, 100), 2))
        m_cell_list.append(temp_cell)
        m_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    m.write(cell_data)
m.close()

#######################################################################################################################

l_upper_limit_row = 500
l_upper_limit_col = 500

l_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(l_upper_limit_row, l_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
l_matrix.buildSpreadsheet(lonely_list)

l_cell_list = []

if os.path.exists("sampleDataLarge_10_density"):
    os.remove("sampleDataLarge_10_density")
l = open("sampleDataLarge_10_density",  "x")

cell_data = str(str(l_upper_limit_row)+ " " + str(l_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
l.write(cell_data)

for i in range(24999):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))
        
        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))

        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))

        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))
        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    l.write(cell_data)
l.close()

#######################################################################################################################

l_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(l_upper_limit_row, l_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
l_matrix.buildSpreadsheet(lonely_list)

l_cell_list = []

if os.path.exists("sampleDataLarge_25_density"):
    os.remove("sampleDataLarge_25_density")
l = open("sampleDataLarge_25_density",  "x")

cell_data = str(str(l_upper_limit_row)+ " " + str(l_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
l.write(cell_data)

for i in range(62499):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))
        
        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))

        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))

        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))
        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    l.write(cell_data)
l.close()

#######################################################################################################################

l_matrix = ArraySpreadsheet()
lonely_list = []
single_cell = Cell(l_upper_limit_row, l_upper_limit_col, random.randint(-100, 100))
lonely_list.append(single_cell)
l_matrix.buildSpreadsheet(lonely_list)

l_cell_list = []

if os.path.exists("sampleDataLarge_50_density"):
    os.remove("sampleDataLarge_50_density")
l = open("sampleDataLarge_50_density",  "x")

cell_data = str(str(l_upper_limit_row)+ " " + str(l_upper_limit_col) + " " + str(random.randint(-100, 100)) + "\n")
l.write(cell_data)

for i in range(124999):
    if (random.randint(0,9) > 4):
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))
        
        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), random.randint(-100, 100))

        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    else:
        temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))

        while l_matrix.arraySpreadsheet[temp_cell.row -1][temp_cell.col -1] != None:
            temp_cell = Cell(random.randint(lower_limit, l_upper_limit_row), random.randint(lower_limit, l_upper_limit_col), round(random.uniform(-100, 100), 2))
        l_cell_list.append(temp_cell)
        l_matrix.update(temp_cell.row, temp_cell.col, temp_cell.val)

    cell_data = str(str(temp_cell.row) + " " + str(temp_cell.col) + " " + str(temp_cell.val) + "\n")
    l.write(cell_data)
l.close()

####################################################################################################################################################################

p_upper_limit_col = 32
p_upper_limit_row = 32

lower_limit = 0

if os.path.exists("sampleDataCommandsSmallIRIC"):
    os.remove("sampleDataCommandsSmallIRIC")
p = open("sampleDataCommandsSmallIRIC",  "x")
IR = "IR"
IC = "IC"
command = str

for i in range(100):
    if (random.randint(0,9) > 4):
        command = IR
    else:
        command = IC

    cell_data = str(command + " " + str(random.randint(lower_limit, p_upper_limit_row)) + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 100
p_upper_limit_row = 100

lower_limit = 0

if os.path.exists("sampleDataCommandsMediumIRIC"):
    os.remove("sampleDataCommandsMediumIRIC")
p = open("sampleDataCommandsMediumIRIC",  "x")
IR = "IR"
IC = "IC"
command = str

for i in range(100):
    if (random.randint(0,9) > 4):
        command = IR
    else:
        command = IC

    cell_data = str(command + " " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 500
p_upper_limit_row = 500

lower_limit = 0

if os.path.exists("sampleDataCommandsLargeIRIC"):
    os.remove("sampleDataCommandsLargeIRIC")
p = open("sampleDataCommandsLargeIRIC",  "x")
IR = "IR"
IC = "IC"
command = str


for i in range(100):
    if (random.randint(0,9) > 4):
        command = IR
    else:
        command = IC

    cell_data = str(command + " " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 32
p_upper_limit_row = 32

if os.path.exists("sampleDataCommandsSmallU"):
    os.remove("sampleDataCommandsSmallU")
p = open("sampleDataCommandsSmallU",  "x")


for i in range(100):
    if (random.randint(0,9) > 4):
        value = str(random.randint(-100, 100))
    else:
        value = str(round(random.uniform(-100, 100), 2))

    cell_data = str("U " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) +  " " + value + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 100
p_upper_limit_row = 100

if os.path.exists("sampleDataCommandsMediumU"):
    os.remove("sampleDataCommandsMediumU")
p = open("sampleDataCommandsMediumU",  "x")

for i in range(100):
    if (random.randint(0,9) > 4):
        value = str(random.randint(-100, 100))
    else:
        value = str(round(random.uniform(-100, 100), 2))

    cell_data = str("U " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) + " " + value + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 500
p_upper_limit_row = 500

if os.path.exists("sampleDataCommandslargeU"):
    os.remove("sampleDataCommandsLargeU")
p = open("sampleDataCommandsLargeU",  "x")

for i in range(100):
    if (random.randint(0,9) > 4):
        value = str(random.randint(-100, 100))
    else:
        value = str(round(random.uniform(-100, 100), 2))

    cell_data = str("U " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) +  " " + value + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 32
p_upper_limit_row = 32

if os.path.exists("sampleDataCommandsSmallF"):
    os.remove("sampleDataCommandsSmallF")
p = open("sampleDataCommandsSmallF",  "x")

for i in range(100):
    cell_data = str("F " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 100
p_upper_limit_row = 100

if os.path.exists("sampleDataCommandsMediumF"):
    os.remove("sampleDataCommandsMediumF")
p = open("sampleDataCommandsMediumF",  "x")

for i in range(100):
    cell_data = str("F " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) + "\n")
    p.write(cell_data)
p.close()

####################################################################################################################################################################

p_upper_limit_col = 500
p_upper_limit_row = 500

if os.path.exists("sampleDataCommandsLargeF"):
    os.remove("sampleDataCommandsLargeF")
p = open("sampleDataCommandsLargeF",  "x")

for i in range(100):
    cell_data = str("F " + str(random.randint(lower_limit, p_upper_limit_row)) + " " + str(random.randint(lower_limit, p_upper_limit_col)) + "\n")
    p.write(cell_data)
p.close()
