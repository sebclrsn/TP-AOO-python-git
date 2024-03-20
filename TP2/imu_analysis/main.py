from plotting import plot_angular_speed, plot_linear_acceleration, show_plots
from processing import calculate_moving_average
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

    t_lissé = []
    wx_lissé = []
    wy_lissé = []
    wz_lissé = []
    ax_lissé = []
    ay_lissé = []
    az_lissé = []

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

    interval_lissage = 1000

    t_lissé.append(calculate_moving_average(t, interval_lissage))
    wx_lissé.append(calculate_moving_average(wx, interval_lissage))
    wy_lissé.append(calculate_moving_average(wy, interval_lissage))
    wz_lissé.append(calculate_moving_average(wz, interval_lissage))
    ax_lissé.append(calculate_moving_average(ax, interval_lissage))
    ay_lissé.append(calculate_moving_average(ay, interval_lissage))
    az_lissé.append(calculate_moving_average(az, interval_lissage))

    plot_angular_speed(t_lissé, wx_lissé, wy_lissé, wz_lissé)
    plot_linear_acceleration(t_lissé, ax_lissé, ay_lissé, az_lissé)

    show_plots()


if __name__ == "__main__":
    main()
