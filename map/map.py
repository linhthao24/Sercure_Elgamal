import csv
import random


def generate_unique_values(cd):
    values = []
    while len(values) < 26 + 10 + 5:
        value = random.randint(pow(10, cd - 1), pow(10, cd) - 1)
        if "0" not in str(value) and value not in values:
            values.append(value)
    return values


def main():
    cd = 2
    values = generate_unique_values(cd)
    # print(values)
    # print(type(values))
    mapping = {}

    # Ánh xạ các chữ cái a-z
    for char_code in range(ord("a"), ord("z") + 1):
        char = chr(char_code)
        mapping[char] = values.pop(0)

    # Ánh xạ các số từ 1-9
    for number in range(0, 10):
        number = str(number)
        mapping[number] = values.pop(0)

    # Ký tự đặc biệt
    special_characters = ["@", "#", "$", "%", "&"]
    for special in special_characters:
        mapping[special] = values.pop(0)

    # Lưu bảng ánh xạ vào file mapping.csv
    with open("map/mapping.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Character", "Number"])
        for char, number in mapping.items():
            writer.writerow([char, number])


if __name__ == "__main__":
    main()
