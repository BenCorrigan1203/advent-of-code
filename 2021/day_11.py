import numpy as np
def extract_data():
    with open("inputs/input_11.txt", "r") as f:
        return [[{'flashing': False, 'energy_level': int(x)} for x in line.replace("\n",'')] for line in f.readlines()]


def add_energy_to_surrounding(octopus_grid: list[list[int]], i: int, j: int) -> list[list[int]]:
    if i > 0:
        octopus_grid[i - 1][j]['energy_level'] += 1 #Top middle
    if i < (len(octopus_grid) - 1):
        octopus_grid[i + 1][j]['energy_level'] += 1 #Bottom Middle
    if j > 0:
        octopus_grid[i][j - 1]['energy_level'] += 1 #Left Middle
    if j < (len(octopus_grid[0]) - 1):
        octopus_grid[i][j + 1]['energy_level'] += 1 #Right Middle
    if i > 0 and j > 0:
        octopus_grid[i - 1][j - 1]['energy_level'] += 1 #Top Left
    if i > 0 and j < (len(octopus_grid[0]) - 1):
        octopus_grid[i - 1][j + 1]['energy_level'] += 1 #Top Right
    if i < (len(octopus_grid) - 1) and j > 0:
        octopus_grid[i + 1][j - 1]['energy_level'] += 1 #Bottom Left
    if i < (len(octopus_grid) - 1) and j < (len(octopus_grid[0]) - 1):
        octopus_grid[i + 1][j + 1]['energy_level'] += 1 #Bottom Right
    

def light_step(octopus_data: list[list[dict]]) -> dict:
    for i, row in enumerate(octopus_data):
        for j, octopus in enumerate(octopus_data):
            octopus_data[i][j]['energy_level'] += 1

    flashing_octupi_count = 0
    while any([(x['flashing'] == False and x['energy_level'] > 9) for row in octopus_data for x in row]):
        for i, row in enumerate(octopus_data):
            for j, octopus in enumerate(octopus_data):
                if octopus_data[i][j]['energy_level'] > 9 and not octopus_data[i][j]['flashing']:
                    octopus_data[i][j]['flashing'] = True
                    add_energy_to_surrounding(octopus_data, i ,j)
                    flashing_octupi_count += 1
                    
    for i, row in enumerate(octopus_data):
        for j, octopus in enumerate(octopus_data):
            if octopus_data[i][j]['flashing']:
                octopus_data[i][j]['energy_level'] = 0
                octopus_data[i][j]['flashing'] = False
    return {'data': octopus_data, 'flash_count': flashing_octupi_count}


def flashes_in_n_steps(octopus_data: list[list[dict]], n: int) -> int:
    total_flashes = 0
    for i in range(n):
        step = light_step(octopus_data)
        octopus_data = step['data']
        total_flashes += step['flash_count']
    return total_flashes


def matrix(data):
    return [[x['energy_level'] for x in row] for row in data]


def find_synchronization(octopus_data: list[list[dict]]) -> int:
    steps = 0
    previous_flashes = 0
    while previous_flashes < 100:
        step = light_step(octopus_data)
        steps += 1
        previous_flashes = step['flash_count']
    return steps

if __name__ == '__main__':
    data = extract_data()

    # output = flashes_in_n_steps(data, 100)
    # print(output)

    part_two = find_synchronization(data)
    print(part_two)