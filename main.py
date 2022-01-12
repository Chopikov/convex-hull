from dyn_ch import DynCH
from point import Point

if __name__ == '__main__':
    dch = DynCH()
    for i in range(700):
        x, y = i, i*i
        dch.add_point(Point(x, y))
        print(dch.get_ch())
    print(len(dch.get_ch()))
