import math

def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()


    instructions = input[0].strip()
    nodeMap = {}
    startingNodes = []

    for i in range(2,len(input)):
      nodeLeftRight = input[i].strip().split('=')
      key = nodeLeftRight[0].strip()
      left = nodeLeftRight[1].strip().split(',')[0][1:]
      right = nodeLeftRight[1].strip().split(',')[1][1:4]
      nodeMap[key] = (left,right)

      if key[-1] == 'A':
        startingNodes.append(key)
    return instructions, nodeMap, startingNodes



if __name__ == "__main__":
  instructions, nodeMap, startingNodes = getInput('input.txt')
  
  pathsCount = []
  for node in startingNodes:
    found  = False
    curNode = node
    count = 0

    while curNode[-1] != "Z":
      for instruction in instructions:
        left,right = nodeMap[curNode]
        if instruction == 'L':
          curNode = left      
        elif instruction == 'R':
          curNode = right
        count += 1
        if curNode[-1] == 'Z':
          break
    
    pathsCount.append(count)
  
  print(math.lcm(*pathsCount))