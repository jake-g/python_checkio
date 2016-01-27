class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try: return self.stack.pop()
        except: return 0

    def peek(self):
        print self.stack[-1]
        return self.stack[-1]
        

def digit_stack(commands):
    s = Stack()
    sum = 0
    for cmd in commands:
        print 'Sum : %d' % sum
        cmd_arg = cmd.split(' ')
        if len(cmd_arg) == 2:
            s.push(cmd_arg[1])
        elif cmd is 'POP':
            sum += int(s.pop())
        elif cmd is 'PEEK':
            sum += int(s.peek())
    print 'final : %d' % sum
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
