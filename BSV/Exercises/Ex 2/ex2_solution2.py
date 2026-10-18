"""Gunpoint function"""

# author: Clemens Loher
# date: 2026-10-09

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal


def plot_gunpoint(v0, alpha_deg, g=9.81, y0=1.6):
    """Berechnet die Flugbahn einer Kugel unter Berücksichtigung der Schulterhöhe y0, plottet sie und gibt die Flugweite zurück."""

    # Umrechnung von Grad in Bogenmaß
    alpha = np.radians(alpha_deg)

    # Exakte Flugzeit mit der Mitternachtsformel für y(t) = 0 berechnen
    a = -0.5 * g
    b = v0 * np.sin(alpha)
    c = y0

    t_end = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)

    # Zeitvektor und Trajektorie berechnen
    t = np.linspace(0, t_end, 500)
    x = v0 * np.cos(alpha) * t
    y = y0 + v0 * np.sin(alpha) * t - 0.5 * g * t**2

    # Flugbahn plotten
    plt.figure()
    plt.plot(x, y, label=f"v0 = {v0} m/s, Winkel = {alpha_deg} Grad")
    plt.plot(x[-1], 0, "rx", markersize=8, label="Impact")  # Einschlagpunkt

    plt.title('Bullet Trajectory ("Gunpoint")')
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m]")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")

    # Flugweite bestimmen
    distance = x[-1]
    return distance


if __name__ == "__main__":
    # Parameter gemäß Aufgabenstellung
    v0 = 1000  # Mündungsgeschwindigkeit in m/s
    alpha = 45  # Beispielwinkel in Grad

    # Funktionsaufruf und Speichern der Weite
    flight_distance = plot_gunpoint(v0=v0, alpha_deg=alpha, y0=1.6)

    # Ausgabe der Flugweite im Terminal
    print(
        f"Bei einem Winkel von {alpha}° und v0 = {v0} m/s beträgt die Flugweite: {flight_distance:.2f} Meter."
    )

    # Plot anzeigen
    plt.show()
  
