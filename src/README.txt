=====================================================================================
                    GAME TRIO : SNAKE , TURMITES , CONWAY
=====================================================================================

Bienvenue dans GAME TRIO, une application interactive et pédagogique vous permettant
de jouer à trois jeux captivants : Snake, Turmites, et Conway

=====================================================================================
                 	          MANUEL D'UTILISATION 
=====================================================================================

Au lancement de **main.py**, une interface graphique conviviale s'affiche, vous 
permettant de choisir entre trois jeux. Faites votre choix et amusez-vous !


===============
JEU 1 : Snake
===============

**Description** : Contrôlez un serpent pour qu'il mange des aliments (carrés rouges) 
tout en évitant les murs et votre propre corps.


1. **Commandes de jeu** :
   - Flèche Haut (↑) : Déplace le serpent vers le haut.
   - Flèche Bas (↓) : Déplace le serpent vers le bas.
   - Flèche Gauche (←) : Déplace le serpent vers la gauche.
   - Flèche Droite (→) : Déplace le serpent vers la droite.

2. **Boutons de Contrôle** :
   - **Pause** : Met le jeu en pause.
   - **Reset** : Réinitialise la partie.
   - **Quitter** : Ferme l'application.

**Objectif** : Obtenez le score le plus élevé possible en mangeant les aliments.
 
--------------------------| FONCTIONNALITÉS AJOUTÉES  |------------------------------

1. **Game Controls** : Basculez facilement entre les jeux.

2. **Compteur de score** : Suivez votre score en temps réel.

3. **Message "Game Over"** : Un label s'affiche pour indiquer la fin de la partie.



=================
JEU 2 : Turmites 
=================

**Description** : Un automates cellulaires représentant une "fourmi" qui explore une 
grille en suivant des règles basées sur plusieurs états et couleurs


1. **Commandes de simulation** :
   - Clic gauche : Place une fourmi sur la grille (autant que vous le souhaité).

2. **Boutons de Contrôle** :
   - **Start** : Lance la simulation.
   - **Pause** : Met la simulation en pause.
   - **Reset** : Réinitialise la simulation.
   - **Quitter** : Ferme l'application.


-------------------------------| FONCTIONNALITÉS AJOUTÉES |-----------------------------

1. **Game Controls** : Basculez entre les jeux en un clic.

2. **Compteur d'itérations** : Suivez le nombre d'itérations des fourmis.

3. **Placement manuel** : Ajoutez plusieurs fourmis en cliquant directement sur les cellules.

4. **Gestion des couleurs** : Personnalisez les couleurs des cellules en modifiant le
dictionnaire dans la fonction _init_ de la classe Turmites.



=================
JEU 3 : Conway
=================

**Description**: Un automate cellulaire où les cellules évoluent en fonction de règles
simples d'apparition, de survie et de mort.


1. **Commandes de simulation** :
   - Clic gauche : Ajoute ou enlève une cellule vivante.

2. **Boutons de Contrôle** :
   - **Start** : Lance la simulation.
   - **Pause** : Met la simulation en pause.
   - **Reset** : Réinitialise la simulation.
   - **Quitter** : Ferme l'application.


---------------------------| FONCTIONNALITÉS AJOUTÉES  |------------------------------

1. **Game Controls** : Basculez entre les jeux.

2. **Compteur d'itérations** : Affiche le nombre d'itérations.

3. **Placement manuel** : Ajoutez des cellules vivantes par un clic gauche.

4. **Gestion des couleurs** : Choisissez la couleur des cellules et placez-les dans 
   la grille.

5. **Configurations prédéfinies** : Sélectionnez des motifs prédéfinis et placez-les où 
  vous le souhaitez.


=======================================================================================
                               CHOIX D'IMPLÉMENTATION
=======================================================================================



**1. Base commune pour les jeux** :
Tous les jeux reposent sur une architecture commune basée sur la classe `PlanetTk`, 
simplifiant la gestion des grilles et des interactions utilisateur. Cette conception
facilite l'ajout de nouveaux jeux.


**2. Interface utilisateur intuitive ** :
Les contrôles sont regroupés dans des cadres bien définis, et des labels affichent 
des informations utiles (score, état de pause, "Game Over").


**3. Gestion avancée des événements** :
L'interaction utilisateur (clics, touches) est fluide grâce à une gestion optimisée 
des événements et une boucle `after()` garantissant un fonctionnement réactif.

**4. Flexibilité** :
Les paramètres (taille de grille, couleurs, configurations prédéfinies) sont facilement
modifiables pour une expérience personnalisée.



======================================================================================
                      	     CONTRIBUTION INDIVIDUELLE
======================================================================================

		      Le travail a été réalisé par COMBO EL-fahad 

======================================================================================
                             	    POUR FINIR
======================================================================================


Merci pour vos conseils et votre soutien tout au long de ce semestre, Ce projet 
reflète mes efforts pour mettre en pratique les connaissances acquises et démontrer 
ma créativité. notamment dans le cadre de ce projet. 

	   je choisis d'exploiter cette place pour vous souhaitez 

======================================================================================
			   	BONNE ANNEE 2025 !!
======================================================================================