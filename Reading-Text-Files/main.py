import re


# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, "r") as f:
        text = f.read()

    return text


def count_words():
    text = read_file_content("./story.txt").strip()
    # [assignment] Add your code here
    word_arr = re.split("[\\s+.?\n,]", text)
    word_dict = {}
    for word in word_arr:
        word_dict[word] = len(word)
    return word_dict


print(count_words())
