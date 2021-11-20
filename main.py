from ulvi import TicToc, FindPi
from threading import Thread
import time
import os

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()

    n = 1000
    find_pis = []
    """finding_pi.throw_points(10000000)"""
    threads = []
    for i in range(os.cpu_count()):
        find_pis.append(FindPi())
        threads.append(Thread(target=find_pis[i].throw_points, args=(n,)))

    for thread in threads:
        thread.start()
        print("Started thread number %d" % threads.index(thread))
    for thread in threads:
        thread.join()

    inner = 0
    total = 0
    for find_pi in find_pis:
        inner += find_pi.i
        total += find_pi.n

    pi = 4 * inner / total
    print("PI = %.8f | N = %d / %d | TIME = %.5f" % (pi, inner, total, tt.toc()))


print("Buz")