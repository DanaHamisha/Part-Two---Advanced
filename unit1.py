# ex1- print the longest name
def max_word_in_file():
    with open(r'C:\Users\user\Desktop\sigitDana\names.txt') as file_input: print(
        max((line.strip() for line in file_input), key=len))


# ex2- print the sum lengths
def sum_lengths():
    with open(r'C:\Users\user\Desktop\sigitDana\names.txt') as file_input: print(
        sum(len(line.strip()) for line in file_input))


# ex3- print the min names
def min_word_in_file():
    with open(r'C:\Users\user\Desktop\sigitDana\names.txt') as f:
        lines = [line.strip() for line in f]
        shortest_length = len(min(lines, key=len))
        list(map(lambda line: print(line), filter(lambda line: len(line) == shortest_length, lines)))


# ex4- create length file
def lengths_file():
    with open(r'C:\Users\user\Desktop\sigitDana\names.txt') as f, open(
            r'C:\Users\user\Desktop\sigitDana\name_length.txt', 'w') as out_f:
        out_f.writelines(str(len(line.strip())) + "\n" for line in f)


# ex5- names in certain length
def names_in_len():
    name_length = int(input("Enter name length: "))
    with open(r'C:\Users\user\Desktop\sigitDana\names.txt') as f:
        list(
            map(lambda line: print(line.strip()), filter(lambda line: len(line.strip()) == name_length, f.readlines())))


def main():
    max_word_in_file()
    sum_lengths()
    min_word_in_file()
    lengths_file()
    names_in_len()


if __name__ == '__main__':
    main()
