from plotting import plot_angular_speed, plot_linear_acceleration, show_plots
from reader import read_measurements_file
from processing import calculate_moving_average

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
    wx_l=calculate_moving_average(wx,100)
    wy_l=calculate_moving_average(wy,100)
    wz_l=calculate_moving_average(wz,100)
    ax_l=calculate_moving_average(ax,100)
    ay_l=calculate_moving_average(ay,100)
    az_l=calculate_moving_average(az,100)

    plot_angular_speed(t, wx_l, wy_l, wz_l)
    plot_linear_acceleration(t, ax_l, ay_l, az_l)

    show_plots()


if __name__ == "__main__":
    main()
