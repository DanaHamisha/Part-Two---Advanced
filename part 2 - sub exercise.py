import string
from functools import reduce
import functools
import winsound
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


def combine_coins2(coin, numbers):
    return ''.join(list(map(lambda num: coin + str(num) + " ,", numbers)))


# ex 1.1.2
def double_letter(my_str):
    return "".join(list(map(lambda l: l + l, my_str)))


# ex 1.1.3
def four_dividers(number):
    return list(filter(lambda num: num % 4 == 0, range(1, number)))


# ex 1.1.4
def sum_of_digits(number):
    return reduce(lambda x, y: int(x) + int(y), str(number))


# ex 1.3.1
def intersection(list_1, list_2):
    return reduce(lambda acc, val: acc + [val] if val in list_2 and val not in acc else acc, list_1, [])


# ex 1.3.2
def is_prime(number):
    return number > 1 and reduce(lambda acc, val: acc and bool(number % val), range(2, int(number), True))


# ex 1.3.3
def is_funny(string):
    return reduce(lambda acc, char: acc and (char == 'h' or char == 'a'), string, True)


# ex 1.3.4
def figure(password):
    return ''.join(list(
        map(lambda l: chr((ord(l) - ord('a') + 2) % 26 + ord('a')) if l not in string.punctuation and l != ' ' else l,
            password)))


# ex 2.2.2 + ex 2.3.3
class Dog:
    _count_animals = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Dog._count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    @classmethod
    def get_count_animals(cls):
        return cls._count_animals


# ex 2.3.4
class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """

    def __init__(self):
        self._x = 0
        self._y = 0
        self._red = 0
        self._green = 0
        self._blue = 0

    def __init__(self, x, y, red):
        self._x = x
        self._y = y
        self._red = red
        self._green = 0
        self._blue = 0

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color = f'({self._red}, {self._green}, {self._blue})'
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color += ' Blue'
        elif self._red == 0 and self._blue == 0 and self._green > 50:
            color += ' Green'
        elif self._green == 0 and self._blue == 0 and self._red > 50:
            color += ' Red'
        print(f'X: {self._x}, Y: {self._y}, Color: {color}')


# ex 2.4.2
class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, (int, float)):
            return self._thing
        else:
            return len(self._thing)


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


# ex 3.1.3
def raise_stop_iteration():
    i = iter([1, 2, 3])
    next(i)
    next(i)
    next(i)
    next(i)


def raise_zero_division_error():
    a = 1
    b = 0
    c = a / b


def raise_assertion_error():
    x = 10
    y = 5
    assert x < y, "AssertionError: x is not less than y"


# def raise_import_error():
#     import non_existent_module


def raise_key_error():
    my_dict = {"key": "value"}
    print(my_dict["non_existent_key"])


# def raise_syntax_error():
#     len('hello') = 5


# def raise_indentation_error():
#         print("IndentationError function")
#             print("IndentationError function - IndentationError")


def raise_type_error():
    a = "5"
    b = 2
    c = a + b


# ex 3.2.5
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}__CONTENT_END__\n"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__\n"


# ex 3.3.2
class UnderAge(Exception):
    def __str__(self):
        return "Your age is less than 18. You're only " + str(
            self.args[0]) + " years old. Come back in a few years for Ido's birthday."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


# ex 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join(words.get(word, word) for word in sentence.split())


# ex 4.1.3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_primes(start):
    current = start
    while True:
        if is_prime(current):
            yield current
        current += 1


def first_prime_over(n):
    primes = generate_primes(n + 1)
    return next(primes)


# ex 4.2.2
def parse_ranges(ranges_string):
    # First generator: split ranges string and convert ranges to (start, stop) tuples
    range_tuples = ((start, stop) for start, stop in (range_str.split('-') for range_str in ranges_string.split(',')))

    # Second generator: generate all numbers in each range
    numbers = (num for start, stop in range_tuples for num in range(int(start), int(stop) + 1))

    return numbers


# ex 4.3.4
def get_fibo():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second


# ex 5.1.2
def sing():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    all_the = notes.split('-')
    print(type(all_the))
    print(all_the)
    for item in all_the:
        both = item.split(',')
        frequency = freqs[both[0]]
        duration = int(both[1])
        winsound.Beep(frequency, duration)


# ex 5.2.2
def good():
    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i)


# ex 5.3.2
class MusicNotes:
    def __init__(self):
        self._notes = {
            'La': [55, 110, 220, 440, 880],
            'Si': [61.74, 123.48, 246.96, 493.92, 987.84],
            'Do': [65.41, 130.82, 261.64, 523.28, 1046.56],
            'Re': [73.42, 146.84, 293.68, 587.36, 1174.72],
            'Mi': [82.41, 164.82, 329.64, 659.28, 1318.56],
            'Fa': [87.31, 174.62, 349.24, 698.48, 1396.96],
            'Sol': [98, 196, 392, 784, 1568]
        }
        self._notes_list = []
        for octave in range(5):
            for note in self._notes:
                self._notes_list.append((note, octave))
        self._index = 0
        self._max_index = len(self._notes_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._max_index:
            note, octave = self._notes_list[self._index]
            freq = self._notes[note][octave]
            self._index += 1
            return freq
        else:
            raise StopIteration


# ex 6.1.3
def gui():
    # Let's create the Tkinter window
    window = tkinter.Tk()
    window.title("GUI")
    tkinter.Label(window, text="What do I like the most?", font=("Arial", 14), fg="red").pack()

    # creating a function called DataCamp_Tutorial()
    def DataCamp_Tutorial():
        label = tkinter.Label(window, text="This is what I like:")
        label.pack()
        image = Image.open(r'C:\Users\user\Desktop\sigitDana\yumi.jpg')
        photo_image = ImageTk.PhotoImage(image)
        image_label = ttk.Label(window, image=photo_image)
        image_label.image = photo_image  # store a reference to the image to prevent garbage collection
        image_label.pack()

    tkinter.Button(window, text="Click Me to find out !", command=DataCamp_Tutorial).pack()
    window.mainloop()


# ex 6.3.3
def text_to_speech():
    import pyttsx3

    # The text that you want to convert to speech
    my_text = "first time i'm using a package in next.py course"

    # Initialize the Text-to-speech engine
    engine = pyttsx3.init()

    # Set the speed of speech
    engine.setProperty('rate', 150)

    # Convert text to speech
    engine.say(my_text)

    # Play the speech
    engine.runAndWait()


def main():
    # print(combine_coins2('$', range(5)))

    # ex 1.1.2
    # print(double_letter("Dana Hamisha"))

    # ex 1.1.3
    # print(four_dividers(9))
    # print(four_dividers(3))

    # ex 1.1.4
    # print(sum_of_digits(104))

    # ex 1.3.1
    # print(intersection([1, 2, 3, 4], [8, 3, 9]))

    # ex 1.3.2
    # print(is_prime(43))

    # ex 1.3.3
    # print(is_funny("hahahahahaha"))

    # ex 1.3.4
    # password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    # print(figure(password))

    # ex 2.2.2 + ex 2.3.3
    # dog1 = Dog(3, "Lucas")
    # dog2 = Dog(2, "Roy")
    # dog1.birthday()
    # print(dog1.get_age())  # should print 4
    # print(dog2.get_age())  # should print 2
    #
    # dog3 = Dog(3)
    # dog4 = Dog(2, "Roy")
    #
    # print(dog3.get_name())  # prints "Octavio"
    # print(dog4.get_name())
    #
    # dog4.set_name("Dana")
    # print(dog4.get_name())
    # print(Dog.get_count_animals())  # prints 2

    # ex 2.3.4
    # p = Pixel(5, 6, 250)
    # p.print_pixel_info()
    # p.set_grayscale()
    # p.print_pixel_info()

    # ex 2.4.2
    # my_thing = BigThing("balloon")
    # print(my_thing.size())
    # cutie = BigCat("mitzy", 22)
    # print(cutie.size())

    # ex 3.1.3
    # raise_stop_iteration()
    # raise_zero_division_error()
    # raise_assertion_error()
    # raise_import_error()
    # raise_key_error()
    # raise_syntax_error()
    # raise_indentation_error()
    # raise_type_error()

    # ex 3.2.5
    # print(read_file(r"C:\Users\user\Desktop\sigitDana\songs.txt"))

    # ex 3.3.2
    # send_invitation("Rom", 17)
    # send_invitation("Naor", 20)

    # ex 4.1.2
    # print(translate("el gato esta en la casa"))

    # ex 4.1.3
    # print(first_prime_over(1000000))

    # ex 4.2.2
    # print(list(parse_ranges("1-2,4-4,8-10")))
    # print(list(parse_ranges("0-0,4-8,20-21,43-45")))

    # ex 4.3.4
    # fibo_gen = get_fibo()
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))

    # ex 5.1.2
    # sing()

    # ex 5.2.2
    # good()

    # ex 5.3.2
    # notes_iter = iter(MusicNotes())
    #
    # for freq in notes_iter:
    #     print(freq)

    # ex 6.1.3
    # gui()

    # ex 6.3.3
    # text_to_speech()


if __name__ == '__main__':
    main()
