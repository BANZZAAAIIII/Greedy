from typing import List
import csv
import os


def get_data(norway=False, short=False) -> List[dict]:
	dataset = []
	if short:
		path = "../data/worldcities_short.csv"
	else:
		path = "../data/worldcities.csv"

	with open(path, encoding='utf-8') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			if norway and row["country"] == "Norway":
				dataset.append({"city": row["city"], "lat": float(row["lat"]), "lng": float(row["lng"])})
			elif not norway:
				dataset.append({"city": row["city"], "lat": float(row["lat"]), "lng": float(row["lng"])})

	return dataset
