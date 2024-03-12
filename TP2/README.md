# TP2 - Utiliser Git avec GitHub

## Objectifs de ces travaux pratiques

* Apprendre à utiliser Git en travaillant sur des programmes Python
* Appliquer le processus de revue de code sur Github

## 1. Téléchargez les fichiers de ce dépôt

Commencez par cloner ce dépôt:
1. retournez à sa racine: https://github.com/sebclrsn/TP-AOO-python-git
2. cliquez sur le bouton vert "Code"
3. copiez l'URL du dépôt
4. ouvrez un terminal Git Bash à l'emplacement de votre choix
5. clonez ce dépôt avec l'URL copiée précédemment.


## 2. Crééz votre espace de travail

### 2.1. Un peu de configuration

Commencez par configurer Git sur votre PC.

Dans l'explorateur de fichiers, allez jusqu'à l'emplacement du dépôt téléchargé, puis ouvrir une console Git Bash avec un clic droit.

```bash
# permet de pousser sur une branche qui n'est pas encore présente sur le dépôt distant
git config --global push.autoSetupRemote true
```

Ensuite, installez les packages Python qui seront nécessaires pour exécuter le programme:

```bash
# matplotlib est une bibliothèque de création de graphiques
pip install matplotlib
```

Finalement, installez pre-commit et initialisez les vérifications du projet:

```bash
# pre-commit permet d'exécuter des vérifications automatiques lors d'un commit
pip install pre-commit
pre-commit install
```

### 2.2. Crééz votre branche

Créez une nouvelle branche que vous appellerez ``"1A_ASE_NOM_Prénom"`` et placez vous sur cette branche à l'aide des commandes vues en cours.

Ce sera votre espace de travail pour la suite de ce TP.


## 3. Travaillez ensemble sur le même fichier

Ce TP vise à manipuler un [fichier de données](/TP2/data/sensor_data.csv) contenant des données temporelle des mesures d'une centrale inertielle.

Ce fichier est au format CSV (Comma-Separated Values, valeurs séparées par virgules) et contient, dans l'ordre:
- le temps en secondes
- les vitesses angulaires selon les axes du repère de la centrale inertielle en °/s
- les accélérations linéaires selon les axes du repère de la centrale inertielle en multiples de la gravité
- les mesures d'intensité des champs magnétiques selon les axes du repère de la centrale inertielle en uT (micro Tesla, ces mesures ne feront pas l'objet d'une étude pendant ce TP).

Ce dépôt contient un dossier "code" ou vous trouverez plusieurs modules Python:
- un [module pour la lecture des données d'entrée](/TP2/imu_analysis/reader.py) en format CSV
- un [module pour la visualisation des données](/TP2/imu_analysis/plotting.py) utilisant la bibliothèque [matplotlib](https://matplotlib.org/stable/)
- un [module pour le traitement des données](/TP2/imu_analysis/processing.py), auquel vous ajouterez des fonctionnalités
- un [module de point d'entrée](/TP2/imu_analysis/main.py) qui utilise les 3 derniers modules pour lire, traiter et visualiser les données.


Vous pouvez exécuter le programme avec la commande suivante:

```bash
python ./TP2/imu_analysis/main.py
```

## 4. Contribuez au projet

### 4.1. Lissage des signaux de mesure

Implémentez une fonction ``calculate_moving_average(data: list[float], interval: int)`` qui va calculer la moyenne glissante d'un des signaux mesurés.

On définira la moyenne glissante comme:

```math
\bar{x}_n = \frac{1}{N} \sum_{k=n}^{n + N} x_{n-k}
```

où:
- $\bar{x}_n$ désigne la moyenne glissante du n-ième terme
- $N$ désigne la fenêtre de la moyenne glissante (représentée par le paramètre ``interval``)

Pour vérifier le bon fonctionnement de la fonction, on pourra la tester avec les valeurs suivantes:
- ``data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]``
- ``n = 4``

On s'attendra alors à obtenir comme valeur de retour ``[1.5, 2.5, 3.5, 4.5, 5.5, 6.5]`` car:
- $\bar{x}_0 = \frac{1}{4} \cdot (0 + 1 + 2 + 3)$
- $\bar{x}_1 = \frac{1}{4} \cdot (1 + 2 + 3 + 4)$
- $\bar{x}_2 = \frac{1}{4} \cdot (2 + 3 + 4 + 5)$

### 4.2. Visualisation du signal lissé

Modifiez le programme dans ``main.py`` afin de visualiser votre signal lissé au lieu du signal brut mesuré.

Vous prendrez le signal qui suit celui de votre voisin de gauche (si votre voisin de gauche prend la
vitesse de rotation selon l'axe y, vous prendrez vitesse de rotation selon l'axe z, s'il prend
l'accélération linéaire selon l'axe z vous reprendrez la vitesse de rotation selon l'axe x).

## 5. Poussez vos changements sur le dépôt

### 5.2. Mettez en ligne vos changements

À l'aide des commandes vues en cours, vous allez ensuite:
- Ajouter les fichiers que vous avez modifié
- Faire un commit avec le message ``<NOM> <Prénom> lissage du signal <signal que vous avez lissé>`` (wx / wy / wz / ax / ay / az)
- Poussez vos changements sur votre branche

### 5.2. Ouvrez une Pull Request

En retournant sur GitHub dans votre navigateur, assurez vous que vous êtes bien connecté avec votre
compte (avec votre adresse UHA).
Ensuite, ouvrez une Pull Request en ajoutez les "Reviewers" suivants:
- ``sebclrsn``
- ``LoicRiegel``

## 6. Pour aller plus loin

Ajoutez des fonctions aux modules Python de traitement et de visualisation pour afficher l'évolution
de l'orientation de la centrale inertielle en degrés selon les 3 axes (angles de roulis, tangage et lacet).

Il faudra alors calculer l'intégrale de la vitesse angulaire. On pourra utiliser une méthode
d'intégration numérique telle que la méthode des rectangles.
