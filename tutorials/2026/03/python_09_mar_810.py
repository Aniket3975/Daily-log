import random

def calculate_cost(item):
    # Assign a random cost to each item
    return random.randint(1, 10)

def schedule_interval(items, budget):
    # Sort items by cost in descending order
    items.sort(key=calculate_cost, reverse=True)
    
    # Initialize variables to track total cost and schedule
    total_cost = 0
    schedule = []
    
    # Iterate over sorted items
    for item in items:
        # Check if item fits within budget
        if total_cost + calculate_cost(item) <= budget:
            # Add item to schedule
            schedule.append(item)
            # Update total cost
            total_cost += calculate_cost(item)
    
    # Return schedule
    return schedule

# Generate random items
items = [i for i in range(1, 21)]

# Set budget
budget = 50

# Schedule interval
schedule = schedule_interval(items, budget)

# Print schedule
print("Scheduled interval:", schedule)

# Print total cost
print("Total cost:", sum(calculate_cost(item) for item in schedule))

# Print cost of each item in schedule
print("Cost of each item in schedule:")
for item in schedule:
    print("Item:", item, "Cost:", calculate_cost(item))