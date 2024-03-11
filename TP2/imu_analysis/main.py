from plotting import plot_angular_speed, plot_linear_acceleration, show_plots
from reader import read_measurements_file


def main():
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
