def extract_data():
    with open("inputs/input_10.txt", "r") as f:
        return [x.replace("\n",'') for x in f.readlines()]

def parentheses_errors(parentheses_line: str) -> dict:
    closed_to_open = {')': '(', '}': '{', ']': '[', '>': '<'}
    stack = []
    for bracket in parentheses_line:
        if bracket in closed_to_open:
            if stack and stack[-1] == closed_to_open[bracket]:
                stack.pop()
            else:
                return {'error': True, 'cause': 'corrupted', 'value': bracket}
        else:
            stack.append(bracket)
    return {'error': True, 'cause': 'incomplete', 'value': stack} if stack else {'error': False, 'cause': None, 'value': None}


def syntax_error_score(navigation_lines: list[str]) -> int:
    bracket_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total_score  = 0
    for line in navigation_lines:
        result = parentheses_errors(line)
        if result['error'] and result['cause'] == 'corrupted':
            total_score += bracket_scores[result['value']]
    return total_score


def complete_incomplete_lines(navigation_lines: list[str]) -> list[str]:
    open_to_closed = {'(': ')', '{': '}', '[': ']', '<': '>'}
    completed_lines = []
    for line in navigation_lines:
        result = parentheses_errors(line)
        if result['error'] and result['cause'] == 'incomplete':
            completion_string = ''
            for bracket in result['value'][::-1]:
                completion_string = completion_string + open_to_closed[bracket]
            completed_lines.append(completion_string)
    return completed_lines


def completed_line_score(completed_string: str) -> int:
    bracket_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for bracket in completed_string:
        score *= 5
        score += bracket_scores[bracket]
    return score


if __name__ == "__main__":
    data = extract_data()
    syntax_score = syntax_error_score(data)
    print(syntax_score)

    completed_lines = complete_incomplete_lines(data)
    completed_lines_scores = list(map(completed_line_score, completed_lines))

    output_score = sorted(completed_lines_scores)[int((len(completed_lines_scores) - 1)/2)]
    print(output_score)