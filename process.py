import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import os
from collections import defaultdict

AREA_OF_PORK = 0.000025

def process_file(filename):
    df = pd.read_csv(filename)

    original_length = df["Size_mm"][0]

    df["strain"]= df["Displacement_mm"] / original_length

    df["stress"] = df["Force_N"] / AREA_OF_PORK / 1000000

    return df

def get_tests(root_folder):
    '''Gets the csv file names for all the tests, sorts them in a dictionary corresponding to each concentration / control

    returns a dictionary of {
        "12":[file1, file2, ...],
        "15":[file1, file2, ...],
        "18":[file1, file2, ...],
        "21":[file1, file2, ...],
        "neg":[file1, file2, ...],
        "pos":[file1, file2, ...],
        "extra:[extra files]
    }
    '''

    output = defaultdict(list)

    for root, dirs, files in os.walk(root_folder):

        for file in files:
            if file.endswith(".csv"):
                name = os.path.basename(file)
                name_list = name.split("-")
                if "PhaseTiming" in name:
                    continue

                if name_list[0] == "TEST":
                    output[name_list[1].split("_")[0]].append(os.path.join(root, file))
                else:
                    output["extra"].append(os.path.join(root, file))
    
    return output

def plot_data(df):
    '''plots data
    '''
    
    plt.plot(df["strain"], df["stress"])
    plt.xlabel("Strain (mm/mm)")
    plt.ylabel("Stress (MPa)")
    plt.show()

def calculate_y_mod(data, visualize=True):
    '''calculates young's modulus from data'''

    max_idx = np.argmax(data["stress"])
    slope, intercept, r_value, p_value, std_er = linregress(np.array(data["strain"])[:max_idx], np.array(data["stress"])[:max_idx])

    if visualize:
        x = np.linspace(np.min(data["strain"]), np.max(data["strain"][max_idx]))
        y = x*slope + intercept
        plt.plot(data["strain"], data["stress"])
        plt.plot(x, y, label=f"Linear Fit, r = {r_value:.2f}, Young's Mod = {slope:.5f}MPa")
        plt.xlabel("Strain (mm/mm)")
        plt.ylabel("Stress (MPa)")
        plt.legend()
        plt.show()

    return slope

if __name__ == "__main__":
    
    # fn = "C:/Users/ryanr/Desktop/MIE439/01 - Experimental Data/TEST-neg_control_01/TEST-neg_control_01Data.csv"
    root = "C:/Users/ryanr/Desktop/MIE439/01 - Experimental Data"

    out = get_tests(root)
    y_mod = []
    plot_vals = ["12", "15", "18", "21"]
    plot_x = []
    plot_y = []
    for ting in out:
        print("Processing Tests:")
        print(ting)
        if ting == "extra":
            continue
        for fn in out[ting]:
            
            df = process_file(fn)

            # print(df.head(10))
            # plot_data(df)
            slope = calculate_y_mod(df, visualize=False)
            y_mod.append(slope)

            if ting in plot_vals:
                plot_x.append(int(ting))
                plot_y.append(slope)
        
        print(f"Mean Young's Mod: {np.mean(y_mod):.4f}MPa, Standard Deviation: {np.std(y_mod):.4f}")

    print(plot_x, plot_y)
    slope, intercept, r_value, p_value, std_er = linregress(plot_x, plot_y)
    x = np.linspace(np.min(plot_x), np.max(plot_x))
    y = x*slope + intercept
    plt.plot(x, y, label=f"Linear Fit, r^2 = {r_value**2:.2f}")
    plt.scatter(plot_x, plot_y, label="Data Points")
    plt.xlabel("Concentration")
    plt.ylabel("Young's Modulus (MPa)")
    plt.legend()
    plt.show()