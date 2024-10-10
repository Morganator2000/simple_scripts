
def calculateMortar(type, volume):
    portlandCement = None
    lime = None
    aggregate = None
    match type:
        case "N":
            portlandCement = 0.125 * volume
            lime = 0.125 * volume
            aggregate = 0.75 * volume
        case _:
            print("Why would you do this?")
    resultsArray = [portlandCement,lime,aggregate]
    return resultsArray

myType = input("Enter your mortar type: ")
myVolume = input("Enter your volume: ")

myRecipe = calculateMortar(myType,int(myVolume))

print("The Portland Cement you need is " + str(myRecipe[0]) + " cubic meters.")
print("The lime you need is " + str(myRecipe[1]) + " cubic meters.")
print("The aggregate you need is " + str(myRecipe[2]) + " cubic meters.")