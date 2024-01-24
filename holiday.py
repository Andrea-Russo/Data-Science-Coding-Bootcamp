"""
Andrea Russo AR23110010747
T14 Practical Task 1

"""
def hotel_cost(num_nights: int) -> float:
    """
    This function will take the number of nights as an argument,
    and return the total cost for the hotel stay.
    """
    
    return


def plane_cost(city_flight: str) -> float:
    """
    This function will take the name of the city as an argument,
    and return the cost for the flight.
    """
    flight_costs = {'Rome':50, 'Turin':30, 'Palermo':20}
    return


def car_rental(rental_days: int) -> float:
    """
    This function will take the number of days of car rental as an argument
    and return the total cost of the car rental
    """
    
    return

def holiday_cost(hotel_cost: float, plane_cost: float, car_rental: float) -> float:
    """
    This function will take the three arguments
    hotel_cost, plane_cost, car_rental. Using these three
    arguments, you can call all three of the above functions with
    respective arguments and finally return a total cost for your
    holiday.
    """
    
    return





city_flight = input('Please insert which city you are flight to:')
num_night = int(input('Please insert the number of nights you will be staying in a hotel'))
rental_days = int(input('Please insert the number of days for whcih you will be hiring a car'))


"""
Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
● First, get the following user inputs:
○ city_flight: The city they will be flying to. (You can create some
options for them. Remember each city will have different flight
costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days for which they will be hiring a
car.

Next, create the following four functions:
● hotel_cost: This function will take num_nights as an argument,
and return a total cost for the hotel stay (you can choose the price
per night charged at the hotel).
● plane_cost: This function will take city_flight as an argument
and return a cost for the flight. (Hint: use if/else if statements in
the function to retrieve a price based on the chosen city.)
● car_rental: This function will take rental_days as an argument
and return the total cost of the car rental (you can choose the daily
rental cost.)
● holiday_cost: This function will take the three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments, you can call all three of the above functions with
respective arguments and finally return a total cost for your
holiday.
● Print out all the details about the holiday in a readable way.
● Try running your program with different combinations of input to show
its compatibility with different options.
"""