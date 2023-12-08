# Go through the input and categorize each hand into the type it belongs to
# For each type, starting at the lowest one, sort them by the *second rule*
# Then, calculate the total winning of each type then add the total winnings of all types together

HIGH_CARD = 'high card'
ONE_PAIR = 'one pair'
TWO_PAIR = 'two pair'
THREE_OF_A_KIND = 'three of a kind'
FULL_HOUSE = 'full house'
FOUR_OF_A_KIND = 'four of a kind'
FIVE_OF_A_KIND = 'five of a kind'


#order 2,3,4,5,6,7,8,9,T,J,Q,K,A
      #map T -> B
      #map J -> C
      #map Q -> D
      #map K -> E
      #map A -> F
CARD_MAPPING ={
  '2':'2',
  '3':'3',
  '4':'4',
  '5':'5',
  '6':'6',
  '7':'7',
  '8':'8',
  '9':'9',
  'T':'B',
  'J':'C',
  'Q':'D',
  'K':'E',
  'A':'F'
}


def getInput(filename):
  with open(filename,'r') as f:
    input = f.readlines()
    input = [(line.strip().split()[0],line.strip().split()[1]) for line in input]
    for i in range(len(input)):
      formatedHand = ''
      for card in input[i][0]:
        formatedHand += CARD_MAPPING[str(card)]
      input[i] = (formatedHand,input[i][1])

    return input

def getType(hand):
  #hand is a string of 5 cards
  # turn the hand into a dictionary of card:count
  cardCount = {}
  for card in hand:
    if card in cardCount:
      cardCount[card] += 1
    else:
      cardCount[card] = 1

  numUniqueCards = len(cardCount.keys())
  # if the dictionary has 5 keys, then return HIGH_CARD
  if numUniqueCards == 5:
    return HIGH_CARD

  # if the dictionary has 4 keys, then return ONE_PAIR
  if numUniqueCards == 4:
    return ONE_PAIR
  # if the dictionary has 3 keys, then return either TWO_PAIR or THREE_OF_A_KIND
  # return TWO_PAIR if max count in dictionary is 2
  # return THREE_OF_A_KIND otherwise
  if numUniqueCards == 3:
    if max(cardCount.values()) == 2:
      return TWO_PAIR
    else:
      return THREE_OF_A_KIND

  # if the dictionary has 2 keys, then return either FULL_HOUSE or FOUR_OF_A_KIND
  # return FULL_HOUSE if max count in dictionary is 3
  # return FOUR_OF_A_KIND otherwise
  if numUniqueCards == 2:
    if max(cardCount.values()) == 3:
      return FULL_HOUSE
    else:
      return FOUR_OF_A_KIND

  #if dictionary has 1 key, then return FIVE_OF_A_KIND
  if numUniqueCards == 1:
    return FIVE_OF_A_KIND

if __name__ == '__main__':
  input = getInput('input.txt')
  
  handTypes = {
    HIGH_CARD: [],
    ONE_PAIR: [],
    TWO_PAIR: [],
    THREE_OF_A_KIND: [],
    FULL_HOUSE: [],
    FOUR_OF_A_KIND: [],
    FIVE_OF_A_KIND: []
  }

  for hand in input:
    handType = getType(hand[0])
    handTypes[handType].append(hand)
  
  total = 0
  rank = 1


  for handType in handTypes:
    if len(handTypes[handType]) > 0:

      #ISSUE: currently we are sorting by the ascii value, but since we have custom rule to follow for which card is bigger than the other, we cant use simple sorting
      # idea: we can modify the initial data (change value of cards suits)  so that they appear in the correct order for normal ascii sorting
      #order 2,3,4,5,6,7,8,9,T,J,Q,K,A
      #map T -> B
      #map J -> C
      #map Q -> D
      #map K -> E
      #map A -> F


      handTypes[handType].sort(key=lambda x: x[0])
      for hand in handTypes[handType]:
        total += rank * int(hand[1])
        rank += 1

  print(total)