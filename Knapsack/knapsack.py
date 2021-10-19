from item import Item
from filemanager import setup

def fractional_knapsack(capacity, items):
    '''
        This algorithm solves the problem by calculating the profit per weight
        and adds the items with highest value first to the knapsack
        until no more items fit
        Assumption: Each item can only be added to the knapsack once
    ''' 
    if capacity <= 0 or len(items) <= 0:
        return None

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


def binary_knapsack(capacity, items):
    '''
        0-1 dynamic solver, bottom up
        Starts at the back it item list
        Max compares two paramter
            First parameter includes the indexed item in the knapsack
            Second paramter excludes the indexed item in the knapsack
    '''

    knapsack = []
    def binary(capacity, items, index):

        if capacity <= 0 or index == 0:
            return 0

        # Skip items with weight larger than capacity
        if items[index - 1].weight > capacity:
            return binary(capacity, items, index - 1)
        else:
            return max(items[index - 1].profit + binary(
                    capacity - items[index - 1].weight, items, index - 1),
                    binary(capacity, items, index - 1))
            # Creates a list of the items added to the knapsack
            # temp1 =  items[index - 1].profit + binary(
            #     capacity - items[index - 1].weight, items, index - 1)
            # temp2 = binary(capacity, items, index - 1)
            # if temp1 >= temp2:
            #     knapsack.append(items[index - 1])
            #     return temp1
            # else:
            #     return temp2
    return knapsack, binary(capacity, items, len(items))


def calc_tests(items):
    weight = 0
    profit = 0
    for item in items:
        profit += item.profit
        weight += item.weight
    return profit, weight


def main():
    # capacity = 30
    # items = [Item(50, 5), Item(60, 10), Item(120, 20)]
    capacity, solution, items, weights, profits = setup()
    item = fractional_knapsack(capacity, list(items))
    profit, weight = calc_tests(item)
    print(f"Profit: {profit}, Weight: {weight}")
    print(f"Remaining capacity: {capacity - weight}")


    knapsack, profit = binary_knapsack(capacity, list(items))
    # print(*knapsack, sep='\n')
    print(f"Binary profit: {profit}")

if __name__ == "__main__":
    main()
