# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack == [] or not are_matching(opening_brackets_stack[-1].char,next):
                return i+1
            else:
                opening_brackets_stack.pop(-1)

    if opening_brackets_stack == []:
        return "Success"
    else:
        return opening_brackets_stack[-1].position

def main():
    text = input()
    if "I" in text[:1]:
        text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
