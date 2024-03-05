# TP 1 - Fondamentaux Python

## Partie 1 : utilisation du terminal de commande

### Commandes à connaitre :
- `echo`
- `cat`
- `cd`
- `pwd`
- `ls [-l]`
- `clear`
- `mkdir` / `rmdir`
- `rm`
- `touch`

Attention, les commandes varient selon le terminal : bash (linux ou git bash) / Windows CMD / PowerShell...
Nous vous conseillons d'utiliser **git bash**.

Pour s'entrainer, exécutez les commandes suivantes :
```shell
touch test.txt
mkdir test_dir
pwd
cd test_dir
pwd
cd ..
pwd
ls
rmdir test_dir
ls
ls ..
```
```shell
echo "hello"
echo "hello" > hello.txt
ls -l
cat hello.txt
rm hello.txt
exit
```

## Partie 2 : exercices en python

**Tout au long du TP :**
- effectuer chaque exercice dans un fichier python séparé
- suivre les conventions de la [PEP8](https://peps.python.org/pep-0008/)
- suivre les principes du code propre vus en cours, en particulier pour les derniers exercices :
  - nommage des variables / fonctions...
  - bonne utilisation des commentaires
  - pas de "magic value"
  - ajouter des docstrings
  - ajouter des annotations de type
  - éviter les duplications de code (DRY)
  - séparation des responsabilités

### 1. Devine le nombre

Pour commencer l'ordinateur va choisir au hasard un nombre compris entre 1 et 100.
L'utilisateur doit alors deviner ce nombre comme ceci :
L'utilisateur propose un nombre. l'ordinateur lui dit s'il est trop petit ou trop grand, et ainsi de suite jusqu'à ce que l'utilisateur trouve le bon nombre.

### 2. Compter les mots

Ecrire un programme qui demande le nom d'un fichier .txt à l'utilisateur. Le fichier devra se trouver dans le même dossier que le script Python.
Le programme devra compter le nombre de fois que le mot "python" est écrit dans le fichier et l'afficher à l'écran. En cas d'échec de lecture du fichier saisi par l'utilisateur, le programme demande à l'utilisateur une nouvelle saisie (maximum 3 essais). Au bout de trois tentatives infructueuses, le programme affiche un message d'erreur et quitte.
Comme exemple, vous pourrez copier-coller un morceau de n'importe quelle documentation de python dans un fichier texte.

### 3. Fizz Buzz

Ecrire une fonction qui prend un nombre entier en paramètre, et qui doit retourner une chaine de caractère :
- "fizz" si le nombre est divisible par 3
- "buzz" si le nombre est divisible par 5
- "fizz buzz" si le nombre est divisible par 3 et 5
- le nombre donné en paramètre s'il n'est divisible par ni 3 ni 5

### 4. Récursion

Ecrire un programme qui utilise la récursion (une fonction qui s'appelle elle-même) pour calculer la somme jusqu'au n-ième terme de la série harmonique.
La série harmonique est la suite des inverses des entiers strictement positifs: `1 + (1 / 2) + (1 / 3) + .. + (1 / n)`.
Example pour N=4:
```py
harmonic_sum(n=4)  # doit retourner 1 + (1 / 2) + (1 / 3) + (1 / 4)
```

### 5. ZCasino

Règles du jeu :
- Le joueur choisi un nombre sur la roulette (entre 0 et 49) et mise une somme d'argent sur ce nombre
  - Si le joueur a choisi le nombre exact choisi par la roulette, le joueur remporte 3 fois sa mise de départ.
  - Si le joueur a misé sur un nombre de la même couleur que celui choisi par la roulette, le joueur remporte 50% de sa mise initiale.
  - Sinon, le joueur ne remporte rien.
- Le joueur peut choisir de miser une nouvelle fois ou de quitter la partie. Le joueur ne peut pas miser une nouvelle fois s'il n'a plus d'argent !

Détails sur la roulette du casino :
- 50 nombres, entre 0 et 49
- les nombres pairs sont noir
- les nombres impairs sont blanc

On veillera à ce que l'utilisateur donne des nombres valides.

Créer un package constitué de plusieurs modules. Par exemple:
- un module consacré à obtenir les inputs de l'utilisateurs
- un module contenant des fonctions utilie au déroulement du jeu
- un module contenant la fonction principale du jeu

### 6. Météo

Le but de cet exercice est d'afficher des données météorologiques à l'utilisateur concernant la ville de son choix.
Le programme devra demander une ville à l'utilisateur. Une fois saisie, récupérer des données comme la température, l'humidité, la vitesse du vent etc, de la ville et les afficher à l'utilisateur.
Si la récupération des données échoue, afficher un message invitant l'utilisateur à réessayer plus tard. Pour tester cela, vous pouvez couper internet.

Détails :
- Pour effectuer des requêtes HTTP, il vous faudra installer [requests](https://pypi.org/project/requests/)
- Nous allons utiliser le service [OpenWeatherMap](https://home.openweathermap.org/) pour récupérer les données météorologiques. Référez-vous au site web et particulièrement à la [documentation de leur API](https://openweathermap.org/api)
- Toute personne utilisant le service doit être identifiée. Une clé (un token, API key en anglais) est souvent utilisé. Cette clé est comme un mot de passe : être doit être unique pour chaque utilisateur et ne jamais être partagée. Cependant, la création de clé API par OpenWeatherMap peut prendre du temps (quelques heures). Pour ce TP, vous allez donc tous utiliser un token déjà créé, **communiqué par email**. Attention : cette clé permet un maximum de 60 requêtes par minute / 1 000 000 de requêtes par mois !

## Partie 3 : utilisation d'un linter et d'un formatter formatter

1. installer ``black`` et `flake8` avec `pip`
2. Executer black et flake8 sur le code écrit durant le TP

Documentations:
- [documentation de flake8](https://flake8.pycqa.org/en/latest/)
- [quickstart documentation de flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart)
- [documentation de black](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)
- [GitHub de flake8](https://github.com/PyCQA/flake8)
- [GitHub de black](https://github.com/psf/black)
