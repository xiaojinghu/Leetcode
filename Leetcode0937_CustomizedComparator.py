class Solution(object):
    def comparator(self, log1, log2):
        """
        rules:
        1. letter log is samller that digit log;
        2. digit logs are equal;
        3. letter logs are sorted lexicographically;
        """
        # first split the logs into identifiers and logpart
        id1, logpart1 = log1.split(" ", 1)
        id2, logpart2 = log2.split(" ", 1)
        if logpart1[0].isdigit():
            if logpart2[0].isdigit():
                return 0
            else:
                return 1
        else:
            if logpart2[0].isdigit():
                return -1
            else:
                if logpart1 < logpart2:
                    return -1
                if logpart1 == logpart2:
                    if id1<id2:
                        return -1
                    if id1==id2:
                        return 0
                    if id1>id2:
                        return 1
                if logpart1 > logpart2:
                    return 1
                
    
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs.sort(cmp = self.comparator )
        return logs
       