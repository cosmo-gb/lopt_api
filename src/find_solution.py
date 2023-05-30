# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:29:29 2023

@author: gbonnet
"""

import numpy as np
import json
from scipy.optimize import minimize


def compute_cost_bounds(fuels, powerplants, period=1):
    N_plants = len(powerplants)
    cost_m = np.zeros((N_plants))
    bounds = []
    names = []
    for i in range(N_plants):
        plant_i = powerplants[i]
        if plant_i['type'] == 'gasfired':
            euro = fuels['gas(euro/MWh)'] # euro/MWh
            bounds += [(plant_i['pmin'], plant_i['pmax'])]
        elif plant_i['type'] == 'turbojet':
            euro = fuels['kerosine(euro/MWh)'] # euro/MWh
            bounds += [(plant_i['pmin'], plant_i['pmax'])]
        elif plant_i['type'] == 'windturbine':
            euro = 0
            bounds += [(plant_i['pmin']*fuels['wind(%)']/100, plant_i['pmax']*fuels['wind(%)']/100)]
        else :
            print('Problem: type of plant NOT identified')
        efficiency = plant_i['efficiency']
        cost_m[i] = euro*period/efficiency
        names += [plant_i['name']]
    return cost_m, bounds, names
    
def get_data(data):
    powerplants = data['powerplants'] 
    fuels = data['fuels']
    load = data['load']
    return load, fuels, powerplants

def save_res(res, names, use_scipy=False):
    if use_scipy :
        p_eff = res.x
        N_plants = len(p_eff)
        p_dic = []
        for i in range(N_plants):
            p_dic += [{'name': names[i], 'p': np.round(p_eff[i],1)}]
        log = [{'status': res.message}, 
               {'optimal cost': np.round(res.fun,1)}]
        return p_dic, log
    else :
        p_eff = res
        N_plants = len(p_eff)
        p_dic = []
        for i in range(N_plants):
            p_dic += [{'name': names[i], 'p': np.round(p_eff[i],1)}]
        return p_dic




if __name__ == '__main__' :
    # load data
    path = '../example_payloads/'
    name = 'payload'
    f = 1
    with open(path + name + str(f) +'.json', 'r') as file:
        data = json.load(file)
    # get load, fuels and powerplant
    load, fuels, powerplants = get_data(data)
    # compute cost function
    cost_m, bounds, names = compute_cost_bounds(fuels, powerplants)
    # find solution
    res = minimize(lambda x: np.sum(cost_m*x),
                   x0=np.zeros((len(powerplants))), 
                   bounds=bounds, 
                   constraints={'type': 'eq', 'fun': lambda x: np.sum(x) - load})
    # step 3: results
    # Affichage des résultats
    print("Statut de la solution:", res.message)
    print("Valeur optimale de x:", res.x,np.sum(res.x))
    print("Valeur optimale de la fonction objectif:", res.fun)
    # save solution
    res_save, log = save_res(res, names)
    res_save