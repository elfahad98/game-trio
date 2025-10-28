import random
from grid_manager import Grid  


class PlanetAlpha(Grid):
    """
    Représente une planète, une spécialisation de la classe Grid.
    """
    # Directions prédéfinies
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    def __init__(self, name: str, latitude_cells_count: int, longitude_cells_count: int, ground: str):
        super().__init__(latitude_cells_count, longitude_cells_count)
        self.name = name
        self.ground = ground
        self.grid = [[ground] * longitude_cells_count for _ in range(latitude_cells_count)]

    def get_name(self) -> str:
        """Retourne le nom de la planète."""
        return self.name

    def get_ground(self) -> str:
        """Retourne le caractère représentant le sol."""
        return self.ground

    def get_random_free_place(self) -> int:
        """Retourne un numéro de cellule libre aléatoire ou -1 si aucune place n'est disponible."""
        free_cells = self.get_same_value_cell_numbers(self.ground)
        if not free_cells:
            return -1
        return random.choice(free_cells)

    def born(self, cell_number: int, element: str) -> int:
        """Ajoute un élément dans une cellule libre donnée."""
        if cell_number == -1:
            return 0
        row, col = self.get_coordinates_from_cell_number(cell_number)
        if self.get_cell(row, col) == self.ground:
            self.set_cell(row, col, element)
            return 1
        return 0

    def die(self, cell_number: int) -> int:
        """Supprime un élément d'une cellule occupée donnée."""
        row, col = self.get_coordinates_from_cell_number(cell_number)
        if self.get_cell(row, col) != self.ground:
            self.set_cell(row, col, self.ground)
            return 1
        return 0

    def get_cell_neighbour_number(self, cell_number: int, delta: tuple, is_tore: bool = True) -> int:
        """Retourne le numéro de cellule voisin en fonction d'un delta."""
        row, col = self.get_coordinates_from_cell_number(cell_number)
        neighbor = self.get_neighbour(row, col, delta, is_tore)
        if neighbor is not None:
            new_row = (row + delta[0]) % self.latitude_cells_count
            new_col = (col + delta[1]) % self.longitude_cells_count
            return self.get_cell_number_from_coordinates(new_row, new_col)
        return -1

    def get_cell_neighborhood_numbers(self, cell_number: int, deltas: list, is_tore: bool = True) -> list:
        """Retourne les numéros des cellules voisines triés par ordre croissant."""
        row, col = self.get_coordinates_from_cell_number(cell_number)
        neighbors = []
        for delta in deltas:
            neighbor = self.get_cell_neighbour_number(cell_number, delta, is_tore)
            if neighbor != -1:
                neighbors.append(neighbor)
        return sorted(neighbors)

    def __repr__(self) -> str:
        """Retourne une représentation textuelle de la planète."""
        inhabitants_count = sum(1 for row in self.grid for cell in row if cell != self.ground)
        grid_str = '\n'.join(' '.join(row) for row in self.grid)
        return f"{self.name} ({inhabitants_count} habitants)\n{grid_str}"

    """ FONCTION AJOUTEE"""


#TEST 

if __name__ == '__main__':
    random.seed(10)
    PLANET_TEST = PlanetAlpha("Terre", 5, 10, '.')
    INHABITANTS_TEST = {'D': 7, 'C': 3}
    RESOURCES_TEST = {'E': 10, 'H': 20}

    print(PLANET_TEST)

    for letter, count in INHABITANTS_TEST.items():
        for _ in range(count):
            PLANET_TEST.born(PLANET_TEST.get_random_free_place(), letter)

    print(PLANET_TEST)

    for letter, count in RESOURCES_TEST.items():
        for _ in range(count):
            PLANET_TEST.born(PLANET_TEST.get_random_free_place(), letter)

    print(PLANET_TEST)

    print(PLANET_TEST.get_neighbour(0, 0, PlanetAlpha.NORTH_WEST))
    print(PLANET_TEST.get_neighborhood(0, 0, PlanetAlpha.CARDINAL_POINTS))
    print(PLANET_TEST.get_neighborhood(0, 0, PlanetAlpha.WIND_ROSE))

    PLANET_TEST.die(0)
    for cell in PLANET_TEST.get_cell_neighborhood_numbers(0, PlanetAlpha.WIND_ROSE):
        PLANET_TEST.die(cell)

    print(PLANET_TEST)
    print(PLANET_TEST. get_neighborhood ( 0 , 0 , PlanetAlpha .WIND_ROSE) )
