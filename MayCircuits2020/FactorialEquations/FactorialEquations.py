def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n):
            product = product * i;
        return product



def run():
    user_input = input()
    numbers = user_input.split(" ")
    base = int(numbers[0])
    power = int(numbers[1])
    calcPower = factorial(power) % 10
    final_answer = base ** calcPower
    final_answer = str(final_answer)
    final_answer = final_answer[len(final_answer) - 1]
    print(final_answer)


if __name__ == '__main__':
    run()
