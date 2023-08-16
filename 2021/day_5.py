def extract_data():
    with open("inputs/input_5.txt", "r") as f:
       return f.readlines()


def organise_data(data: str) -> list:
    return [[list(map(int, axes.split(","))) for axes in vent_line] for vent_line in [line.replace("\n", "").split(" -> ") for line in data]]


def valid_horizontal_vent(vent: list[list[int]]):
    return vent[0][1] == vent[1][1]


def valid_vertical_vent(vent: list[list[int]]):
    return vent[0][0] == vent[1][0]


def valid_diagonal_vent(vent: list[list[int]]):
    return abs(vent[0][0] - vent[1][0]) == abs(vent[0][1] - vent[1][1])


def place_vents(organised_data: list[list[list[int]]]) -> dict:
    vents = {}
    for vent_line in organised_data:
        if valid_horizontal_vent(vent_line):
            for i in range(min(vent_line[0][0], vent_line[1][0]), max(vent_line[0][0], vent_line[1][0]) + 1):
                position = f'{i},{vent_line[0][1]}'
                vents[position] = vents[position] + 1 if position in vents else 1

        if valid_vertical_vent(vent_line):
            for i in range(min(vent_line[0][1], vent_line[1][1]), max(vent_line[0][1], vent_line[1][1]) + 1):
                position = f'{vent_line[0][0]},{i}'
                vents[position] = vents[position] + 1 if position in vents else 1

        if valid_diagonal_vent(vent_line):
            start_x_pos = vent_line[0][0]
            start_y_pos = vent_line[0][1]
            x_increment = int((vent_line[1][0] - vent_line[0][0])/abs(vent_line[1][0] - vent_line[0][0]))
            y_increment = int((vent_line[1][1] - vent_line[0][1])/abs(vent_line[1][1] - vent_line[0][1]))
            for i in range (abs(vent_line[0][0] - vent_line[1][0]) + 1):
                position = f'{start_x_pos + i * x_increment},{start_y_pos + i * y_increment}'
                vents[position] = vents[position] + 1 if position in vents else 1
    return vents


def danger_areas(vents: dict):
    count = 0
    for vent in vents.values():
        if vent > 1:
            count += 1
    return count


if __name__ == "__main__":
    data = organise_data(extract_data())
    vents = place_vents(data)
    print(len(vents.keys()))
    print(danger_areas(vents))