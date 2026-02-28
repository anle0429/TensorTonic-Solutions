def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid
    """
    assignments = []
    D = len(points[0])

    for p in points:
        best_dist = float("inf")
        best_idx = 0

        for j, c in enumerate(centroids):
            dist = 0
            for d in range(D):
                diff = p[d] - c[d]
                dist += diff * diff
            if dist < best_dist:
                best_dist = dist
                best_idx = j
        assignments.append(best_idx)
    return assignments