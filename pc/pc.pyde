import random
import sys
import csv

print(sys.executable)

i = 0
xa = 0
ya = 0
xg = 0
yg = 0
s = 0
r = 30
step = 0
agentNumber = 1
fieldSize = 100
agentAry = []
goalAry = []

agentAryAry = []

'''
f = open("agentAry.csv","r")
reader = csv.reader(f)
for row in reader:
    agentAry.append(row)
f.close
'''

f = open("goalAry.csv","r")
reader = csv.reader(f)
for row in reader:
    goalAry.append(row)
f.close

for i,agent in enumerate(agentAry):
    xa = int(agent[0])
    ya = int(agent[1])
    s = int(agent[2]) * r
    xg = int(goalAry[i][0])
    yg = int(goalAry[i][1])

def setup():
    #frame.setTitle("Python Test")
    size(500, 500)
    noStroke()
    fill(255, 0, 0)
    
def openFile(step):
    
    global xa
    global ya
    global xg
    global yg
    global s
    global agentAryAry
    

    f = open("../result/" + str(step) + "agentAry.csv","r")
    reader = csv.reader(f)
    agentAryAry.append([])
    for row in reader:
        agentAryAry[step].append(row)
    f.close

    for i,agent in enumerate(agentAryAry[step]):
        xa = int(agent[0])
        ya = int(agent[1])
        s = int(agent[2]) * r
    
def draw():
    global i
    global xa
    global ya
    global xg
    global yg
    global s
    global step
    global agentNumber
    
    openFile(step)
    
    for i in range(agentNumber):
        xg = int(goalAry[i][0])
        yg = int(goalAry[i][1])
    
    background(0)
    fill(0,255,0)
    ellipse(xa,ya,5,5)
    fill(255,0,0)
    ellipse(xg,yg,5,5)
    fill(0,255,0,50)
    arc(xa,ya,500,500,radians(s*r-r/2),radians(s*r+r/2))
    
    saveFrame("frames/" + str(step) + ".tif")
    
    step += 1

'''
def draw():
    global i
    global xa
    global ya
    global xg
    global yg
    global s
    background(0)
    fill(0,255,0)
    ellipse(xa, ya, 5, 5)
    fill(255,0,0)
    ellipse(xg, yg, 5, 5)
    fill(0,255,0,50)
    arc(xa,ya,500,500,radians(s-r/2),radians(s+r/2))
    xa += random.randint(-1,1)
    ya += random.randint(-1,1)
    s += random.randint(-1,1) * 15
    if xa > 500:
        xa = 0
    if ya > 500:
        ya = 0
    if xa < 0:
        xa = 500
    if ya < 0:
        ya = 500
    #saveFrame("frames/" + str(i) + ".tif")
    i += 1
    
'''
    
print(sys.executable)