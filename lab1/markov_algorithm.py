class Rule:
    def __init__(self, left, right, terminal=False):
        self.left = left
        self.right = right
        self.terminal = terminal

    def __str__(self):
        if self.terminal:
            return self.left + " -> " + self.right + "."
        return self.left + " -> " + self.right


class MarkovAlgorithm:
    def __init__(self, word, rules):
        self.word = word
        self.rules = rules
        self.stopped = False

    def step(self):
  
        for rule in self.rules:

            if rule.left in self.word:

                self.word = self.word.replace(
                    rule.left,
                    rule.right,
                    1
                )

                if rule.terminal:
                    self.stopped = True

                return True

        self.stopped = True
        return False

    def run(self, max_steps=100):
        steps = 0

        while not self.stopped and steps < max_steps:
            if not self.step():
                break

            steps += 1

        print("\nAlgorithm stopped.")
        print("Steps:", steps)
        print("Result:", self.word)

    def show(self):
        print("\nCurrent word:", self.word)

    def show_rules(self):
        print("\nRules:")

        for i, rule in enumerate(self.rules, 1):
            print(i, ".", rule)

rules = [
    Rule("01", "10"),
    Rule("10", "01", terminal=True)
]

def main_menu():

    print("================================")
    print("       MARKOV ALGORITHM")
    print("================================")

    word = input("Enter the word: ")

    algorithm = MarkovAlgorithm(word, rules)

    while True:

        print("\n================================")
        print("             MENU")
        print("================================")
        print("1. Show current word")
        print("2. Make one step")
        print("3. Run algorithm")
        print("4. Show rules")
        print("5. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            algorithm.show()

        elif choice == "2":
            print("\nMaking one step...")

            if algorithm.step():
                algorithm.show()
            else:
                print("No rule can be applied.")

        elif choice == "3":
            print("\nRunning algorithm...")
            algorithm.run()

        elif choice == "4":
            algorithm.show_rules()

        elif choice == "5":
            print("\nProgram finished.")
            break

        else:
            print("\nInvalid choice.")
            print("Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()