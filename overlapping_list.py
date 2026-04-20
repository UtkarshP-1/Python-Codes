# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise

def overlapping(l1: list, l2: list) -> bool:
    if set(l1) & set(l2):
        return True
    else:
        return False

list1 = [10,20,30,40,50]
list2 = [50,60,70,80,90]
list3 = [0]

print(overlapping(list1, list2))
print(overlapping(list2, list3))
