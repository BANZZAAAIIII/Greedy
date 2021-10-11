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
