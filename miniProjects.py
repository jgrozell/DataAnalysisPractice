words = ['racecar', 'madAm', 'Civic', 'state']

for word in words:
    
    wordSplit = list(word.lower())
    idx = 0
    palidrome = True

    while idx < len(wordSplit)/2:
        
        if(wordSplit[idx] != wordSplit[len(wordSplit)-idx-1]):
            palidrome = False
            
        idx = idx + 1
        
    print(palidrome)