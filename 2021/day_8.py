def extract_data():
    with open("inputs/input_8.txt", "r") as f:
       return [[y.split() for y in x.replace("\n", '').split(" | ")] for x in f.readlines()]
    

def count_unique_values(signal_data: list[list[list[str]]]) -> int:
    """Counts the values in all of the output that correspond to unique signal lenghts"""
    count = 0
    for signal in signal_data:
        for digit in signal[1]:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count


def configure_length_five(configured_signals: dict, signal: str) -> dict:
    """differentiates between the length five signals"""
    if configured_signals['1'][0] in signal and configured_signals['1'][1] in signal:
        configured_signals['3'] = signal
        return configured_signals
    
    count = 0
    for letter in configured_signals['4']:
        if letter in signal:
            count += 1

    if count == 3:
        configured_signals['5'] = signal
    if count == 2:
        configured_signals['2'] = signal
    return configured_signals


def configure_length_six(configured_signals: dict, signal: str) -> dict:
    """differentiates between the length six signals"""
    count = 0
    for letter in configured_signals['4']:
        if letter in signal:
            count += 1
    
    if count == 4:
        configured_signals['9'] = signal
    if count == 3:
        if configured_signals['1'][0] in signal and configured_signals['1'][1] in signal:
            configured_signals['0'] = signal
        else:
            configured_signals['6'] = signal
    return configured_signals


def find_letters_to_numbers(configuration_signals: list[str]):
    """Finds out what set of letter signals correspond to which number"""
    configured_signals = {}
    for signal in configuration_signals:
        if len(signal) == 2:
            configured_signals['1'] = signal
        if len(signal) == 3:
            configured_signals['7'] = signal
        if len(signal) == 4:
            configured_signals['4'] = signal
        if len(signal) == 7:
            configured_signals['8'] = signal
    for signal in configuration_signals:
        if len(signal) == 5:
            configure_length_five(configured_signals, signal)
        if len(signal) == 6:
            configure_length_six(configured_signals, signal)
    return configured_signals


def find_output_number(signal_line: list[list[list[str]]]) -> int:
    """Find the output number for a give input signal"""
    configured_numbers = find_letters_to_numbers(signal_line[0])
    num = ""
    for output_number in signal_line[1]:
        num += list(configured_numbers.keys())[["".join(sorted(x)) for x in configured_numbers.values()].index("".join(sorted(output_number)))]
    return int(num)


def total_sum(input_data) -> int:
    """Sums the values for each line of input"""
    sum = 0
    for line in input_data:
        sum += find_output_number(line)
    return sum

if __name__ == "__main__":
    data = extract_data()
    # print(data)
    print(total_sum(data))