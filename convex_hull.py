import numpy as np

# compute convex hull for a set of 2-d points.
def convex_hull(points):
    points = points[np.lexsort(np.rot90(points))]
    if (len(points) < 3):
        return points.copy()
    
    upper = [points[0], points[1]]
    for i in range(2, len(points)):
        upper.append(points[i])
        while (len(upper) > 2 and not is_right_turn(upper)):
            upper.pop(-2)

    lower = [points[-1], points[-2]]
    for i in range(len(points) - 3, -1, -1):
        lower.append(points[i])
        while (len(lower) > 2 and not is_right_turn(lower)):
            lower.pop(-2)
    lower.pop(0), lower.pop(-1)

    hull = upper + lower
    return np.array(hull)


# check if the last three points from the `points` turn to the right
def is_right_turn(points):
    p1, p2, p3 = points[-3], points[-2], points[-1]
    mat = [[1.0, p1[0], p1[1]],
           [1.0, p2[0], p2[1]],
           [1.0, p3[0], p3[1]]]
    return np.linalg.det(mat) < 0