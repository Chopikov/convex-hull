from dyn_ch import DynCH
from point import Point

if __name__ == '__main__':
    dch = DynCH()
    while True:
        print(dch.get_ch())
        inp = input()
        if inp == 'q':
            break
        x, y = map(int, inp.split())
        dch.add_point(Point(x, y))
