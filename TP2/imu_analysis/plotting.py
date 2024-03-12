"""
Module pour la visualisation des mesures
****************************************
"""

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    raise ImportError(
        f"La bibliothèque {e.name} n'a pas pu être trouvée. "
        f"Veuillez l'installer avec 'pip install {e.name}'"
    )


def plot_angular_speed(t: list[float], wx: list[float], wy: list[float], wz: list[float]):
    """Crée un nouveau sous-graphe pour la visualisation des vitesses angulaires.

    :param t: liste des mesures temporelles.
    :param wx: liste des mesures de vitesse de rotation selon l'axe x.
    :param wy: liste des mesures de vitesse de rotation selon l'axe y.
    :param wz: liste des mesures de vitesse de rotation selon l'axe z.
    """
    # La figure comprendra 2 lignes de sous-figures et 1 colonne de sous-figures.
    # Notre sous-figure sera en 1ère position (en haut).
    axes = plt.subplot(2, 1, 1)
    # On s'assure qu'on a le même nombre de points
    # pour le temps et pour les vitesses de rotation
    tx = t[len(t) - len(wx) :]
    ty = t[len(t) - len(wy) :]
    tz = t[len(t) - len(wz) :]
    # On ajoute une courbe pour les vitesses de rotation en fonction du temps
    line_wx, line_wy, line_wz = plt.plot(tx, wx, "r", ty, wy, "b", tz, wz, "g")

    # On ajoute une légende à chaque courbe
    line_wx.set_label(r"$\omega_x$")
    line_wy.set_label(r"$\omega_y$")
    line_wz.set_label(r"$\omega_z$")
    axes.legend()
    axes.grid()

    # On ajoute une légende à chaque axe
    plt.xlabel("Temps [s]")
    plt.ylabel(r"Vitesse de rotation [$\frac{°}{s}$]")


def plot_linear_acceleration(t: list[float], ax: list[float], ay: list[float], az: list[float]):
    """Crée un nouveau sous-graphe pour la visualisation des acélérations linéaires.

    :param t: liste des mesures temporelles.
    :param ax: liste des mesures d'accélération linéaire selon l'axe x.
    :param ay: liste des mesures d'accélération linéaire selon l'axe y.
    :param az: liste des mesures d'accélération linéaire selon l'axe z.
    """
    axes = plt.subplot(2, 1, 2)
    tx = t[len(t) - len(ax) :]
    ty = t[len(t) - len(ay) :]
    tz = t[len(t) - len(az) :]
    line_ax, line_ay, line_az = plt.plot(tx, ax, "r", ty, ay, "b", tz, az, "g")

    line_ax.set_label(r"$a_x$")
    line_ay.set_label(r"$a_y$")
    line_az.set_label(r"$a_z$")
    axes.legend()
    axes.grid()

    plt.xlabel("Temps [s]")
    plt.ylabel(r"Accélération linéaire [$\frac{9,81 \cdot m}{s^2}$]")


def show_plots():
    """Fait apparaître une figure avec tous les graphes précédemment construits."""
    plt.show()
