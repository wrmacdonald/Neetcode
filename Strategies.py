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

...




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
        # create global result to keep track of max diameter
        # create dfs() func that updates max diameter &
        # returns max height of left & right subtrees
        # call dfs with root & then return max_diameter



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














