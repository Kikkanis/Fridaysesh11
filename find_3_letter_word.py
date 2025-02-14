# find 3 letter words starting with b or B
punctuation = ",.?!;:"  # puncuation we want to get rid of
def find_words(filename):

    #prints 3 letter words starting from b from a file
    #: param filename: the name of the filename:
    #return: none (nothing)

    with open(filename) as f:
        for line in f:
            for p in punctuation:
                line = line.replace(p," ")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
find_words("input.txt")
