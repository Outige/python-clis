import time

start = time.perf_counter()

time.sleep(2.5)

end = time.perf_counter()

print('time taken: %.2f'%(end-start))