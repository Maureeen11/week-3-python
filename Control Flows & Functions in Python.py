def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (price * discount_percent) / 100
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the  the original price if no discount was applied
print(f"The final price after applying the discount is: {final_price:.2f}")
