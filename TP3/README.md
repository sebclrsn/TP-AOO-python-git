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


#### 3.2 Produit scalaire

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

#### 3.4 Constructeur alternatif

On souhaite pouvoir créer un vecteur en donnant à l'initialisation seulement le point d'arrivé. Dans ce cas, le point de départ sera l'origine.
On souhaite que ce code fonctionne :
```py
vector_OB = Vector.from_origin(point_B)
```

En utilisant une **méthode de class**, implémenter la méthode `from_origin` sur la classe `Vector`.
