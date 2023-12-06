def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    for index, row in enumerate(input):
      temp = row.split(':')
      cards = temp[1].split('|')
      winningNumbers = cards[0].strip()
      myCards = cards[1].strip()

      winningNumbers = winningNumbers.split(' ')
      myCards = myCards.split()

      input[index] = [set(winningNumbers), myCards]
    
    return input


input = getInput('input.txt')
sum = 0
for row in input:
  winningNumbers = row[0]
  myCards = row[1]

  count = 0
  for card in myCards:
    if card in winningNumbers:

      count += 1

  if count > 0:

    sum += 2 ** (count - 1)

print(sum)
