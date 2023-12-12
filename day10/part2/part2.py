from collections import deque


def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    input = [list(x.strip()) for x in input]
    startingNode = (0,0)
    for row in range(len(input)):
      for col in range(len(input[0])):
        if input[row][col] == 'S':
          startingNode = (row,col)
    return input, startingNode
  
  

    
  
if __name__ == '__main__':
  input, startingNode = getInput('input.txt')


  q = deque([startingNode])
  visited = {startingNode}
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



  #part 2:

  # we can count how many enclosed areas are in each line from top to bottom:

  # we start with inside = False:

  # if we see a |, we set inside = !inside
  # if we see any character not as a boarder: count += 1 if inside = True
  # when we see L or F, we don't change , set prev = L or F
  # when we see J , if prev is L, don't change, if prev is F, change inside = !inside
  # when we see 7, if prev is L, change inside = !inside, if prev is F, don't change
  

  #make S go back to original pipe
  startR, startC = startingNode

  if (startR+1,startC) in visited and (startR-1,startC) in visited:
    input[startR][startC] = '|'
  elif (startR,startC+1) in visited and (startR,startC-1) in visited:
    input[startR][startC] = '-'
  elif (startR,startC + 1) in visited and (startR+1,startC) in visited:
    input[startR][startC] = 'F'
  elif (startR,startC - 1) in visited and (startR+1,startC) in visited:
    input[startR][startC] = '7'
  elif (startR,startC + 1) in visited and (startR-1,startC) in visited:
    input[startR][startC] = 'L'
  elif (startR,startC - 1) in visited and (startR-1,startC) in visited:
    input[startR][startC] = 'J'
  

  count = 0
  for r in range(len(input)):
    inside = False
    prev = None
    for c in range(len(input[r])):

      char = input[r][c]

      if (r,c) in visited and char == '|':
        inside = not inside
        # print("changing inside")
        # print((r,c))
        # print(inside)
      
      if (r,c) in visited and char in 'FL':
        prev = char
        # print("setting prev")
        # print((r,c))
        # print(prev)
      
      if (r,c) in visited and char == 'J':
        if prev == 'F':
          inside = not inside
          # print("changing inside")
          # print((r,c))
          # print(inside)
        prev = None
      
      if (r,c) in visited and char == '7':
        if prev == 'L':
          inside = not inside
          # print("changing inside")
          # print((r,c))
          # print(inside)
        prev = None

      
      if inside and (r,c) not in visited:
        # print("increasing count")
        # print((r,c))

        count += 1

  print(count)



  