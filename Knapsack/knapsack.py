'''
Use the weights, profits and knapsack capacity from 
the P08 dataset to find the optimal packing in two ways
1. With the fractional knapsack problem
2. With the binary (0/1) knapsack problem
'''
import os
from item import Item


def read(filename):
    try:
        file = open(f"Knapsack\data\{filename}.txt", 'r')
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

    return capacity, solution, items

def main():
    capacity, solution, items = setup()
    print(*items, sep='\n')
    

if __name__ == "__main__":
    main()
