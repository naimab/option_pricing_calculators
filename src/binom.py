import numpy as np
from scipy.sparse import diags


def binom_val(type, s, strike, vol, r, t, n):
    """
    Calculate the binomial option price.
    Parameters:
    vol: Volatility
    r: Risk-free interest rate
    strike: Strike price
    s: Current stock price
    t: Time to maturity
    n: Number of time steps in the binomial
    type (string): 'c' for call 'p' for put
    Return:
    Option price (float)
    """

    # Set up parameters for the binomial tree model
    dt = t / n  # Calculate time per step
    u = np.exp(vol * np.sqrt(dt))  # Calculate upward movement factor
    d = 1 / u  # Calculate downward movement factor
    p = (np.exp(r * dt) - d) / (u - d)  # Calculate risk-neutral probability for upward movement
    q = 1 - p  # Calculate risk-neutral probability for downward movement

    # Pseudocode: Construct the stock price vector at maturity
    s_vec = np.cumprod(
        [u**n * s] + [d] * (2 * n), axis=0
    )  # Stock prices at maturity for all possible paths

    # Pseudocode: Construct the present value matrix (sparse)
    # Initialize an empty sparse matrix
    # pv = np.zeros((m,m))
    m = 2 * n + 1
    pv = diags([p, q], [-1, 1], shape=(m, m))
    pv = np.multiply(np.exp(-r * dt), pv)  # element wise multiplication

    # Calculate the terminal payoffs for the option
    if type == "c":
        op_vec = np.maximum(s_vec - strike, 0)  # Option values at maturity for all possible paths

    else:
        # Calculate the terminal payoffs for the option
        op_vec = np.maximum(strike - s_vec, 0)  # Option values at maturity for all possible paths

    # Backward induction to calculate option price at t=0
    for i in range(n - 1, -1, -1):
        op_vec = pv.dot(op_vec)  # Use sparse matrix-vector multiplication

    return op_vec[n]


# this is for demonstration purpose only.
if __name__ == "__main__":
    opt_val = binom_val("c", 100, 100, 0.3, 0.05, 1, 500)
    print(opt_val)
