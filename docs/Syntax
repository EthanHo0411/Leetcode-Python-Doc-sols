set():
Unordered
Can be used for O(1) access to check entry existence 

Dict:
Use .get(x, 0) to get value for key x and default value 0
list(dict.values() ) for the value array, but the dict object can be used for checks and printing
.keys() for the key array 
.items() would produce the dict object with (key, value)

Lambda + map 


max(freq, key=freq.get) # 'b' (because freq['b'] = 7)
number = min(2, 3, key=lambda x: 4 - x)



Map function:
map(int, array) this would apply the function to individual element in the array and then return a map object 
Use list() to convert into a list

String methods:
char.isalnum() watch out for the negative sign in negative numbers
X = “ ”.join(<list or sorted()>) , the symbol inside the double quote is the separator between elements after they are joined
.split(“<separator>”) would separate the string into a list with the given separator

Condition comparison:
Remember to check for (if i >0) before doing checks on the element before such as nums[i] == nums[i-1]

List comprehension:
X = [ <item to be placed>  for sth in collections <filtering conditions>] 

Array methods:
array.index(0) returns the element of array at index 0
.append() add to the rightmost
.insert(i, item) insert item at index i in the array , takes O(n) time as shifting is needed

Deque:
from  collections import deque
Stack = deque(<some list>)
.popleft()
.appendleft() O(1) time
.pop()
dq.rotate(2) shift the array to the right by 2 places
dq = deque(maxlen=3) act as a buffer,when the fourth element is added, the leftmost is removed
.extend(<some list>) to extend the current array 

zip():
zip(list1, list2) produce list1[i] and list2[i] iterable  
list(zip(list1,list2)) to produce a tuple list

.sort():
.sort(key = lambda x : x[0] , reverse = True) means to sort by the first element of the 2D array or tuple , then sort by descending order

sorted():
Returns a new sorted list object
E.g. “”.join(sorted(somestring))

Binary search: O(nlogn) time
1.Use left and right pointer to shrink the  search space by half each time
2.use left+((right-left)//2) instead of (left+right)//2 to avoid overflow
l<=r : when considering both endpoints and when trying to find an exact number
l<r: when trying to find the min or max of an interval that satisfy the condition
e
L = mid , r = mid : use to find a value that first satisfy a condition or a value that last doesnt satisfy a condition. Used to find boundaries. Not used when trying find an exact match in the list. 
*Have to use a variable keep track of the latest result if we unsure if it exists and wish to find the number next to it 

Bucket Sort: O(n) time
Initialise a bucket list with n buckets (n is the length of the number list)
Create a hashmap and store the frequency of each item in there
Now append the items into the buckets according to their frequency
The buckets are in ascending order

LinkedList:
head : the start of the linked list , rmb to check if head is none and use a dummy head
Hare and tortoise cycle detection algo: hare = head.next.next while tortoise is head.next , if a cycle exist then the hare would eventually come to the same node as the tortoise
Reverse linked list: 
Find middle of a linkedlist: use hare and tortoise algo with hare = head.next and tortoise = head, by the time the hare becomes None , the tortoise would be at the last item of the first half

Replace the max variable : var = max(var, value)

Max:
max(dict, key = dict.get) to find the key with highest value
max(dict, key = lambda k : f[k])



R-l+1 : means the number of elements including the two indexes
r-l : means the number of elements excluding the lower end
R-l-1: means only the number of elements between the two indexes 

Tree:
Inorder traversal: (left, root, right)
Preorder traversal: ( root, left ,right)
Level order traversal ( layer by layer)



Heap: a type of binary tree where parent node is smaller than its child nodes ( min heap)
and the minimum value node is always at the root

Heapq : module used for heap queue (priority queue)
heapq.heapify (List) , this will make this into a binary heap
heapq.heappush(heap, item) push an item onto the heap while maintaining the property
heapq.heappop() pop and return the smallest item from the heap
heapq.nlargest(n, iterable) : return the n largest item from an iterable like list,The returned list is sorted in descending order (largest to smallest)
heapq.nsmallest(n, iterable):return the n smallest item from an iterable like list,The returned list is sorted in ascending order (smallest to largest)
Heap[0]: after heapify , this would return the smallest item , but wont pop it

Implement max heap
import heapq # Since heapq implements a min heap, we can negate the values # to get a max heap behavior 
def add_to_max_heap(heap, item): # Insert negative value to simulate max heap heapq.heappush(heap, -item) 
def get_max(heap): # Return the actual value by negating it back return -heap[0] if heap else None 
def extract_max(heap): # Extract and return the max value return -heapq.heappop(heap) if heap else None


Use case for n smallest:

import heapq

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 20}
]

# Get the 2 youngest people based on age
youngest_two = heapq.nsmallest(2, people, key=lambda x: x['age'])
print(youngest_two)  
# Output: [{'name': 'David', 'age': 20}, {'name': 'Bob', 'age': 25}]




DP: best tiem to sell and buy




Backtracking: a form of dfs where you explore the option , then remove the changes and explore the other option . For example try some path, then pop the doings to try for another way


