class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right, cnt, goal, minLen = 0, 0, 0, len(set(t)), float('inf')
        minWin = ""
        tCount = collections.Counter(t)
        sCount = collections.defaultdict(int)        
        
        while(right<len(s)):
            # Now the current window is s[left:right+1]
            sCount[s[right]] += 1
            if s[right] in tCount and sCount[s[right]]==tCount[s[right]]:
                # to avoid repeated counting, we only increase cnt when the counts are equal.
                cnt += 1
            # we check if we've achieved our goal
            while left<=right and cnt == goal:
                #we move left farward to see if we could find a shorter window
                # update the minimum window
                if minLen > right-left+1:
                    minLen = right-left+1
                    minWin = s[left:right+1]
                sCount[s[left]] -= 1
                if s[left] in tCount and sCount[s[left]] < tCount[s[left]]:
                    cnt -= 1
                left += 1
            # now either left=right+1 or cnt<goal
            # we need to move right farward
            right += 1
        return minWin