class StringQuestions():

    # Problem : Reverse String
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def reverse_string_stack(self, s):
        stack = list(s)
        reversed = ""
        for i in range(0, len(s)):
            reversed += stack.pop()
        return reversed

    # Problem : Reverse String
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def reverse_string_list(self, s):
        n = len(s)
        slist = list(s)
        for i in range(0, int(len(s) / 2)):
            temp = slist[i]
            slist[i] = slist[n - i - 1]
            slist[n - i - 1] = temp
        return ''.join(slist)