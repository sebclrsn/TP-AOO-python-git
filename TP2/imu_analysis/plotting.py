"""
Module pour la visualisation des mesures
****************************************
"""

try:
    import matplotlib.pyplot as plt
except ImportError as e:
    raise ImportError(
        f"La bibliothèque {e.name} n'a pas pu être trouvée. "
        "Veuillez l'installer avec 'pip install {e.name}'"
    )


def plot_angular_speed(t: list[float], wx: list[float], wy: list[float], wz: list[float]):
    """Crée un nouveau sous-graphe pour la visualisation des vitesses angulaires.

    :param t: liste des mesures temporelles.
    :param wx: liste des mesures de vitesse de rotation selon l'axe x.
    :param wy: liste des mesures de vitesse de rotation selon l'axe y.
    :param wz: liste des mesures de vitesse de rotation selon l'axe z.
    """
    # on crée un nouveau subplot
    axes = plt.subplot(2, 1, 1)
    line_wx, line_wy, line_wz = plt.plot(
        t[len(t) - len(wx) :],
        wx,
        "r",
        t[len(t) - len(wy) :],
        wy,
        "b",
        t[len(t) - len(wz) :],
        wz,
        "g",
    )

    line_wx.set_label(r"$\omega_x$")
    line_wy.set_label(r"$\omega_y$")
    line_wz.set_label(r"$\omega_z$")
    axes.legend()

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
    line_ax, line_ay, line_az = plt.plot(t, ax, "r", t, ay, "b", t, az, "g")

    line_ax.set_label(r"$a_x$")
    line_ay.set_label(r"$a_y$")
    line_az.set_label(r"$a_z$")
    axes.legend()

    plt.xlabel("Temps [s]")
    plt.ylabel(r"Accélération linéaire [$\frac{9,81 \cdot m}{s^2}$]")


def show_plots():
    plt.show()
