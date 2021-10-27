import sys
import time
import nbody as nbody

start_time = time.perf_counter()
for i in range(int(sys.argv[1])):
    nbody.main(i)
end_time = time.perf_counter()

print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Execution Time: {end_time - start_time:0.6}")