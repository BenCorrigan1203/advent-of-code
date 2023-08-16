import copy


def load_commands() -> list:
    """Loads the commands from a text file, putting them into a list"""
    with open("inputs/input_2.txt", "r") as f:
        return [x.replace('\n', '') for x in f.readlines()]


def move_sub(sub_pos: dict, command: str):
    """Executes a single movement command on the sub"""
    split_command = command.split(" ")
    if split_command[0] == 'up':
        sub_pos['aim'] -= int(split_command[1])
    if split_command[0] == 'down':
        sub_pos['aim'] += int(split_command[1])
    if split_command[0] == 'forward':
        sub_pos['horizontal'] += int(split_command[1])
        sub_pos['vertical'] += (int(split_command[1]) * sub_pos['aim'])
    return sub_pos


def execute_movements(start_pos: dict, commands: list) -> dict:
    """Executes all of the movement commands on the sub"""
    current_pos = copy.deepcopy(start_pos)
    for command in commands:
        move_sub(current_pos, command)
    return current_pos


if __name__ == "__main__":
    start_pos = {'horizontal': 0, 'vertical': 0, 'aim': 0}
    commands = load_commands()
    final_pos = execute_movements(start_pos, commands)
    print(start_pos)
    print(final_pos)
    print(final_pos['vertical'] * final_pos['horizontal'])
