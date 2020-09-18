

class LineOfSight:
    pass

def is_in_line_of_sight(surface, point):
    return point[2] > surface[point[0], point[1]]