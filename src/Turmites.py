
import tkinter as tk
from PlanetTk import PlanetTk


class Turmites(PlanetTk):
    

    def __init__(self, parent, parent_app, rows=30, cols=30, cell_size=20):
        super().__init__(parent, "Conway's Game of Life with Ants", rows, cols)
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.running = False
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.iteration = 0 
        self.parent_app = parent_app
        self.ants = {}
        self.cell_colors = ["black", "#E0115F", "#007FFF", "#50C878", "#FFD700"]  ## COULEUR CELLS ICI ON'A 5 COULEURS ## 
        self.current_color = "black"  


        ## CREATION ET POSITIONNEMENT DU LABEL POUR LE PLACER EN HAUT ##
    
        self.iteration_label = tk.Label(self, text=f"Iteration: {self.iteration}", font=("Arial", 14))
        self.iteration_label.pack(side=tk.TOP, pady=5)  # Positionnement en haut avec un espace vertical

        self.create_controls()
        self.bind("<Button-1>", self.toggle_cell)
        self.draw_grid()


    def create_controls(self):
        
        controls_frame = tk.Frame(self)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X)

        
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

        self.btn_turmites = tk.Button(self.game_controls_frame, text="Conway", command=self.parent_app.switch_to_conway)
        self.btn_turmites.pack(side=tk.LEFT, padx=5, pady=5)

        btn_quit = tk.Button(controls_frame, text="Quitter", command=self.parent_app.master.quit)
        btn_quit.pack(side=tk.RIGHT, padx=5, pady=5)


    def update_color(self):
        self.current_color = self.color_var.get()  # met a jour la couleur actuel 

    def start_simulation(self):
        self.running = True
        self.run_game()

    def pause_simulation(self):
        self.running = False

    def reset_simulation(self):
        self.running = False
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.ants.clear()
        self.iteration = 0 
        self.update_iteration()
        self.draw_grid()

    def draw_grid(self):
        self.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = self.grid[row][col] if isinstance(self.grid[row][col], str) else "white"
                self.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


        for ant_id, ant_info in self.ants.items():
            lin, col = ant_info["position"]
            x, y = col * self.cell_size, lin * self.cell_size
            self.create_oval(x, y, x + self.cell_size, y + self.cell_size, fill="red", tags=f"ant_{ant_id}")


    def toggle_cell(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # cahnge la couleur la cells selon la couleurs selectionner 
            self.grid[row][col] = self.current_color
            self.draw_grid()
            self.add_ant(row, col)

    def add_ant(self, row, col):
        ant_id = len(self.ants) + 1
        self.ants[ant_id] = {"position": (row, col), "direction": 0}
        self.draw_grid()

    def run_game(self):
        if self.running:
            self.iteration += 1
            self.update_iteration()
            self.update_ants()
            self.draw_grid()
            self.after(100, self.run_game)

    def update_ants(self):
        for ant_id, ant_info in self.ants.items():
            row, col = ant_info["position"]
            current_color = self.grid[row][col] if isinstance(self.grid[row][col], str) else "white"

            # index couleur actuel
            color_index = self.cell_colors.index(current_color) if current_color in self.cell_colors else 0

            # Cchange la couleur suivant 
            next_color_index = (color_index + 1) % len(self.cell_colors)
            self.grid[row][col] = self.cell_colors[next_color_index]

            # Change la direction de la fourmi
            if color_index == 0:  
                ant_info["direction"] = (ant_info["direction"] + 1) % 4
            else:  
                ant_info["direction"] = (ant_info["direction"] - 1) % 4

            # Déplace la fourmi
            if ant_info["direction"] == 0:  # Haut
                row -= 1
            elif ant_info["direction"] == 1:  # Droite
                col += 1
            elif ant_info["direction"] == 2:  # Bas
                row += 1
            elif ant_info["direction"] == 3:  # Gauche
                col -= 1

            if 0 <= row < self.rows and 0 <= col < self.cols:
                ant_info["position"] = (row, col)
            else:
                self.running = False
                break

    def update_iteration(self):
        self.iteration_label.config(text=f"Iteration: {self.iteration}")
