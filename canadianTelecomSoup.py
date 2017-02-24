import os
import xmlhtmlsaver as xh


class TelecomStats:
    url = "https://services.crtc.gc.ca/pub/OpenData/CASP/Telecomlist/TelecomList_NDC_29.xml"
    file_path = os.getcwd() + "/resources/Telecomdata"

    cities = {}
    provinces = {}
    soup = None

    def make_soup(self):
        if os.path.exists(self.file_path):
            self.soup = xh.make_soup_from_file(open(self.file_path), "xml")
        else:
            self.soup = xh.make_soup_from_URL(self.url, "xml")
            xh.save_soup(self.soup, self.file_path)

    def cities_telecom(self, soup):
        for i in soup.find_all("c"):
            city = i['city']
            if city in self.cities:
                self.cities[city] += 1
            else:
                self.cities[city] = 1

    def provinces_telecom(self, soup):
        for i in soup.find_all("c"):
            province = i['province']
            if province in self.provinces:
                self.provinces[province] += 1
            else:
                self.provinces[province] = 1
                
    def __init__(self):
        self.make_soup()
        self.cities_telecom(self.soup)
        self.provinces_telecom(self.soup)