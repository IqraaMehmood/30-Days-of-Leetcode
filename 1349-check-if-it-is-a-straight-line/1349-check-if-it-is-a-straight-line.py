class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates)<2:
            return True
        x=(coordinates[1])[0]-(coordinates[0])[0];
        y=(coordinates[1])[1]-(coordinates[0])[1];
        for i in range(2,len(coordinates)):
            X=(coordinates[i])[0]-(coordinates[0])[0];
            Y=(coordinates[i])[1]-(coordinates[0])[1];
            if x*Y!=y*X:
                return False
        return True