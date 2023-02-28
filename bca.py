#Loading in the libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import time
from subprocess import check_output
import warnings
warnings.filterwarnings('ignore')

# Reading the input file
data = pd.read_csv(r'C:\Users\HELLIX NEBULA\Dropbox\PC\Desktop\Files\Breast Cancer Analysis\data.csv')
