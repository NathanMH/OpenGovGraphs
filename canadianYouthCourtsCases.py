import xmlhtmlsaver as xh
import zipopen
from bs4 import BeautifulSoup


zip_url = "http://www20.statcan.gc.ca/tables-tableaux/cansim/sdmx/02520071.zip"
xml_file = zipopen.unzip_xml(zip_url, "02520071_1.xml")
soup = BeautifulSoup(xml_file, 'lxml')


dictionary = {}

for i in soup.find_all("cansim:obs"):
	if int(i['time_period']) > 2009 and int(i['obs_value']) > 0:
		print(i['time_period'])
		print(i['obs_value'])
