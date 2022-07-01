import cProfile
import pstats
from pstats import SortKey






lst = []
def number():

	num = 8999889

	count = 0 
	while count < num:
		lst.append(count)
		count+=1

	return lst

if __name__ == "__main__":
	cProfile.run('number()',"output.dat")

	with open("output_time.txt","w") as f:
		p = pstats.Stats("output.dat", stream= f)
		p.sort_stats("time").print_stats()

	with open("output_calls.txt","w") as f:
		p = pstats.Stats("output.dat",stream= f)
		p.sort_stats("calls").print_stats()


#number of holes 318238

# draw the diagram 
#get profiling
#get the stats 
#get the number of the holes filled finally

 