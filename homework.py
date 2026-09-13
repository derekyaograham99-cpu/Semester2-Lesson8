import random


def count_occurrence(item, my_list):
    total = 0
    for i in my_list:
        if i == item:
            total += 1
    return total


grocery_item = ["apple", "banana", "broccoli", "milk", "bread"]
shopping_cart = []

for i in range(100):
    shopping_cart.append(random.choice(grocery_item))

print("Mom bought:")
print(str(count_occurrence("apple", shopping_cart)) + " apples")
print(str(count_occurrence("banana", shopping_cart)) + " bananas")
print(str(count_occurrence("broccoli", shopping_cart)) + " broccolis")
print(str(count_occurrence("milk", shopping_cart)) + " gallons of milk")
print(str(count_occurrence("bread", shopping_cart)) + " loaves of bread")

for i in reversed (range(len(shopping_cart))):
    if shopping_cart[i] == "banana":
        shopping_cart.pop(i)

print("After removing all bananas, mom bought:")
print(str(count_occurrence("apple", shopping_cart)) + " apples")
print(str(count_occurrence("banana", shopping_cart)) + " bananas")
print(str(count_occurrence("broccoli", shopping_cart)) + " broccolis")
print(str(count_occurrence("milk", shopping_cart)) + " gallons of milk")
print(str(count_occurrence("bread", shopping_cart)) + " loaves of bread")
