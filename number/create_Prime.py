import math
from sympy import isprime


def main():
    file_name = "number/prime_numbers.txt"
    limit = 2000  # 100 tỷ

    with open(file_name, "w") as file:
        for number in range(2, limit):
            if isprime(number):
                file.write(str(number) + "\n")

    print("Đã tạo xong tệp prime_numbers.txt")


if __name__ == "__main__":
    main()
