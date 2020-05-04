import numpy as np

def forced_oscillation(y, v, t, params):

    if t < params["end"]:
        dvdt = - params["A"]*v - params["B"]*y + params["C"]*np.cos(params["D"]*t)
    else:
        dvdt = - params["A"]*v - params["B"]*y

    return dvdt