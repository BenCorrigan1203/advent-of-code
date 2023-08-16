def read_input() -> list[str]:
    with open("inputs/input.txt", "r") as f:
        return f.readlines()
    
def format_file_list(file: list) -> list:
    depths = [int(x.replace('\n', '')) for x in file]
    return depths


def depth_increases(depths: list, measurement: int) -> int:
    increase_count = 0
    grouped_depths = []
    for i in range(0, len(depths) - measurement + 1):
        grouped_depths.append(sum(depths[i: i + measurement]))
    for i in range(0, len(grouped_depths) - 1):
        if grouped_depths[i] < grouped_depths[i+1]:
            increase_count += 1
    return increase_count


if __name__ == "__main__":
    depths = format_file_list(read_input())
    print(depth_increases(depths,3))
