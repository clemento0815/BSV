"""Solution Assingment FIR-filters"""

# author:	Thomas Haslwanter
# date:		2025-09-23

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal, io
from pathlib import Path

# For the GUI
import FreeSimpleGUI as sg


def get_data() -> np.ndarray:
    """Read in the data

    Returns
    -------
    data : ECG-data for the exercise
    """

    # Select the in-file
    file_name = sg.popup_get_file(
        "Select the data-file",
        no_window=True,
        file_types=(("Data Files", ["*.dat", "*.mat", "*.txt"]),),
    )
    # >> file_name = r'.\data\ecg_hfn.txt'

    # Find the extension
    in_file = Path(file_name)
    extension = in_file.suffix[1:].lower()

    if extension == "dat":
        data_raw = pd.read_csv(file_name, header=None)
        data = data_raw.values
    elif extension == "txt":
        data_raw = pd.read_csv(file_name)
        data = data_raw.values
    elif extension == "mat":
        data_raw = io.loadmat(file_name)
        data = data_raw["ecg_hfn"]
    else:
        data = None
        print("Sorry, I don't know that extension")

    return data


def smooth_data(data: np.ndarray) -> None:
    """Smooth the data with a running average and with savolg

    Parameters
    ----------
    data : ECG-Data

    Returns
    -------
    rate : sample rate [Hz]
    """

    # Set the parameters
    filter_width = 11

    # Smooth the data
    fir_b = np.ones(filter_width) / filter_width
    smoothed = {"fir": signal.lfilter(fir_b, 1, data, axis=0)}
    smoothed["savgol"] = signal.savgol_filter(
        data, window_length=filter_width, polyorder=3, deriv=0, axis=0
    )

    # Plot the three data sets
    plt.plot(data, label="original")
    plt.plot(smoothed["fir"], label="fir")
    plt.plot(smoothed["savgol"], label="savgol")

    # Format and show the plot
    plt.legend()
    plt.xlabel("Points")
    plt.ylabel("ECG-Signal")
    plt.xlim([2400, 2600])
    plt.show()


def estimate_sampling_rate(data: np.ndarray) -> float:
    """Estimate the sample rate, based on a heart-beat with 1 Hz
    Note: The acual sampling rate is 1 kHz.

    Parameters
    ----------
    data : ECG-Data

    Returns
    -------
    rate : sample rate [Hz]
    """

    # Get 2 adjacent points
    plt.plot(data)
    plt.title("Select two peaks, to estimate the sample frequency:")
    selected = plt.ginput(2)
    plt.close()

    # Estimate and show the sample rate
    estimated_rate = np.round(selected[1][0] - selected[0][0])
    print(
        "The time between two heart-beats is about 1 sec, so the sampling "
        + f"rate is about {estimated_rate} Hz"
    )

    return estimated_rate


def show_derivatives(data: np.ndarray, rate: float) -> None:
    """Show the first two derivatives

    Parameters
    ----------
    data : ECG-Data
    """

    # Set the parameters
    filter_width = 11

    time = np.arange(len(data)) / rate
    dt = 1 / rate

    fig, axs = plt.subplots(3, 1, sharex=True)

    axs[0].plot(time, data)
    axs[0].margins(x=0)  # To eliminate margins on the hor axis
    axs[0].set_ylabel("ECG-Signal")

    axs[1].plot(
        time,
        signal.savgol_filter(
            data, window_length=filter_width, polyorder=3, deriv=1, delta=dt, axis=0
        ),
    )
    axs[1].set_ylabel("1st deriv")

    axs[2].plot(
        time,
        signal.savgol_filter(
            data, window_length=filter_width, polyorder=3, deriv=2, delta=dt, axis=0
        ),
    )
    axs[2].set_ylabel("2nd deriv")
    axs[2].set_xlabel("Time (sec)")

    plt.tight_layout()  # To ensure all labels are visible
    plt.show()


if __name__ == "__main__":
    data = get_data()  # Ex 1
    smooth_data(data)  # Ex 2
    rate = estimate_sampling_rate(data)  # Ex 3
    show_derivatives(data, rate)  # Ex 4
