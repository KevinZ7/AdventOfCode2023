# get input into columns and rows

# go through each column, if characters are all ".", add the column to the emptyCol list
# go through each row, if characters are all ".", add the row to the emptyRow list

# go through all input and find the galaxy coordinates, put them into list (row,col)

# for each star x, get the distance for each star y from 0:x, by doing a loop, if row or col in emptyRol or emptyCol, count += scale, otherwise count += 1

def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    return [x.strip() for x in input]

def findEmptyCols(input):
  emptyCols= []
  for i,col in enumerate(zip(*input)):
    if all([ch=='.' for ch in col]):
      emptyCols.append(i)
  
  return set(emptyCols)

def findEmptyRows(input):
  emptyRows = []
  for i,row in enumerate(input):
    if all([ch=='.' for ch in row]):
      emptyRows.append(i)
  
  return set(emptyRows)



if __name__ == "__main__":
  input = getInput("input.txt")
  m,n = len(input),len(input[0])

  emptyCols = findEmptyCols(input)
  emptyRows = findEmptyRows(input)

  galaxies = []
  for i,row in enumerate(input):
    for j,col in enumerate(row):
      if col == "#":
        galaxies.append((i,j))
  scale = 2
  total = 0
  for i,galaxy in enumerate(galaxies):
    row1,col1 = galaxy
    for j,pairGalaxy in enumerate(galaxies[:i]):
      row2,col2 = pairGalaxy

      for r in range(min(row1,row2),max(row1,row2)):
        total += scale if r in emptyRows else 1
      
      for c in range(min(col1,col2),max(col1,col2)):
        total += scale if c in emptyCols else 1
    
  print(total)
    

  