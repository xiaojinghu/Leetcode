
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            # f is a user-defined key generarion function for comparison and sorting
            id_, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, id_)
            else:
                return (1,)
            
        if not logs or len(logs) == 1:
            return logs
        
        logs.sort(key=f)
        return logs
