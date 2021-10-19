from item import Item
def read(filename):
    try:
        with open(f"Knapsack\data\{filename}.txt", 'r') as file:
            result = file.readlines()
            file.close()
        return list(map(int, result))  # Map string to int
    except FileNotFoundError:
        print("File was not found, this should never happen")


def setup():
    capacity = read("capacity")[0]  # LMAO
    solution = read("solution")  # More lmao
    profits = read("item_profits")
    weights = read("item_weights")

    items = []
    for profit, weight in zip(profits, weights):
        items.append(Item(profit, weight))

    return capacity, solution, items, weights, profits


# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def knapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack of capacity W,
	# then this item cannot be included
	# in the optimal solution
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			    knapSack(W, wt, val, n-1))

# end of function knapSack


#Driver Code
capacity, solution, items, weights, profits = setup()
# capacity = 30
# items = [Item(50, 5), Item(60, 10), Item(120, 20)]
wt = [5, 10, 20]
val = [50, 60, 120]
n = len(items)
print (knapSack(capacity, weights, profits, n))

# This code is contributed by Nikhil Kumar Singh
