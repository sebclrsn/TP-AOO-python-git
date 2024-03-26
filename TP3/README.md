# TP3 - Orienté Objet

## Exercices 1

Utiliser [person.py](./person.py).

#### 1.1 Ajouter des attributs

Rajouter les attributs `email` et `phone` à la classe `Person` et ajouter ce code à `main`:
```py
print(f"Email: {john.email}")
print(f"Phone: {john.phone}")
```

#### 1.2 Method `__str__`

Exécuter `print(john)` dans `main`

```py
def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"
```

Exécuter `print(john)` dans `main` à nouveau.

## Exercice 2

Utiliser [person_2.py](./person_2.py).

Rajouter une ligne au niveau du TODO pour obtenir la sortie suivante :
```
Is John of age: True
Is Bob of age: True
Change the age of majority to 32
Is John of age: False
Is Bob of age: True
```
Cette ligne ne **doit pas utiliser les objets `john` ou `bob`**

## Exercice 3

Utiliser [vectors.py](./vectors.py).

#### 3.1 Création des classes

Un vecteur du plan est composé d'un point de départ et d'un point d'arrivé.
Créez une classe `Point` et une classe `Vector` de manière à représenter des points et des vecteurs du plan en Python.
Vérifier que la fonction `main` s'exécute sans erreurs et que les éléments affichés sont mathématiquements corrects.


#### 3.2 Produit scalaire et norme

Ajouter une méthode qui calcule la norme d'un vecteur.
Ajouter une méthode qui calcule le produit scalaire de deux vecteurs.


#### 3.3 Ajouter des méthodes spéciales

Ajouter la méthode spéciale `__str__` aux deux classes. Résultat attendu :
```sh
print(point_A)  # "Point(-2, -1)"
print(vector_AB)  # "Vector(5, 8)"
```

Ensuite, ajouter les méthodes séciales à la classe `Vector`:
- `__add__`
- `__sub__`
- `__neg__`
- `__mul__`
Vérifier que la fonction `main_2` s'exécute sans erreurs et vérifier que les résultats sont mathématiquement corrects.

Pour les annotations de types, on pourra utiliser le type `Self`
```py
from typing import Self
```
ou bien utiliser `Vector` directement (dans ce cas, il sera nécessaire d'importer `from __future__ import annotations`).

#### 3.4 Constructeur alternatif

On souhaite pouvoir créer un vecteur en donnant à l'initialisation seulement le point d'arrivé. Dans ce cas, le point de départ sera l'origine.
On souhaite que ce code fonctionne :
```py
origin = Point.origin()  # Point(0, 0)
vector_OB = Vector.from_points(point_A, point_B)
```

En utilisant une **méthode de class**, implémenter la méthode `origin` sur la classe `Point` et `from_points` sur la classe `Vector`.


## Exercice 4

Utiliser [threads.py](./threads.py).

#### 4.1 Exécuter et comprendre le code

Jusqu'à présent, les programmes que nous avons écrit s'exécutaient dans un seul thread (le thread principal). Exécuter du code dans un nouveau thread permet d'exécuter ce code **en parallèle**.
Il y a plusieurs manières de créer un thread en Python. Pour ce TP, nous allons nous créer une classe qui **hérite de `threading.Thread`**. `threading.Thread` contient plusieurs méthodes et attributs utiles :
- `my_thread.is_alive()`: renvoie True si le thread est en cours d'exécution, False sinon
- `my_thread.start()`: crée le thread et commence l'exécution du code de la méthode `run`
- `my_thread.run()`: code exécuté dans le thread.
- `my_thread.run()`: code exécuté dans le thread.
- `my_thread.join()`: block l'exécution (attend) jusqu'á ce que `my_thread` ait fini (jusqu'à que ce `my_thread.run` ait fini).

A noter qu'un thread ne peut être démarré qu'une seule fois !

Lisez le code, exécutez-le et comprenez son fonctionnement. Vous pouvez changer les valeurs des `time.sleep` et observer le résultat.

Resources pour aller plus loin après le TP :
- https://realpython.com/intro-to-python-threading/

#### 4.2 Factorisation

Le code actuel contient plusieurs problèmes :
- "magic values" pour 1s et 3s utilisés dans time.sleep(...)
- "magic values" pour 1 et 3 utilisés dans for i in range(...)
- duplications de code : les deux classes sont quasi identiques

Factorisez ces deux classes en une seule pour enlever la duplication de code. Pour éviter d'hardcoder les valeurs cités plus haut, passez-les en paramètre de l'initialiseur.
Exemple de code main:
```py
counter1_thread = Counter(stop_value=10, sleep_delay_s=1)  # count from 0 to 10 with 1s delay
counter2_thread = Counter(50, 3)  # count from 0 to 50 with 3s delay
counter3_thread = Counter(20)  # count from 0 to 20 with 1s delay (1s is the default)
```

Vous devrez pour cela *overrider* la méthode `__init__`. Pensez à appeler `super()__init__()`.
