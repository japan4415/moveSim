import moveSim
import numpy as np
import os
import shutil

from dqn_agent import DQNAgent

shutil.rmtree("result")
os.mkdir("result")

envName = "test"

agentNumber = 1
enableAction = range(10)

'''
step = 500

testDive = moveSim.Dive(agentNumber)
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

#np.savetxt('agentEye.csv',a[0],delimiter=",")
#np.savetxt('trueEye.csv',b,delimiter=",")
np.savetxt('result/0agentAry.csv',aa,fmt="%.0f",delimiter=",")
np.savetxt('result/goalAry.csv',bb,fmt="%.0f",delimiter=",")

for i in range(step):
    a,b,c = testDive.getMove([[0,1]])
    aa,bb = testDive.getAgentAry()

    np.savetxt("result/" + str(i) + 'agentAry.csv',aa,fmt="%.0f",delimiter=",")
'''

#環境の初期化
env = moveSim.Dive(agentNumber)

#エージェントの初期化
agentAry = []
for i in range(agentNumber):
    agentAry.append(DQNAgent(enableAction,envName+str(i)))

#環境の初期状態の取得
agentEyeAry,tField,rewardAry,finish = env.getMove([[0,1]])

#学習中に使う変数宣言
epoch = 0

#調整する場所
maxEpoch = 100000

for i in range(maxEpoch):
    print("epoch:" + str(i))

    #前回の結果を避ける
    prevAgentEyeAry = agentEyeAry
    prevTField = tField

    #動作を取得
    moveAry = []
    for j,agent in enumerate(agentAry):
        moveAry.append(agent.select_action(agentEyeAry[j],agent.exploration))

    #動作を適応、報酬を受取
    moveAryPush = []
    for j,move in enumerate(moveAry):
        moveAryPush.append([j,move])
    agentEyeAry,tField,rewardAry,finish = env.getMove(moveAryPush)

    #学習
    for j,agent in enumerate(agentAry):
        agent.store_experience(agentEyeAry[j],moveAry[j],rewardAry[j],prevAgentEyeAry[j],finish)
        agent.experience_replay()

    #結果保存
    print(rewardAry[0])
    if finish:
        print("goal!!!")
    aa,bb = env.getAgentAry()
    np.savetxt("result/" + str(i) + 'agentAry.csv',aa,fmt="%.0f",delimiter=",")

    # save model
    for agent in agentAry:
        agent.save_model()