from typing import List

class Point:
    def __init__(self, input: str) -> None:
        self.x, self.y = [int(n) for n in input.split(',')]

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, input: str) -> None:
        self.start, self.end = [ Point(p) for p in input.strip().split(' -> ')]

    def is_straight(self) -> bool:
        return self.is_horizontal() or self.is_vertical()

    def is_horizontal(self) -> bool:
        return self.start.x == self.end.x

    def is_vertical(self) -> bool:
        return self.start.y == self.end.y

    def in_between_points(self) -> List[Point]:
        if self.is_horizontal():
            return [ Point(f'{self.start.x},{y}') for y in self._y_range() ]
        if self.is_vertical():
            return [ Point(f'{x},{self.start.y}') for x in self._x_range() ]
        return [ Point(f'{x},{y}') for x, y in zip(self._x_range(), self._y_range()) ]

    def _y_range(self) -> List[int]:
        if self.start.y < self.end.y:
            return range(self.start.y, self.end.y + 1)
        else:
            return reversed(range(self.end.y, self.start.y + 1))

    def _x_range(self) -> List[int]:
        if self.start.x < self.end.x:
            return range(self.start.x, self.end.x + 1)
        else:
            return reversed(range(self.end.x, self.start.x + 1))

    def __repr__(self) -> str:
        return f'{self.start} -> {self.end}'


def part1(lines: List[Line]):
    points = {}
    straight_lines = [ l for l in lines if l.is_straight()]

    for line in straight_lines:
        for point in line.in_between_points():
            point_key = str(point)
            if point_key not in points:
                points[point_key] = 0
            points[point_key] += 1

    return len([ v for v in points.values() if v >= 2 ])


def part2(lines: List[Line]):
    points = {}

    for line in lines:
        for point in line.in_between_points():
            point_key = str(point)
            if point_key not in points:
                points[point_key] = 0
            points[point_key] += 1

    return len([ v for v in points.values() if v >= 2 ])


def main():
    with open('resources/day5-lines', 'r') as file:
        lines = [ Line(l) for l in file ]
        print('Part 1: ' + str(part1(lines)))
        print('Part 2: ' + str(part2(lines)))


if __name__ == '__main__':
    main()

"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""