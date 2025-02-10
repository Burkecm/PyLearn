# Generate a PW based on user input
import random as rand
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

class Password:
    def __init__(self, num_letters, num_numbers, num_symbols):
        self.num_letters = num_letters
        self.num_numbers = num_symbols
        self.num_symbols = num_numbers

    def generate(self):
        let = [rand.choice(letters) for _ in range(self.num_letters)]
        num = [rand.choice(numbers) for _ in range(self.num_numbers)]
        sym = [rand.choice(symbols) for _ in range(self.num_symbols)]
        password_list = let + num + sym
        rand.shuffle(password_list)
        print(password_list)
        return str("".join(password_list))