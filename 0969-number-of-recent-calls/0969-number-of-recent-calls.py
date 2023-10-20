class RecentCounter(object):

    def __init__(self):
        self.r=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.r.append(t)
        while(self.r[0]<t-3000):
            self.r.pop(0)
        return len(self.r)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)