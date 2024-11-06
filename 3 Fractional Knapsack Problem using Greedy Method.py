class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    # Calculate value to weight ratio for each item and sort them in descending order
    items.sort(key=lambda item: item.value/item.weight, reverse=True)
    
    total_value = 0.0
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            # If the item can be fully taken, take it
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item cannot be fully taken, take the fractional part
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value

def main():
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        value = float(input(f"Enter value of item {i + 1}: "))
        weight = float(input(f"Enter weight of item {i + 1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))

    max_value = fractional_knapsack(items, capacity)
    print(f"The maximum value of items that can be carried: {max_value}")

if __name__ == "__main__":
    main()
