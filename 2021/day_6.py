import copy
def extract_data():
    with open("inputs/input_6.txt", "r") as f:
       return list(map(int, f.readlines()[0].replace("\n", '').split(",")))
    

def pass_day(fish_count: list[int]):
    count = 0
    for i, fish in enumerate(fish_count):
        if fish == 0:
            fish_count[i] = 6
            count += 1
        else:
            fish_count[i] -= 1
    fish_count.extend([8] * count)
    return fish_count


def count_total_fish(fish_count: list[int], day_count: int) -> int:
    for i in range(day_count):
        fish_count = pass_day(fish_count)
    return len(fish_count)



def pass_day_improved(fish_counts: list[int]):
    """passes a single day"""
    zero_days_remaining = fish_counts.pop(0)
    fish_counts[6] += zero_days_remaining
    fish_counts.append(zero_days_remaining)
    return fish_counts


def count_total_fish_improved(fish_counts: list[int], days_to_pass: int) -> int:
    for i in range(days_to_pass):
        fish_counts = pass_day_improved(fish_counts)
    return sum(fish_counts)


def order_fish_into_groups(fish_data: list) -> list:
    """Turns the list of fish data into a list of grouped fish data based on days left"""
    fish_counts = [0,0,0,0,0,0,0,0,0]
    for fish in fish_data:
        fish_counts[fish] += 1
    return fish_counts


if __name__ == "__main__":
    data = extract_data()
    fish_counts = order_fish_into_groups(data)
    output = count_total_fish_improved(fish_counts, 256)
    print(output)

    # The below lines are my original solution to part 1, but are too slow for part 2
    # output = count_total_fish(data, 80)
    # print(output)

