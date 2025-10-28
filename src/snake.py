import tkinter as tk
import random
from PlanetTk import PlanetTk


class Snake(PlanetTk):
    
    
    def __init__(self, parent, parent_app, grid_size=20, grid_width=30, grid_height=22):
        super().__init__(parent, "Snake Game", grid_height, grid_width)
        self.grid_size = grid_size
        self.grid_width = grid_width
        self.grid_height = grid_height  # initialise hauteur de la grille 
        self.parent_app = parent_app
        self.paused = False 
        self.running = True
        self.score = 0      # initialisation du score

        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = "Right"
        self.food = None

        self.place_food()
        self.draw_elements()

        
        ## CREATION ET POSITIONNEMENT DU LABEL POUR AFFICHER SCORE IL SERA PLACER EN HAUT ##

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(side=tk.TOP, pady=5)  # Ajouter le label en haut

        parent.bind("<Up>", lambda _: self.change_direction("Up"))
        parent.bind("<Down>", lambda _: self.change_direction("Down"))
        parent.bind("<Left>", lambda _: self.change_direction("Left"))
        parent.bind("<Right>", lambda _: self.change_direction("Right"))

        self.create_controls()
        self.game_over_label = None  # initialise var du label GAMEOVER
        self.run_game()


    def create_controls(self):
        
        controls_frame = tk.Frame(self)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X)


        ## CADRE POUR CONTROLER LA SIMULATION ##
        
        
        self.simulation_frame = tk.LabelFrame(controls_frame, text="Simulation Controls", padx=5, pady=5)
        self.simulation_frame.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.btn_pause = tk.Button(self.simulation_frame, text="Pause", command=self.toggle_pause)
        self.btn_pause.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_reset = tk.Button(self.simulation_frame, text="Reset", command=self.reset_game)
        self.btn_reset.pack(side=tk.LEFT, padx=5, pady=5)
        
        ## CADRE CONTROLE DU JEU ##
        
        self.game_controls_frame = tk.LabelFrame(controls_frame, text="Game Controls", padx=5, pady=5)
        self.game_controls_frame.pack(side=tk.LEFT, fill=tk.X, padx=5)

        self.btn_snake = tk.Button(self.game_controls_frame, text="Snake", command=self.parent_app.switch_to_snake)
        self.btn_snake.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_turmites = tk.Button(self.game_controls_frame, text="Turmites", command=self.parent_app.switch_to_turmites)
        self.btn_turmites.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_conway = tk.Button(self.game_controls_frame, text="Conway", command=self.parent_app.switch_to_conway)
        self.btn_conway.pack(side=tk.LEFT, padx=5, pady=5)


        btn_quit = tk.Button(controls_frame, text="Quitter", command=self.parent_app.master.quit)
        btn_quit.pack(side=tk.RIGHT, padx=5, pady=5)


    def place_food(self):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break


    def draw_elements(self):
        self.delete("all")
        for x, y in self.snake:
            self.create_rectangle(x * self.grid_size, y * self.grid_size,
                                  (x + 1) * self.grid_size, (y + 1) * self.grid_size,
                                  fill="green")
        if self.food:
            fx, fy = self.food
            self.create_rectangle(fx * self.grid_size, fy * self.grid_size,
                                  (fx + 1) * self.grid_size, (fy + 1) * self.grid_size,
                                  fill="red")

    def change_direction(self, new_direction):
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite.get(self.direction):
            self.direction = new_direction


    def reset_game(self):
        self.running = True
        self.score = 0  # réinitialise le score 
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = "Right"
        self.place_food()
        self.draw_elements()
        self.update_score()
        self.remove_game_over()  # supprimer "GameOver" avant de redémarrer
        self.run_game()

    def run_game(self):
        if self.running:
            if not self.paused:
                self.update()
                self.draw_elements()
            self.after(100, self.run_game)
        else:
            self.display_game_over()  # afficher "Game Over" lorsqu'on perd

    def toggle_pause(self):
        self.paused = not self.paused  # on alterne l'état pause 
        if self.paused:
            self.parent_app.master.title("Snake Game - Paused")  # change le titre en haut fen pour indiquez l'état de pause 
        else:
            self.parent_app.master.title("Snake Game")  # remet le titre normale 

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1

        # Ajuster la condition de détection des limites en fonction de la nouvelle hauteur
        if (head_x, head_y) in self.snake or not (0 <= head_x < self.grid_width and 0 <= head_y < self.grid_height):
            self.running = False
            return

        self.snake.insert(0, (head_x, head_y))
        if (head_x, head_y) == self.food:
            self.place_food()
            self.score += 1  # augmente +1 le score lorsqu'il mange food 
            self.update_score()  # mettre a jour le label du score 
        else:
            self.snake.pop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")  # mettre a jour le score affichée 

    def display_game_over(self):
        """crée un label "GAMEOVER" au centre de la fenêtre """
        if not self.game_over_label:  
            self.game_over_label = tk.Label(self, text="Game Over", font=("Arial", 30), fg="red")
            self.game_over_label.place(relx=0.5, rely=0.5, anchor="center")   # centrer le label 

    def remove_game_over(self):
        """ supprimer le label "Game Over" si il existe """
        if self.game_over_label:
            self.game_over_label.destroy()
            self.game_over_label = None
