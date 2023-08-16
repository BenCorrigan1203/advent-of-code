from functools import reduce

def extract_data():
    with open("inputs/input_9.txt", "r") as f:
       return [list(map(int,list(x.replace("\n","")))) for x in f.readlines()]
    

def is_low_point(i: int, j: int, grid: list[list[int]]):
    if i > 0 and grid[i-1][j] <= grid[i][j]:
        return False
    if j > 0 and grid[i][j-1] <= grid[i][j]:
        return False
    if i < len(grid) - 1 and grid[i+1][j] <= grid[i][j]:
        return False
    if j < len(grid[0]) - 1 and grid[i][j+1] <= grid[i][j]:
        return False
    return True

def low_point_score(grid: list[list[int]]):
    total_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_low_point(i,j, grid):
                total_score += (1 + grid[i][j])
    return total_score


def new_adjacent_basin_points(grid:list[list[int]], basin_points: list[str], point: str) -> bool:
    evaluate_point = point.split(",")
    i = int(evaluate_point[0])
    j = int(evaluate_point[1])
    new_points_added = False
    if i > 0 and grid[i-1][j] < 9 and f"{i-1},{j}" not in basin_points:
        basin_points.append(f"{i-1},{j}")
        new_points_added == True
    
    if j > 0 and grid[i][j-1] < 9 and f"{i},{j-1}" not in basin_points:
        basin_points.append(f"{i},{j-1}")
        new_points_added == True

    if i < len(grid) - 1 and grid[i+1][j] < 9 and f"{i+1},{j}" not in basin_points:
        basin_points.append(f"{i+1},{j}")
        new_points_added == True

    if j < len(grid[0]) - 1 and grid[i][j+1] < 9 and f"{i},{j+1}" not in basin_points:
        basin_points.append(f"{i},{j+1}")
        new_points_added == True

    return new_points_added


def basin_size(grid: list[list[int]], low_point: str):
    basin_points = [low_point]
    while not all([new_adjacent_basin_points(grid, basin_points, point) == False for point in basin_points]):
        for point in basin_points:
            new_adjacent_basin_points(grid, basin_points, point)
    return len(basin_points)


def find_all_basin_sizes(grid: list[list[int]]) -> list:
    basin_sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_low_point(i,j, grid):
                basin_sizes.append(basin_size(grid, f'{i},{j}'))
    return basin_sizes


def n_largest_basins(basin_sizes: list, n: int) -> list:                
    return sorted(basin_sizes, reverse=True)[0:n]


if __name__ == "__main__":
    data = extract_data()
    # Task 1
    output = low_point_score(data)

    # Task 2
    basin_sizes = find_all_basin_sizes(data)
    largest_basins = n_largest_basins(basin_sizes, 3)
    print(reduce(lambda x, y: x*y, largest_basins))