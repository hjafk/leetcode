class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            c = ((num1 & num2) << 1) & 0xffffffff
            num1 = (num1 ^ num2) & 0xffffffff
            num2 = c

            # （长度不超过31位）第32位是0
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = num1
            # result = ~(num1 ^ 0xffffffff)
            # result = 0xffffffff - num1 - 1
        return result

so = Solution()
print(so.Add(1, -2))