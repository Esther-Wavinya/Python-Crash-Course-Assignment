
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

nestedList = [1, [4, [6]]]
class Solution:
  def depthSum(self, nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    def dfs(list, depth):
      total = 0
      for n in list:
        if n.isInteger():
          total += n.getInteger()*depth
        else:
          total += dfs(n.getList(), depth+1)
      return total
    return dfs(nestedList, 1)
