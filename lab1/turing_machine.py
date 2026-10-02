class Rule:
    def __init__(self, initial_state, target_state):
        self.initial_state = initial_state
        self.target_state = target_state

    def __eq__(self, other):
        if isinstance(other, Rule):
            return (self.initial_state, self.target_state) == (
                other.initial_state,
                other.target_state
            )
        return False

    def __hash__(self):
        return hash((self.initial_state, self.target_state))


class TuringMachine:
    def __init__(self, tape, rules):
        self.tape = list(tape)
        self.head = 0
        self.state = "q0"
        self.rules = rules

    def read(self):
        return self.tape[self.head]

    def write(self, symbol):
        self.tape[self.head] = symbol

    def move_right(self):
        self.head += 1

        if self.head >= len(self.tape):
            self.tape.append("_")

    def move_left(self):
        if self.head > 0:
            self.head -= 1

    def step(self):
        current_symbol = self.read()
        current_key = (self.state, current_symbol)

        matching_rule = None

        for rule in self.rules:
            if rule.initial_state == current_key:
                matching_rule = rule
                break

        if matching_rule is None:
            print("No rule found.")
            return False

        next_state, new_symbol, direction = matching_rule.target_state

        self.write(new_symbol)

        if direction == "R":
            self.move_right()

        elif direction == "L":
            self.move_left()

        self.state = next_state

        return True

    def run(self, max_steps=100):
        steps = 0

        while steps < max_steps:

            if not self.step():
                break

            steps += 1

        print("Machine stopped.")
        print("Number of steps:", steps)

    def show(self):
        print("\nTape:", "".join(self.tape))
        print("Head position:", self.head)
        print("State:", self.state)

rules_1 = {
    Rule(("q0", "0"), ("q0", "1", "R")),
    Rule(("q0", "1"), ("q0", "0", "R"))
}

def main_menu():

    print("================================")
    print("       TURING MACHINE")
    print("================================")

    tape = input("Enter the tape : ")

    machine = TuringMachine(tape, rules_1)

    while True:

        print("\n================================")
        print("             MENU")
        print("================================")
        print("1. Show machine")
        print("2. Make one step")
        print("3. Run machine")
        print("4. Show current symbol")
        print("5. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":

            machine.show()

        elif choice == "2":

            print("\nPerforming one step...")

            if machine.step():
                machine.show()

        elif choice == "3":

            print("\nRunning machine...")

            machine.run()

            machine.show()

        elif choice == "4":

            print("\nCurrent symbol:", machine.read())

        elif choice == "5":

            print("\nProgram finished.")
            break

        else:

            print("\nInvalid choice.")
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main_menu()