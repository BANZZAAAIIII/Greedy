import math
from typing import List, Optional
import util
import random

import filemanager as fm


def tsp_greedy(matrix):
	n = len(matrix)
	cost = 0	     # The current total cost of path
	counter = 1      # Position or how far we have traversed
	col, row = 0, 0  # Position in matrix
	min_cost = math.inf  # Local minimum cost

	path = [-1 for _ in range(0, n)]   # path taken by index, and visited nodes
	path[0] = 0

	# Loops until all but the path back to start are done
	while counter < n:
		if col not in path and col != row:
			if matrix[row][col] < min_cost:
				min_cost = matrix[row][col]
				path[counter] = col

		col += 1

		# All possible path from this node is checked
		if col == n:
			cost += min_cost     # Adds cost from the path with min cost
			min_cost = math.inf
			col = 0
			row = path[counter]  # next node is from the node
			counter += 1

	return cost, path


def create_matrix(dataset):
	n = len(dataset)
	matrix = [[-1 for _ in range(0, n)] for _ in range(0, n)]

	for row, data in enumerate(dataset):
		dist_from_x = util.calculateDistance(data["lat"], data["lng"])
		for col in range(0, n):
			city = dataset[col]
			matrix[row][col] = int(dist_from_x(city["lat"], city["lng"]))

	# for d in matrix:
	# 	print(d)

	return matrix


def main():
	dataset = fm.get_data(False, True)
	matrix = create_matrix(dataset)
	cost, route = tsp_greedy(matrix)
	print(f"min cost: {cost}")
	print(f"route: {route}")


if __name__ == '__main__':
	main()