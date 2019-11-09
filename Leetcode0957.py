class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # since there are only 8 numbers in the list, there are at most 2**8 states in the result. if N>2**8, there must be a cycle.
        # we need to find the period of the cycle.
        # we build a hashMap to map the state to its ocurred time. And another hashMap to map to date to the state
        state0 = ''.join(map(str, cells))
        stateToDay = {state0:0}
        dayToState = {0:state0}
        day = 0
        prevState = state0
        flag = False
        while(day<N):
            day += 1
            nextState = ''
            for i in range(1, 7):
                if prevState[i-1] == prevState[i+1]:
                    nextState +='1'
                else:
                    nextState += '0'
            nextState = '0'+nextState+'0'
            if nextState in stateToDay:
                startDay = stateToDay[nextState]
                cycle = day - startDay
                flag = True
                break
            else:
                stateToDay[nextState] = day
                dayToState[day] = nextState
                prevState = nextState
        if flag:
            # this means we found a cycle 
            # print cycle, N%cycle, startDay, N%cycle+startDay
            N = (N-startDay)%cycle+startDay
            # print N
        # print dayToState  
        res = dayToState[N]
        res = map(int, list(res))
        return res
                