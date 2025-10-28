
import tkinter as tk
from PlanetTk import PlanetTk


class Conway(PlanetTk):
    
    
    def __init__(self, parent, parent_app, rows=30, cols=30, cell_size=20):
        super().__init__(parent, "Conway's Game of Life", rows, cols)
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.running = False
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.iteration = 0         
        self.parent_app = parent_app

        # DICTIONNAIRE COULEUR EN HEXA 
        self.color_names = {
            "#000000": "Noir",
            "#007FFF": "Bleu",
            "#E0115F": "Rouge",
        }

        # initialisation de la forme et de la couleur cells 
        self.selected_shape = tk.StringVar(value="None")      
        self.selected_color = tk.StringVar(value="#000000")  # Couleur par défaut (noir en hexa)


        ## CREATION ET POSITIONNEMENT DU LABEL POUR LE PLACER EN HAUT ##
        
        self.iteration_label = tk.Label(self, text=f"Iteration: {self.iteration}", font=("Arial", 14))
        self.iteration_label.pack(side=tk.TOP, pady=5)  

        self.create_controls()
        self.bind("<Button-1>", self.handle_click)
        self.draw_grid()


    def create_controls(self):
        controls_frame = tk.Frame(self)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X)


        self.shapes_frame = tk.LabelFrame(controls_frame, text="Formes", padx=5, pady=5)
        self.shapes_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)  

        shapes = ["None","Glider","Spacefiller"]
        for shape in shapes:
            tk.Radiobutton(
                self.shapes_frame,
                text=shape,
                variable=self.selected_shape,
                value=shape,
                anchor="w"  
            ).pack(side=tk.TOP, anchor="w") 


        ## CADRE POUR COULEURS CASES ##
        
        self.colors_frame = tk.LabelFrame(controls_frame, text="Couleurs cases", padx=5, pady=5)
        self.colors_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        # On va recup les couleur du dico dans init qu'on va use ici 
        for color_hex, color_name in self.color_names.items():
            tk.Radiobutton(
                self.colors_frame,
                text=color_name,
                variable=self.selected_color,
                value=color_hex,
                anchor="w"
            ).pack(side=tk.TOP, anchor="w")

        ## CADRE POUR CONTROLER LA SIMULATION ##
        
        self.simulation_frame = tk.LabelFrame(controls_frame, text="Simulation Controls", padx=5, pady=5)
        self.simulation_frame.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.btn_start = tk.Button(self.simulation_frame, text="Start", command=self.start_simulation)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_pause = tk.Button(self.simulation_frame, text="Pause", command=self.pause_simulation)
        self.btn_pause.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_reset = tk.Button(self.simulation_frame, text="Reset", command=self.reset_simulation)
        self.btn_reset.pack(side=tk.LEFT, padx=5, pady=5)

        ## CADRE CONTROLE DU JEU ## 
        
        self.game_controls_frame = tk.LabelFrame(controls_frame, text="Game Controls", padx=5, pady=5)
        self.game_controls_frame.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.btn_snake = tk.Button(self.game_controls_frame, text="Snake", command=self.parent_app.switch_to_snake)
        self.btn_snake.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_turmites = tk.Button(self.game_controls_frame, text="Turmites", command=self.parent_app.switch_to_turmites)
        self.btn_turmites.pack(side=tk.LEFT, padx=5, pady=5)

        btn_quit = tk.Button(controls_frame, text="Quitter", command=self.parent_app.master.quit)
        btn_quit.pack(side=tk.LEFT, padx=5, pady=5)

    def start_simulation(self):
        self.running = True
        self.run_game()

    def pause_simulation(self):
        self.running = False

    def reset_simulation(self):
        self.running = False
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.iteration = 0  # réinitialiser le compteur d'itérations
        self.update_iteration()  # mettre a jour l'affichage 
        self.draw_grid()


    def draw_grid(self):
        self.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = self.selected_color.get() if self.grid[row][col] == 1 else "white"
                self.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


    def handle_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            shape = self.selected_shape.get()
            if shape == "None":
                self.grid[row][col] = 1 - self.grid[row][col]
            else:
                self.place_shape(row, col, shape)
            self.draw_grid()

    def get_spacefiller(self,x, y):
        """Retourne une forme de type Spacefiller à une position donnée (x, y)"""
        spacefiller = [
            (x + 0, y + 0), (x + 1, y + 0), (x + 2, y + 0), (x + 3, y + 0), (x + 4, y + 0),
            (x + 0, y + 1), (x + 4, y + 1),
            (x + 0, y + 2), (x + 1, y + 2), (x + 2, y + 2), (x + 3, y + 2), (x + 4, y + 2),
            (x + 0, y + 3), (x + 4, y + 3),
            (x + 0, y + 4), (x + 1, y + 4), (x + 2, y + 4), (x + 3, y + 4), (x + 4, y + 4)
        ]
        return spacefiller



    def place_shape(self, row, col, shape):
        # Détermine la forme qu'on va placer 
        if shape == "Glider":
            pattern = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        elif shape == "Block":
            pattern = [(0, 0), (0, 1), (1, 0), (1, 1)]
        elif shape == "Blinker":
            pattern = [(0, -1), (0, 0), (0, 1)]
        elif shape == "Spacefiller":
            pattern = self.get_spacefiller(0, 0)  # on va use la fonction get pour recup la forme sans décalage initial
        else:
            pattern = []


        ## TROUVER DIMENSION LA FORME POUR BIEN CENTRER LA FORME AVEC D2CALAGE ##
        min_row = min(dr for dr, dc in pattern)
        max_row = max(dr for dr, dc in pattern)
        min_col = min(dc for dr, dc in pattern)
        max_col = max(dc for dr, dc in pattern)

        # CALCUL DU D2CALAGE 
        shape_height = max_row - min_row + 1
        shape_width = max_col - min_col + 1

        # CALCULE L'OFSET
        offset_row = (shape_height // 2)
        offset_col = (shape_width // 2)

        # pLACE LA FORME EN (row, col)
        for dr, dc in pattern:
            r, c = row - offset_row + dr, col - offset_col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.grid[r][c] = 1



    def run_game(self):
        if self.running:
            self.iteration += 1  
            self.update_iteration()  # mise a jour l'affichage itération 
            self.update_grid()
            self.draw_grid()
            self.after(100, self.run_game)


    def update_grid(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.grid[row][col] == 1:
                    if live_neighbors in (2, 3):
                        new_grid[row][col] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[row][col] = 1
        self.grid = new_grid


    def count_live_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count


    def update_iteration(self):
        self.iteration_label.config(text=f"Iteration: {self.iteration}")
