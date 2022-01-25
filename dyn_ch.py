from enum import Enum
from point import Point


class EqualsStates(Enum):
    EQUAL = 1
    MORE = 2
    LESS = 3


class DynCH:
    def __init__(self):
        self._ch = []
        self.scaled_centre = None
        self.scale = 3
        self._intermediate_ch = [[], []]

    def get_ch(self):
        return self._ch

    def add_point(self, point: Point):
        point_count = len(self._ch)
        if point_count >= 3:
            self._insert_into_ch(point)
            return
        elif point_count == 2:
            if self._check_is_points_collinear(self._ch[0], self._ch[1], point):
                self._ch.append(point)
                self._ch.sort(key=lambda dot: (dot[0], dot[1]))
                self._ch.pop(1)
            else:
                self.scaled_centre = self._ch[0] + self._ch[1] + point
                self._ch.append(point)
                for dot in self._ch:
                    j, array_num = self._binary_insert_position(dot)
                    self._intermediate_ch[array_num] = self._intermediate_ch[array_num][:j] + [dot] + \
                                                       self._intermediate_ch[array_num][j:]
                self._ch = self._intermediate_ch[0] + self._intermediate_ch[1]
            return
        elif point_count == 1:
            if not point == self._ch[0]:
                self._ch.append(point)
            return
        else:
            self._ch.append(point)
            return

    @staticmethod
    def _check_is_points_collinear(a: Point, b: Point, c: Point) -> bool:
        vec_1 = a - b
        vec_2 = a - c
        if vec_1.x * vec_2.y == vec_1.y * vec_2.x:
            return True
        return False

    @staticmethod
    def _sign_func(x):
        if x > 0:
            return 1
        if x == 0:
            return 0
        return -1

    @staticmethod
    def _is_point_on_segment(start_segment: Point, end_segment: Point, point: Point):
        if DynCH._check_is_points_collinear(start_segment, end_segment, point) is True:
            vec_1 = end_segment - start_segment
            vec_2 = point - start_segment
            vec_prod = vec_1.x * vec_2.x + vec_1.y * vec_2.y
            if 0 <= vec_prod <= vec_1.x ** 2 + vec_1.y ** 2:
                return True
        return False

    def get_equal_state_by_polar_angle(self, point_1, point_2):
        point_1_scaled, point_2_scaled = self.scale * point_1 - self.scaled_centre, \
                                         self.scale * point_2 - self.scaled_centre

        x_1, y_1 = int(point_1_scaled[0]), int(point_1_scaled[1])
        x_2, y_2 = int(point_2_scaled[0]), int(point_2_scaled[1])

        if self._sign_func(x_1) == self._sign_func(x_2) and \
                x_1 ** 2 * (x_2 ** 2 + y_2 ** 2) == x_2 ** 2 * (x_1 ** 2 + y_1 ** 2):
            return EqualsStates.EQUAL

        if x_1 >= 0 and x_2 >= 0:
            if x_1 ** 2 * (x_2 ** 2 + y_2 ** 2) < x_2 ** 2 * (x_1 ** 2 + y_1 ** 2):
                return EqualsStates.LESS if y_1 < 0 else EqualsStates.MORE
            else:
                return EqualsStates.MORE if y_1 < 0 else EqualsStates.LESS

        if x_1 < 0 and x_2 < 0:
            if x_1 ** 2 * (x_2 ** 2 + y_2 ** 2) > x_2 ** 2 * (x_1 ** 2 + y_1 ** 2):
                return EqualsStates.LESS if y_1 < 0 else EqualsStates.MORE
            else:
                return EqualsStates.MORE if y_1 < 0 else EqualsStates.LESS

        if x_1 >= 0 > x_2:
            return EqualsStates.MORE if y_1 < 0 else EqualsStates.LESS
        if x_1 < 0 <= x_2:
            return EqualsStates.LESS if y_1 < 0 else EqualsStates.MORE

    def _binary_search(self, arr, val, start, end):
        if start == end:
            if self.get_equal_state_by_polar_angle(arr[start], val) == EqualsStates.MORE:
                return start
            else:
                return start + 1
        if start > end:
            return start
        mid = (start + end) // 2
        if self.get_equal_state_by_polar_angle(arr[mid], val) == EqualsStates.LESS:
            return self._binary_search(arr, val, mid + 1, end)
        elif self.get_equal_state_by_polar_angle(arr[mid], val) == EqualsStates.MORE:
            return self._binary_search(arr, val, start, mid - 1)
        else:
            return mid

    def _binary_insert_position(self, point: Point):
        array_num = 0
        if self.scale * point.y - self.scaled_centre.y >= 0:
            arr = self._intermediate_ch[0]
        else:
            array_num = 1
            arr = self._intermediate_ch[1]
        j = self._binary_search(arr, point, 0, len(arr) - 1)
        return j, array_num

    def _insert_into_ch(self, point: Point):
        def check_det_cond(a: Point, b: Point, c: Point):
            return a.x * (b.y - c.y) - a.y * (b.x - c.x) + b.x * c.y - b.y * c.x

        def get_dir(vec_1, vec_2):
            return vec_1.x * vec_2.y - vec_1.y * vec_2.x

        def get_insert_ids():
            res = [None, None]
            n = len(self._ch)

            vl = self._ch[1] - self._ch[0]
            to_l = self._ch[0] - point
            v_prev = self._ch[0] - self._ch[n - 1]
            to_prev = self._ch[n - 1] - point
            pointing_l = get_dir(to_l, vl)
            pointing_prev = get_dir(to_prev, v_prev)
            l = 0
            r = n - 1
            if pointing_prev > 0 and pointing_l <= 0:
                res[0] = 0
                if pointing_l == 0:
                    v_next = self._ch[2] - self._ch[1]
                    to_next = self._ch[1] - point
                    pointing_next = get_dir(to_next, v_next)
                    if pointing_next > 0:
                        res[0] = 1
                    elif pointing_next == 0:
                        return [1, 1]
            else:
                while l < r - 1:
                    m = (r + l + 1) // 2
                    vm = self._ch[m + 1] - self._ch[m]
                    to_m = self._ch[m] - point
                    pointing_m = get_dir(to_m, vm)
                    lm_dir = get_dir(to_l, to_m)
                    if (pointing_m <= 0 or lm_dir < 0) and (pointing_l > 0 or lm_dir >= 0):
                        r = m
                    else:
                        l = m
                        to_l = to_m
                        pointing_l = pointing_m
                next = (r + 1) % n
                to_r = self._ch[r] - point
                vr = self._ch[next] - self._ch[r]
                pointing_r = get_dir(to_r, vr)
                if pointing_r <= 0 and pointing_l > 0:
                    res[0] = r
                    v_next = self._ch[(next + 1) % n] - self._ch[next]
                    to_next = self._ch[next] - point
                    pointing_next = get_dir(to_next, v_next)
                    if pointing_r == 0 and pointing_next == 0:
                        return [r, r]
                else:
                    return [None, None]
            vl = self._ch[1] - self._ch[0]
            to_l = self._ch[0] - point
            v_prev = self._ch[0] - self._ch[n - 1]
            to_prev = self._ch[n - 1] - point
            pointing_l = get_dir(to_l, vl)
            pointing_prev = get_dir(to_prev, v_prev)
            l = 0
            r = n - 1
            if pointing_prev <= 0 and pointing_l > 0:
                res[1] = 0
                if res[0] != n - 1 and pointing_prev == 0:
                    res[1] = n - 1
            else:
                while l < r - 1:
                    m = (r + l + 1) // 2
                    vm = self._ch[m + 1] - self._ch[m]
                    to_m = self._ch[m] - point
                    pointing_m = get_dir(to_m, vm)
                    lm_dir = get_dir(to_l, to_m)
                    if (pointing_l <= 0 or lm_dir <= 0) and (pointing_m > 0 or lm_dir > 0):
                        r = m
                    else:
                        l = m
                        to_l = to_m
                        pointing_l = pointing_m
                to_r = self._ch[r] - point
                vr = self._ch[(r + 1) % n] - self._ch[r]
                pointing_r = get_dir(to_r, vr)
                if pointing_r > 0 and pointing_l <= 0:
                    res[1] = r
            return res

        def insert_into_ch():
            res = get_insert_ids()
            if res[0] is None or res[1] is None:
                print(f'WRONG ANSWER: {res[0]}, {res[1]}')
                return
            len_pos = len(self._intermediate_ch[0])
            if res[0] > res[1]:
                if res[1] < len_pos and res[0] < len_pos:
                    self._intermediate_ch[0] = self._intermediate_ch[0][res[1]:res[0] + 1]
                    self._intermediate_ch[1] = []
                elif res[1] < len_pos <= res[0]:
                    self._intermediate_ch[0] = self._intermediate_ch[0][res[1]:]
                    self._intermediate_ch[1] = self._intermediate_ch[1][:res[0] + 1 - len_pos]
                elif res[1] >= len_pos and res[0] >= len_pos:
                    self._intermediate_ch[0] = []
                    self._intermediate_ch[1] = self._intermediate_ch[1][res[1] - len_pos:res[0] + 1 - len_pos]
            else:
                if res[0] < len_pos and res[1] < len_pos:
                    self._intermediate_ch[0] = self._intermediate_ch[0][:res[0] + 1] + self._intermediate_ch[0][res[1]:]
                elif res[0] < len_pos <= res[1]:
                    self._intermediate_ch[0] = self._intermediate_ch[0][:res[0] + 1]
                    self._intermediate_ch[1] = self._intermediate_ch[1][res[1] - len_pos:]
                elif res[1] >= len_pos and res[0] >= len_pos:
                    self._intermediate_ch[1] = self._intermediate_ch[1][:res[0] + 1 - len_pos] \
                                               + self._intermediate_ch[1][res[1] - len_pos:]
            j, array_num = self._binary_insert_position(point)
            self._intermediate_ch[array_num] = self._intermediate_ch[array_num][:j] + [point] \
                                               + self._intermediate_ch[array_num][j:]
            self._ch = self._intermediate_ch[0] + self._intermediate_ch[1]

        j, array_num = self._binary_insert_position(point)
        self._ch = self._intermediate_ch[0] + self._intermediate_ch[1]
        ch_len = len(self._ch)
        shift = array_num * len(self._intermediate_ch[0])
        det = check_det_cond(point, self._ch[j - 1 + shift], self._ch[(j + shift) % ch_len])
        if self._sign_func(det) == 1:
            return
        elif self._sign_func(det) == -1:
            insert_into_ch()
        else:
            if self._is_point_on_segment(self._ch[j - 1 + shift], self._ch[(j + shift) % ch_len], point) is False:
                insert_into_ch()
            return
