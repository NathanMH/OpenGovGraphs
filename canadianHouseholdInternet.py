import xmlhtmlsaver as xh
import zipopen
from bs4 import BeautifulSoup


zip_url = "http://www20.statcan.gc.ca/tables-tableaux/cansim/sdmx/03580021.zip"
xml_file = zipopen.unzip_xml(zip_url, "03580021.xml")
soup = BeautifulSoup(xml_file, 'lxml')

for i in soup.find_all("cansim:obs"):
	if int(i['time_period']) > 2002:
		print(i['time_period'])
