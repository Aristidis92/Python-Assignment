def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price
               if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and print the final price
    final_price_after_discount = calculate_discount(original_price, discount_percentage)

    if final_price_after_discount == original_price:
        print(f"No discount applied. Original price: ${original_price:.2f}")
    else:
        print(f"Final price after discount: ${final_price_after_discount:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount percentage.")