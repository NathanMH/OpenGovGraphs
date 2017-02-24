import matplotlib as plt
import numpy as np
import csv

csv_filepath = "./resources/Legal_Aid_Data.csv"

def make_csv_soup(filepath):
    with open(filepath, newline='') as csvfile:
        news_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in news_reader:
            print(','.join(row))
    
    
make_csv_soup(csv_filepath)