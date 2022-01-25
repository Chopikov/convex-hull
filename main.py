import math
import time

from dyn_ch import DynCH
from point import Point

if __name__ == '__main__':
    N = 500
    start = time.time()
    dch = DynCH()
    for i in range(N):
        x, y = i, i*i
        dch.add_point(Point(x, y))
        # print(dch.get_ch())
    T = time.time() - start
    print(f'Elapsed time: {T}s')
    print(f'Coef: {N * math.log(N) / T}')

    print(f'Convex hull size: {len(dch.get_ch())}')
    # while True:
    #     str = input()
    #     if str == 'q':
    #         break
    #     x, y = map(int, str.split())
    #     dch.add_point(Point(x, y))
    #     print(f'{len(dch.get_ch())}:{dch.get_ch()}')

