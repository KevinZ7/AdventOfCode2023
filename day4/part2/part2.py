def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    for index, row in enumerate(input):
      temp = row.split(':')
      cardNumber = temp[0][4:].strip()
      cards = temp[1].split('|')
      winningNumbers = cards[0].strip()
      myCards = cards[1].strip()


      winningNumbers = winningNumbers.split(' ')
      myCards = myCards.split()

      input[index] = [cardNumber,set(winningNumbers), myCards]
    
    return input

input = getInput('input.txt')


#create a dictionary to keep track of how many cards we have by card number, initialize every card amount to 1
cardsAmount = {str(i): 1 for i in range(1,len(input) + 1) }


#for every card i, check how many matching numbers x we have, for cards from i+1 to i+x, cardsAmountp[i+x] += cardsAmount[i]

for card in input:
  cardNumber = card[0]
  winningNumbers = card[1]
  myCards = card[2]

  count = 0
  for card in myCards:
    if card in winningNumbers:

      count += 1

  for x in range(1,count + 1):
    copyCardNumber = str(int(cardNumber) + x)
    cardsAmount[copyCardNumber] += cardsAmount[cardNumber]

sum = 0

for card in cardsAmount:
  sum += cardsAmount[card]

print(sum)
