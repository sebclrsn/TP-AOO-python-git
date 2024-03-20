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

    for measurement in read_measurements_file():
        t.append(measurement.t)
        wx.append(measurement.wx)
        wy.append(measurement.wy)
        wz.append(measurement.wz)
        ax.append(measurement.ax)
        ay.append(measurement.ay)
        az.append(measurement.az)

    t_liss = calculate_moving_average(t, 4)
    wx_liss = calculate_moving_average(wx, 4)
    wy_liss = calculate_moving_average(wy, 4)
    wz_liss = calculate_moving_average(wz, 4)
    ax_liss = calculate_moving_average(ax, 4)
    ay_liss = calculate_moving_average(ay, 4)
    az_liss = calculate_moving_average(az, 4)

    plot_angular_speed(t_liss, wx_liss, wy_liss, wz_liss)
    plot_linear_acceleration(t_liss, ax_liss, ay_liss, az_liss)

    show_plots()


if __name__ == "__main__":
    main()
