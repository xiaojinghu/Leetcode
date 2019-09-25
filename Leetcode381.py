class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valToIndexSet = collections.defaultdict(set)
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.valToIndexSet[val].add(len(self.nums)-1)
        return len(self.valToIndexSet[val])==1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.valToIndexSet[val])==0:
            return False
        # if val is the last number
        if self.nums[-1] == val:
            index = len(self.nums)-1
            # pop the last element out
            self.nums.pop()
            # pop the index from the corresponding set
            self.valToIndexSet[val].remove(index)
            return True
        # if val is not the last number
        popedIndex = self.valToIndexSet[val].pop()
        reOrderIndex = len(self.nums)-1
        reOrderElem = self.nums.pop()
        # update nums
        self.nums[popedIndex] = reOrderElem
        # update the dictionary
        self.valToIndexSet[reOrderElem].remove(reOrderIndex)
        self.valToIndexSet[reOrderElem].add(popedIndex)
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)