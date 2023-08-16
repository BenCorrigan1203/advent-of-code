def extract_data():
    with open("inputs/input_7.txt", "r") as f:
       return [int(x) for x in f.readlines()[0].replace("\n", '').split(",")]
    

def determine_best_position(crab_positions: list[int]):
    fuel_per_position = []
    for i in range(max(crab_positions) + 1):
        fuel_used = 0
        for j in range(len(crab_positions)):
            fuel_used += sum(range(abs(crab_positions[j] - i) + 1))
        fuel_per_position.append(fuel_used)
    return min(fuel_per_position)


if __name__ == "__main__":
    crab_pos = extract_data()
    output = determine_best_position(crab_pos)
    print(output)
