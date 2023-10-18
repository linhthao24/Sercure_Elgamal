import math
import random
import csv
import json
from sympy import isprime


def get_random_prime_and_generator(file_path):
    prime_numbers = []

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề

        for row in reader:
            prime_number = int(row[0])  # Lấy giá trị số nguyên tố từ cột đầu tiên
            prime_numbers.append(prime_number)

    random_prime_number = random.choice(prime_numbers)

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề

        for row in reader:
            if int(row[0]) == random_prime_number:
                generators = row[1].split(",")
                random_generator = random.choice(generators)
                break

    return random_prime_number, random_generator.strip()


def createKey(file_path):
    p, g = get_random_prime_and_generator(file_path)
    g = int(g)
    x = random.randint(2, p - 1)
    y = pow(g, x, p)
    key_pair = {"public_pgy": [p, g, y], "secrets_px": [p, x]}
    return key_pair


def trans_data_in(data, p):
    i = 0
    num = ""
    data_array = []
    while i < len(data):
        num += data[i]
        num1 = int(num)
        if not math.isnan(num1) and num1 > p:
            num = num[:-1]
            i -= 1
            num2 = int(num)
            data_array.append(num2)
            num = ""
        i += 1
    if num != "":
        num2 = int(num)
        data_array.append(num2)
    return data_array


def encrypt(data, key_public):
    p = key_public[0]
    g = key_public[1]
    y = key_public[2]

    data_array = trans_data_in(data, p)
    C = []
    k = random.randint(2, p - 1)
    K = pow(y, k, p)
    R = pow(g, k, p)
    for i in range(len(data_array)):
        C.append((K * data_array[i]) % p)
    Ciphertext = {"information": C, "R": R}
    return Ciphertext


file_path = "./number/generators.csv"


def main_input():
    get_data = open("./data/input.txt", "r")
    if get_data == -1:
        raise Exception("can't read file")
    data = ""
    for line in get_data:
        data += line.strip()
    get_data.close()
    keys = createKey(file_path)
    key_secret = keys["secrets_px"]
    key_public = keys["public_pgy"]
    data_send = encrypt(data, key_public)
    print(data_send)
    # Lưu trường "information" vào file data_send.json
    with open("./data/data_send.json", "w") as file:
        json.dump(data_send["information"], file)
    # Lưu trường "R" vào file public.txt
    with open("./data/key_trans.txt", "w") as file:
        R = data_send["R"]
        file.write(str(R))

    # Lưu key_public vào file key_public.json
    with open("./data/key_public.json", "w") as file:
        json.dump(key_public, file)

    # Lưu key_secret vào file key_secret.json
    with open("./data/key_secret.json", "w") as file:
        json.dump(key_secret, file)


if __name__ == "__main__":
    main_input()
