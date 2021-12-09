def part1(points):
    total = 0
    for i in range(len(points)):
        for j in range(len(points[i])):
            adjacents = find_adjacents(points, i, j)
            if points[i][j] < min(adjacents):
                total += 1 + points[i][j]
    return total


def find_adjacents(points, i, j):
    adjacents = []
    if i - 1 >= 0:
        adjacents.append(points[i-1][j])
    if j - 1 >= 0:
        adjacents.append(points[i][j-1])
    if i + 1 < len(points):
        adjacents.append(points[i+1][j])
    if j + 1 < len(points[i]):
        adjacents.append(points[i][j+1])
    return adjacents
            

def part2(points):
    basins = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            current_basin = search(points, i, j)

            if len(basins) < 3:
                basins.append(current_basin)
            elif len(current_basin) > len(basins[-1]):
                basins.append(current_basin)
                basins = sorted(basins, key=len, reverse=True)[:3]
    
    return len(basins[0]) * len(basins[1]) * len(basins[2])


def search(points, i, j):
    if points[i][j] >= 9:
        return []
    
    points[i][j] += 10 # Numeric mark for which points were visited
    found = [ points[i][j] ]
    
    if i - 1 >= 0:
        found += search(points, i-1, j)
    if j - 1 >= 0:
        found += search(points, i, j-1)
    if i + 1 < len(points):
        found += search(points, i+1, j)
    if j + 1 < len(points[i]):
        found += search(points, i, j+1)

    return found


def main():

    test = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

    with open('resources/day9-heightmap', 'r') as file:
        points = [ [ int(n) for n in l.strip() ] for l in file ]
        # points = [ [ int(n) for n in l ] for l in test.split('\n') ]
        print('Part 1: ' + str(part1(points)))
        print('Part 2: ' + str(part2(points)))


if __name__ == '__main__':
    main()

"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""