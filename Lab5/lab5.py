import operator as op

operators = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

running = True

print("rpn calculator, type  \"q\" when you want finish")

if __name__ == "__main__":
    while running:
        stack = []
        print("Give me data:")
        data = input()

        if data.find('q') != -1:
            running = False
            continue

        if len(data) < 5:
            print("Your data is not valid")
            continue

        for item in data.split(" "):
            if item in operators:
                res = operators[item](stack.pop(), stack.pop())
            else:
                res = float(item)

            stack.append(res)

        if len(stack) == 1:
            print(stack.pop())

    print("End of program")

