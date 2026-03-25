def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    hist = [0]*256
    for row in image:
        for p in row:
            hist[p] += 1
    return hist