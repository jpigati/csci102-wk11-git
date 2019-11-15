# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        number = fibs[i] + fibs[i-1]
        fibs.append(number)       

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
