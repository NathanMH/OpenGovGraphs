import os
import chef

# Imports for graphing
import matplotlib.pyplot as plt
import numpy as np

# Variables
url = "https://services.crtc.gc.ca/pub/OpenData/CASP/Telecomlist/TelecomList_NDC_29.xml"
soup = chef.make_soup_from_URL(url, "xml")

class TelecomStats:

    def cities_telecom(self, soup):
		cities = {}
        for i in soup.find_all("c"):
            city = i['city']
            if city in self.cities:
                self.cities[city] += 1
            else:
                self.cities[city] = 1

    def provinces_telecom(self, soup):
		provinces = {}
        for i in soup.find_all("c"):
            province = i['province']
            if province in self.provinces:
                self.provinces[province] += 1
            else:
                self.provinces[province] = 1

    
	def plot_provinces(dictionary):
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

	def __init__(self):
        self.cities_telecom(soup)
        self.provinces_telecom(self.soup)