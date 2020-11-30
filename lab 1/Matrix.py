from constants import *
from math import ceil
from copy import deepcopy

class Matrix():
    def __init__(self, columns=0, rows=0, data=None, filename=None):
        if filename is None:
            self.data = [[0 for j in range(columns)] for i in range(rows)] if data is None else data
        else:
            self.read_data(filename)
        self.rows = len(self.data)
        self.columns = len(self.data[0])
    
    def copy(self):
        return Matrix(self.columns, self.rows, data=deepcopy(self.data))
    
    def __repr__(self):
        representation = ""
        for i in range(self.rows):
            for j in range(self.columns):
                representation += str(self[i, j]) + "\t"
            representation += "\n"
        return representation

    def __setitem__(self, t, value):
        if isinstance(t, tuple):
            i, j = t
            self.data[i][j] = value
        else:
            self.data[t] = value

    def __getitem__(self, t):
        if isinstance(t, tuple):
            i, j = t
            return self.data[i][j]
        else:
            return self.data[t]
    
    def __eq__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self[i, j] - other[i, j] > EPSYLON:
                        return False
            return True
        else:
            return False
    
    def __iadd__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("To be added, matrices have to have both dimensions equal.")
        self.data = [[self[i, j]+other[i, j] for j in range(self.columns)] for i in range(self.rows)]
        return self
    
    def __add__(self, other):
        new_data = self.copy()
        new_data += other
        return new_data
    
    def __isub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("To be subtracted, matrices have to have both dimensions equal.")
        self.data = [[self[i, j]-other[i, j] for j in range(self.columns)] for i in range(self.rows)]
        return self
    
    def __sub__(self, other):
        new_data = self.copy()
        new_data -= other
        return new_data
    
    def __mul__(self, other):
        # multiply A*B or A*123
        if not isinstance(other, Matrix):
            return self.scalar_multiply(other)

        if self.columns != self.rows:
            raise ValueError("Matrix dimensions do not match (first columns, second rows)")
        data = []
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                new_value = 0
                for k in range(self.columns):
                    new_value += self[i, k]*other[k, j]
                row.append(new_value)
            data.append(row)
        return Matrix(other.columns, self.rows, data)
    
    def __invert__(self):
        # transpose ~
        new_data = []
        for j in range(self.columns):
            row = []
            for i in range(self.rows):
                row.append(self[i, j])
            new_data.append(row)      
        self.data = new_data
        self.rows, self.columns = self.columns, self.rows
        return self
    
    def __pow__(self, other):
        # invert **-1
        if other != -1:
            raise ValueError("Matrix only allowed to the power of -1 (inverted matrix)")
        det = self.determinant_LUP()
        if abs(det) < EPSYLON:
            raise TypeError("Matrix does not have an inverse.")
        LU, P = self.copy().LUP_decomposition()
        n = self.rows
        solution_columns = []
        for i in range(n):
            b = Matrix(data=[[1 if P[i] == j else 0] for j in range(n)])
            y = self.forward_substitution(b)
            x = self.backward_substitution(y) # stupac
            ~x
            solution_columns.append(x.data[0])
        return ~Matrix(data=solution_columns)
    
    def scalar_multiply(self, scalar):
        for i in range(self.rows):            
            for j in range(self.columns):
                self[i, j] *= scalar
        return self
    
    def determinant_LUP(self):
        try:
            LU, P = self.copy().LUP_decomposition()
        except ValueError as e:
            print(e)
        n = len(P)
        out_of_place = 0
        for i in range(n):
            if P[i] != i:
                out_of_place += 1
        number_of_permutations = ceil(out_of_place/2)
        det = (-1)**number_of_permutations
        for i in range(n):
            det *= LU[i, i]
        return det
    
    def column_swap(self, i, j):
        for k in range(self.rows):
            self[k, i], self[k, j] = self[k, j], self[k, i]
        return self
    
    def isSquare(self):
        return self.rows == self.columns
    
    def enforceSquare(self):
        if not self.isSquare:
            raise ValueError("Matrix needs to be square")
    
    def setSize(self, columns=0, rows=0):
        if rows != 0 and rows != self.rows:
            if rows < self.rows:
                self.data = self.data[:rows]
            else:
                new_rows_count = rows - self.rows
                new_rows = [[0 for i in range(self.columns)] for j in range(new_rows_count)]
                self.data.extend(new_rows)
            self.rows = rows

        if columns != 0 and columns != self.columns:
            for i in range(self.rows):
                if columns < self.columns:
                    self[i] = self[i][:columns]
                else:
                    new_columns_count = columns - self.columns
                    self[i].extend([0 for i in range(new_columns_count)])
            self.columns = columns
        
        return self
    
    def read_data(self, filename): 
        with open(filename, "r") as file:
            lines = file.readlines()
        self.data = []
        self.columns = 0
        for line in lines:
            row = line.split(" ")
            if self.columns == 0:
                self.columns = len(row)
            elif len(row) != self.columns:
                raise ValueError("Inaccurate matrix description.")
            row = [float(row[i]) for i in range(columns)]
            data.append(row)
        self.rows = len(data)
        return self
    
    def write_data_file(self, filename='matrix.txt'):
        with open(filename, "w") as file:
            for i in range(self.rows):
                for j in range(self.columns):
                    file.write("{} ".format(self[i, j]))
                file.write("\n")
    
    def write_data_console(self):
        print(self)

    def mirror_rows(self):
        for i in range(self.rows/2):
            for j in range(self.columns):
                self[i, j], self[-1-i, j] = self[-1-i, j], self[i, j]
    
    def permutation(self, P):
        # P is a list of order or rows
        length = len(P)
        permuted_data = [[0] for i in range(length)]
        for i in range(length):
            permuted_data[i] = self[P[i]]
        self.data = permuted_data
        return self
    
    def forward_substitution(self, b):
        self.enforceSquare()
        if self.rows != b.rows:
            raise ValueError("The matrix and vector numbers of rows do not match.")
        n = self.rows
        for i in range(n-1):
            for j in range(i+1, n):
                b[j, 0] -= self[j, i] * b[i, 0]
        return b
    
    def backward_substitution(self, y):
        self.enforceSquare()
        if self.rows != y.rows:
            raise ValueError("The matrix and vector numbers of rows do not match.")
        n = self.rows
        for i in reversed(range(n)):
            if abs(self[i, i]) < EPSYLON:
                raise ValueError("Zero appeared on the main diagonal - no solution for this system.")
            y[i, 0] /= self[i, i]
            for j in range(i):
                y[j, 0] -= self[j, i] * y[i, 0]
        return y
    
    def LUP_decomposition(self):
        self.enforceSquare()
        n = self.rows
        P = [i for i in range(n)]
        for i in range(n-1):
            pivot = i
            for j in range(i+1, n):
                if abs(self[j, i]) > abs(self[pivot, i]):
                    pivot = j
            if abs(self[pivot, i]) < EPSYLON:
                print(self[pivot, i])
                raise ValueError("The pivot in LUP managed to end up 0, cannot be solved!")
            if pivot != i:
                self[pivot], self[i] = self[i], self[pivot]
                P[pivot], P[i] = P[i], P[pivot]
            for j in range(i+1, n):
                self[j, i] /= self[i, i]
                for k in range(i+1, n):
                    self[j, k] -= self[j, i] * self[i, k]
        return (self, P)
    
    def LU_decomposition(self):
        self.enforceSquare()
        n = self.rows
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(self[i, i]) - 0.0 < EPSYLON:
                    raise ValueError("LU cannot handle zeros as pivots.")
                self[j, i] /= self[i, i]
                for k in range(i+1, n):
                    self[j, k] -= self[j, i] * self[i, k]
        return self

