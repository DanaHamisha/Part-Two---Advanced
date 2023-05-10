from functools import reduce


# ex1
def check_id_valid(id_number):
    """check if the id is current"""
    # convert the int into a list of numbers
    number_list = [int(d) for d in str(id_number)]

    # the first step
    step_one_list = [x * 1 if i % 2 == 0 else x * 2 for i, x in enumerate(number_list)]

    # the second step
    step_two_list = [x % 10 + x // 10 if x > 9 else x for x in step_one_list]

    # sum all the digits
    sum_list = reduce(lambda n, x: n + x, step_two_list)

    return sum_list % 10 == 0


# ex4
def id_generator(start_id):
    """Generator function that yields valid ID numbers in the range (start_id, 999999999)"""
    for i in range(start_id, 1000000000):
        if check_id_valid(i):
            yield i


# ex2
class IDIterator:
    def __init__(self, start_id):
        self._id = int(start_id)
        self._current_id = self._id - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._current_id += 1
        while not check_id_valid(self._current_id):
            self._current_id += 1
        if self._current_id > 999999999:
            raise StopIteration
        return self._current_id


def print_using_gen(input_id):
    print("\nID from generator---->")
    # ex4
    # Create the generator
    gen = id_generator(int(input_id))

    # Iterate over the first 10 values
    for i in range(10):
        print(str(next(gen)))


def print_using_it(input_id):
    # create an iterator
    id_iter = IDIterator(int(input_id))
    print("\nID from iterator---->")
    # Iterate over the first 10 values
    for i in range(10):
        print(str(next(id_iter)))


# ex6
def wanted_print(input_id, print_way):
    """print in the wanted way"""
    if print_way == 'it':
        print_using_it(input_id)
    else:
        print_using_gen(input_id)


def main():
    input_id = input("Enter ID: ")
    print_way = input("Generator or Iterator? (gen/it)? ")
    wanted_print(input_id, print_way)


if __name__ == '__main__':
    main()
