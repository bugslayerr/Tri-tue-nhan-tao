#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_file_csv(path):
	data = pd.read_csv(path, index_col=0)
	data_array = np.array(data)
	return data_array

def main():
	path = r"data_Breath_first_search.csv"
	data_array = read_file_csv(path)
	print(data_array)

if __name__ == '__main__':
	main()
