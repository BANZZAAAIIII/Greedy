from typing import List
import csv

def get_data() -> List[dict]:
	dataset = []

	with open("data/worldcities.csv", encoding='utf-8') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			dataset.append({"city": row["city"], "lat": float(row["lat"]), "lng": float(row["lng"])})

	return dataset
