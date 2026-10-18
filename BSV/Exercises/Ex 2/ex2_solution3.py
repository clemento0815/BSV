"""Bullet trajectories for different gun inclinations [deg]"""
# author: Clemens Loher
# date: 2026-10-09

# Import standard packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal


# Assignment 2.2 Gunpointfunction
def plot_gunpoint(v0, alpha_deg, g=9.81, y0=1.6):
    """Berechnet die Flugbahn unter Berücksichtigung der Abwurfhöhe y0, plottet sie in das aktuelle Diagramm und gibt die Gesamtdistanz zurück."""
    # Umrechnung von Grad in Bogenmaß
    alpha = np.radians(alpha_deg)

    # Exakte Flugzeit mit Schulterhöhe (1.6 m) y0 berechnen mit der Mitternachtsformel für y(t) = 0
    a = -0.5 * g
    b = v0 * np.sin(alpha)
    c = y0

    # Mitternachtsformel für t_end (positives Ergebnis für die Flugdauer bis y=0)
    t_end = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)

    # Zeitvektor, x- und y-Koordinaten
    t = np.linspace(0, t_end, 500)
    x = v0 * np.cos(alpha) * t
    y = y0 + v0 * np.sin(alpha) * t - 0.5 * g * t**2

    # Flugbahn im Plot einzeichnen
    plt.plot(x, y, label=f"{alpha_deg}")

    # Einschlagspunkt am Boden (letzter x-Wert entspricht der exakten Flugweite)
    distance = x[-1]
    print(f"Winkel: {alpha_deg:2d}° -> Flugweite: {distance:8.2f} m")
    return distance


# Assignment 2.3 Plotting all trajectories together for different angles
if __name__ == "__main__":
    v0 = 1000  # m/s (gemäß Aufgabe 3)
    g = 9.81

    plt.figure()

    # Winkel von 5 bis 45 Grad in 5er-Schritten
    angles = range(5, 50, 5)

    # Speichern der Einschlagspunkte für die Legende ("Impacts")
    impact_x = []
    impact_y = []

    for alpha in angles:
        dist = plot_gunpoint(v0, alpha, g, y0=1.6)
        impact_x.append(dist)
        impact_y.append(0)  # y ist beim Einschlag am Boden immer 0

    # Rote Sternchen für die Einschlagpunkte
    plt.plot(impact_x, impact_y, "rx", markersize=8, label="Impacts")

    # Plot Beschriftungen und Legende
    plt.title("Bullet trajectories for different gun inclinations [deg]")
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m]")
    plt.grid(True)
    plt.legend()

    # Plot aller Flugbahnen zusammen
    plt.show()
