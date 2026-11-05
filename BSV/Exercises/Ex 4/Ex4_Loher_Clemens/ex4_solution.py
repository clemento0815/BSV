""" Dicom File einlesen (mit Claude AI gelöst)

-> Gemini trotz ca. 20 Versuchen nicht erfolgreich abgebrochen und Claude gekauft. 
Claude hatte alle Fehler die Gemini gemacht hat mit 2 Prompts beseitigt und die Aufgabe sauber gelöst!

Aufgabe:
1. Je eine DICOM-Datei aus data/SER00002 und data/SER00003 einlesen.
2. Bestimmen, welche Ansichten und Einstellungen (vgl. Abbildung in der
   Aufgabenstellung) in den Daten gezeigt werden.
3. Für einen Datensatz Kanten mit skimage.filters.sobel finden, Original und
   Kantenbild in einer gemeinsamen Abbildung darstellen und als
   'knee_edges.jpg' speichern.
"""

# author: Clemens Loher
# date: 2026-10-30

# Import standard packages
import os
import matplotlib.pyplot as plt
import numpy as np
import pydicom
from skimage.filters import sobel

# Absoluter Pfad zum Skript-Verzeichnis und zum Datenordner
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "Assignment_IIR", "data")

path_ser2 = os.path.join(data_dir, "SER00002")
path_ser3 = os.path.join(data_dir, "SER00003")


# ---------------------------------------------------------------------------
# 1. Einlesen der DICOM-Daten
# ---------------------------------------------------------------------------
def lade_dicom(pfad):
    """Liest eine DICOM-Datei ein. Ist 'pfad' ein Ordner, wird die mittlere
    Schicht der Serie (nach InstanceNumber sortiert) eingelesen."""
    if os.path.isfile(pfad):
        return pydicom.dcmread(pfad)

    slices = []
    for name in os.listdir(pfad):
        voll = os.path.join(pfad, name)
        if os.path.isfile(voll):
            try:
                ds = pydicom.dcmread(voll)
                if "PixelData" in ds:
                    slices.append(ds)
            except Exception:
                pass  # keine DICOM-Datei, überspringen

    if not slices:
        raise ValueError(f"Keine DICOM-Bilder gefunden in: {pfad}")

    slices.sort(key=lambda s: int(getattr(s, "InstanceNumber", 0)))
    return slices[len(slices) // 2]


dcm2 = lade_dicom(path_ser2)
dcm3 = lade_dicom(path_ser3)


# ---------------------------------------------------------------------------
# 2. Bestimmen der Ansichten und Einstellungen anhand der Metadaten
# ---------------------------------------------------------------------------
def bestimme_ansicht(ds):
    """Ordnet ein DICOM-Bild anhand des Protokollnamens einer der vier
    Ansichten aus der Abbildung der Aufgabenstellung zu."""
    protokoll = str(getattr(ds, "ProtocolName", "")).lower()

    if "cor" in protokoll:
        ansicht = "koronal (Bild oben links)"
    elif "tra" in protokoll:
        ansicht = "transversal (Bild oben rechts)"
    elif "sag" in protokoll and protokoll.startswith("t1"):
        ansicht = "sagittal (Bild unten rechts)"
    elif "sag" in protokoll:
        ansicht = "sagittal (Bild unten links)"
    else:
        ansicht = "nicht eindeutig bestimmbar"

    if protokoll.startswith("t1"):
        gewichtung = "T1-gewichtet"
    elif protokoll.startswith("t2"):
        gewichtung = "T2-gewichtet"
    elif protokoll.startswith("pd"):
        gewichtung = "PD-gewichtet (Protonendichte)"
    else:
        gewichtung = "unbekannte Gewichtung"

    if "_fs" in protokoll:
        gewichtung += ", mit Fettsättigung"

    return ansicht, gewichtung


ergebnisse = {}
for name, ds in [("SER00002", dcm2), ("SER00003", dcm3)]:
    ansicht, gewichtung = bestimme_ansicht(ds)
    ergebnisse[name] = (getattr(ds, "ProtocolName", "Unbekannt"), ansicht, gewichtung)

    print(f"=== {name} ===")
    print(f"Protokollname:        {getattr(ds, 'ProtocolName', 'Unbekannt')}")
    print(f"Serienbeschreibung:   {getattr(ds, 'SeriesDescription', 'Unbekannt')}")
    print(f"TE (Echozeit):        {getattr(ds, 'EchoTime', 'Unbekannt')} ms")
    print(f"TR (Repetitionszeit): {getattr(ds, 'RepetitionTime', 'Unbekannt')} ms")
    print(f"Schichtdicke:         {getattr(ds, 'SliceThickness', 'Unbekannt')} mm")
    print(f"Matrixgröße:          {ds.pixel_array.shape}")
    print(f"--> Ansicht:          {ansicht}")
    print(f"--> Einstellung:      {gewichtung}\n")

print("=== Ergebnis ===")
for name, (protokoll, ansicht, gewichtung) in ergebnisse.items():
    print(f"{name}: {protokoll} -> {ansicht}, {gewichtung}")


# ---------------------------------------------------------------------------
# 3. Kantenfindung mit skimage.filters.sobel und Speichern als knee_edges.jpg
# ---------------------------------------------------------------------------
image_data = dcm3.pixel_array.astype(float)
edge_image = sobel(image_data)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image_data, cmap="gray")
axes[0].set_title(f"Original ({getattr(dcm3, 'ProtocolName', 'SER00003')})")
axes[0].axis("off")

axes[1].imshow(edge_image, cmap="gray")
axes[1].set_title("Kanten (Sobel-Filter)")
axes[1].axis("off")

plt.tight_layout()

output_filename = os.path.join(script_dir, "knee_edges.jpg")
plt.savefig(output_filename, dpi=300)
plt.show()

print(f"\nDie Abbildung wurde als '{output_filename}' gespeichert.")