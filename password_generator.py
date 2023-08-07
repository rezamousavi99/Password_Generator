from string import ascii_letters, digits
from random import choice, sample

class PasswordGenerator:
    letters = ascii_letters
    digits = digits
    symbols = "~!@#$%^&*()_+-|:;?></\\{}"

    total = letters + digits + symbols

    def __init__(self, length=12) -> None:
        self.length = length
        self.password = ""  

    def generate(self):
        for i in range(0, self.length):
            # self.password += choice(PasswordGenerator.total)
            self.password = "".join(sample(PasswordGenerator.total, self.length))
        return self.password

def command():
    print('Choose an option:\n\t1.Generate Password\n\t2.Exit')
    return input('Enter a command: ')

def main():
    while(True):
        user_input = command()

        match user_input:
            case '1':
                length = int(input('Enter length of Password: '))
                p = PasswordGenerator(length)
                print(f'your password: {p.generate()})')
                print(20 * '*')

            case '2':
                print('exiting...')
                break


if __name__ == '__main__':
    main()