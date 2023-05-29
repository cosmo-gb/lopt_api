# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:58:52 2023

@author: gbonnet
"""

import numpy as np

def cost_function(x, cost_vector):
    return np.dot(cost_vector, x)

def projection(x, bounds):
    lower_bounds = [bound[0] for bound in bounds]
    upper_bounds = [bound[1] for bound in bounds]
    return np.clip(x, lower_bounds, upper_bounds)

def minimize_with_constraints(cost_vector, bounds, load,
                              learning_rate=0.001, max_iterations=10000, th=5):

    num_variables = len(cost_vector)
    # initialization to the minimum
    x = np.array([bound[0] for bound in bounds])
    cost = np.zeros(max_iterations)

    for i in range(max_iterations):
        # update x
        x -= learning_rate * cost_vector
        # force x to be always inside the bounds
        x = projection(x, bounds) # force x to be always inside the bounds
        # enforce the equality constraint
        # if np.sum(x) larger, it decreases x, otherwise, it increases x
        x -= (np.sum(x) - load) / num_variables
        # early stopping
        cost[i] = cost_function(x, cost_vector)
        if i > 2*th+1 :
            if np.mean(cost[i-th:i+1]) > np.mean(cost[i-2*th-1:i-th]):
                break

    return x