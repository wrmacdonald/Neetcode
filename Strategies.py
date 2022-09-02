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
















