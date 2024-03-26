# Test unitaire

## Prérequis

Nous utiliserons [pytest](https://docs.pytest.org/en/8.0.x/) pour ce TP. [pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)

Veuillez installer `pytest`, `pytest-cov` et `pytest-html` avec :
```sh
pip install pytest pytest-cov pytest-html
```

## 1. Tester FizzBuzz

Reprenez l'exercice "FizzBuzz" du TP1. Avant de commencer, vérifiez que la fonction que vous avez implémenté retourne une string, et n'effectue pas directement de `print`.

## 1.1 Tests cas par cas

1. Créez un fichier `test_fizzbuzz.py` dans le même dossier que `fizzbuzz.py`
1. Ajoutez une fonction `test_fizz`: on testera ici que l'implémentation renvoie bien "Fizz" lorsqu'on l'appelle en donnant 3 en argument
1. Ajoutez une fonction `test_buzz`: on testera ici que l'implémentation renvoie bien "Buzz" lorsqu'on l'appelle en donnant 5 en argument
1. Ajoutez une fonction `test_fizzbuzz`: on testera ici que l'implémentation renvoie bien "FizzBuzz" lorsqu'on l'appelle en donnant 15 en argument
1. Ajoutez une fonction `test_number`: on testera ici que l'implémentation renvoie bien "2" lorsqu'on l'appelle en donnant 2 en argument

## 1.2 Tests paramétrisés

On aimerait bien tester la fonction avec plus de valeurs, mais de manière plus efficace. Pour cela, nous utiliserons la paramétrisation de tests avec `@pytest.mark.parametrize`

[Documentation pytest.mark.parametrize](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)

1. Créer un nouveau module `test_fizzbuzz_parametrized.py`
1. Créer une seule fonction de test `test_fizzbuzz`. En utilisant le décorateur `@pytest.mark.parametrize`, testez tous les mêmes cas que précédemment. Les paramètres de notre fonction de test seront :
    - `value: int` : la valeur à donner en argument de la fonction `fizzbuzz` à tester
    - `expected: int` : la valeur de retour attendue
1. Il est maintenant très facile de tester plus de valeurs. Ajouter les tests pour les valeurs suivantes :
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    - 10
    - 20

A noter qu'il est intéressant de tester 0, car c'est un "cas limite".

# 2 Tester une levée d'exception et utilisation du TDD

## 2.1 Ajouter la fonctionnalité en utilisant le TDD

Pour cet exercice, nous allons ajouter une fonctionnalité à notre implémentation de "FizzBuzz" en utilisant le workflow du TDD (Test Driven Development).

Objectif : on voudrait que notre fonction lève une `ValueError` si le nombre donné en argument est strictement négatif.

**ETAPE 1** : ajouter un test à `test_fizzbuzz_parametrized.py`:

- fonction de test `test_value_error_is_raised_for_negative_input`
- quoi tester : on appelle la fonction avec un nombre négatif (par exemple -1) et on vérifie que la fonction a bien levée une exception de type `ValueError`. Pour cela, on pourra utiliesr `with pytest.raises(ValueError)` (cf documentation de pytest)
- Pour l'instant, ce test n'est pas paramétrisé

Exécutez ce test. Il devrait échouer. C'est normal, c'est l'étape "ROUGE" du workflow du TDD.

**ETAPE 2** : modifier notre implémentation de la fonction `fizz_buzz` dans `fizzbuzz.py` jusqu'á ce que notre test  `test_value_error_is_raised_for_negative_input` passe.
C'est l'étape "VERTE" du workflow du TDD.

A priori, cette tâche étant siple et nécessitant peu de code, **l'étape 3 : REFACTOR** n'est pas nécessaire.

## 2.2 Tester plus de valeurs avec la paramétrisation

Paramétrisez le test `test_value_error_is_raised_for_negative_input` et tester les valeurs : -1, -2, -10, -100

# 3. Tester la classe ``Vector``

L'objectif est de tester la classe `Vector` du TP3.

Ouverz le fichier [TP3/test_vectors.py](../TP3/test_vectors.py) et complétez les tests.

Si vous avez besoin d'éxecuter un même test avec plusieurs combinaisons de valeurs, paramétrisez le test.

A tout moment, vous pouvez visualiser la **couverture de test** (code coverage). Pour cela, lancer
```
cd TP3

pytest --cov=. --cov-report=html --cov-report html:./coverage_report.html
```
Ouvrer ensuite le le rapport de coverage `TP3/coverage_report/index.html`. Après chaque nouveau lancement de la commande pytest, vous pouvez simplement actualiser la page web dans votre navigateur.

# 4. Utilisation de mocks

On voudrait tester l'implémentation de l'éxercice "Météo" du TP1.
Nous voulons tester que notre programme est bien capable d'extraire les bonnes informations des données renvoyées par l'API d'OpenWeatherMap.

Nous ne voulons pas déclencher de vraies requêtes vers l'API du service OpenWeatherMap lors de nos tests, car :
- les tests sont exécutés de nombreuses fois, et le risque d'atteindre le quota maximal d'appel de l'API est significatif
- les tests doivent pouvoir être exécutés même si l'API est hors-service
- les tests doivent pouvoir être exécutés même sans connexion internet

Pour cela, nous allons donc **patcher** la fonction `get` de `requests`. C'est-à-dire : à chaque fois que `request.get` sera appelé, python appelera en fait notre fonction mock et non l'implémentation originale dans le package `requests`.

Nous allons utiliser la fixture `monkey_patch` incluse avec `pytest`, mais sachez qu'il y a d'autres possibilités.

[Documentation monkeypatch](https://docs.pytest.org/en/latest/how-to/monkeypatch.html). Cette documentation donnes justement des exemples d'utilisation de monkeypatch pour patcher `requests.get` (section [Monkeypatching returned objects: buliding mock classes](https://docs.pytest.org/en/latest/how-to/monkeypatch.html#monkeypatching-returned-objects-building-mock-classes))

Voici un exemple de ce que l'API renvoie :
```python
{'base': 'stations',
 'clouds': {'all': 9},
 'cod': 200,
 'coord': {'lat': 44.34, 'lon': 10.99},
 'dt': 1707724928,
 'id': 3163858,
 'main': {'feels_like': 277.81,
          'grnd_level': 918,
          'humidity': 85,
          'pressure': 1004,
          'sea_level': 1004,
          'temp': 277.81,
          'temp_max': 279.43,
          'temp_min': 276.6},
 'name': 'Zocca',
 'sys': {'country': 'IT',
         'id': 2044440,
         'sunrise': 1707718882,
         'sunset': 1707755961,
         'type': 2},
 'timezone': 3600,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 194, 'gust': 2.03, 'speed': 1.23}}
```

1. Créez un module ``test_weather.py``
1. Ajouter une fonction `test_get_weather_info` dont le but est de tester la fonction `get_weather`. On patchera la fonction `request.get` avec `get_mock` dans ce test, exactement comme expliqué dans la documentation.
