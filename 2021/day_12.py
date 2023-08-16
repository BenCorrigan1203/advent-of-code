from collections import Counter

class Cave:
    def __init__(self, name):
        self.name = name
        if name.isupper():
            self.cave_size = 'L'
        else:
            self.cave_size = 'S'
        self.neighbours = []


def extract_data():
    with open("inputs/input_12.txt", "r") as f:
        return [x.replace("\n","").split("-") for x in f.readlines()]
    

def create_caves(data: list[list]) -> list[Cave]:
    cave_names = []
    for link in data:
        for cave in link:
            if cave not in cave_names:
                cave_names.append(cave)
    return [Cave(name) for name in cave_names]


def add_neigbours(caves: list[Cave], cave_links: list[list[str]]) -> None:
    for link in cave_links:
        for cave in caves:
            if cave.name == link[0] and link[1] not in [cave.name for cave in cave.neighbours]:
                cave.neighbours.append([cave for cave in caves if cave.name == link[1]][0])
            if cave.name == link[1] and link[0] not in [cave.name for cave in cave.neighbours]:
                cave.neighbours.append([cave for cave in caves if cave.name == link[0]][0])


def is_valid_travel_point(neighbour: Cave, route: list[str], small_cave_most_visited: int, task_number: int) -> bool:
    if neighbour.cave_size == "L" or (neighbour.cave_size == "S" and neighbour.name not in route):
            return True
    
    if task_number == 2:
        if neighbour.cave_size == "S" and neighbour.name in route and neighbour.name != "start":
            if small_cave_most_visited < 2:
              return True  
        else:
            return False
    else:
        raise ValueError('Invalid task number')


def is_continuable(route: list[str], caves: list[Cave], task_number: int):
    if route[-1] == "end":
        return True
    for cave in caves:
        if route[-1] == cave.name:
            small_cave_most_visited = max(list(Counter([x for x in route if x.islower()]).values()))
            for neighbour in cave.neighbours:
                if is_valid_travel_point(neighbour, route, small_cave_most_visited, task_number):
                    return True
    return False


def remove_non_continuable_routes(routes: list[list[str]], caves: list[Cave], task_number: int):
    for route in routes:
        if not is_continuable(route, caves, task_number):
            routes.remove(route)
    return routes


def add_cave_step(cave_routes: list[list[str]], caves: list[Cave], task_number: int) -> list[list[str]]:
    new_routes = []
    for route in cave_routes:
        if route[-1] != "end":
            for cave in caves:
                if route[-1] == cave.name:
                    small_cave_most_visited = max(list(Counter([x for x in route if x.islower()]).values()))
                    for neighbour in cave.neighbours:
                        if is_valid_travel_point(neighbour, route,small_cave_most_visited, task_number):
                            new_route = [cave for cave in route]
                            new_route.append(neighbour.name)
                            new_routes.append(new_route)
                    break
        else:
            new_routes.append(route)
    new_routes = remove_non_continuable_routes(new_routes, caves, task_number)
    return new_routes


def find_all_routes(caves: list[Cave], task_number: int) -> list[list[str]]:
    routes = [['start']]
    while not all([route[-1] == 'end' for route in routes]):
        routes = add_cave_step(routes, caves, task_number)
    return routes


if __name__ == "__main__":
    cave_links = extract_data()
    caves = create_caves(cave_links)
    add_neigbours(caves, cave_links)

    all_routes = find_all_routes(caves, task_number=2)
    print(len(all_routes))
