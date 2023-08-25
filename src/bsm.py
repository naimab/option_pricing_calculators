import numpy as np
import scipy.stats as sc


class Option(object):
    def __init__(self, type, s, k, vol, r, t, q=0):
        self.type = type
        self.s = s
        self.k = k
        self.vol = vol
        self.t = t
        self.r = r
        self.q = q

    @staticmethod
    def european_val(type, s, k, vol, t, r, q=0):
        """
        Use the Black Scholes Model to value an option on a stock with European Exercise.

        Parameters:
        type (string): c for call and p for put
        vol (float):  annualized volatility
        s (float): stock price
        r (rate):  annualized interest rate
        k (float): strike price
        t (float): time in years
        q (float): dividend yield

        Returns:
        Option price (float)

        """
        d1 = ((np.log(s / k)) + ((r - q) + 0.5 * vol**2) * t) / (vol * np.sqrt(t))
        d2 = d1 - vol * np.sqrt(t)
        nd1 = sc.norm.cdf(d1)
        nd2 = sc.norm.cdf(d2)

        if type == "c":
            if q > 0:
                call_val = s * np.exp(-q * t) * nd1 - k * np.exp(-r * t) * nd2

            else:
                call_val = s * nd1 - k * np.exp(-r * t) * nd2

            return call_val

        else:
            if q > 0:
                put_val = k * np.exp(-r * t) * sc.norm.cdf(-d2) - s * np.exp(-q * t) * sc.norm.cdf(
                    -d1
                )

            else:
                put_val = k * np.exp(-r * t) * sc.norm.cdf(-d2) - s * sc.norm.cdf(-d1)

            return put_val


# this is for demonstration purpose only.
if __name__ == "__main__":
    print(Option.european_val("c", 100, 100, 0.3, 0.05, 1))
