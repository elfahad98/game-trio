import tkinter as tk
from planetalpha import PlanetAlpha
from Element import Ground


class PlanetTk(PlanetAlpha, tk.Canvas):
    def __init__(self, root, name, latitude_cells_count, longitude_cells_count,
                 cell_size=40, gutter_size=2, margin_size=10, show_content=True, 
                 show_grid_lines=True, background_color="white", foreground_color="dark blue", 
                 gridlines_color="maroon", authorized_classes=None, **kwargs):

        super().__init__(name, latitude_cells_count, longitude_cells_count, Ground())
        

        kwargs['width'] = longitude_cells_count * (cell_size + gutter_size) + 2 * margin_size
        kwargs['height'] = latitude_cells_count * (cell_size + gutter_size) + 2 * margin_size
        kwargs['background'] = background_color
        tk.Canvas.__init__(self, root, **kwargs)


        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        self.__root = root
        self.__show_content = show_content
        self.__show_grid_lines = show_grid_lines
        self.__authorized_classes = authorized_classes or {Ground}
        self.__background_color = background_color
        self.__foreground_color = foreground_color
        self.__gridlines_color = gridlines_color

        self.__cell_tags = {}
        self.initialize_grid()

    def initialize_grid(self):
        for cell_number in range(self.get_lines_count() * self.get_columns_count()):
            i, j = self.get_coordinates_from_cell_number(cell_number)
            x = j * (self.__cell_size + self.__gutter_size) + self.__margin_size + 2
            y = i * (self.__cell_size + self.__gutter_size) + self.__margin_size + 2
            tag = f"t_{cell_number}"
            self.__cell_tags[cell_number] = self.create_text(x, y, text=str(self.get_cell(i, j)), 
                                                             fill=self.__foreground_color, font=("Arial", self.__cell_size // 2),
                                                             tag=tag, anchor="nw")
        if self.__show_grid_lines:
            self.__draw_grid_lines()

    def __draw_grid_lines(self):
        for i in range(self.get_lines_count() + 1):
            y = i * (self.__cell_size + self.__gutter_size) + self.__margin_size
            self.create_line(self.__margin_size, y, 
                             self.__margin_size + self.get_columns_count() * (self.__cell_size + self.__gutter_size), y,
                             fill=self.__gridlines_color)

        for j in range(self.get_columns_count() + 1):
            x = j * (self.__cell_size + self.__gutter_size) + self.__margin_size
            self.create_line(x, self.__margin_size, 
                             x, self.__margin_size + self.get_lines_count() * (self.__cell_size + self.__gutter_size),
                             fill=self.__gridlines_color)

    def move_element(self, cell_number, new_cell_number):
        """déplacer un élément d'une cellule à une autre"""
        element = self.get_cell(*self.get_coordinates_from_cell_number(cell_number))
        self.set_cell(cell_number, Ground())
        self.set_cell(new_cell_number, element)
        self.itemconfigure(f"t_{cell_number}", text=str(self.get_cell(*self.get_coordinates_from_cell_number(cell_number))))
        self.itemconfigure(f"t_{new_cell_number}", text=str(element))

    def born(self, cell_number, element):
        """placer un element endroit spécific"""
        if cell_number == -1:
            return
        super().born(cell_number, element)
        self.itemconfigure(f"t_{cell_number}", text=str(element))

    def die(self, cell_number):
        """enlever un element a un endroit spécific"""
        super().die(cell_number)
        self.itemconfigure(f"t_{cell_number}", text=str(Ground()))

    def populate(self, class_names_count):
        for class_name, count in class_names_count.items():
            for _ in range(count):
                self.born_randomly(class_name())

    def born_randomly(self, element):
        free_cell = self.get_random_free_place()
        if free_cell != -1:
            self.born(free_cell, element)

    def get_classes_cell_numbers(self):
        return {cls: self.get_same_value_cell_numbers(cls()) for cls in self.__authorized_classes}

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()
    
    def get_lines_count(self):
        return self.latitude_cells_count

    def get_columns_count(self):
        return self.longitude_cells_count
