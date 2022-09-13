"""

let us solve sudoku, this might be challenging but we must solve it


"""

def solve_sudoku(sudoku):
    game = sudoku.copy()
    solved = False

    top_left = [
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)
        ]
    top_center = [
        (0,3),(0,4),(0,5),
        (1,3),(1,4),(1,5),
        (2,3),(2,4),(2,5)
        ]
    top_right = [
        (0,6),(0,7),(0,8),
        (1,6),(1,7),(1,8),
        (2,6),(2,7),(2,8)
        ]
    mid_left = [
        (3,0),(3,1),(3,2),
        (4,0),(4,1),(4,2),
        (5,0),(5,1),(5,2)]
    mid_center = [
        (3,3),(3,4),(3,5),
        (4,3),(4,4),(4,5),
        (5,3),(5,4),(5,5)
        ]
    mid_right = [
        (3,6),(3,7),(3,8),
        (4,6),(4,7),(4,8),
        (5,6),(5,7),(5,8)
        ]
    bottom_left = [
        (6,0),(6,1),(6,2),
        (7,0),(7,1),(7,2),
        (8,0),(8,1),(8,2)]
    bottom_center = [
        (6,3),(6,4),(6,5),
        (7,3),(7,4),(7,5),
        (8,3),(8,4),(8,5)
        ]
    bottom_right = [
        (6,6),(6,7),(6,8),
        (7,6),(7,7),(7,8),
        (8,6),(8,7),(8,8)
        ]

    squares = [top_left, top_center, top_right, mid_left, mid_center,mid_right, bottom_left, bottom_center, bottom_right]
    
    while not solved:
        for i, row in enumerate(game):
            for j, item in enumerate(row):
                if item == 0:
                    coord = (i,j)
                    # get the row
                    item_row = row

                    # get the column
                    item_col = [row[j] for row in game ]

                    # get the square
                    item_square = [square for square in squares if coord in square]
                    # square items
                    square_items = [game[i][j] for i,j in item_square[0]]
                    # all numbers [0-9] 
                    master = [num for num in range(0,10)]
                    # missing number
                    missing = [item for item in master if item not in square_items]

                    # find a unique element to fill the place
                    possible_items = []
                    for item in missing:
                        if item not in item_row:
                            if item not in item_col:
                                if item not in square_items:
                                    possible_items.append(item)
                    
                    if len(possible_items) == 1:
                        game[i][j] = possible_items[0]
                else:
                    pass
                

        all_items = []
        for row in game:
            for j in row:
                all_items.append(j)
            
        if 0 not in all_items:
            solved = True

    return  game


if __name__ == '__main__':
    puzzle = [
        [4,2,7,1,0,0,0,6,8],
        [0,0,5,0,0,6,3,0,0],
        [6,0,3,0,0,0,1,0,0],
        [2,0,0,0,1,0,4,0,0],
        [3,4,0,0,6,7,0,5,1],
        [8,0,1,0,5,0,0,2,0],
        [0,9,0,0,0,0,7,3,0],
        [7,0,4,3,0,0,2,0,9],
        [0,3,2,0,9,4,6,0,0]
    ]
    print("Puzzle")
    for j in puzzle:
        print(j)

    solution = solve_sudoku(puzzle)

    print("\nSolution:")
    for data in solution:
        print(data)

    