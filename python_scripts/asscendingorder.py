demo_list= [ 12, 3,6, 4, 19, 16, 13]

def sort_list_ascending(demo_list):
    return sorted(demo_list)
def sort_list_descending(demo_list):
    return sorted(demo_list, reverse=True)

def get_even_numbers(demo_list):
    even_numbers =[]
    for num in demo_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

ascend_list=sort_list_ascending(demo_list)
descend_list=sort_list_descending(demo_list)
sum_list= sum(demo_list)
even_list= get_even_numbers(demo_list)
print("Original list:\n\n", demo_list)
print("-" * 50)
print("List in ascending order:\n\n", ascend_list)
print("-" * 50)
print("List in descending order:\n\n", descend_list)
print("-" * 50)
print("Sum of the list is:\n\n", sum_list)
print("-" * 50)
print("Even numbers from the lists are: \n\n", even_list)


