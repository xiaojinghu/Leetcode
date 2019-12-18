class Solution(object):
    def key(self, log):
        """
        rules:
        1. letter log is samller that digit log;
        2. digit logs are equal;
        3. letter logs are sorted lexicographically;
        """
        identifier, logpart = log.split(" ", 1)
        if logpart[0].isdigit():
            return (1, 0, 0)
        return (0, logpart, identifier)
    
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs.sort(key = self.key)
        return logs
