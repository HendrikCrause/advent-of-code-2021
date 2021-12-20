def pad_image(image, char = '0', size = 5):
    line = [ char for _ in range(len(image[0]) + 2 * size) ]
    pad = [ [char for _ in range(size)] + l + [char for _ in range(size)] for l in image ]
    return [line for _ in range(size)] + pad + [line for _ in range(size)]


def unpad_image(image):
    return [ [ c for c in r[1:-1] ] for r in image[1:-1] ]


def part1(enhance, image, runs=2):

    working = image
    char = '1'
    for _ in range(runs):
        char = '0' if char == '1' else '1'
        working = pad_image(working, char, 5)
        # for r in working:
        #     print(''.join(['.' if c == '0' else '#' for c in r]))
        new_image = [ [ '0' for c in r ] for r in working ]
        for r in range(1,len(working) - 1):
            for c in range(1,len(working[r]) - 1):
                adjacents = working[r-1][c-1:c+2] + working[r][c-1:c+2] + working[r+1][c-1:c+2]
                idx = int(''.join(adjacents), 2)
                new_image[r][c] = enhance[idx]
        working = unpad_image(new_image)
        # for r in working:
        #     print(''.join(['.' if c == '0' else '#' for c in r]))

    # for r in working:
    #     print(''.join(['.' if c == '0' else '#' for c in r]))
    
    return sum( [ sum([ int(c) for c in r ]) for r in working ])


def main():

    test_input_1 = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''

    test_input_2 = '''##....###.#.##...##....####..###.#.######.#.#.##.#.####.#.#####.##.##..##.###.###..##.##..#####.##..#..##..#...#.####..#.###..#....####.#..##.##...#######.###...#.######..#..#...###..###.#####.##..#.#.###.#.###.#..#.###.###.#..##.....####..#.##.##.#..#...###.#.....##..#....#.##..#....#....####.#...#.#.##.#...#.##..#..#.#..###.###.#.##...##.#.##.##..#..##.#..#...######.#.#..###....##...##....#....##....#.#..##..#####.####.#.##...#...#.#.#....#.####...#.##..#...#..#....#..#..#..##.#.#.#.#######.###..##.#.....

#..#.
#....
##..#
..#..
..###'''

    with open('resources/day20', 'r') as file:
        lines = [ l.strip() for l in file ]
        # lines = [ l.strip() for l in test_input_2.split('\n') ]
        enhance = [ '0' if c == '.' else '1' for c in lines[0]]
        image = [ ['0' if c == '.' else '1' for c in l ] for l in lines[2:] ]
        print('Part 1: ' + str(part1(enhance, image)))
        print('Part 2: ' + str(part1(enhance, image, 50)))


if __name__ == '__main__':
    main()

"""
--- Day 20: Trench Map ---
With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #
Starting from the top-left and reading across each row, these pixels are ..., then #.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
In the middle of this first group of characters, the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............
Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............
Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?

Your puzzle answer was 5461.

--- Part Two ---
You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit in the final output image.

Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?
"""