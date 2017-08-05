import numpy as np
import random
import math

class Dive:
    
    def __init__(self):
        self.agentNumber = 1
        self.fieldX = 100
        self.fieldY = 100
        self.agentEye = 10
        self.agentEyeAngle = 45

        self.agentAry = [[0 for i in range(3)] for j in range(self.agentNumber)]
        self.goalAry = [[0 for i in range(2)] for j in range(self.agentNumber)]

        self.visionFieldAry = [np.zeros((self.fieldX,self.fieldY))] * self.agentNumber

        self.reset()

        print("finish init!")

    def reset(self):
        for i in range(self.agentNumber):
            self.agentAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY),random.randint(0,360/self.agentEyeAngle-1)]
            self.goalAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY)]
            while self.agentAry[i][0] == self.goalAry[i][0] and self.agentAry[i][1] == self.goalAry[i][1]:
                self.goalAry[i] = [random.randint(0,self.fieldX-1),random.randint(0,self.fieldY)]



    def checkEye(self,eye,target,degreeType):
        eToT = np.array((eye[0]-target[0],eye[1]-target[1]))
        eToC = np.array((math.cos(degreeType * self.agentEyeAngle),math.sin(degreeType * self.agentEyeAngle)))
        dot = np.dot(eToT,eToC)
        eToTn = np.linalg.norm(eToT)
        eToCn = np.linalg.norm(eToC)
        cos = dot/(eToCn*eToTn)
        rad = np.arccos(cos)
        theta = rad * 180 /np.pi
        dist = math.sqrt(math.pow(eye[0]-target[0],2)+math.pow(eye[1]-target[1],2))
        if theta <= self.agentEyeAngle and dist <= self.agentEye:
            return True
        else:
            return False

    def makeField(self):
        for i in range(self.agentNumber):
            self.visionFieldAry[i] = np.zeros((self.fieldX,self.fieldY))
            for j in range(self.agentNumber):
                if i==j:
                    self.visionFieldAry[i][self.agentAry[j][0]][self.agentAry[j][1]] = j
                elif self.checkEye([self.agentAry[i][0],self.agentAry[i][1]],[self.agentAry[j][0],self.agentAry[j][1]],self.agentAry[i][2]):
                    self.visionFieldAry[i][self.agentAry[j][0]][self.agentAry[j][1]] = j
                if self.checkEye([self.agentAry[i][0],self.agentAry[i][1]],[self.goalAry[j][0],self.goalAry[j][1]],self.agentAry[i][2]):
                    self.visionFieldAry[i][self.agentAry[j][0]][self.agentAry[j][1]] = j + self.agentNumber