## Profiling 

Profiling helps to optimize the python code and make it faster and help to found out which parts are going faster or slower. We can use a profiler such cProfile. 

```python
import cProfile
import pstats
from pstats import SortKey



#here the number is the function 
if __name__ == "__main__":
	cProfile.run('number()',"output.dat")

	with open("output_time.txt","w") as f:
		p = pstats.Stats("output.dat", stream= f)
		p.sort_stats("time").print_stats()

	with open("output_calls.txt","w") as f:
		p = pstats.Stats("output.dat",stream= f)
		p.sort_stats("calls").print_stats()
```

