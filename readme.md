# Anagrams Readme

## getLenWordAmount
This function takes an int argument of which it counts how many words are within the txt file that have that length. Returns the count.

## getWord
This function takes two arguments, one of the word length, and the second is the nth word with that length. (in main it calls for a random int based on getLenWordAmount)

## scrambleWord
Pretty obvious on what this function does. It takes the word and scrambles it into a random order.

## isAnagram
This function takes two arguments, one of which is the base word the other is the possible anagram. Putting anagram into a list, it slowly pops off the letters based on if they are within the base word, the base word's index is then bumped up one to avoid repetition.

## getAnagrams
Using isAnagram, this function goes through the text file and makes a nested list of all anagrams.

## main
This function is a recursively called function that will continue to run and recieve guesses, compare it to the list of anagrams, etc. until the user enter q for quit or have guessed all anagrams. (Checks if there is a word argument but empty anagrams list.)