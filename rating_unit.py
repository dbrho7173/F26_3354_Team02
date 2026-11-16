def calculate_average_rating(ratings): 

	if not ratings: 

		return None 

	return round(sum(ratings) / len(ratings), 2) 