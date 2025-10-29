#  Game-Trio – Mini Collection de Jeux en Python

Une application Python regroupant **trois mini-jeux interactifs** :  
le **Jeu de la Vie de Conway**, le **Snake**, et les **Fourmis de Langton (Turmites)**.  
Chaque jeu est développé avec une logique indépendante mais une structure commune.

---

##  À propos du projet

Ce projet a été réalisé dans le cadre d’un apprentissage en **programmation Python orientée objet** et **simulation de systèmes dynamiques**.  
Il permet d’explorer plusieurs logiques de calcul et d’animation dans une interface graphique simple.

---

##  Jeux inclus

###  1. Conway – Jeu de la Vie
Simulation d’un automate cellulaire où chaque cellule évolue selon ses voisines.  
Les motifs naissent, survivent ou meurent selon les célèbres règles de John Conway.

###  2. Snake
Le classique jeu du serpent : mangez la nourriture, grandissez et évitez les murs !  
Contrôles : flèches directionnelles .

###  3. Turmites
Variation du concept de **fourmis de Langton**, simulant un comportement complexe à partir de règles simples.

---

##  Structure du projet

```bash
game-trio/
├── src/
│   ├── main.py              # Menu principal / point d’entrée
│   ├── snake.py             # Jeu Snake
│   ├── Turmites.py          # Jeu des fourmis de Langton
│   ├── Conway.py            # Jeu de la Vie
│   ├── PlanetTk.py          # Gestion graphique (Tkinter)
│   ├── planetalpha.py       # Gestion des entités / éléments
│   ├── grid_manager.py      # Gestion de la grille
│   └── Element.py           # Classe de base pour les éléments
│
├── docs/
│   └── README.md/         
│
├── .gitignore               # Fichiers ignorés (Python)
├── LICENSE                  # Licence MIT
└── README.md                # Présentation du projet
```


---

## 👤 Auteur

Projet réalisé par **COMBO El-Fahad** – Université de Caen (2024).  
Contact : `el-fahad.combo@etu.unicaen.fr`

---

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier `LICENSE`.


