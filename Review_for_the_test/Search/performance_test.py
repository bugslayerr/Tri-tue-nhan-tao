from Breadth_first_search import deapth_first_search
from Breadth_first_search import read_file_csv
import cProfile

profiler = cProfile.Profile()

path = r"data_Breath_first_search.csv" #Path of the data file
data_array = read_file_csv(path)
begin = 1 #begin test case = 1
goal = 3 #goal test case = 3

profiler.enable()

for i in range(200000):
	deapth_first_search(data_array, begin, goal)

profiler.disable()

profiler.print_stats()