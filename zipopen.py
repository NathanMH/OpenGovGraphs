import requests
import io
import pandas as pd
import easygui
import chef
import zipfile

def unzip_csv(url, name):
	results = requests.get(url)
	unzipped = zipfile.ZipFile(io.BytesIO(results.content))
	zip_file_list = unzipped.namelist()
	zip_files_choose(zip_file_list)
	unzipped = zip.open(name)
	csv = pd.read_csv(unzipped)
	return csv

def unzip_xml(url, name):
	results = requests.get(url)
	unzipped = zipfile.ZipFile(io.BytesIO(results.content))
	zip_file_list = unzipped.namelist()
	zip_files_choose(zip_file_list)
	unzipped = unzipped.open(name)
	return unzipped

def zip_files_choose(file_list):
	""" User chooses which file contains the data from the zip archive """
	msg = "Please select the file containing the data."
	title = "Zip File List"
	choices = file_list
	choice = easygui.choicebox(msg, title, choices)
	return choice

def return_soup(url, source_type):
	if source_type == "xml":
		soup = chef.make_soup_from_URL(url, "xml")
	return soup