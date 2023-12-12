from collections import deque


def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    input = [x.strip() for x in input]
    startingNode = (0,0)
    for row in range(len(input)):
      for col in range(len(input[0])):
        if input[row][col] == 'S':
          startingNode = (row,col)
    return input, startingNode
  
  

    
  
if __name__ == '__main__':
  input, startingNode = getInput('input.txt')

  q = deque([startingNode])
  visited = set(startingNode)

  print(startingNode)
  while q:
    nodeCoord = q.popleft()
    r,c = nodeCoord
    char = input[r][c]
    if char in 'S|LJ' and r-1 >= 0 and input[r-1][c] in '|F7' and (r-1,c) not in visited:
      visited.add((r-1,c))
      q.append((r-1,c))
    
    if char in 'S|7F' and r + 1 < len(input) and input[r+1][c] in '|LJ' and (r+1,c) not in visited:
      visited.add((r+1,c))
      q.append((r+1,c))
    
    if char in 'S-J7' and c-1 >= 0 and input[r][c-1] in 'L-F' and  (r,c-1) not in visited:
      visited.add((r,c-1))
      q.append((r,c-1))

    if char in 'SLF-' and c+1 < len(input[0]) and input[r][c+1] in '-J7' and (r,c+1) not in visited:
      visited.add((r,c+1))
      q.append((r,c+1))

  print(len(visited)//2)

  