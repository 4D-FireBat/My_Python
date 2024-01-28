# AB Challenge 2.3
# Write a Tipper program where the user enters a restaurant bill total. The program should then display two amounts:
# A 15 percent tip and a 20 percent tip.

# Display the title
print("\n\t\t\tThe Tipper")

# Ask the user for the base price.
base_price = float(input("\nPlease enter the bill total: "))

# Calculate 15 percent and 20 percent of the base price and present those numbers to the user.

lower_tip = round(base_price * 0.15, 2)
higher_tip = round(base_price * 0.20, 2)

print("\n15% Tip =", lower_tip)
print("\n20% Tip =", higher_tip)

input("\n\nPress the Enter key to exit")
