import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y, dtype = float)
    values, count = np.unique(y, return_counts = True)
    prob = count/ count.sum()
    return -np.sum(prob * np.log2(prob))
    pass