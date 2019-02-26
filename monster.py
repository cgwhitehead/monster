# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:24:57 2019

@author: chris
"""
import optimize
import time

def main():
    print("hungry?")
    print("Oh yeah, you're a monster and can't talk.")
    print("Use your big ol' monster hands to press \'Y\' for hungry")
    print("and \'N\' for not hungry")
    response = input("Y or N: ")
    if response == "Y":
        happyMenu=optimize.walking(100000)
        print('Here\'s your hunting list:')
        time.sleep(1)
        print(happyMenu['menu'].to_string(index=False))
        time.sleep(1)
        print('It will cost you {cost} energy in exchange for {happy} happiness'.format(cost=happyMenu['cost'], happy=happyMenu['happiness']))
    else:
        print('Too bad...you came here so you\'re leaving with a list')
        happyMenu=optimize.walking(100000)
        print('Here\'s your hunting list:')
        time.sleep(1)
        print(happyMenu['menu'].to_string(index=False))
        time.sleep(1)
        print('It will cost you {cost} energy in exchange for {happy} happiness'.format(cost=happyMenu['cost'], happy=happyMenu['happiness']))
        
        
            
    
if __name__ =="__main__":
    main()