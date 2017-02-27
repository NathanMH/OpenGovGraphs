import requests
import zipfile
import io
import pandas as pd
import easygui
from bs4 import BeautifulSoup

def unzip_csv(url, name):
	results = requests.get(url)
	zip = zipfile.ZipFile(io.BytesIO(results.content))
	zip_file_list = zip.namelist()
	zip_files_choose(zip_file_list)
	unzipped = zip.open(name)
	csv = pd.read_csv(unzipped)
	return csv

def unzip_xml(url, name):
	results = requests.get(url)
	zip = zipfile.ZipFile(io.BytesIO(results.content))
	zip_file_list = zip.namelist()
	zip_files_choose(zip_file_list)
	unzipped = zip.open(name)
	return unzipped

def zip_files_choose(file_list):
	""" User chooses which file contains the data from the zip archive """
	msg = "Please select the file containing the data."
	title = "Zip File List"
	choices = file_list
	choice = easygui.choicebox(msg, title, choices)

def return_soup(type):
	if type == "xml":
		soup = xh.make_soup_from_URL(url, "xml")
	elif type == "csv":
		soup = xh