points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    result = 0
    for coord in zip(coordinates, coordinates[1:]):
        coord = *sorted(coord),
        result += points[coord]
    return result


print( calculate_distance([0, 1, 3, 2, 0, 2]) )
