# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list – whose elements may also be integers or other lists.



# Example 1: Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)
#
# Example 2: Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)

#- **Intuition**
#    - Seems like a simple recursion.
#    - Should be able to be done iteratively as well.
#- **Time and Space Complexity Considerations**
#    - O(n), where n ⇒ count of values in all lists combined, since all values will need to be looked
#    - O(d), where d ⇒ depth of the nesting

#- **Solution**
# This question can be solved by Depth First Search.

# Weight sum is level depth times sum. We will go throught the list, if the element is digit, we sum up. If element is list, we use dfs to get into new depth and go through the new list again. The depth is start from 1.

def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def DFS(nestedList, depth):
        temp_sum = 0
        for elem in nestedList:
            if elem.isInteger():
                temp_sum += elem.getInteger() * depth
            else:
                temp_sum += DFS(elem.getList(), depth + 1)
        return temp_sum

    return DFS(nestedList, 1)

# We traversal all elements of nested list so total time complexity is O(n)