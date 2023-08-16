def extract_data():
    with open("inputs/input_4.txt", "r") as f:
       return f.readlines()


def create_board(lines: list[str]) -> list[list]:
    """Creates a board, turing a list of strings into a list of lists of ints"""
    return [list(map(int, x.split())) for x in lines]


def clean_data(file_lines: list):
    """cleans the text data into resonable lists"""
    lines = list(map( lambda x: x.replace("\n", ""), filter(lambda x: x != "\n", file_lines)))
    turns = [int(x) for x in lines.pop(0).split(",")]
    boards = []
    for i in range(0, len(lines), 5):
        boards.append(create_board(lines[i:i+5]))
    return {"boards": boards, "turns": turns}


def play_turn(boards: list, bingo_ball_played: int):
    """plays a single bingo ball, checking them off in the boards"""
    for board in boards:
        for line in board:
            for i, square in enumerate(line):
                if square == bingo_ball_played:
                    line[i] = "Found"
    return boards


def win_horizontal(board: list) -> bool:
    """Checks to see if there is a win in the horizontal lines"""
    for line in board:
        if all([True if x == "Found" else False for x in line]):
            return True
    return False


def win_vertical(board: list) -> bool:
    """Checks to see if there is a win in the vertical lines"""
    for i in range(5):
        if all([True if x[i] == "Found" else False for x in board]):
            return True
    return False


def play_game(boards: list, turns: list) -> list:
    """Takes in a set of game boards and the turns to play, returning the winning board"""
    winners = []
    while not winners:
        next_ball = turns.pop(0)
        play_turn(boards, next_ball)

        for board in boards:
            if win_horizontal(board) or win_vertical(board):
                winners.append(board)
    return {'winners': winners, 'winning_ball': next_ball}


def play_game_badly(boards: list, turns: list) -> list:
    """Takes in a set of game boards and the turns to play, returning the winning board"""
    winners = []
    while len(boards) > 0:
        next_ball = turns.pop(0)
        play_turn(boards, next_ball)

        for board in boards:
            if win_horizontal(board) or win_vertical(board):
                winners.append(board)
                boards.remove(board)
    return {'winners': winners[-1], 'winning_ball': next_ball}


def winning_score(winner: list, winning_ball: int):
    score = 0
    for line in winner:
        for square in line:
            if square != 'Found':
                score += square
    return score * winning_ball


if __name__ == "__main__":
    game_data = clean_data(extract_data())
    
    winners = play_game(game_data['boards'], game_data['turns'])
    print(winners['winners'])
    print(winners['winning_ball'])
    print(winning_score(winners["winners"][0], winners["winning_ball"]))


    last_winner = play_game_badly(game_data['boards'], game_data['turns'])
    print(last_winner['winners'])
    print(last_winner['winning_ball'])
    print(winning_score(last_winner["winners"], last_winner["winning_ball"]))