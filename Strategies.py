# Question Type Header = 🔲
# Difficulty: Easy = 🟢, Medium = 🟠, Hard = 🔴

# 🔲 --- Arrays & Hashing ---

# - Contains Duplicate - 🟢
# Set Soln:
        # create set from nums, if length is different, there's a duplicate
        # otherwise, not a duplicate, return False
# HashSet Soln:
        # create hashSet to save nums, 
        # iterate through nums, check if in hashSet, if so: return True
        # if not: add it to hashSet,
        # once reach end of nums, return False

# - Valid Anagram - 🟢
# HashSet Soln:
        # create hashset, with letter: num uses
        # iterate through s1, adding letter: num uses
        # iterate through s2, decrementing letter: num uses
        # if letter not in hashset, return False
        # iterate through hashSet.values, if all not == 0, return False
# HashSet Soln 2:
        # first check lengths are same
        # create 2 hashSets for letter counts
        # iterate through len(s), adding letters: count using get(letter,0)
        # return comparson hashSet1 == hashSet2

# - Two Sum - 🟢
# HashMap Soln:
        # create hashMap with value: index, to hold values already seen
        # iterate through nums list, 
        # check if corresponding num (target - num) already in hashMap
        # if so: return current index, & index of corresponding num
        # if not: add current num: index to hashMap & move on

# - Group Anagrams - 🟠
# HashMap Soln:
        # use a collections.defaultdict([list]) to create default list when key not found
        # dict holds tuple(letter_count): [string, string, ...]
        # iterate through strings, set up letter count array
        # iterate through char in string, update letter count using ord('char')
        # append to dict 
        # return dict.values, list of lists

# - Top K Frequent Elements - 🟠
# HashMap Soln:
        # create count hashMap, for holding num: frequency
        # & frequency array<list> for sorting frequencies
        # iterate through nums, counting nums into count 
        # iterate through count, adding into correct frequency box
        # create result array,
        # iterate backwards through frequency list, adding into result
        # until reaches k results, return result

# - Product of Array Except Self - 🟠
# Array Soln:
        # create result array, len of nums, with all 1's
        # set prefix var = 1 & postfix var = 1
        # iterate through nums, setting result[i] = prod of all prev nums
        # iterate backwards through nums, 
        #       setting result[i] = result[i] * postfix
        #       update postfix *= nums[i]
        # return the result arr

# - Valid Sudoku - 🟠
# HashMap Soln:
        # create col, row, & square, hashMaps 
        # use collections.defaultdict, eg: row #: set of nums in row
        # iterate through row & iterate through col
        # if empty space, skip
        # otherwise check if already in row, col, & square: if so: return False
        # otherwise: add it to the row, col, & square
        # reach end without dups found: return True

# - Encode & Decode Strings - 🟠
# Array Soln:
        # create one string to hold all strings, with separators & lengths
        # encode: loop through srings, adding str length + a separator(#) + str
        # decode: create result array to hold strings, i to hold length
        # iterate through combined string,
        # get length from string (up to separator), skip sep
        # get the string using curr_position + length
        # append it to result array & repeat
        # return result array

# - Longest Consecutive Sequence - 🟠
# Set Soln:
        # create a set to hold all nums without dups & lookup quickly
        # create var to hold longest_seq found so far
        # iterate through nums: if (num - 1) is not in set, 
        # then it's the start of a sequence, of at least length 1
        # check length of the sequence using num + len 
        # save length if it's new max
        # @ end, return longest_seq



# 🔲 --- Two Pointers ---

# - Valid Palindrome - 🟢
# 2 Pointer soln:
        # 2 pointers: left = 0, right @ end
        # move pointers towards each other until they meet/pass
        # move each on if not alphaNum()
        # then compare letter.lower() @ each step
        # return True if pointers meet/pass
# Easy Soln:
        # make new string with only valid, lowercase letters, 
        # compare it to its reversed slice string[::-1]



# 🔲 --- Sliding Window ---
        # Ask: Move window (fixed or dynamic size), 
        # each time asking, Is this the best I can do?
        # Expand window right as much as poss, when can't anymore
        # shrink from left until valid, then expand from right again

# - Best Time to Buy & Sell Stock - 🟢
# Sliding Window Soln:
        # create 2 pointers to indexes: left = 0 & right = 1,
        # left will be updated to new min whenever it's found
        # create max_profit var to hold max profit found so far
        # while r < len(prices), iterate r through prices list
        # update max profit, with prices[r] - prices[l]
        # check if r pointer found a new min, update l if so
        # move r through list
        # return max_profit

# - Longest SubString Without Repeating Characters - 🟠
# Sliding Window Soln:
        # create set to keep track of letters in substring
        # create result var for tracking longest length
        # 2 pointers for sliding substring, l & r
        # iterate through s, using r,
        # if s[r] is a duplicate (in the set):
        # remove s[l] from set until removed dup
        # then add s[r] to the set & update result with max len
        # return result

# - Longest Repeating Character Replacement - 🟠
# Sliding Window Soln:
        # create letter count hashMap
        # create result var to keep track of longest substring found
        # create sliding window, l & r = 0
        # update letter count with letter at s[r]
        # check whether window is valid with:
        # calc window length - most freq char = replacements needed > k
        # while not: move l on and remove s[l] from count
        # if so: update result to max window length
        # return result

# - Permutation in String - 🟠
# Sliding Window of Fixed Size Soln:
        # same chars from s1 in same length window of s2
        # create hashMap of letter counts from s1, won't change
        # create hashMap of letter counts from s2[window], will update as shifts down
        # l = 0, r = range(len(s1), len(s2))
        # while window shifts down (as r moves(and l incremented as well))
        # compare the hashmaps first: return True if match
        # remove l element from hashmap, add r element to hashmap
        # compare one last time, & return False



# 🔲 --- Stack ---

# - Valid Parentheses - 🟢
# Stack & HashMap soln:
        # use a stack (just an array, append & pop) to hold history of open parens
        # use hashMap to define close paren match to open paren
        # iterate through s, appending any open parens to stack
        # when reach close paren, pop off top of stack, & make sure it matches
        # ensure the stack is not empty before trying pop
        # if they don't match: return False, otherwise, move on
        # @ end of string, return whether stack is empty

# - Min Stack - 🟠
# Stack Soln:
        # implement stack with an array
        # for tracking min in O(1) time, implement a 2nd stack tracking min @ each point
        # push & pop to min stack along with actual stack, always know min @ curr point
        # with each push, compare top of min_stack with val & save min()

# - Evaluate Reverse Polish Notation - 🟠
# Stack Soln:
        # implement stack with an array
        # iterate through tokens:
        # conditionally: 5 checks, whether curr_tok == +, -, *, /, else num
        # if +: pop top 2 nums, add them, append result
        # if -: pop top 2 nums (a, b), subtract b-a, append result
        # if *: pop top 2 nums, mult them, append result
        # if /: pop top 2 nums (a, b), divide b/a, round down using int(), append result
        # else: (if num) append the int
        # return only remaining elem in stack

# - Generate Parentheses - 🟠
# Stack Soln:
        # rule 1: only add open p. if open_count < n
        # rule 2: only add closing p. if close_count < open_count
        # done when: open_count == close_count == n
        # create a stack [] to add parens to build up solutions
        # create a result array to hold found solutions
        # define recursive func, take in open_count & close_count
        # check if valid combo, if so, add to result & return out
        # if open_c < n: add ( to stack, call recursive func with open_count++
        # if close_c < open_c: add ) to stack, call recur_func with close_count++
        # start recursive call with 0,0
        # return result

# - Daily Temperatures - 🟠
# Stack Soln:
        # create a result array, same len as temps, all 0s
        # create a stack, to hold arrays with: [temp, index]
        # iterate through temps, comparare to temp on top of stack
        # if temp greater than top: pop, save index diff (curr-stack) to result,
        # then add current [temp, index] to top of stack, move on
        # if less, also add [t, i] to top of stack, move on
        # when get to end, return result array

# - Car Fleet - 🟠
# Stack Soln:
        # create stack to hold car fleets
        # create array of cars, each w/ their [pos, speed]
        # sort array of cars by their position, in reverse order (start <- dest)
        # iterate through cars, calc time it takes for car to reach dest = (targ-p)/s
        # add to stack, if more than 2 cars in stack, compare them
        # if new car (top of stack) faster than car below it, pop top (will be 1 fleet)
        # return length of the stack, # of car fleets



# 🔲 --- Binary Search ---

# - Binary Search - 🟢
        # two pointers (L=0, R=end)
        # continue while L <= R, calc middle (L+R//2)
        # if nums[middle] less than target: move L up to middle+1
        # if nums[middle] greater than target: move R back to middle-1
        # else: return nums[middle] because found target
        # reach end looking through? return -1, did not find target

# - Search a 2D Matrix - 🟠
        # calc total_#_of_elems in matrix, and convert that to matrix row & col
        # then binary search total_elems, using that conversion
        # row = middle // row_len, col = middle % row_len

# - Koko Eating Bananas - 🟠
        # min rate would be k=1 per hour, max rate would be k=max(elem in piles) 
        # need to find min k that satisfies time constraint in range [1...max_p]
        # use binary search to check elems in that range
        # binary search template:
        # two pointers: L = 1, R = max(piles)
        # while L less than R
        # calc Middle = (L+R//2
        # check if Middle is feasible
        # if yes: move R back to mid
        # if not: move L up to mid+1
        # return L

# - Search Rotated Sorted Array - 🟠
# Binary Search soln:
        # two pointers (L=0, R=end)
        # continue while L <= R, calc middle (L+R//2)
        # check if middle num == target
        # check if in left-sorted section, with nums[l] <= nums[mid] eg: [4,-L-,7,0,-R-,3]
        #  check if result on right side of mid, with t > nums[mid] or t < nums[l], move l pointer up
        #  otherwise result on left side of mid, move r pointer down
        # otherwise in right-sorted section, eg: [4,-L-,7,0,-R-,3]
        #  check if result on left side of mid, with t < nums[mid] or t > nums[l], move r pointer down
        #  otherwise result on right side of mid, move l pointer up

# - Find Minimum in Rotated Sorted Array - 🟠
# Binary Search soln:
        # two pointers (L=0, R=end)
        # create result var to hold temp_found_min
        # continue while L <= R, calc middle (L+R//2)
        # check if case section is sorted, if so, set result to min(result, nums[L]) & break
        # otherwise, compare M elem to L elem, 
        #   if M elem is smaller: on L side, move R to M - 1
        #   if larger: on R side, move L to M + 1
        # return result

# - Time Based Key-Value Store - 🟠
# Binary Search soln:
        # Data Struct to hold data: HashMap with key: array of [timestamp, val]
        # set method -
        # if key not already added, add key: []
        # append [timestamp, val] to HashMap[key]
        # get method - 
        # create res var, & get array of matching values
        # binary search it for timestamp match or closest time less than timestamp
        # two pointers (L=0, R=end)
        # continue while L <= R, calc middle (L+R//2)
        # check if middle time <= timestamp: 
        #  if so: update result & check to Right for a closer time
        #  if not: middle time is too large, check to the Left for a valid time
        # return result



# 🔲 --- Linked List ---

# - Reverse Linked List - 🟢
# Iterative soln
        # 2 pointers (prev=None, curr=head), iterate through curr until end
        # hold next node in temp var,
        # change curr.next to point back to prev,
        # move prev up to curr & curr up to saved next
# Recursive soln
        # BC - if head is Null, return None
        # hold newHead, iterate through recursively call on ll.next
        # on way back, reverse link: head.next.next = head & head.next = None
        # return newHead, the built up ll from beginning

# - Reverse Linked List - 🟢
# Iterative Soln:
        # dummy node to start new_list, 
        # while elems in both, compare elems, add lesser to new_list
        # if elems in only one list, add the rest of it
        # return new_list, dummy.next

# - Reorder List - 🟠
# Tortice & Hare soln:  
        # iterate a slow & fast pointer through LL to find the middle
        # split the lists in half, with slow.next being start of second half list & end first list with = None 
        # reverse second half of LL using prev = None & temp
        # iterate through both lists, interlacing second half elems inbetween first half elems

# - Remove Nth Node from End of List - 🟠
# O(2n) Soln:
        # get length of LL using a while loop to iterate through until end
        # create dummy node to hold front of LL
        # calc node_to_remove by length - n
        # iterate through node_to_remove times, to get to node just before node_to_remove
        # remove it by updating next ptr
        # return dummy.next
# 2 pointer Soln: 
        # create dummy node
        # 2 ptrs, L @ dummy, R @ head + n 
        # iterate through until R reaches end of LL,
        # then L will be just before node to remove, remove it, & return dummy.next

# - Copy List with Random Pointer - 🟠
# 2 pass soln w/ HashMap: 
        # create HashMap to map old nodes to new nodes, also None: None
        # 1st pass: move through old LL, making new node with just same val
        #  add old Node: new Node in HashMap
        # 2nd pass: move through old LL again, 
        #  updating both pointers (next & random), using map to get matching new nodes
        # return new head

# - Add Two Numbers - 🟠
        # create dummy node to point to start of our answer LL
        # create a carry var, starting @ 0
        # continue while l1, l2, & carry
        # get vals from each ll, if not use 0
        # calc answer_val = v1 + v2 + carry
        # update carry with int division by 10
        # update answer_val with mod by 10
        # save answer_val into answer LL
        # update pointers to move on LLs
        # return head of our answer LL

# - Linked List Cycle - 🟢
# BF Soln:
        # make hashSet to hold nodes
        # go through LL, check if currNode in the hashSet, 
        # if not add it to hashSet and move to next
        # once reach null -> False 
        # or find match in HashSet -> True
# Tortoice & Hare Soln:
        # 2 pointers (slow+1, fast+2), both start at beginning
        # go though LL, incrementing slow by 1 & fast by 2,
        # if fast ever meets slow, return True, there's a cycle
        # otherwise, if fast reaches None, return False

# - Find the Duplicate Number - 🟠
        # With only using constant extra space (with linear space use a Hashmap)
        # imagine the array values are LL pointers, the duplicate num will create a cycle
        # create a slow & fast pointer, when they meet, found cycle, use Floyds Algo to find dup
        # leave slow ptr where it is, discard fast, create a slow2 ptw @ the begining,
        # move slow & slow2 through +1 until they meet, that's the dup

# - LRU Cache - 🟠
        # setup a cache to map keys to nodes
        # setup doubly LL with nodes to keep track of LRU=left & MostRecentlyUsed=right
        # helper functions: remove node & insert node @ right (MRU)
        # get: check if key exists: if so return val & update node to MRU (del & insert)
        #  else: return -1
        # put: check if key exists, if so remove it before adding new val
        #  insert new key & new node into LL
        #  check if exceeds capacity: if so: remove LRU (left) by removing node from LL & deleting from cache



# 🔲 --- Trees ---

# - Invert Binary Tree - 🟢
# Recursive Soln:
        # dfs, recursively swapping left & right 
        # BC: if reach None: return None
        # swap root's left & right nodes
        # recurse on left side, then right side, then return root

# - Max Depth of Binary Tree - 🟢
# Recursive DFS:
        # BC: if reach None node: return 0 depth
        # otherwise, return max of left & right subtrees, + 1 (for curr node)
# Iterative BFS
        # BC: if reach None node: return 0 depth level
        # set depth = 0, create deque to help with dfs
        # while elems in deque, loop through elems & add any child nodes
        # increment depth level, once no elems in deque, return depth
# Iterative DFS (pre-order)
        # BC: if reach None node: return 0 depth level
        # create stack to hold node & depth, also keep result var for depth
        # while elems on stack, pop them off, update result with max
        # append left & right nodes, with depth + 1
        # return result

# - Diameter of a Binary Tree - 🟢
# Recursive Soln:
        # create global diam_result to keep track of max diameter
        # create dfs() func, passing in a node to explore
        # BC: if null node, return height of -1
        # find height of root.left & root.right
        # find diameter @ current node, (2 + l_height + r_height)
        # update diam_result if it's greater
        # returns max height of left & right subtrees (1 + max(l, r))
        # call dfs with root & then return max_diameter

# - Balanced Binary Tree - 🟢
# Recursive Soln:
        # Traverse all the way down, dfs, checking if_balanced from bottom up
        # return [balanced bool, height of each node] up to the parent
        # create dfs(root) func,
        # BC: if null node, return [True bool, 0 height]
        # call dfs on left & right subtrees of root
        # check if subtrees are balanced with abs & each bool
        # return [balanced bool, 1 + max(l & r heights)]
        # return dfs(root) bool

# - Same Tree - 🟢
# Recursive Soln:
        # BCs - check both root nodes
        #  first check if both nodes don't exist: return True
        #  check if one exists & other doesn't: return False
        #  check if values aren't equal: return False
        # Recurse - recurse on L & R subtrees
        #  returning the "and" of the returns from L & R subtrees

# - Subtree of Another Tree - 🟢
# Recursive Soln:
        # create a helper func to compare whether sameTree
        #  BC: compare root nodes
        #   if both Null: return True
        #   if one Null & one not Null: return False
        #   if values are different: return False
        #  Recurse on left & right, return True if both return True, else False
        # BC: if subRoot is Null: return True
        #  if root is Null: return False
        # call sameTree with root & subRoot, if True: return True
        # recurse with root.left & subRoot and root.right & subRoot, return True if either returns True

# - Lowest Common Ancestor of a Binary Search Tree - 🟢
# Recursive Soln:
        # use that root is common ancestor of all nodes in BST, start there
        # the LCA is where p & q split into L & R subtrees (smaller & larger than curr)
        # start curr pointing to root node
        # loop: 
        #  moving curr left if both p & q are > curr
        #  moving curr right if both p & q are < curr
        #  else: return curr, have found split



# 🔲 --- Heap / Priority Queue ---

# - Kth Largest Element in a Stream - 🟢
# MinHeap Soln:
        # __init__()
        # create a minHeap, to hold only k largest integers (kth @ top)
        # add all nums to heap, then pop min until heap len == k
        # add()
        # push val to heap, if push causes heap to be len > k, remove min
        # then return the min elem (which is the kth element)

# - Last Stone Weight - 🟢
# MaxHeap Soln:
        # create a maxHeap from stones (in Python, use minHeap with neg vals)
        # while 2+ stones in heap, pop off top 2 heaviest stones, smash them calc 
        # if there's a resulting stone, add end_stone back into heap
        # when 1 or 0 stones left, return that stone



# 🔲 --- Backtracking - make Decisions ---

# - Subsets - 🟠
# Backtracking Soln:
        # create result array to hold each found subset
        # create subset array
        # create dfs func to call with index
        # basically iterate through nums array until i >= len(nums)
        # append copy of subset to result
        # recursively call dfs with 2 decisions:
        # decision TO add nums[i] 
        # decision NOT TO add nums[i]
        # return result array

# - Combination Sum - 🟠
# Backtracking Soln:
        # Decision: add element or not
        # create result array to hold each found combination
        # create dfs func to call with (index, curr_combo, curr_total)
        # BC1: reach solution - append copy of curr to result
        # BC2: curr pass target or reach end of list: exit
        # Decision: Add num, & recursively call dfs
        # Decision: Don't add num, & recursively call dfs
        # return result array
















