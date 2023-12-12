def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    input = [x.strip().split() for x in input]
    for row in range(len(input)):
      for col in range(len(input[row])):
        input[row][col] = int(input[row][col])

    return input

def getNext(numbers):
  if len(numbers) == 0:
    return 0
  
  newNumber = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

  return numbers[-1] + getNext(newNumber)

if __name__ == '__main__':
  input = getInput('input.txt')
  total = 0
  for line in input:
    total += getNext(line)
  
  print(total)
  

