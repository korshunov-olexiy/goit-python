points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    dist = [tuple(sorted((c, coordinates[idx+1]))) for idx, c in enumerate(coordinates[:-1])]
    return sum([points.get(d) for d in dist if d in points])


print( calculate_distance([0, 1, 3, 2, 0, 2]) )
