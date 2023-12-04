def getInput(filename):
  with open(filename, 'r') as file:
    input = file.readlines()
    input = [x.strip() for x in input]
    for index, row in enumerate(input):
      input[index] = list(row)
    return input

def expandOnDigit(input, row, col,visited):
  
    left,right = col, col

    while (left - 1 >= 0 and input[row][left - 1].isdigit()) or (right + 1 < len(input[row]) and input[row][right + 1].isdigit()):
      if left - 1 >= 0 and input[row][left - 1].isdigit():
        left -= 1
      if right + 1 < len(input[row]) and input[row][right + 1].isdigit():
        right += 1
    
    number = int("".join(input[row][left:right + 1]))
    for i in range(left, right + 1):
      visited.add((row, i))

    return number


  

input = getInput('input.txt')

DIRECTIONS = [
  (-1, -1),
  (-1, 0),
  (-1, 1),
  (0, -1),
  (0, 1),
  (1, -1),
  (1, 0),
  (1, 1)
]

# loop through each character in the 2d array, 
#   if the current character is a symbol, 
#     perform a check on it's surrounding characters
#       if  there is a number char neighbouring the symbol, check if the number char belongs to a number that we already added previously:
#         if it doesn't, expand on that number char to get the full number and then add each number digit into the set so that it is visted, then perform addtion to the overall sum

#each index in visited will be marked as (row,col)
visited = set()
sum = 0

for row in range(len(input)):
  for col in range(len(input[row])):
    
    if not input[row][col].isdigit() and input[row][col] != ".":

      for direction in DIRECTIONS:
        newRow = row + direction[0]
        newCol = col + direction[1]

        if newRow >= 0 and newRow < len(input) and newCol >= 0 and newCol < len(input[row]):
          if input[newRow][newCol].isdigit() and (newRow,newCol) not in visited:
            number = expandOnDigit(input, newRow, newCol, visited)
            sum += number


print(sum)
            

            





