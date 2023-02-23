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

# - Squares of a Sorted Array - 🟢 - Quastor
# 2 Pointer Soln:
        # edge case: len is 1, just return arr with square of elem
        # create a list to hold squares
        # find separating point of sorted array, between neg & pos, make left/right index vars
        # while l & r haven't run off either end: compare abs val of nums[l & r] to find smaller num
        # append the square of it to square_list
        # once done with comparisons, add rest of whatever left in other list
        # return square_list
# 2 Pointer Soln_2:
        # start 2 pointers @ either end, & move inwards, comparing squares & adding largest
        # will build up square_list largest->smallest, reverse it & return 

# - Is Subsequence - 🟢
# ~2 Pointer Soln:
        # s_i pointer start @ beginning of s
        # short circuit an empty s string: return True
        # iterate through t, when find elem @ s_i: increment s_i
        #  when s_i reaches end of s, have found full subseq: return True
        # otherwise: return False 


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

# - Rotate List - 🟠 - Quastor
        # iterate through LL to get length
        # once reach end, link the last node to the head to create a cycle
        # find amount needed to rotate: len - (k % len)
        # iterate through that many times, hold next node as newHead, break cycle with newTail->None
        # return newHead



# 🔲 --- Trees ---

# - Invert Binary Tree - 🟢
# Recursive Soln:
        # DFS, recursively swapping left & right 
        # BC: if reach None: return None
        # swap root's left & right nodes
        # recurse on left side, then right side, then finished, so return root

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
        #  BC: if null node, return [True, 0 height]
        #  call dfs on left & right subtrees of root
        #  balanced bool = check if subtrees are balanced with abs height cals & all children balanced bools
        #  return [balanced bool, 1 + max(l & r heights)]
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

# - Lowest Common Ancestor of a Binary Search Tree - 🟠
# Recursive Soln:
        # use that root is common ancestor of all nodes in BST, start there
        # the LCA is where p & q split into L & R subtrees (smaller & larger than curr)
        # start curr pointing to root node
        # loop: 
        #  moving curr left if both p & q are > curr
        #  moving curr right if both p & q are < curr
        #  else: return curr, have found split

# - Binary Tree Level Order Traversal - 🟠
# BFS Soln:
        # create a fifo queue (collections.deque), & result array
        # add root to queue
        # loop while there's still elems in queue:
        #  create level array, get curr_length of queue,
        #  loop through length, popping from left of queue, 
        #   append to level_array, append children to q
        #  if nodes in level, add to result array
        # return result array

# - Binary Tree Right Side View - 🟠
# Iterative BFS Soln:
        # create a result array, to hold node values on the right side
        # create a deque to hold nodes, level by level
        # while q: get current level length
        #  iterate through level, 
        #   popping off each elem, add any children of theirs
        #   once reach last elem on that level (rightmost), add val to list
        # return result list

# - Count Good Nodes in Binary Tree - 🟠
# Recursive DFS Soln:
        # define a dfs func, takes (node, maxValInPath)
        #  BC: if empty node, return 0, no good nodes
        #  create result var, set to 1 if node.va greater than maxVal, else 0
        #  maybe update maxVal if node.val is greater
        #  explore children, adding their return val to res
        #  return res
        # call dfs with root & root.val

# - Kth Smallest Element in a BST - 🟠
# Recursive DFS Soln:
        # create a sorted array to hold sorted elems
        # recurse dfs in-order through the tree to add elems in order to the array
        # return kth elem in arr
# Iterative Stack Soln:
        # create a stack, & curr pointer to root
        # loop while elems in stack or curr
        #  while curr is not a null node, 
        #   add curr to the stack & go left, going as left as possible
        #  pop smallesst elem from stack, hold in curr
        #  decrement k, & check if k == 0: reached kth: return curr.val
        #  otherwise, then go right, setting curr to curr.right



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
        # when 1 or 0 stones left, return that stone or 0

# - K Closest Points to Origin - 🟠
# MinHeap Soln:
        # create a heap arr
        # iterate through points:
        #  creating a tuple for each, holding dist from center (to sort by), & point coords
        #  add tuple to heap
        # create result arr, for k times, pop smallest dist tuple from heap
        # add point coord to result array, return result array @ end

# - Kth Largest Element in an Array - 🟠
# Sorting Soln: - O(nLogn)
# MinHeap Soln: - O(n)
        # make a min_heap (heapq.heapify(all neg nums)) with all (neg) elems in it
        # pop k-1 times, top of stack will then be kth largest (remember to swap signs back)
# Quick Select: - Average: O(n), Worst: O(n^2)
        # reassign k in terms of kth smallest elem
        # define quickSelect(l, r): to randomly pick a pivot elem & sort larger/smaller than it
        #  set pivot elem to rightmost elem, p=swap_to_point leftmost elem
        #  iterate up to pivot point, comparing elems to pivot
        #   if elem smaller than pivot, move to left part & increase p
        #  swap pivot into p spot, separating l & r sides
        #  check if p == k or which side to keep looking @

# - Task Scheduler - 🟠
# MaxHeap Soln:
        # find frequency of each different task, add to maxHeap to always get most freq
        # create time var 
        # create deque for tracking when tasks have timed_back_in, hold [freq, valid_time]
        # loop while maxHeap & deque:
        #  increment time counter
        #  if maxHeap: heappop + 1 to process task, if not 0: add it to deque with [freq, time+n]
        #  if deque and deque[0][time] equals curr time: pop from deque & add freq back to maxHeap
        # when loop done (all tasks processed & out of queue): return time

# - Design Twitter - 🟠
# MinHeap Soln:
        # __init__()
        #  create count var, as timestamp helper, start @ 0 & decrement each tweet
        #  create followMap defaultdict(set) of user_ids: HashSet of followee_ids, O(1) add/discard
        #  create tweetMap defaultdict(list) of user_ids: List of [count, tweet_ids]
        # follow()
        #  add followeeId to set mapped to followerId
        # unfollow()
        #  discard followeeId to set mapped to followerId
        # postTweet()
        #  append [count, tweetId] to a userId's list in tweetMap, decrement count for next one
        # getNewsFeed()
        #  create a result array to hold 10 most recent tweetIds to return (most->least recent)
        #  create an array to be made into a minHeap to help get most recent tweets
        #  add a user to their own followMap
        #  go through a users followees, get from followMap[userId]
        #   ensure the followee has any tweets, check in the tweetMap, then:
        #    get index of their most recent tweet, last elem in tweetMap list
        #    use index to get its count, tweetId 
        #    add list of tweet things to heap [count, tweetId, followeeId, index-1]
        #  once all 10 tweets added, heapify the minHeap
        #  while elems still in minHeap and res list doesn't have 10 tweets yet
        #   heappop the things from minHeap
        #   append the tweetId to res
        #   if that user has more tweets, get it, & heappush it to minHeap
        # return res array with 10 tweets



# 🔲 --- Backtracking - make Decisions ---

# - Subsets - 🟠
# Backtracking Soln:
        # create result array to hold each found subset
        # define dfs func to call with index, subset
        #  BC: check if index >= len(nums): if so: append copy of subset to result & return
        #  recursively call dfs with 2 decisions:
        #  decision TO add nums[i], append to subset & call dfs @ next index
        #  decision NOT TO add nums[i], pop from subset & call dfs @ next index
        # call dfs with 0 index, & [] subset array (to hold current subset being built up)
        # return result array

# - Subsets II - 🟠
# Backtracking Soln:
        # create result array to hold each found subset
        # sort the nums array to make it easier to skip duplicate nums
        # define dfs func to call with index, subset
        #  BC: check if index >= len(nums): if so: append copy of subset to result & return
        #  recursively call dfs with 2 decisions:
        #  decision TO add nums[i], append to subset & call dfs @ next index
        #  decision NOT TO add nums[i] nor same num @ nums[i] elsewhere in nums,
        #  pop from subset
        #  move index down enough to next different num, call dfs using that index
        # call dfs with 0 index, & [] subset array (to hold current subset being built up)
        # return result array

# - Combination Sum - 🟠
# Backtracking Soln:
        # Decision: add element or not
        # create result array to hold copy of each found combination
        # define dfs func to call with (index, curr_combo, curr_total)
        #  BC1: reached solution - append copy of curr_combo to result, exit
        #  BC2: curr_combo passed target or reached end of list: exit
        #  Decision: append num @ index to curr_combo, & recursively call dfs
        #  Decision: Don't add num, recursively call dfs moving index on
        # start dfs with index=0, curr_combo=[], & curr_total=0
        # return result array

# - Combination Sum II - 🟠
# Backtracking Soln: O(2^n)
        # create result array to hold copy of each found combination
        # sort the candidates array to make it easier to skip duplicate nums to not include
        # define dfs func to call with (index, curr_combo, curr_total)
        #  BC1: reached solution - append copy of curr_combo to result, exit
        #  BC2: curr_combo passed target or reached end of list: exit
        #  Decision: append num @ index to curr_combo, & recursively call dfs on next index
        #  Decision: Don't add same num, move index down until next num in candidates is different 
        #  recursively call dfs moving index on
        # start dfs with index=0, curr_combo=[], & curr_total=0
        # return result array

# - Word Search - 🟠
# Backtracking Soln:
        # create row, col vars, & path set to hold valid found board positions 
        # define dfs func to call with (r,c,i) current row,col to check, and index in word to check with
        #  BC: found full word (index is len of word): return True
        #  BC: not correct letter (r,c off board, or not correct letter, or (r,c) in path): return False
        #  Recurse: found matching letter (word[i] @ (r,c)), recurse on adjacent board tiles
        #   add (r,c) to path, then recurse with 4 positions & increase i, save to res var
        #   remove (r,c) from path, return res
        # check from all starting positions, if any are True: return True
        # if @ end, return False

# - Palindrome Partitioning - 🟠
# Backtracking Soln:
        # create res array, & curr_part array to hold current partition
        # define dfs func to call with index checking in word
        #  BC: reached end (i passed end of word): valid partition, append part to res
        #  Recurse: 
        #   iterate through from i to end of s, use j, check if section from i-j is a pali:
        #    if so: append it to path & recurse dfs from j+1
        #    clean up by removing pali from path
        # call dfs with i=0, return res array
        # define isPalindrome func, comparing either ends & while match: move in

# - Letter Combinations of a Phone Number - 🟠
# Backtracking Soln:
        # create res array, & digitToChar hashMap to hold num:letter mapping
        # define dfs func to call with index & current built up string
        #  BC: built up valid string (len of i same as currStr): append currStr to res, return
        #  Recurse: 
        #   iterate through chars @ i digit: recursing with i+1 & curStr+char
        # call dfs with i=0 & empty str, return res array



# 🔲 --- Graphs ---

# - Number of Islands - 🟠
# BFS Soln:
        # get row, col dimensions of the graph
        # create a visited set to hold (r,c) tuples of land visited
        # create island count var to return at end
        # define bfs func, take in starting r,c of an island
        #  create a queue to hold nodes & iteratively bfs through island
        #  append the starting node to the queue
        #  create a directions array to hold tuples of 4 directions
        #  while nodes in queue: 
        #   popleft the closest node in the queue
        #   for direction in directions:
        #    check if node in bounds and land and not visited:
        #     append it to queue & add it to visited set
        #
        # iterate through all nodes, nested rows & cols:
        #   if water: do nothing, if land ('1' and not in visited):
        #    run bfs from that node to mark whole island as visited & increment island count
        # return island count

# - Clone Graph - 🟠
# DFS recursive Soln:
        # create hashMap to hold oldNode: newNode
        # define dfs function, take in node
        #  check if node has already been cloned in hashMap: return node
        #  if not: create copy of node, add it to hashMap
        #  iterate through neighbor nodes: calling dfs on each neighbor & appending to copyNode.neighbors
        #  return copyNode
        # if node: return dfs(node), else: return None

# - Max Area of Island - 🟠
# My BFS recursive Soln:
        # create visited set to hold explored nodes
        # create max_area var to hold largest island area
        # define bfs function, take in r,c for island to explore
        #  create a queue, appending start coord to it, local area
        #  while queue: popleft() & check if island extends in any direction (in range, land, not visited)
        #   visit, add to queue, update area
        #  update max_area if local island area is greater
        # iterate through each coord in grid, call bfs() when find unexplored island
        # return max_area

# - Pacific Atlantic Water Flow - 🟠
# DFS recursive Soln:
        # work backwards from ocean-adjacent land, to find all coords accessible from each ocean, then return overlap
        # create pac & atl sets to hold coords that can reach either ocean
        # define dfs func, take in r,c to search from, visited set, & prevHeight
        #  BC: if visited, out of bounds, or less than prevHeight: return
        #  otherwise: visit curr & recurse on all 4 neighbors
        # loop through cols, call dfs for each coord on top & bottom side, with correct set
        # loop through rows, call dfs for each coord on R & L side, with correct set
        # create result array, iterate through all coords, adding to result if they're in both pac & atl sets
        # return result array

# - Surrounded Regions - 🟠
# BFS Soln with queue: - Slow
# Reverse Thinking Soln:
        # capture everything except unsurrounded regions (O's connected to the border)
        # iterate through border cells, if it's an O, run dfs on it, swapping O->T
        # define dfs func, take in r,c for O to start at
        #  BC: if out of bounds or not an O, return
        #  swap the O->T and recurse on 4 neighbors
        # iterate through all cells, swapping all O's to X's
        # iterate through all cells, swapping all T's back to O's

# - Rotting Oranges - 🟠
# BFS Soln with queue: 
        # create a q (deque) to bfs, hold rotten oranges (2) to go through & spread to fresh (1)
        # create rows, cols, fresh_count, minute
        # iterate through gris, counting 1s in fresh_count & append starting 2s to q
        # while q & still fresh oranges left:
        #  iterate through all oranges currently in q, by getting len(q)
        #   popleft from q, check 4 neighbors from rotten, if 1: turn rotten, add to queue & decrement fresh
        #  increment minute 
        # return minute if no fresh left else -1

# - Course Schedule - 🟠
# DFS Soln:
        # create an adjacencyList of prerecs for each course {crs: [pre crs],}
        # create a visit set to track visited already
        # define dfs func, take in crs currently visiting
        #  check for cycle: crs in visit: return False
        #  check for no prereqs, can visit: adjList for crs == []: return True
        #  add crs to visit set
        #  iterate through a crs' prereqs using adjList: 
        #   calling dfs on each prereq, checking for cycle (in visit) each time, returning False if found
        #  remove crs from visit, set adjList to [] to show it's been explored fully, return True
        # iterate through all courses, calling dfs for each, but check if any return False -> a cycle
        #  if so, return False immediately, there's a cycle, otherwise let finish & return True @ end, it's possible

# - Course Schedule II - 🟠
# DFS Soln:
        # create an adjacencyList of prerecs for each course {crs: [pre crs],}
        # create an output array to build up the ordering
        # create a visit set to track visited already
        # create a cycle set to track whether there's a cycle
        # define dfs func, take in crs currently visiting
        #  check for cycle: crs in cycle: return False
        #  check for already visited: crs in visit: return True
        #  add crs to cycle
        #  iterate through a crs' prereqs using adjList: 
        #   calling dfs on each prereq, checking for cycle each time, returning False if found
        #  remove crs from cycle
        #  add crs to visit, append crs to output, & return True
        # iterate through all courses, calling dfs for each, but check if any return False -> a cycle
        #  if so, return an empty list immediately, otherwise let finish & return output arr @ end



# 🔲 --- 1-D Dynamic Programming ---

# - Climbing Stairs - 🟢
# BF Soln: Too slow
        # define climb func, take in n
        #  BC1: if n == 1: return 1 way
        #  BC2: if n == 2: return 2 ways
        #  otherwise: return recursive calls to climb(n-1) + climb(n-2)
        # call climb with n stairs
# Memoization Soln:
        # Same as above, but first define a memo dict
        # add 1:1 & 2:2 to memo
        # then in climb, check if n in memo before calculating (& saving res in memo)
# DP Soln:
        # create 2 vars to hold prev 2 numbers (one, two), initially set to 1, 1
        # iterate n-1 times: updating one = (one + two) and two to what one had been
        # then return one after loop, basically fibonacii sequence

# - Min Cost Climbing Stairs - 🟢
# DP Soln:
        # start @ end, working backwards, minimizing cost
        # append 0 to end of cost arr
        # iterate backwards through cost, setting cost[i] to min of (cost[i+1] or cost[i+2]) PLUS cost[i]
        # return the min of costs calculated in cost[0] or cost[1]

# - House Robber - 🟠
# DP Soln - Iterative with N vars (bottom-up)
        # imagine nums = [n1, n2, curr_n, ...]
        # create 2 vars, n1 & n2 = 0
        # iterate through nums: 
        #  calc the max_n (that aren't adjacent) with max of n1 + curr_n or just n2
        #  update n1 to n2, and n2 to max_n
        # return n2

# - House Robber II - 🟠
# DP Soln - Iterative with N vars (bottom-up)
        # use House Robber I soln as a helper function, 
        # call it with 2 slices of nums, excluding the first elem & last elem, since they're adjacent
        # (also include nums[0] in max calc incase nums has only 1 elem)

# - Longest Palindromic Substring - 🟠
# DP Soln:
        # create 2 vars, res to hold palindrome result string, & resLen to hold its length
        # iterate through s, checking each elem & expanding out from it (odd len) or out from two elems (even len) to check if pali
        #  if any found are longer than current resLen: save it
        #  check odd len: 
        #   set l & r pointers both to i, while they're inbounds & elem @ l&r index are equal: check longer than current pali: if so save it
        #   then decrement l & increment r
        #  check even len: 
        #   set l & r pointers to i & i+1, while they're inbounds & elem @ l&r index are equal: check longer than current pali: if so save it
        #   then decrement l & increment r
        # return res string



# 🔲 --- Greedy ---

# - Maximum Subarray - 🟠
# BF Soln: Too slow
        # just going through & calc each sum, saving max
# Sliding window Soln: O(n)
        # set maxSum to first elem
        # set curSum to 0, the prefix, if it ever starts neg, reset it to 0
        #  iterate through all nums, as n
        #  check if curSum is neg, reset to 0 if so. meaning full prefix was neg & will not maximize soln
        #  add current n to curSum
        #  check & update maxSum if found new max
        # return maxSum

# - Jump Game - 🟠
# Shift goalpost Soln:
        # set goal to the end i
        # iterate backwards through nums indices, curr_i
        #  if curr_i + elem @ curr_i >= the goal: move the goal to i, if start can reach here it can reach the end
        # return True if the goal has reached beginning index 0, otherwise not possible: False



# 🔲 --- Intervals ---

# - Insert Interval - 🟠
# Build up new arr Soln:
        # make new_arr to build up
        # iterate through intervals with i
        #  if NewInterval_end less than i_start: no overlap, just insert it to new_arr
        #   return new_arr + slice of rest of intervals array 
        #  elif NewInterval_start greater than i_end: no overlap, just continue, adding i to new_arr
        #  else: there's overlap: update NewInterval with min(starts) & max(ends)
        # append newInterval if got to the end without appending it
        # return new_arr

# - Merge Intervals - 🟠
# Build up new arr Soln:
        # make new_arr to build up answer
        # sort intervals arr, key = start
        # append the first interval to new_arr
        # iterate through rest of intervals:
        #  get the last_end from new_arr
        #  if i_start overlaps with last_end: merge them by updating end of last interval in new_arr to whatever max is
        #  if no overlap: append i interval to new_arr
        # return new_arr

# - Non-overlapping Intervals - 🟠
# Soln:
        # Sort by start, & then end
        # make result var, set = 0, return it at end
        # set prev_end var to end of first interval
        # iterate through rest of intervals:
        #  check if overlapping (i_start >= prev_end): 
        #   if not: move up prev_end to i_end
        #   if overlapping: increment res, & set prev_end to min(i_end, prev_end)
        # return res

# - Meeting Rooms - 🟢
# Soln:
        # Sort by start vals
        # iterate through intervals[1:], getting i-1 & i intervals
        #  check if i.start < i-1.end: if ever: return False, there's an overlap
        # if reach end: return True, no overlaps

# - Meeting Rooms II - 🟠
# Soln: 
        # create 2 new arrs, all_starts & all_ends, that are both sorted
        # create count & max_count vars, starting @ 0
        # create start_i & end_i pointer vars, starting @ 0
        # while s_i has not reached end of start array: 
        #  check if all_starts[s_i] < all_ends[e_i] (a new meeting started):
        #   increment s_i & count
        #  otherwise (a meeting ended):
        #   increment e_i & decrement count
        #  maybe update max_count
        # return max_count















