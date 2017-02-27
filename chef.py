import urllib.request
from bs4 import BeautifulSoup

def make_soup_from_URL(url, site_type):
    site = urllib.request.urlopen(url)
    if site_type == None:
        soup = BeautifulSoup(site)
    else:
        soup = BeautifulSoup(site, 'lxml')
    return soup

def make_soup_from_file(file_location, site_type=""):
    if site_type == "":
        soup = BeautifulSoup(file_location)
    else:
        soup = BeautifulSoup(file_location, 'lxml')
    return soup

def save_soup(soup, local_file):
    with open(local_file, 'w') as xml_file:
        for line in soup.prettify():
            xml_file.write(line)
