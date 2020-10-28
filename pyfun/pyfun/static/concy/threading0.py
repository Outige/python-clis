import time
import threading


def foo(x=1.2):
    print('sleeping..')
    time.sleep(x)
    print('done sleeping..')

def two_threads():
    start = time.perf_counter()

    # init hreads
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)

    # execute threads
    t1.start()
    t2.start()

    # wait for threads to complete
    t1.join()
    t2.join()

    end = time.perf_counter()
    print('time taken: %.2f'%(end-start))

def n_threads(n):
    start = time.perf_counter()

    threads = []

    for _ in range(n):
        # spin up n threads with a wait time of 1.5
        t = threading.Thread(target=foo, args=[1.5])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.perf_counter()
    print('time taken: %.2f'%(end-start))


if __name__ == '__main__':
    print('two threads:')
    two_threads()

    print('\nn threads:')
    n_threads(10)