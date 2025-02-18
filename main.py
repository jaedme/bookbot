def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_dict = {}

    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return letter_dict


def main():
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()
        answer = count_words(text)
        count = count_letters(text)

        #how to sort the dictionary
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        
        print(f"--- Begin report of {file.name} ---")
        print(f"{answer} words found in the document\n")
        for key, value in sorted_dict.items():
            print(f"The '{key}' character was found {value} times")
        print('--- End report ---')




if __name__ == "__main__":
    main()
