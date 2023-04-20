import pandas as pd
import os
import numpy as np


array = np.loadtxt("D:/MachinLerning/ClassificationData/tic_tac_toe.txt", delimiter= ',')
print(array)
def convert_txt_to_csv(txt_directory, sep):
    txt_row = pd.read_csv(txt_directory, sep=sep)
    csv_directory, filename = os.path.split(txt_directory)

    filename = filename.replace('.txt', '.csv')
    txt_row.to_csv(csv_directory + '/' + filename, sep=sep)
