#!/usr/bin/env python
# coding: utf-8

# Q.1 Can you explain the logic and working of the Tower of Hanoi algorithm by writing a Python program?
# How does the recursion work, and how are the movements of disks between rods accomplished?

# In[1]:


def tower_of_hanoi(n,source,target,auxiliary):
    if n==0:
        return 
    tower_of_hanoi(n-1,source,auxiliary,target)
    print(f"Move disk from {n} from {source} to {target}")
    tower_of_hanoi(n-1,auxiliary,target,source)
tower_of_hanoi(3,"A","C","B")


# In[ ]:





# Q.2 Given two strings word1 and word2, return the minimum number of operations required to convert word1
# to word2.

# In[2]:


def min_distance(word1, word2):
    return min_distance_helper(word1, word2, len(word1), len(word2))

def min_distance_helper(word1, word2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if word1[m - 1] == word2[n - 1]:
        return min_distance_helper(word1, word2, m - 1, n - 1)

    return 1 + min(
        min_distance_helper(word1, word2, m, n - 1), 
        min_distance_helper(word1, word2, m - 1, n),  
        min_distance_helper(word1, word2, m - 1, n - 1) 
    )

word1 = "horse"
word2 = "ros"
result = min_distance(word1, word2)
print(result)


# In[ ]:





# Q. 3 Print the max value of the array [ 13, 1, -3, 22, 5].

# In[3]:


#without using max function
def find_max_value(arr):
    if not arr:
        return None
    max_value=arr[0]
    for num in arr[1:]:
        if num>max_value:
            max_value=num
    return max_value
arr=[10,20,30,40,50,60,99]
print(find_max_value(arr))


# In[ ]:





# Q.4 Find the sum of the values of the array [92, 23, 15, -20, 10].

# In[4]:


def sum_of_array(arr):
    sum=0
    for num in arr:
        sum+=num
    return sum
print(sum_of_array([1,2,3,4,5,6,7,8,9]))


# In[ ]:





# Q.5 Given a number n. Print if it is an armstrong number or not.An armstrong number is a number if the sum
# of every digit in that number raised to the power of total digits in that number is equal to the number.

# In[1]:


def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    if armstrong_sum == n:
        return "Yes"
    else:
        return "No"

input_number = int(input("Enter a number: "))
result = is_armstrong_number(input_number)
print("Output:", result)


# In[ ]:




