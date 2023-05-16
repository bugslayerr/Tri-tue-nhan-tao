#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_file_csv(path):
	data = pd.read_csv(path, index_col = 0) #chage the index_col to correct with construction of csv file
	data_array = np.array(data)
	return data_array #return 2-dimensional arrays

def deapth_first_search(data_array, begin, goal):
	open_nodes = [begin]
	close_nodes = [begin]
	parent = {f'{begin}': None} #Contains parent and child
	while open_nodes:
		n = open_nodes.pop(0) #Replace 0 with -1 to convert to Depth_first_search algorithm 
		if n == goal:
			road = []
			while n is not None:
				road.append(n)
				n = parent[f"{n}"]
			return list(reversed(road))
		else:
			An = [i for i in range(len(data_array[n])) if data_array[n][i] == 1]
			for i in An:
				if i not in close_nodes:
					open_nodes.append(i)
					close_nodes.append(i)
					parent[f"{i}"] = n
	return None


def main():
	path = r"data_Breath_first_search.csv" #Path of the data file
	data_array = read_file_csv(path)
	begin = 1 #begin test case = 1
	goal = 3 #goal test case = 3
	check = deapth_first_search(data_array, begin, goal)
	if check is None:
		print(f"Không có đường đi từ đỉnh {begin} đến đỉnh {goal}")
	else:
		print("Đường đi là: ", check)
		
if __name__ == '__main__':
	main()
