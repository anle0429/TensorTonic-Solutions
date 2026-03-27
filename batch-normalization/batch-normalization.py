import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.array(x, dtype=float)
    gamma = np.array(gamma, dtype=float)
    beta = np.array(beta, dtype=float)
    if x.ndim == 2:
        axes = 0
        gamma_bc = gamma
        beta_bc = beta
        
    elif x.ndim == 4:
        axes = (0, 2, 3)
        gamma_bc = np.reshape(gamma, (1, -1, 1, 1))
        beta_bc = np.reshape(beta, (1, -1, 1, 1))
        
    else:
        raise ValueError("Input x must be 2D or 4D.")
    mean = np.mean(x, axis=axes, keepdims=True)
    var = np.var(x, axis=axes, keepdims=True)

    x_norm = (x - mean) / np.sqrt(var + eps)
    out = gamma_bc * x_norm + beta_bc

    return out
    pass