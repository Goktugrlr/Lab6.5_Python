#Task1
def find_same_elements(list1, list2):
    list3 = []

    for elements in list1:
        if elements in list2:
            list3.append(elements)

    return list3


list1 = [1, 2, 3, 4, 5, 6]
list2 = [5, 6, 7, 8, 9, 10]
print("Here are common elements of 'list1' and 'list2':", find_same_elements(list1, list2))


#Task2
def find_palindromes(list):
    palindromes = []

    for words in list:
        if words == words[::-1]:
            palindromes.append(words)

    return palindromes


stringList = ["noon", "car", "cake", "tenet", "door", "level"]
print("Here are palindromes from 'stringList':", find_palindromes(stringList))


#Task3
def find_primes(list):
    primeList = list.copy()

    for i in range(2, max(primeList) + 1):
        if i in primeList:
            for j in range(i * 2, max(primeList) + 1, i):
                if j in primeList:
                    primeList.remove(j)

    return primeList


numberList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print("Here are prime numbers from 'numberList':", find_primes(numberList))


#Task4
def anagrams(word, word_list):
    output = []
    word = word.lower().replace(" ", "")
    sorted_input = sorted(word)

    for targetWords in word_list:
        targetWords = targetWords.lower().replace(" ", "")
        sorted_target_words = sorted(targetWords)

        if sorted_input == sorted_target_words:
            output.append(targetWords)

    return output


input_word = "live"
print("Here are anagram(s) of", input_word, ":", anagrams(input_word, ["computer", "evil", "google", "pasta", "banana"]))
