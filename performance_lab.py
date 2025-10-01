# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    most_frequent = 0
    input_list = numbers

    if not numbers: #checks if the list is empty
        return("List is empty")
    else:
        for item in input_list: #loops through list
            appearances = input_list.count(item) #counts the item in the list

            if appearances > most_frequent: #highest count item is most_frequent
                most_frequent = appearances
                highest_num_app = item
        return(highest_num_app)

#Tests and Edge Cases:
print(most_frequent([1, 3, 2, 3, 4, 1, 3])) #checks that code works for example
print(most_frequent([1, 2, 3, 4, 1, 3])) #checks that code works with multiple numbers with same number of appearance
print(most_frequent([])) #checks that code doesn't break from an empty list

"""
Time and Space Analysis for problem 1:
- Best-case: 
    O(1) List is empty, code ends at first if statement.
- Worst-case: 
    O(n^2) List is looped through and checked. Worst and average case are the same due to the fact that the entire list must be looped through.
    The code is O(n^2) due to being in a for loop, and the inclusion of .count()
- Average-case: 
    O(n^2) List is looped through and checked.
- Space complexity: 
    O(1) Code does not create a new data structure, so it is O(1)
- Why this approach?
    I chose this approach since it was the most simple one available to loop through the list. Since we just needed any of the numbers with the    
    most appearances, .count worked fine.
- Could it be optimized?
    I do not believe this code can be optimized any farther, since a loop, and checking the item in that loop with always be necessary.
    If it could be optimized a trade off would be the code's siimplicity.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    input_list = nums
    no_dupes_in_order = []

    if not input_list: #checks if the list is empty
        return("List is empty")
    else:
        for item in input_list: #loops through lists
            if item not in no_dupes_in_order: #Checks for item in list, if it isn't there it is added with .append()
                no_dupes_in_order.append(item) 
        return(no_dupes_in_order)

#Tests and Edge Cases:
print(remove_duplicates([4, 5, 4, 6, 5, 7])) #checks that code works using example
print(remove_duplicates([])) #checks that list with nothing in it doesn't break code

"""
Time and Space Analysis for problem 2:
- Best-case:
    O(1) List is empty, code ends at first if statement.
- Worst-case:
    O(n^2) Code loops through for loop, and "not in" also checks through list for items.
- Average-case:
    O(n^2) Same reasoning, code loops through for loop, and "not in" also checks through list for items.
- Space complexity:
    O(n) This code creates another list, so the space complexity is O(n)
- Why this approach?
    I chose this approach because it allowed for me to loop through a list, remove the duplicates and keep the items in order. 
    If I used a set for example, the items would not have stayed ordered.
- Could it be optimized?
    This code could probably be optimized by changing the "not in". The tradeoff in this case is that you would most likely need another data structure.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):

    final_list = []

    if not nums: #checks if the list is empty
        return("List is empty")
    else:
        for item1 in nums:#loops through num
            current_num = item1
            for item2 in nums: #holds onto item 1 and loops through list again adding and comparing to target
                current_second_num = item2
                if current_num + current_second_num == target:
                    final_list.append((current_num,current_second_num))#if nums add to target it is added to final_list
                
        return(final_list)

#Tests and Edge Cases:
print(find_pairs([1, 2, 3, 4], target=5))
print(find_pairs([], target=5)) #check that code works with empty list

"""
Time and Space Analysis for problem 3:
- Best-case:
    O(1) List is empty, code ends at first if statement.
- Worst-case:
    O(n^2) Worst and average cases are the same, 2 for loops need to be used to check every item to the list and if they add to the target.
- Average-case:
    O(n^2) Same logic as worst case.
- Space complexity:
    O(n) The code creates a list, so the complexity is O(n)
- Why this approach?
    I chose this approach because it is simple and does exactly what you need it to do. The loops add the items together and then compare it to the
    target without any problems.
- Could it be optimized?
    Theoretically this code could be optimized in some way, most likely involving removing the second loop. A trade off in this case would be an
    increase in complexity.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):

    initial_capacity = 6
    main_list = []
    current_capacity = initial_capacity

    for num in range(n): #loops for evey number up to n
        if len(main_list) == current_capacity:  #checks if length hits capacity
            updated_capacity = current_capacity * 2 #doubles capacity
            print(f"Capacity {current_capacity} -> {updated_capacity}")
            current_capacity = updated_capacity
            new_list = [] #simulates new list being made
            for x in main_list:
                new_list.append(x) #adds to new list
            main_list  = new_list
        
        main_list.append(num) #adds num to main_list
        print(f"Added {num}")

#Tests and Edge Cases:
add_n_items(10)
add_n_items(14) #Checks that code works when doubling capacity for a second time.

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
    Resizes happen when a list runs out of space in python.
- What is the worst-case for a single append?
    The worst case for a single append is O(n), when the list need to be copied after running out of space.
- What is the amortized time per append overall?
    The amortized time per append is O(1) on average, occasionally being O(n)
- Space complexity: 
    O(n) This code creates another list so the complexity is O(n)
- Why does doubling reduce the cost overall?
    Doubling reduces the cost because of the fact that you are gaining exponentially more space in the list, reducing the workload python need to do.

"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):

    totals = []
    sum = 0

    if not nums: #checks if the list is empty
        return("List is empty")
    else:
        for num in nums:
            sum = sum + num #adds item to the current sum, aka last item in the new list
            totals.append(sum)
        return(totals)

#Tests and Edge Cases:
print(running_total([1, 2, 3, 4.4])) #Test floats
print(running_total([1, 2, 3, -4])) #Tests negative numbers
print(running_total([])) #Tests empty lists


"""
Time and Space Analysis for problem 5:
- Best-case:
    O(1) List is empty, code ends at first if statement.
- Worst-case:
    O(n) Worst case and average are the same, entire list is looped through with for loop to add totals together.
- Average-case:
    O(n) Same logic as worst case with for loop.
- Space complexity:
    O(n) This code has a space complexity of O(n) since it creates a list and uses one loop.
- Why this approach?
    I chose this approach because it is very simple, and can handle most input. any type of number can be added and they will be properly added together
    and put into a results list to be printed out.
- Could it be optimized?
    I don't think this code has any room to be optimized. The actual code to perform what is required only takes up O(n), which is going to be 
    required no matter what you do, since you need to loop through the whole thing to add items together.


    I chose to refactor this code. The best-case was the same, while the worst-case and average case where brought down to O(n) from O(n^2).
    I optimized the code by putting the solutions directly into a new list, and then using a single for loop to add each item to the last using
    each's index.


"""
