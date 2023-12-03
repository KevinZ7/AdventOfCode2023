

def getInput(filename):
  with open(filename, 'r') as file:

    #format data into:
    # {
    #   game: 1,
    #   sets: [{blue: x, red: y, green: z}, {blue: x, red: y, green: z}]
    # }
    formatted_input = []
    input = file.readlines()
    input = [x.strip() for x in input]

    for x in input:
      formattedEntry = {}
      gameInfo, setsData =  x.split(":")
      gameNumber = gameInfo.split()[1].strip()
      formattedEntry["game"] = gameNumber
      formattedEntry["sets"] = []

      setsData = setsData.split(';')
      for setData in setsData:
        setData = setData.strip().split(",")
        formattedSetData = {}
        for data in setData:
          count, color = data.strip().split()
          formattedSetData[color] = int(count)
        formattedEntry["sets"].append(formattedSetData)
      
      formatted_input.append(formattedEntry)

  
    return formatted_input


input = getInput('input.txt')

powerSum = 0
for game in input:
  redAmount = 0
  greenAmount = 0
  blueAmount = 0
  for set in game["sets"]:
    if "red" in set:
      redAmount = max(redAmount, set["red"])
    if "green" in set:
      greenAmount = max(greenAmount, set["green"])
    if "blue" in set:
      blueAmount = max(blueAmount, set["blue"])
  
  powerSum += redAmount * greenAmount * blueAmount

print(powerSum)