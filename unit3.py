import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_char, index):
        self._message = f"The username contains an illegal character '{illegal_char}' at index {index}"
        super().__init__(self._message)
        self._illegal_char = illegal_char
        self._index = index


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 3 characters"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 16 characters"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 8 characters"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 40 characters"


def check_input(username, password):
    try:
        if not is_valid_username(username):
            for index, c in enumerate(username):
                if c not in string.ascii_letters + string.digits + '_':
                    raise UsernameContainsIllegalCharacter(c, index)
            raise UsernameTooShort() if len(username) < 3 else UsernameTooLong()

        if not is_valid_password(password):
            if not any(char.isupper() for char in password):
                raise PasswordMissingUppercase()
            elif not any(char.islower() for char in password):
                raise PasswordMissingLowercase()
            elif not any(char.isdigit() for char in password):
                raise PasswordMissingDigit()
            elif not any(char in string.punctuation for char in password):
                raise PasswordMissingSpecial()
            raise PasswordTooShort() if len(password) < 8 else PasswordTooLong()

        print("OK")
    except Exception as e:
        print(e)


# check if the username valid
def is_valid_username(username):
    legal_chars = string.ascii_letters + string.digits + '_'

    # Check username length
    if len(username) < 3 or len(username) > 16:
        return False

    # Check if all chars are legal
    for c in username:
        if c not in legal_chars:
            return False

    # If all checks pass, return True
    return True


# check if the username valid
def is_valid_password(password):
    # Check password length
    if len(password) < 8 or len(password) > 40:
        return False

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if password contains at least one special character
    if not any(char in string.punctuation for char in password):
        return False

    # If all checks pass, return True
    return True


def main():
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")


if __name__ == '__main__':
    main()
