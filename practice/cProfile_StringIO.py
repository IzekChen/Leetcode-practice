import cProfile, pstats
from io import StringIO

pr = cProfile.Profile()
pr.enable()

for i in range(100): print(i)

s = StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative') 
ps.print_stats() 
print(s.getvalue())
