VOWELS = set("aeiou")

def identify_vowels(sentence):
    return [character for character in sentence if character.lower() in VOWELS]

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    vowels = identify_vowels(sentence)
    print("Vowels:", vowels)
    print("Total vowels:", len(vowels))
