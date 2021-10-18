import math
from typing import List, Optional
import util
import random

import filemanager as fm


def tsp_dynamic(matrix):
	def tsp(start, set):
		if graph[start][set] != -1:
			return graph[start][set]

		for i in range(set):
			current_cost = matrix[start][i]
			other_cost = tsp(i, i)

			total_cost = current_cost + other_cost

		return total_cost

	size = len(matrix)
	graph = [[-1 for _ in range(0, size+1)] for _ in range(0, size+1)]
	path = [[-1 for _ in range(0, size+1)] for _ in range(0, size+1)]

	for i in range(size):
		graph[i][0] = matrix[i][0]

	print(tsp(0, size))


def tsp_greedy(matrix):
	n = len(matrix)
	total_cost = 0    # The current total cost of path
	current_node = 0  # Index for row in the matrix, represented as the current node

	path = [-1 for _ in range(0, n)]   # Path taken by index, and visited nodes
	path[0] = current_node             # Adds starting node to first index

	for i in range(1, n):
		min_cost = math.inf  # Local minimum cost

		# Check all possible routs from this node
		for next_node in range(n):
			if next_node not in path and next_node != current_node:
				if matrix[current_node][next_node] < min_cost:
					min_cost = matrix[current_node][next_node]
					path[i] = next_node

		# Setting up for next loop as all possible path from this node, row, is checked
		total_cost += min_cost  # Adds cost from the path with min cost
		current_node = path[i]  # Next node we look at is the one we found with min cost

	return total_cost, path


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
	# cost, route = tsp_greedy(matrix)
	# print(f"route: {route}")
	# print(f"min cost: {cost}")

	tsp_dynamic(matrix)



if __name__ == '__main__':
	main()