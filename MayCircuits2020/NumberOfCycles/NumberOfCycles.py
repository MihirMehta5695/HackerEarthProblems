def no_of_cycles(number):
    return ((number*number)+1) - number

def main():
    queries = int(input())
    for i in range(0,queries):
        print(no_of_cycles(int(input())))


if __name__ == '__main__':
    main()
