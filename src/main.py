""" 
Auteur : COMBO EL-fahad 
Date de création : 22 Decembre 2023

"""

import tkinter as tk
from tkinter import ttk
from snake import Snake
from Turmites import Turmites
from Conway import Conway



class MyApp(tk.Tk):
    def __init__(self, master):
        self.master = master
        self.master.title("Main App - Choose Your Game")
        self.master.geometry("600x500")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 14, 'bold'), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 18, 'bold'), foreground='#000000')

        # Le fond du gradient #
        
        self.background_canvas = tk.Canvas(self.master, width=600, height=500)
        self.background_canvas.pack(fill=tk.BOTH, expand=True)
        self.create_gradient(self.background_canvas, '#1E3A8A', '#3B82F6')

        # mainframe avec un effet 
        
        self.shadow_frame = tk.Frame(self.master, bg="#BBBBBB")
        self.shadow_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=460, height=410)

        self.main_frame = tk.Frame(self.master, bg="#FFFFFF", highlightbackground="#C0C0C0", highlightthickness=2)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=450, height=400)

        title_label = ttk.Label(self.main_frame, text=" Welcome to My App ", anchor="center")
        title_label.pack(pady=(20, 10))

        ##  BOUTON LANCEMENT JEU ## 

        btn_snake = ttk.Button(self.main_frame, text="Snake Game", command=self.launch_snake)
        btn_snake.pack(pady=20, ipadx=10, ipady=5)

        btn_turmites = ttk.Button(self.main_frame, text="Turmites Simulation", command=self.launch_turmites)
        btn_turmites.pack(pady=20, ipadx=10, ipady=5)

        btn_conway = ttk.Button(self.main_frame, text="Conway Game of Life", command=self.launch_conway)
        btn_conway.pack(pady=20, ipadx=10, ipady=5)

    def create_gradient(self, canvas, start_color, end_color):
        """Cree un dégradé vertical"""
        for i in range(500):
            r1, g1, b1 = self.hex_to_rgb(start_color)
            r2, g2, b2 = self.hex_to_rgb(end_color)
            r = int(r1 + (r2 - r1) * (i / 500))
            g = int(g1 + (g2 - g1) * (i / 500))
            b = int(b1 + (b2 - b1) * (i / 500))
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, 600, i, fill=color)

    @staticmethod
    def hex_to_rgb(hex_color):
        """Convertir colour hexa en tuple RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def launch_snake(self):
        self.clear_main_frame()
        snake_game = Snake(self.master, parent_app=self)
        snake_game.pack(fill=tk.BOTH, expand=True)

    def launch_turmites(self):
        self.clear_main_frame()
        turmites_sim = Turmites(self.master, parent_app=self)
        turmites_sim.pack(fill=tk.BOTH, expand=True)

    def launch_conway(self):
        self.clear_main_frame()
        conway_game = Conway(self.master, parent_app=self)
        conway_game.pack(fill=tk.BOTH, expand=True)

    def switch_to_snake(self):
        self.launch_snake()

    def switch_to_turmites(self):
        self.launch_turmites()

    def switch_to_conway(self):
        self.launch_conway()

    def clear_main_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    master = tk.Tk()
    app = MyApp(master)
    master.mainloop()


