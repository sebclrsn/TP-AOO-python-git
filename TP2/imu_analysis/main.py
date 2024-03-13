from plotting import plot_angular_speed, plot_linear_acceleration, show_plots
from reader import read_measurements_file


def main():
    """Fonction principale du projet.

    Cette fonction va:
    - lire le fichier de mesures et en extraire les données
    - lisser les données (A AJOUTER)
    - créer les graphes des données
    - afficher les graphes créés.
    """
    t = []
    wx = []
    wy = []
    wz = []
    ax = []
    ay = []
    az = []

    for measurement in read_measurements_file():
        t.append(measurement.t)
        wx.append(measurement.wx)
        wy.append(measurement.wy)
        wz.append(measurement.wz)
        ax.append(measurement.ax)
        ay.append(measurement.ay)
        az.append(measurement.az)

    plot_angular_speed(t, wx, wy, wz)
    plot_linear_acceleration(t, ax, ay, az)

    show_plots()


if __name__ == "__main__":
    main()
def calculate_moving_average(data: list[float],interval: int):
    moyennes = []
    for i in range(len(data) - interval + 1):
        moyenne = sum(data[i:i+interval]) / interval
        moyennes.append(moyenne)
    return moyennes

# Exemple d'utilisation
data = [0,1,2,3,4,5,6,7,8,9]
interval = 4
resultat = moyenne_glissante(data, interval)
print("Moyennes glissantes:", resultat)