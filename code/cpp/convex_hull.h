#pragma once
#include <vector>
#include <algorithm>

struct Point {
    Point() : x(0), y(0) {}
    Point(double x, double y) : x(x), y(y) {}
    double x;
    double y;
};

namespace math {
    double crossProduct(Point p1, Point p2) {
        return p1.x * p2.y  - p2.x * p1.y;
    }

    double direction(Point p1, Point p2, Point p3) {
        Point v1(p3.x - p1.x, p3.y - p1.y);
        Point v2(p2.x - p1.x, p2.y - p1.y);
        return crossProduct(v1, v2);
    }

    bool isRightTurn(const std::vector<Point>& points) {
        auto n = points.size();
        assert(n > 2);
        return direction(points[n - 3], points[n - 2], points[n - 1]) > 0;
    }
}

struct ConvexHull {
    ConvexHull() = default;
    ConvexHull(std::vector<Point> points) {
        if (points.size() < 3) {
            hull = points;
            return;
        }
        auto comp = [](Point p1, Point p2) {
            if (p1.x < p2.x) return true;
            if (p2.x < p1.x) return false;
            return p1.y < p2.y;
        };

        std::sort(points.begin(), points.end(), comp);

        std::vector<Point> upper;
        for (auto point : points) {
            upper.push_back(point);
            while (upper.size() > 2 && !math::isRightTurn(upper)) {
                upper.erase(upper.begin() + upper.size() - 2);
            }
        }

        std::vector<Point> lower;
        for (int i = points.size() - 1; i > -1; --i) {
            lower.push_back(points[i]);
            while (lower.size() > 2 && !math::isRightTurn(lower)) {
                lower.erase(lower.begin() + lower.size() - 2);
            }
        }
        lower.pop_back();
        lower.erase(lower.begin());
        hull = upper;
        hull.insert(hull.end(), lower.begin(), lower.end());
    }
    std::vector<Point> hull;
};


