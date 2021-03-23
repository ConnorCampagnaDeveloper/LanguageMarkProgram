

languages = []
testResults = []
loopCounter = 1

for i in range(1,4):
    print("What Is Language", loopCounter)
    lang = input()
    languages.append(lang)
    loopCounter = loopCounter + 1

loopCounter = 0

for i in range(1,4):
    print("What Did You Get In Your", languages[loopCounter], "test?")
    result = int(input())
    testResults.append(result)
    loopCounter = loopCounter + 1

if testResults[0] > 75 and testResults[1] > 75 or testResults[2] > 75:
    print("Congrats You Passed Your Tests! You Got", str(testResults[0]) + "%", "on", languages[0],str(testResults[1]) + "%", "on", languages[1] ,str(testResults[2]) + "%", "on", languages[2])
else : 
    print("You Did Not Pass!") 