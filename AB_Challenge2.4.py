# AB Challenge 2.4
# Write a Car Salesman program where the user enters the base price of a car.
# The program should add on a buncn of extra fees such as tax, license, dealer prep, and destination charge.
# Make tax and license a percent of the base price. The other fees should be set values.
# Display the actual price of the car once all the extras are applied.

# Title!

print("\n\t\t\tThe Car Salesman!")

base_price = float(input("\nPlease enter the base price of this vehicle and I will provide you with the final dealer price: "))
tax = base_price * 0.07
license = base_price * 0.04
dealer_prep = 500
destination = 1250

total_price = round(base_price + license + dealer_prep + destination, 2)

print("\nYour total price after taxes, license and dealer fees is: $",total_price)

input("\n\nPlease press the Enter key to exit.")
