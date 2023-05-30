# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:25:31 2023

@author: gbonnet
"""

from flask import Flask, request, jsonify
import numpy as np
from scipy.optimize import minimize
from find_solution import get_data, compute_cost_bounds, save_res
from my_minimization import minimize_with_constraints #, cost_function

app = Flask(__name__)


@app.route('/productionplan', methods=['POST'])
def production_plan():
    payload = request.get_json()  # get back the payload of request
    # get load, fuels and powerplant
    load, fuels, powerplants = get_data(payload)
    # compute cost function
    cost_m, bounds, names = compute_cost_bounds(fuels, powerplants)
    # find solution
    # minimization with scipy
    if use_scipy :
        res = minimize(lambda x: np.sum(cost_m*x),
                       x0=np.zeros((len(powerplants))), 
                       bounds=bounds, 
                       constraints={'type': 'eq', 'fun': lambda x: np.sum(x) - load})
        # save solution
        res_save, log = save_res(res, names,use_scipy)
    # minimization with simple gradient descent
    else :    
        res = minimize_with_constraints(cost_m, bounds, load)
        # save solution
        res_save = save_res(res, names,use_scipy)

    return jsonify(res_save)

if __name__ == '__main__':
    use_scipy=False
    app.run()
    #app.run(host="0.0.0.0",port=8888)
    #app.run(port=8888)