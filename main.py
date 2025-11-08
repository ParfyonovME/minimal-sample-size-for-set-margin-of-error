from scipy.stats import norm
import math


def min_sample_size(me = 0.03, cl = 0.9, p = 0.5):
    """"
    This function returns the minimum number sample size to obtain the desired margin of error (assuming p = 0.5)
    :param me: margin of error
    :param cl: confidence level
    :param p: assumed sample proportion
    :return: minimum sample size
    """
    alpha = (1 - cl ) / 2
    z = norm.ppf(1 - alpha)
    result = math.ceil((z ** 2)*p*(1 - p)/(me ** 2))
    return result


#############
#Example
#############
confidence_level = 0.90
margin_of_error = 0.04
p_assumed = 0.5
print(f"Minimum sample size: {min_sample_size(margin_of_error, confidence_level, p_assumed)}.")