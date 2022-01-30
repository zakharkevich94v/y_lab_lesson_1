def distance_calc(x1, y1, x2, y2):
    """Calculates distance between two points"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def full_path_calc(locations):
    """Calculates full path distance"""
    res = 0

    for i in range(len(locations) - 1):
        res += distance_calc(*locations[i], *locations[i + 1])
    return res


def postman_print(locations):
    """Prints full path and distance between points"""
    res = 0
    distances = []

    for i in range(len(locations) - 1):
        res += distance_calc(*locations[i], *locations[i + 1])
        distances.append(res)
    print(
        f"{locations[0]} -> "
        f"{locations[1]}[{distances[0]}] -> "
        f"{locations[2]}[{distances[1]}] -> "
        f"{locations[3]}[{distances[2]}] -> "
        f"{locations[4]}[{distances[3]}] -> "
        f"{locations[5]}[{distances[4]}] = {distances[4]}")


def postman(start, locations):
    """Locates best path for postman"""
    res_list = []
    res_distance = -1
    for i in range(0, 4):
        j_copy = locations[:i] + locations[i + 1:]
        for j in range(len(j_copy)):
            k_copy = j_copy[:j] + j_copy[j + 1:]
            for k in range(len(k_copy)):
                compare_list = [start, locations[i], j_copy[j], k_copy[k], k_copy[1 - k], start]
                compare_distance = full_path_calc(compare_list)
                if res_distance == -1 or compare_distance < res_distance:
                    res_list = compare_list[:]
                    res_distance = compare_distance
    postman_print(res_list)

# location points
postal_office = (0, 2)
griboedova = (2, 5)
beyker_str = (5, 2)
big_sadovaya = (6, 6)
vechno_green_alleya = (8, 3)

postman(postal_office, [griboedova, beyker_str, big_sadovaya, vechno_green_alleya])