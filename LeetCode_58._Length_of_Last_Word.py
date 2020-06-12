class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        
        s=s.rstrip(' ').split(' ')[-1] #rstrip:刪除string字符串末尾的指定字符後生成的新字符串
        return len(s)

#Example
s=Solution()
s.lengthOfLastWord("Hello World")
