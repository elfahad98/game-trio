##  Concepts mathématiques : Turmites et Jeu de la Vie

###  Turmites (Fourmi de Langton)

Une **turmite** est une variante d’**automate cellulaire bidimensionnel**.  
Elle évolue sur une grille en suivant des **règles locales simples** :

1. Lire la couleur de la cellule actuelle.  
2. Tourner selon cette couleur (ex. droite sur blanc, gauche sur noir).  
3. Changer la couleur de la cellule.  
4. Avancer d’une case.

Malgré cette simplicité, la turmite génère des **motifs complexes et émergents**.  
Après un certain nombre d’itérations, elle construit souvent un **“highway”** — une structure stable et périodique.  

Ce comportement illustre la **complexité émergente** :  
des règles déterministes très simples peuvent produire une organisation apparente et imprévisible.  

 **Aspects mathématiques :**
- Automates cellulaires discrets.  
- Systèmes dynamiques déterministes.  
- Auto-organisation et comportements chaotiques.  

---

###  Jeu de la Vie (Conway’s Game of Life)

Le **Jeu de la Vie** (John Conway, 1970) est un automate cellulaire où chaque cellule d’une grille  
est soit **vivante (1)** soit **morte (0)**.  
L’évolution dépend du nombre de cellules voisines vivantes selon quatre règles :  

| État actuel | Voisins vivants | État futur |
|--------------|----------------|-------------|
| Vivante      | < 2             | Meurt (solitude) |
| Vivante      | 2 ou 3          | Survit |
| Vivante      | > 3             | Meurt (surpopulation) |
| Morte        | = 3             | Naît (reproduction) |

Ces règles simples produisent des motifs étonnamment variés :
- **Stables** : blocs, ruches  
- **Oscillants** : blinkers, toads   
- **Mobiles** : gliders   

 **Intérêt mathématique :**
- Exemple classique d’**émergence** dans un système déterministe.  
- Le Jeu de la Vie est **Turing-complet**, c’est-à-dire qu’il peut simuler tout calcul logique.  
- Utilisé en **modélisation**, **vie artificielle** et **théorie des automates**.

---

 Ces deux automates démontrent qu’à partir de règles locales et discrètes,  
on peut faire émerger des comportements complexes, une idée centrale en **mathématiques appliquées**, **physique computationnelle** et **intelligence artificielle**.

