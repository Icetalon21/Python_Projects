#integer_list.py
import random
import math
from collections import deque
ten_random = random.sample(range(0,100), 10)
#integer_list = list()
print("Random Integers: ", ten_random)

#Swap the first and last elements in a list
def swap():
    ten_random_swap = ten_random.copy()
    swap_first_and_last = ten_random_swap[-1], ten_random_swap[0]
    ten_random_swap[0], ten_random_swap[-1] = swap_first_and_last
    print("Swapping the first and last elements: ", ten_random_swap)
swap()

#Shift all elements by one to the right and move the last element into the first position [rotate operation]; for example, 1 4 9 16 25 would become 25 1 4 9 16
def shift():
    shift_list = deque(ten_random)
    shift_list.rotate(1)
    #shift_elements = ten_random[-1] + ten_random[:-1]
    print("Shifting elements to the right", list(shift_list))
shift()

#Replace all even elements with a zero
def replace_evens():
    replace_all_evens = ten_random.copy()
    #for individual_number in replace_all_evens
        #if 
    print("Replace evens with 0's: ", [x if x % 2 != 0 else 0 for x in replace_all_evens])
replace_evens()

print("Original Test: ", ten_random)
#Replace each element except the first and last by the larger of its two neighbors
# [1, 3, 4, 6, 9]
#def replace_by_largest
def replace_by_largest():
    l = ten_random.copy()
    for i in range(1, len(l)-1):
        #curr = ten_random[i]

        left = ten_random[i-1]
        right = ten_random[i+1]
        if left>right:
            l[i] = left
        else:
            l[i] = right
    
    print("Replace by larger of two neighbors: ", l)
replace_by_largest()

    

#Remove the middle element if the list length is odd, or the middle two elements if the list length is even
def find_length():
    length = len(ten_random)
    print("List length: ", length)
find_length()

def remove_middle():
    if len(ten_random) % 2 == 0:
        remove_from_ten_random = ten_random.copy()
        # remove1 = remove_from_ten_random.pop((len(remove_from_ten_random)//2)+0)
        # remove2 = remove_from_ten_random.pop((len(remove_from_ten_random)//2)-0)
        remove1 = math.floor(len(remove_from_ten_random)//2)-1
        remove2 = math.floor(len(remove_from_ten_random)//2)+ 1
        del remove_from_ten_random[remove1:remove2]
        print("Removed Items:", remove1, remove2)
    print("New list with removed: ", remove_from_ten_random)
remove_middle()

#Move all even elements to the front, otherwise preserving the order of the elements
# [1, 2, 4, 5, 6, 8]
# [2, 4, 6, 8, 1, 5]
def move_evens():
    #move_even_to_front = ten_random.copy()
    evens = []
    for i in ten_random:
        if i % 2 == 0:
            evens.append(i)
    for i in ten_random:
        if i % 2 == 1:
            evens.append(i)
    print('Moving evens to the front: ', evens)
    #for i in move_even_to_front:
        #if i % 2 == 0:
            #evens.append(i)
        #return evens
    #evens = list([x for x in move_even_to_front if x % 2 == 0])
    #move = move_even_to_front.insert(0, move_even_to_front.pop(move_even_to_front.index(evens)))
    #print("Evens: ", move_evens)
    
move_evens()

#Return the second-largest element of the list
def second_largest():
    length = len(ten_random)
    ten_random.sort()
    print("Second largest element is: ", ten_random[length-2])
second_largest()
    
#Return true if the list is currently sorted in increasing order
def increasing_order_sort():
    if ten_random.sort == ten_random:
        print("List is sorted in increasing order")
    else:
        print("True. List is not sorted in increasing order")
increasing_order_sort()

#Return true if the list contains two adjacent duplicate elements
def remove_adjacent():
    i = 1
    while i < len(ten_random):
        if ten_random[i] == ten_random[i-1]:
            ten_random.pop(i)
            i -= 1
        i += 1
    return "True"
print(remove_adjacent())
remove_adjacent()

#Return true if the list contains any duplicate elements; this time they need not be adjacent
def has_duplicates():
    if len(set(ten_random)) == len(ten_random): 
        print("False. No duplicates")
    else:
        print("True. Has duplicates: ")
has_duplicates()


