# -*- coding: utf-8 -*-
import random
import turtle



class Grid:
    
    def __init__(self, latitude_cells_count, longitude_cells_count):
        self.latitude_cells_count = latitude_cells_count
        self.longitude_cells_count = longitude_cells_count
        self.grid = [['.' for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)]

    def fill_random(self, values):
        """ Rempli la grille de valeurs aléatoires de la liste 'values'"""
        self.grid = [[random.choice(values)
                      for _ in range(self.columns_count)]
                     for _ in range(self.lines_count)]

    def get_line(self, line_number):
        return self.grid[line_number]

    def get_column(self, column_number):
        return [row[column_number] for row in self.grid]

    def get_line_str(self, line_number, separator='\t'):
        return separator.join(map(str, self.grid[line_number]))

    def get_grid_str(self, separator='\t'):
        return '\n'.join(self.get_line_str(i, separator) for i in range(self.latitude_cells_count))

    def get_diagonal(self):
        return [self.grid[i][i] for i in range(min(self.latitude_cells_count, self.longitude_cells_count))]

    def get_anti_diagonal(self):
        return [self.grid[i][self.longitude_cells_count - 1 - i] for i in range(min(self.latitude_cells_count, self.longitude_cells_count))]

    def has_equal_values(self, value):
        return all(cell == value for row in self.grid for cell in row)

    def is_square(self):
        return self.latitude_cells_count == self.longitude_cells_count

    def get_count(self, value):
        return sum(row.count(value) for row in self.grid)

    def get_sum(self):
        return sum(sum(row) for row in self.grid)

    def get_coordinates_from_cell_number(self, cell_number):
        line_number = cell_number // self.longitude_cells_count
        column_number = cell_number % self.longitude_cells_count
        return line_number, column_number

    def get_cell_number_from_coordinates(self, line_number, column_number):
        return line_number * self.longitude_cells_count + column_number

    def get_cell(self, row, col):
        if 0 <= row < self.latitude_cells_count and 0 <= col < self.longitude_cells_count:
            return self.grid[row][col]
        return None

    def set_cell(self, row, col, value):
        if 0 <= row < self.latitude_cells_count and 0 <= col < self.longitude_cells_count:
            self.grid[row][col] = value

    def get_same_value_cell_numbers(self, value):
        return [
            self.get_cell_number_from_coordinates(i, j)
            for i in range(self.latitude_cells_count)
            for j in range(self.longitude_cells_count)
            if self.grid[i][j] == value
        ]

    def get_neighbour(self, line_number, column_number, delta, is_tore=True):
        new_line = line_number + delta[0]
        new_column = column_number + delta[1]
        if is_tore:
            new_line %= self.latitude_cells_count
            new_column %= self.longitude_cells_count
        elif not (0 <= new_line < self.latitude_cells_count and 0 <= new_column < self.longitude_cells_count):
            return None
        return self.grid[new_line][new_column]

    def get_neighborhood(self, line_number, column_number, deltas, is_tore=True):
        neighbors = []
        for delta in deltas:
            neighbor = self.get_neighbour(line_number, column_number, delta, is_tore)
            neighbors.append(neighbor)
        return neighbors

    def draw_with_turtle(self, cell_size=50, margin=50, show_values=True):
        """ Dessine avec le module 'turtle' la grille centrée avec 'margin' pixels de marge. Les cases ont une taille de
        'cell_size' pixels. Les valeurs de la grille sont affichées au centre de chaque case uniquement si 'show_values'
        a pour valeur 'True'."""
        grid_width, grid_height = cell_size * self.columns_count, cell_size * self.lines_count
        turtle.setup(grid_width + 2 * margin, grid_height + 2 * margin)
        turtle.title(f"grille de {self.lines_count} lignes et {self.columns_count} colonnes")
        turtle.speed(0)
        for cell_number in range(self.lines_count * self.columns_count):
            line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
            cell_center_x = -grid_width // 2 + cell_size // 2 + column_number * cell_size
            cell_center_y = grid_height // 2 - cell_size // 2 - line_number * cell_size
            if show_values:
                turtle.up()
                turtle.goto(cell_center_x, cell_center_y)
                turtle.down()
                turtle.write(self.get_cell(cell_number))
            if line_number == 0:
                cell_top_left_x = cell_center_x - cell_size // 2
                cell_top_left_y = cell_center_y + cell_size // 2
                turtle.up()
                turtle.goto(cell_top_left_x, cell_top_left_y)
                turtle.down()
                turtle.goto(cell_top_left_x, cell_top_left_y - grid_height)
            if column_number == 0:
                cell_top_left_x = cell_center_x - cell_size // 2
                cell_top_left_y = cell_center_y + cell_size // 2
                turtle.up()
                turtle.goto(cell_top_left_x, cell_top_left_y)
                turtle.down()
                turtle.goto(cell_top_left_x + grid_width, cell_top_left_y)
        turtle.up()
        turtle.goto(grid_width // 2, grid_height // 2)
        turtle.down()
        turtle.goto(grid_width // 2, grid_height // 2 - grid_height)
        turtle.up()
        turtle.goto(-grid_width // 2, -grid_height // 2)
        turtle.down()
        turtle.goto(-grid_width // 2 + grid_width, -grid_height // 2)
        turtle.exitonclick()


## AJOUT FONCTION ##

    @staticmethod
    def create_grid(lines_count, columns_count, value):
        grid = Grid(lines_count, columns_count)
        grid.grid = [[value] * columns_count for _ in range(lines_count)]
        return grid

    @staticmethod
    def create_random_grid(lines_count, columns_count, values):
        grid = Grid(lines_count, columns_count)
        grid.grid = [[random.choice(values) for _ in range(columns_count)] for _ in range(lines_count)]
        return grid

# Tests
if __name__ == '__main__':
    random.seed(1000)  # Permet de générer toujours le 'même' hasard pour les tests

    # Constantes de directions
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    # Constantes de test
    LINES_COUNT_TEST, COLUMNS_COUNT_TEST = 5, 7
    LINE_NUMBER_TEST, COLUMN_NUMBER_TEST = 1, 6
    VALUE_TEST = 0
    VALUES_TEST = list(range(2))
    IS_TORE_TEST = True
    DIRECTION_TEST = EAST
    GRID_CONST_TEST = Grid.create_grid(LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUE_TEST)
    GRID_RANDOM_TEST = Grid.create_random_grid(LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUES_TEST)

    # Tests
    assert GRID_CONST_TEST.grid == [[0] * COLUMNS_COUNT_TEST for _ in range(LINES_COUNT_TEST)]
    assert GRID_RANDOM_TEST.grid == [[1, 0, 1, 1, 0, 1, 0],
                                     [1, 0, 0, 0, 1, 1, 0],
                                     [1, 0, 1, 0, 0, 1, 0],
                                     [1, 1, 0, 0, 1, 0, 0],
                                     [0, 1, 0, 1, 0, 0, 1]]

    assert GRID_RANDOM_TEST.latitude_cells_count == LINES_COUNT_TEST
    assert GRID_RANDOM_TEST.longitude_cells_count == COLUMNS_COUNT_TEST
    assert GRID_RANDOM_TEST.get_line_str(2) == "1\t0\t1\t0\t0\t1\t0"
    assert GRID_RANDOM_TEST.get_grid_str('') == "1011010\n1000110\n1010010\n1100100\n0101001"
    assert GRID_RANDOM_TEST.get_line(LINE_NUMBER_TEST) == [1, 0, 0, 0, 1, 1, 0]
    assert GRID_RANDOM_TEST.get_column(COLUMN_NUMBER_TEST) == [0, 0, 0, 0, 1]
    assert GRID_RANDOM_TEST.get_diagonal() == [1, 0, 1, 0, 0]
    assert GRID_RANDOM_TEST.get_anti_diagonal() == [0, 1, 0, 0, 0]
    assert GRID_CONST_TEST.has_equal_values(0)
    assert not GRID_RANDOM_TEST.has_equal_values(0)
    assert not GRID_RANDOM_TEST.is_square()
    assert GRID_RANDOM_TEST.get_count(1) == GRID_RANDOM_TEST.get_sum() == 16
    assert GRID_RANDOM_TEST.get_coordinates_from_cell_number(13) == (1, 6)
    assert GRID_RANDOM_TEST.get_cell_number_from_coordinates(1, 6) == 13
    assert GRID_RANDOM_TEST.get_cell(1, 6) == 0
    GRID_RANDOM_TEST.set_cell(1, 6, 1)
    assert GRID_RANDOM_TEST.get_cell(1, 6) == 1
    print("Tests all OK")
