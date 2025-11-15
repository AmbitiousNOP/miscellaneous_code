import detectEnglish
import vigenereCipher
import pyperclip
from math import log


# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("popular.txt").read().split()
wordcost = dict((k.upper(), log((i+1)*log(len(words))))
                for i, k in enumerate(words))
maxword = max(len(x) for x in words)


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k, c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1, len(s)+1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


def main():
    ciphertext = """TLFRJKLNYUSPKKMUXNFDEZNNFDTKSAUUSPO"""
    # ciphertext = """TzxisnzeccjxkgnfqlolmysbbqqIlxcz"""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackVigenereDictionary(ciphertext):
    fo = open('popular.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()  # Remove the newline at the end.
        decryptedText = vigenereCipher.decryptMessage(
            word.upper(), ciphertext.upper())

        # print(decryptedText)
        # Check with user to see if the decrypted key has been found:
        guess = infer_spaces(decryptedText)
        if detectEnglish.isEnglish(guess, wordPercentage=10):
            # print(guess.count(' '))
            print(infer_spaces(decryptedText), f"KEY: {word.upper()}")

    """
        matched_words = []
        tmp_decrpt = decryptedText
        for word in words:
            # print(f"COMPARING {decryptedText} to {word}")
            if word.strip() in tmp_decrpt:
                # tmp_decrpt = decryptedText
                matched_words.append(word)
                idx = tmp_decrpt.index(word.strip())
                tmp_decrpt = tmp_decrpt[:idx] + \
                    tmp_decrpt[idx + len(word.strip()):]
                # print(tmp_decrpt)
            # quit(1)
        if len(matched_words) >= 5:
            print(decryptedText, f"MATCHED WORDS: {matched_words}")
        matched_words.clear()
    """

    """
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText
        """


if __name__ == '__main__':
    main()
