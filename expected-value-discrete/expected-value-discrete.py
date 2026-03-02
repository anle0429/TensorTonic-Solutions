import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x)
    p = np.asarray(p)

    if x.shape != p.shape:
        raise ValueError(f"Size of x and p not matched")
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Sum of possibility has to be 1")
    expected_value = np.sum(x * p)

    return float(expected_value)
    pass
