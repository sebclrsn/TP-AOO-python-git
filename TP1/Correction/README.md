# Correction

## Usage

Attention, je n'ai pas créé de package python. Il faut donc exécuter les scripts python **depuis ce dossier** avec le terminal:

```sh
cd correction
python guess_the_number.py
python count_words.py  # then input testfiles/words.txt
```

Notez que la fonction `utils.get_int_from_user` est assez grande et a beaucoup de responsabilités. Si, dans le futur, nous voulons changer le comportement (ajouter des checks, ou en modifier...), on pourrait extraire chaque vérification dans une petite fonction spécialisée:
- une fonction qui vérifie la conversion en nombre
- une fonction qui vérifie qu'on a un int et pas un float
- une fonction qui vérifie le range
- ...
