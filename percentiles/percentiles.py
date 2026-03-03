import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    xar = np.array(x)
    qar = np.array(q)
    result = np.percentile(xar,qar, method = 'linear')
    return result
    pass