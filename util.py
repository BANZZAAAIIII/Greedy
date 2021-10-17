import math


def calculateDistance(lat1, lng1):
	""""
	uses haversine formula from: https://www.movable-type.co.uk/scripts/latlong.html
	a = sin²(delta_phi/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
	c = 2 ⋅ atan2( √a, √(1−a) )
	d = R ⋅ c
	"""
	def inner(lat2, lng2):
		R = 6371  # earths radius in km
		phi1 = math.radians(lat1)
		lambda1 = math.radians(lng1)
		phi2 = math.radians(lat2)
		lambda2 = math.radians(lng2)

		delta_phi = phi2 - phi1
		delta_lambda = lambda2 - lambda1

		a = (math.sin(delta_phi / 2) * math.sin(delta_phi / 2) +
			 math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2))
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		return R * c

	return inner


def create_matrix(dataset):
	n = len(dataset)
	matrix = [[-1 for _ in range(0, n)] for _ in range(0, n)]

	for row, data in enumerate(dataset):
		dist_from_x = calculateDistance(data["lat"], data["lng"])
		for col in range(0, n):
			city = dataset[col]
			matrix[row][col] = int(dist_from_x(city["lat"], city["lng"]))

	# for d in matrix:
	# 	print(d)

	return matrix


def matrix_to_edges(matrix):
	edge_list = []
	for r, row in enumerate(matrix):
		for c, col in enumerate(row):
			if matrix[r][c] != 0 and matrix[r][c] != math.inf:
				edge_list.append((matrix[r][c], r, c))
	return edge_list


class DisjointSet:
	"""
	Simple disjoint set datastructures implementation
	Based on the code and information from techiedelight:
	https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
	"""
	_disjoint_set = {}

	def createSet(self, N):
		""" Creates set of N disjointed sets """
		for i in range(N+1):
			self._disjoint_set[i] = i

	def find(self, k):
		""" Finds which subset a element is in """
		if self._disjoint_set[k] == k:
			return k
		else:
			return self.find(self._disjoint_set[k])

	def union(self, set1, set2):
		""" Joins two subsets combining them to a single subset """
		root1 = self.find(set1)
		root2 = self.find(set2)

		self._disjoint_set[root1] = root2
