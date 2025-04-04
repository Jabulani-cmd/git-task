# Function to calculate hotel cost
def hotel_cost(num_nights):
    price_per_night = 800  # Price per night in the hotel
    return num_nights * price_per_night

# Function to calculate plane cost based on the city
def plane_cost(city_flight):
    # Flight costs for different cities
    if city_flight == "Cape Town":
        return 2000
    elif city_flight == "Durban":
        return 1500
    elif city_flight == "Johannesburg":
        return 1200
    elif city_flight == "East London":
        return 1500
    else:
        return 0  # Default cost if city is not listed

# Function to calculate car rental cost
def car_rental(rental_days):
    daily_rental_cost = 450  # Daily cost of car rental
    return rental_days * daily_rental_cost

# Function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)
    total_plane = plane_cost(city_flight)
    total_car = car_rental(rental_days)
    return total_hotel + total_plane + total_car

# Main program
if __name__ == "__main__":
    # Get user inputs
    print("Welcome to the Holiday Cost Calculator!")
    print("Available cities: Capetown, Durban, Johannesburg, East London")
    city_flight = input("Enter the city you will be flying to: ").strip()
    num_nights = int(input("Enter the number of nights you will stay at the hotel: "))
    rental_days = int(input("Enter the number of days you will hire a car: "))

    # Calculate total holiday cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    # Print holiday details
    print("\n--- Holiday Details ---")
    print(f"City: {city_flight}")
    print(f"Number of nights at hotel: {num_nights}")
    print(f"Number of days for car rental: {rental_days}")
    print(f"Total hotel cost: R{hotel_cost(num_nights)}")
    print(f"Total plane cost: R{plane_cost(city_flight)}")
    print(f"Total car rental cost: R{car_rental(rental_days)}")
    print(f"Total holiday cost: R{total_cost}")