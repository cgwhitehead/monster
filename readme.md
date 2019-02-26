# Monster

This is a simple project to demo my ability to optimize a simple problem.

# TODO
* run instructions
* req txt

## Why Feed the Monster
In this case I spend several days looking for the right data for a problem I've been thinking about for quite some time. I realized that for demo purposes it would be quicker to use mock data for a mock problem.

## Premise
You're a monster on a budget. You want to eat as many animals as possible, but there's an energy cost for hunting, catching, and eating each monster.

Given your energy budget, the optimizer will give you, the monster, a hunting list

Considering all the available animals, you don't have the time or the monster math chops to think through each combo. You're also worried that an optimization algorithm might be lazy and give you a 'better' result, but not the bets (ie local maximum).

## Requirements
* [pandas](https://pandas.pydata.org/)
* [numpy](http://www.numpy.org/)
* [tqdm](https://github.com/tqdm/tqdm)

## Optional
* [matplotlib](https://matplotlib.org/) Several plotting functions are commented out and are useful for exploring the optimization process. 

## Running
```
python monster.py
```
Then answer Y or N.

## Thoughts
I wanted to work on a problem with more than one dimension without previous bounds. A sports team for example has a given number of members with a set position configuration.
For the monster problem I removed the bounds on how many animals could be on the list, meaning the optimizer can go for high cost, high ROI or several low cost
low ROI. At a later date I'd like to analyze the configurations produced by the optimizer. This could be used to develop a shortcut strategy, create bounds, and speed up optimization

Speed was another consideration, the temperature strategy here forces breaking local maxes and trying again over and over which creates
several optimal menus. If time weren't an option this could run for a long period of time and the best menu could be selected.

Instead, (after a lot of runs) I chose 900 happiness to be a good enough menu and so if a menu is found that meets 900 happiness we
call it good enough and return the list so as not to waste too much of the 'Monsters' time. 

This optimizer uses [simlated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) and a novel approach at temperature control.
## Data
Courtesy of [Mockaroo](https://www.mockaroo.com)

## Author
github [@cgwhitehead](https://github.com/cgwhitehead)