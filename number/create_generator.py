import csv
import math
from sympy import isprime, factorint


def create_Generator(p):
    generators = []
    phi_p = p - 1  # Số Euler phi của p

    for g in range(2, p):
        if math.gcd(g, p) != 1:
            continue

        isGenerator = True
        prime_factors = factorint(phi_p)

        for prime_factor in prime_factors:
            if pow(g, phi_p // prime_factor, p) == 1:
                isGenerator = False
                break

        if isGenerator:
            generators.append(g)

    return generators


def main():
    input_file = "number/prime_numbers.txt"
    output_file = "number/generators.csv"

    with open(input_file, "r") as file_in, open(
        output_file, "w", newline="", encoding="utf-8"
    ) as file_out:
        writer = csv.writer(file_out)
        writer.writerow(["Số nguyên tố", "Phần tử sinh"])

        for line in file_in:
            prime_number = int(line.strip())
            generator = create_Generator(prime_number)
            writer.writerow([prime_number, generator])

    print(f"Kết quả đã được ghi vào file CSV: {output_file}")


if __name__ == "__main__":
    main()
