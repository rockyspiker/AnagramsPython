from random import randint, shuffle

def getWordLenAmount(length): #gets how many word with set length are in the file
  with open('words.txt', 'r') as words:
    amount = 0
    for rawWord in words:
      word = rawWord.strip()
      if len(word) == length:
        amount += 1
  return amount

def getWord(length, index): #gets the nth word with set length
  result = ''
  with open('words.txt', 'r') as words:
    passedWords = 0
    for rawWord in words:
      word = rawWord.strip()
      if len(word) == length:
        if passedWords < index:
          passedWords += 1
        elif passedWords == index:
          result = word
          passedWords += 1
  return result

def scrambleWord(word):
  word = list(word)
  shuffle(word)
  return ''.join(word)

def isAnagram(word, anagram):
  if len(word) < len(anagram):
    return False
  anagram = list(anagram)
  wIndex = 0
  while wIndex < len(word):
    aIndex = 0
    foundMatch = False
    while aIndex < len(anagram):
      if wIndex < len(word):
        if anagram[aIndex] == word[wIndex]:
          anagram.pop(aIndex)
          wIndex += 1
          foundMatch = True
        else:
          aIndex += 1
      else:
        return False
    if not foundMatch:
      wIndex += 1
  if len(anagram) == 0:
    return True
  else:
    return False

def getAnagrams(word):
  anagrams = []
  for i in range(len(word)-2):
    anagrams.append([])
  with open('words.txt', 'r') as words:
    for rawWord in words:
      anagram = rawWord.strip()
      if len(anagram) > 2 and isAnagram(word, anagram):
        anagrams[len(anagram)-3].append(anagram)
  return anagrams

def main(scrambled, anagrams):
  if scrambled:
    for x in range(len(anagrams)):
      if not anagrams[x]:
        print('~~~You Win!~~~')
        return
  if not scrambled:
    word = getWord(6, randint(1, getWordLenAmount(6)+1))
    scrambled = scrambleWord(word)
    print('TEST: base word is', word, '\n')
  if not anagrams:
    anagrams = getAnagrams(scrambled)
  print(str(scrambled) + ':\n')
  for i in range(len(anagrams)):
    nestListLen = 0
    for j in range(len(anagrams[i])):
      nestListLen += 1
    print(nestListLen, str(i+3) + '-letter words')
  guess = input('\nEnter a guess: ')
  if guess == 'q':
    print('\nYou gave up.\nThe anagrams are:')
    newAnagrams = []
    for i in range(len(anagrams)):
      for j in range(len(anagrams[i])):
        newAnagrams.append(anagrams[i][j])
    print(newAnagrams)
    return
  if len(guess) <= len(scrambled):
    hasMatch = False
    for anagram in anagrams[len(guess)-3]:
      if anagram == guess:
        anagrams[len(guess)-3].remove(anagram)
        print('Correct!\n')
        hasMatch = True
        main(scrambled, anagrams)
    if hasMatch == False:
      print('Incorrect!\n')
      main(scrambled, anagrams)
  else:
    print('Invalid guess, words of minimum length three.')
    main(scrambled, anagrams)
      

main('', [])

# main('win', getAnagrams('win'))