import canadianTelecomSoup
import matplotlib.pyplot as plt
import numpy as np
import re
from canadianTelecomSoup import TelecomStats

# Source: http://open.canada.ca/data/en/dataset/5a0c9cbb-e0d3-47db-b5bc-dd57430ef200
def plot_cities(dictionary):
    cities_am = []
    cities_nz = []
    telecom_counts_am = []
    telecom_counts_nz = []

    for k, v in dictionary.items():
        if re.match("^[a-mA-M]", k[0]):
            cities_am.append(k)
            telecom_counts_am.append(v)
        elif re.match("^[n-zN-Z]", k[0]):
            print(k + " starts with " + k[0])
            cities_nz.append(k)
            telecom_counts_nz.append(v)

    # a-m cities
    x_pos = np.arange(len(cities_am))
    plt.yticks(x_pos, cities_am)
    plt.barh(x_pos, telecom_counts_am, align='center', alpha=0.5)
    
    plt.ylabel("Cities A-M")
    plt.xlabel("Number of companies")
    plt.title("Distribution of telecommunication companies throughout Canada")
    plt.show()

    # n-z cities
    x_pos = np.arange(len(cities_nz))
    plt.yticks(x_pos, cities_nz)
    plt.barh(x_pos, telecom_counts_nz, align='center', alpha=0.5)
    
    plt.ylabel("Cities N-Z")
    plt.xlabel("Number of companies")
    plt.title("Distribution of telecommunication companies throughout Canada")
    plt.show()

def __main__():

    data = TelecomStats()
    plot_cities(data.cities)

__main__()