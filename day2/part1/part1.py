

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
print(input)
sum = 0
for game in input:
  valid = True
  for set in game["sets"]:
    if ("red" in set and set["red"] > 12) or ("green" in set and set["green"] > 13) or ("blue" in set and set["blue"] > 14):
      valid = False
  
  if valid:
    sum+= int(game["game"])

print(sum)