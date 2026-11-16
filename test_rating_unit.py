from rating_unit import calculate_average_rating 

 

def test_average(): 

	assert calculate_average_rating([3, 4, 5]) == 4.0 

 

def test_rounding(): 

	assert calculate_average_rating([4, 5, 5]) == 4.67 

 

def test_single_rating(): 

	assert calculate_average_rating([5]) == 5.0 

 

def test_no_ratings(): 

	assert calculate_average_rating([]) is None 