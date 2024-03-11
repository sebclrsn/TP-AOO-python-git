"""
Module pour la lecture du fichier de mesures
********************************************
"""

import csv

# un namedtuple est comme un tuple, mais on peut accéder à ses éléments comme à des attributs
from collections import namedtuple

# pathlib permet de parcourir et manipuler des dossiers et fichiers
# c'est une alternative plus orientée objets à os.path
from pathlib import Path

# typing contient tous les types du langage Python afin de construire des annotations de type
from typing import Iterator

# Un namedtuple qui représente les données de mesure de la centrale intertielle.
#
# Example:
#
# ```python
# mesure = SensorData(0.1, 0, -0.2, 1.42, 0, -9.81)
# assert mesure.az == mesure[5]
# ```
ImuData = namedtuple("ImuData", ["t", "wx", "wy", "wz", "ax", "ay", "az"])


SAMPLE_DATA_PATH = Path(__file__).parent.parent / "data/sensor_data.csv"


def read_measurements_file(
    path_to_csv_file: Path = SAMPLE_DATA_PATH,
) -> Iterator[ImuData]:
    """Lecture du fichier de mesures de la centrale inertielle.

    Utilisation:

    ```python
    for measurement in read_measurements_file():
        ...
    ```
    """
    with open(path_to_csv_file, "r", encoding="utf-8") as measurements_content:
        csv_reader = csv.reader(measurements_content)
        # on omet la 1ère ligne du fichier qui contient les noms des champs
        # (on considère les champs déjà connus)
        field_names = next(csv_reader)  # noqa: F841
        # on boucle sur le reste des valeurs du fichier de mesures
        for measurement in csv_reader:
            # on extrait les vitesse angulaires et les accélérations
            # et on omet toute valeur supplémentaire
            t, wx, wy, wz, ax, ay, az, *_ = map(float, measurement)
            yield ImuData(t, wx, wy, wz, ax, ay, az)
