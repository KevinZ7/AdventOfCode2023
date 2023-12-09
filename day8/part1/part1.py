def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()


    instructions = input[0].strip()
    nodeMap = {}

    for i in range(2,len(input)):
      nodeLeftRight = input[i].strip().split('=')
      key = nodeLeftRight[0].strip()
      left = nodeLeftRight[1].strip().split(',')[0][1:]
      right = nodeLeftRight[1].strip().split(',')[1][1:4]
      nodeMap[key] = (left,right)
    return instructions, nodeMap
  

if __name__ == '__main__':
  instructions,nodeMap = getInput('input.txt')
  found = False
  curNode = 'AAA'
  count = 0
  while curNode != 'ZZZ':
    for instruction in instructions:
      left,right = nodeMap[curNode]
      if instruction == 'L':
        curNode = left      
      elif instruction == 'R':
        curNode = right
      count += 1
      if curNode == 'ZZZ':
        break
  
  print(count)
  

        
      
