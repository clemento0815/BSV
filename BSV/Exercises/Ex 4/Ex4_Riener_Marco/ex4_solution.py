""" Working with DICOM-data """

# author: Riener Marco
# date: 2026-10-30

# Import standard packages

import matplotlib.pyplot as plt
import pydicom
from skimage.filters import sobel

if __name__ == '__main__':
    
    # Daten einlesen
    in_file1 = 'SER00002/2A1A1ADC'
    in_file2 = 'SER00003/0B8C096A'
    
    # Daten Variablen zuweisen
    data1 = pydicom.dcmread(in_file1)
    data2 = pydicom.dcmread(in_file2)
    
    # Daten zuweisen (Bilddatei)
    img_data1 = data1.pixel_array
    img_data2 = data2.pixel_array
    
    # Sobel-Filter auf eines der Datasets anwenden
    edges = sobel(img_data2)
    
    # Plotten des ersten Bildes
    plt.title("Koronale Ansicht")
    plt.imshow(img_data1, cmap = 'gray')
    plt.show()
    
    # Eine gemeinsame Abbildung erstellen (1 Zeile, 2 Spalten, Bildgröße: B = 12, H = 6)
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Erstes Subplot: Originales Bild, axes[0] = erstes Bilder der Zeile
    axes[0].imshow(img_data2, cmap='gray')
    axes[0].set_title("Original (Sagittale Ansicht)")
    axes[0].axis('off')
    
    # Zweites Subplot: Kantenbild (Sobel), axes[1] = zweites Bild der Zeile
    axes[1].imshow(edges, cmap='gray')
    axes[1].set_title("Kanten (Sobel-Filter)")
    axes[1].axis('off')
    
    # Layout anpassen
    plt.tight_layout()
    
    # Bild abspeichern (vor dem plotten)
    plt.savefig('knee_edges.jpg', dpi=300)
    
    #Ausgabe
    plt.show()
            

   
   
    
    
    
  
