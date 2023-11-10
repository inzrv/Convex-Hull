import numpy as np
import convex_hull as MyHull
from scipy.spatial import ConvexHull

def test():
    sizes = [3, 10, 50, 100, 150, 200, 400, 800]
    repetitions = 5
    for n in sizes:
        for i in range(0, repetitions):
            res, points = test_n_points(n)
            if not res:
                print("Test Failed! Points=", points)
                np.savetxt('test.out', points, delimiter=',')
                return
    print("All test are passed!")

def test_n_points(n):
    rng = np.random.default_rng()
    points = rng.random((n, 2))   # n random points in 2-D 
    hull_points = MyHull.convex_hull(points)
    scipy_hull = ConvexHull(points)
    scipy_hull_points = points[scipy_hull.vertices]
    return [compare(hull_points, scipy_hull_points), points]

def compare(arr1, arr2):
    sorted1 = arr1[np.lexsort(np.rot90(arr1))]
    sorted2 = arr2[np.lexsort(np.rot90(arr2))]
    return np.array_equal(sorted1, sorted2)