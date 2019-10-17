class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # SLIDING WINDOW + HASHMAP
        if not s:
            return 0
        if len(s)<=1:
            return 1
        
        hashmap = {}
        maxLen = 0
        startIndex = 0
        for i in range(len(s)):
            # if current char hasn't appeared in the hashtable, we can add it to our substring
            if s[i] not in hashmap:
                hashmap[s[i]] = i
                currLen = i-startIndex+1
                maxLen = max(maxLen, currLen)
                continue
            # if current char has appeared in the hashtable, we need to fetch its original index, adn update our startIndex
            # we need to pop chars from the original startIndex to the index of s[i]
            for j in range(startIndex, hashmap[s[i]]):
                hashmap.pop(s[j])
            # we update the startIndex
            startIndex = hashmap[s[i]]+1
            # update the index of s[i]
            hashmap[s[i]] = i
            currLen = i-startIndex+1
            maxLen = max(maxLen, currLen)
        return maxLen
