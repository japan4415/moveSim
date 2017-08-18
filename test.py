import moveSim
import numpy as np

testDive = moveSim.Dive()
print(testDive.checkEye([0,0],[1,0],2))
testDive.makeField()
a,b,c = testDive.getMove([[0,1]])
aa,bb = testDive.getAgentAry()

for i,aaa in enumerate(aa[0]):
    aa[0][i] = int(aaa)
    print(aa[0][i])

for i,bbb in enumerate(bb[0]):
    bb[0][i] = int(bbb)
    print(bb[0][i])

print(aa)

np.savetxt('agentEye.csv',a[0],delimiter=",")
np.savetxt('trueEye.csv',b,delimiter=",")
np.savetxt('agentAry.csv',aa,fmt="%.0f",delimiter=",")
np.savetxt('goalAry.csv',bb,fmt="%.0f",delimiter=",")