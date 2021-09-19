class Solution:
    def isValidSerialization(self, preorder):
        stack = []
        for elem in preorder.split(","):
            stack.append(elem)
            while len(stack) > 2 and stack[-2:] == ["#"]*2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            
        return stack == ["#"]