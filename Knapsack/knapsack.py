'''
Use the weights, profits and knapsack capacity from 
the P08 dataset to find the optimal packing in two ways
1. With the fractional knapsack problem
2. With the binary (0/1) knapsack problem

# optimal profit 13 549 094
'''
from typing import List
from item import Item
from random import random
from math import floor

def read(filename):
    try:
        with open(f"Knapsack\data\{filename}.txt", 'r') as file:
            result =  file.readlines()
            file.close()
        return list(map(int, result)) # Map string to int
    except FileNotFoundError:
        print("File was not found, this should never happen")

def setup():
    capacity = read("capacity")[0]  # LMAO
    solution = read("solution") # More lmao
    profits = read("item_profits")
    weights = read("item_weights")

    items = []
    for profit, weight in zip(profits, weights):
        items.append(Item(profit, weight))

    return capacity, solution, items, weights, profits


def fractional_knapsack(capacity, items):
    '''
        This algorithm solves the problem by calculating the profit per weight
        and adds the items with highest value first to the knapsack
        until no more items fit
        Assumption: Each item can only be added to the knapsack once
    ''' 
    weight = 0
    knapsack = []
    def sort():
        '''Sort items by profit/weight'''
        items.sort(key=lambda x: x.profit/x.weight, reverse=True)


    def binary(weight):
        index = 0
        while(items and index < len(items)):
            if weight + items[index].weight <= capacity:
                knapsack.append(items[index])
                weight += items[index].weight
                items.pop(index)
            else:
                index += 1
                
        return weight
    
    def fraction(weight):
        remainder = capacity - weight
        item = items[0]
        newWeight = remainder / item.weight
        newProfit = newWeight * item.profit
        newItem = Item(newProfit, remainder)
        knapsack.append(newItem)

    sort()
    weight = binary(weight)
    fraction(weight)
    
    return knapsack

def calc_tests(items):
    weight = 0
    profit = 0
    for item in items:
        profit += item.profit
        weight += item.weight
    return profit, weight


def main():
    capacity, solution, items, weights, profits = setup()
    tempItems = [Item(5, 1), Item(5, 2), Item(5, 3), Item(5, 4), Item(5, 5)]
    tempItems = sorted(tempItems, key=lambda _: random())
    item = fractional_knapsack(capacity, items)
    profit, weight = calc_tests(item)
    print(f"Profit: {profit}, Weight: {weight}")
    print(f"Remaining capacity: {capacity - weight}")
    # print(*item, sep='\n')
    # optimal profit 13 549 094
if __name__ == "__main__":
    main()
