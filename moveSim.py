import numpy as np
import random
import math

class Dive:
    
    def __init__(self,agentNumber):
        self.agentNumber = agentNumber
        self.fieldX = 100
        self.fieldY = 100
        self.agentEye = 10
        self.agentEyeAngle = 30

        self.agentAry = [[0 for i in range(3)] for j in range(self.agentNumber)]
        self.goalAry = [[0 for i in range(2)] for j in range(self.agentNumber)]

        self.visionFieldAry = [np.zeros((self.fieldX,self.fieldY))] * self.agentNumber
        self.trueField = np.zeros((self.fieldX,self.fieldY))

        self.finish = False
        self.turn = 1

        self.reset()

        print("finish init!")

    def reset(self):
        for i in range(self.agentNumber):
            self.agentAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY-1),random.randint(0,360/self.agentEyeAngle-1)]
            self.goalAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY-1)]
            while self.agentAry[i][0] == self.goalAry[i][0] and self.agentAry[i][1] == self.goalAry[i][1]:
                self.goalAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY)]

        self.turn = 1
        self.finish = False

    def checkEye(self,eye,target,degreeType):
        eToT = np.array((target[0]-eye[0],target[1]-eye[1]))
        #print(eToT)
        eToC = np.array((math.cos(degreeType * self.agentEyeAngle - 90),math.sin(degreeType * self.agentEyeAngle - 90)))
        #print(eToC)
        dot = np.dot(eToT,eToC)
        eToTn = np.linalg.norm(eToT)
        eToCn = np.linalg.norm(eToC)
        cos = dot/(eToCn*eToTn)
        rad = np.arccos(cos)
        theta = rad * 180 /np.pi
        dist = math.sqrt(math.pow(eye[0]-target[0],2)+math.pow(eye[1]-target[1],2))
        #print(dist)
        #print(theta)
        if theta <= self.agentEyeAngle/2 and dist <= self.agentEye:
            return True
        else:
            return False

    def makeField(self):
        for i in range(self.agentNumber):
            self.visionFieldAry[i] = np.zeros((self.fieldX,self.fieldY))
            for j in range(self.agentNumber):
                #print((i,j))
                if i==j:
                    self.visionFieldAry[i][self.agentAry[j][0]][self.agentAry[j][1]] = j
                elif self.checkEye([self.agentAry[i][0],self.agentAry[i][1]],[self.agentAry[j][0],self.agentAry[j][1]],self.agentAry[i][2]):
                    self.visionFieldAry[i][self.agentAry[j][0]][self.agentAry[j][1]] = j
                if self.checkEye([self.agentAry[i][0],self.agentAry[i][1]],[self.goalAry[j][0],self.goalAry[j][1]],self.agentAry[i][2]):
                    self.visionFieldAry[i][self.goalAry[j][0]][self.goalAry[j][1]] = j + self.agentNumber
            #print(self.visionFieldAry[0])
            self.trueField[self.agentAry[i][0]][self.agentAry[i][1]] = i + 1
            self.trueField[self.goalAry[i][0]][self.goalAry[i][1]] = i + 1 + self.agentNumber
            #print(self.trueField)

    def culcReward(self):
        result = []
        for i in range(self.agentNumber):
            result.append(-10000)
            if self.agentAry[i][0] == self.goalAry[i][0] and self.agentAry[i][1] == self.goalAry[i][1]:
                result[i] = -0.1 * self.turn
                self.finish = True
        return result

    def getMove(self,moveAry):
        for move in moveAry:
            #print(move[1])
            if move[1] / 5 < 1:
                self.agentAry[move[0]][2] += -1 * self.agentEyeAngle
            elif move[1] / 5 >= 2:
                self.agentAry[move[0]][2] += self.agentEyeAngle
            if move[1] % 5 == 1:
                self.agentAry[move[0]][0] += 1
            elif move[1] % 5 == 2:
                self.agentAry[move[0]][1] += 1
            elif move[1] % 5 == 3:
                self.agentAry[move[0]][0] -= 1
            elif move[1] % 5 == 4:
                self.agentAry[move[0]][1] -= 1
        for agent in self.agentAry:
            if agent[0] == self.fieldX:
                print("xover")
                print(self.agentAry)
                agent[0] = 0
            elif agent[0] == -1:
                agent[0] = self.fieldX
            if agent[1] == self.fieldY:
                print("yover")
                print(self.agentAry)
                agent[1] = 0
            elif agent[1] == -1:
                agent[1] = self.fieldY
        self.makeField()
        self.turn += 1
        return (self.visionFieldAry,self.trueField,self.culcReward(),self.finish)

    def getAgentAry(self):
        return self.agentAry,self.goalAry
