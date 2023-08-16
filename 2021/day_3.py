import copy
def load_bytes() -> list:
    """Loads the commands from a text file, putting them into a list"""
    with open("inputs/input_3.txt", "r") as f:
        return [x.replace('\n', '') for x in f.readlines()]


def bytes_into_eight_bits(bytes: list) -> list:
    """Turns a list of bytes into 8 list of bits"""
    bits = []
    for i in range(len(bytes[0])):
        bits.append([])
        for byte in bytes:
            bits[i].append(byte[i])
    return bits


def most_common_bit(bits: list):
    if bits.count('0') == bits.count('1'):
        return('1')
    return max(bits, key=bits.count)


def least_common_bit(bits: list):
    if bits.count('0') == bits.count('1'):
        return ('0')
    return min(bits, key=bits.count)


def get_gamma_rate(all_bits: list):
    return "".join(list(map(most_common_bit, all_bits)))
   

def get_epsilon_rate(all_bits: list):
    return "".join(list(map(least_common_bit, all_bits)))


def get_oxygen_level(bytes: list):
    oxygen_level = copy.deepcopy(bytes)
    for i in range(len(bytes[0])):
        bits = [x[i] for x in oxygen_level]
        max_bit = most_common_bit(bits)
        oxygen_level = list(filter(lambda x: x[i] == max_bit, oxygen_level))
    return oxygen_level[0]


def get_carbon_level(bytes: list):
    carbon_level = copy.deepcopy(bytes)
    for i in range(len(bytes[0])):
        bits = [x[i] for x in carbon_level]
        min_bit = least_common_bit(bits)
        carbon_level = list(filter(lambda x: x[i] == min_bit, carbon_level))
    return carbon_level[0]

if __name__ == "__main__":
    bytes = load_bytes()
    bits = bytes_into_eight_bits(bytes)
    gamma = get_gamma_rate(bits)
    epsilon = get_epsilon_rate(bits)
    gamma_rate = int(gamma, 2)
    epsilon_rate = int(epsilon, 2)
    print(gamma_rate * epsilon_rate)
    oxygen_level = get_oxygen_level(bytes)
    carbon_level = get_carbon_level(bytes)
    print(int(oxygen_level, 2) * int(carbon_level, 2))