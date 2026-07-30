from collections import Counter

orders = [
    {"customer_name": "Alice", "food_item": "Burger", "quantity": 2, "unit_price": 5.50},
    {"customer_name": "Bob", "food_item": "Pizza", "quantity": 1, "unit_price": 12.00},
    {"customer_name": "Charlie", "food_item": "Burger", "quantity": 1, "unit_price": 5.50},
    {"customer_name": "David", "food_item": "Pasta", "quantity": 3, "unit_price": 8.00},
    {"customer_name": "Eve", "food_item": "Salad", "quantity": 2, "unit_price": 6.00}
]

def analyze_orders(order_list):
    print("--- RESTAURANT ORDER ANALYSIS ---")
    
    total_daily_revenue = 0.0
    highest_value = 0.0
    highest_order = None
    food_items_ordered = []
    processed_orders = []

    for order in order_list:
        bill_amount = order["quantity"] * order["unit_price"]
        total_daily_revenue += bill_amount
        
        food_items_ordered.extend([order["food_item"]] * order["quantity"])
        
        
        order_info = order.copy()
        order_info["bill_amount"] = bill_amount
        processed_orders.append(order_info)
        
        if bill_amount > highest_value:
            highest_value = bill_amount
            highest_order = order_info

    
    print("\n1. Total Bills Per Customer:")
    for po in processed_orders:
        print(f"   Customer: {po['customer_name']} | Bill: ${po['bill_amount']:.2f}")

    
    print("\n2. Highest-Value Order:")
    if highest_order:
        print(f"   Customer: {highest_order['customer_name']} | Total: ${highest_order['bill_amount']:.2f} ({highest_order['food_item']})")

    print("\n3. Most Frequently Ordered Food Item:")
    if food_items_ordered:
        item_counts = Counter(food_items_ordered)
        most_common_item, frequency = item_counts.most_common(1)[0]
        print(f"   Item: {most_common_item} (Ordered {frequency} times)")

    print(f"\n4. Total Daily Revenue:\n   ${total_daily_revenue:.2f}")

    print("\n5. Orders Sorted by Bill Amount (Highest to Lowest):")
    sorted_orders = sorted(processed_orders, key=lambda x: x["bill_amount"], reverse=True)
    for so in sorted_orders:
        print(f"   ${so['bill_amount']:.2f} -> {so['customer_name']} ({so['quantity']}x {so['food_item']})")

if __name__ == "__main__":
    analyze_orders(orders)
