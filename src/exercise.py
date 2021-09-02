def main():
    #write your code below this line
    sum = 0
    count = 0
    even = 0
    odd = 0
    while True:
        num = int(input("Give numbers:"))
        if (num == -1):
            print("Thx! Bye!")
            print("Sum: " + str(sum))
            print("Numbers: " + str(count))
            print("Average: " + str(sum / count))
            print("Even: " + str(even))
            print("Odd: " + str(odd))
            break
        elif (num >= 0):
            sum += num
            count += 1
            even += 1
        elif (num < 0):
            sum += num
            count += 1
            odd += 1


if __name__ == '__main__':
    main()
