import canadianTelecomSoup
import matplotlib.pyplot as plt
import numpy as np
import re
from canadianTelecomSoup import TelecomStats

def plot_provinces_amount(dictionary):
    provinces = []
    telecom_counts = []

    for k, v in dictionary.items():
        provinces.append(k)
        telecom_counts.append(v)

    x_pos = np.arange(len(provinces))
    plt.yticks(x_pos, provinces)
    plt.barh(x_pos, telecom_counts, align='center', alpha=0.5)
    
    plt.ylabel("Provinces")
    plt.xlabel("Number of companies")
    plt.title("Distribution of telecommunication companies throughout Canada")
    plt.show()

def __main__():

    data = TelecomStats()
    plot_provinces_amount(data.provinces)

__main__()