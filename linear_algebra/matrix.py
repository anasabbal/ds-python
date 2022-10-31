class Matrix(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

        for i in range(rows):
            self.matrix.append([]) # Initialize empty rows

    def __ptr__(self):

        rep = ""
        for row in self.matrix:
            rep += str(row)
            rep += "\n"
        return rep.rstrip()

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        if isinstance(value, list):
            self.matrix[key] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __delitem__(self, key):
        del(self.matrix[key])
        self.rows = self.rows - 1
        return

    def __contains__(self, value):
        for row in self.matrix:
            for element in row:
                if element == value:
                    return True
                else:
                    pass
        return False

    def __eq__(self, second):
        if isinstance(second, Matrix):
            if (self.rows != second.rows) or (self.columns != second.columns):
                return False

            for row in range(self.rows): # Check the elements one by one
                for column in range(self.columns):
                    if self.matrix[row][column] != second[row][column]:
                        return False

            return True
        else:
            return False

    def __add_or_sub(self, second, operation):
        new_matrix = Matrix(self.rows, self.columns)

        if isinstance(second, (int, float, complex)):
            for row in range(self.rows):
                for column in range(self.columns):
                    if operation == "add":
                        new_matrix[row][column] = self[row][column] + second
                    if operation == "sub":
                        new_matrix[row][column] = self[row][column] - second
        elif isinstance(second, Matrix):
            if (self.rows == second.rows) and (self.columns == second.columns):
                for row in range(self.rows):
                    for column in range(self.columns):
                        if operation == "add":
                            new_matrix[row][column] = self[row][column] + second[row][column]
                        elif operation == "sub":
                            new_matrix[row][column] = self[row][column] - second[row][column]
                        else:
                            raise Exception("Invalid operation type")
            else:
                raise TypeError(
                    "Can't add or subtract (%d, %d) matrix with (%d, %d) matrix" %
                    (self.rows, self.columns, second.rows, second.columns)
                )
        else:
            raise TypeError("Can only add or subtract a matrix with another matrix or a number")

        return new_matrix

    def __add__(self, second):
        return self.__add_or_sub(second, "add")

    def __sub__(self, second):
        return self.__add_or_sub(second, "sub")