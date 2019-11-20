class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # idea: 
        # view the sentence as a infinitely looping package that contains only one sentence and find the index of the last position of the screen in the package. 
        # initially the index of the first char in a row is 0
        start = 0
        # we need to put a space between scentences.
        sentence = ' '.join(sentence)+' '
        length = len(sentence)
        
        
        for i in range(rows):
            # the index of the next start should be start+cols
            start += cols
            # we check what is on the position start:
            # if it is a space, then we can skip this space and   the next row starts with a word and the position is start+1
            if sentence[start%length]==' ':
                start += 1
            else:
            # if it is a letter, there are two possibilities
            # 1. it is the start of a new word, in this case we do not need to the start;
            # 2. it is inside a word, in this case we need to move start back to the start of the word. 
            # In both of the two cases, we need to find the " " before start.
                while(start>0 and sentence[(start-1)%length]!=" "):
                    start -= 1
                # now either start-1 is a " " or start is at the very begining of the package.
        return start/length
        