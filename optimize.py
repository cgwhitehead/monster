# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from random import randint, random
from matplotlib import pyplot


menu = pd.read_csv('monster_data.csv')

Cost=menu['cost'].values
Happy=menu['happiness'].values


def first_list_builder():
    size=randint(5,15)
    options = np.random.choice(a=menu['id'], size=30, replace=False)
    return options[0:size]

    
def change_list(hunting_list):
    if sum(Cost[hunting_list-1])>500:
        coin=3
    else:
        coin = randint(1,3)
    options=np.random.choice(a=menu['id'], size=1000, replace=False)
    new_item = options[0]
    counter=1
    while new_item in hunting_list:
        new_item = options[counter]
        counter += 1
    if coin == 1:
        return np.append(hunting_list , [new_item])
    elif coin == 2:
        return np.append(hunting_list[1:] , [new_item])
    else:
        return np.append(hunting_list[2:] , [new_item])
    

def evaluate_list(hunting_list):
    cost=sum(Cost[hunting_list-1])
    happy = sum(Happy[hunting_list-1])
    if cost > 500:
        return 0
    else:
        return happy

    
def walking(steps):
    iters = steps
    top_happiness = -99999
    counter = 1
    graph_x=[]
    graph_y=[]
    graph_y2=[]
    temp = 30
    hunting_list = first_list_builder()
    while counter <= iters:
        counter+=1
        score1=evaluate_list(hunting_list)
        new_hunting_list=change_list(hunting_list)
        score2=evaluate_list(new_hunting_list)
        if score2 > score1:
            hunting_list=new_hunting_list.copy()
            if score1>top_happiness:
                top_happiness=score1
                hunting_list=new_hunting_list.copy()
        else:
            p = np.exp(-(score1)/temp)
            if random()<p:
                hunting_list=new_hunting_list
        temp = 50*np.sin(2*np.pi*counter/(steps/5))
        #temp=30
        print(score1, score2)
        graph_x.append(counter)
        graph_y.append(evaluate_list(hunting_list))
        graph_y2.append(sum(Cost[hunting_list-1]))
    pyplot.plot(graph_x,graph_y)
    #pyplot.plot(graph_x,graph_y2)
    print(menu[menu['id'].isin(hunting_list)])
    print('Cost: {}'.format(sum(Cost[hunting_list-1])))
    print('Happy: {}'.format(evaluate_list(hunting_list)))

    
    