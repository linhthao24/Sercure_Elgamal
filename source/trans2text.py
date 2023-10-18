import csv


def load_mapping(filename):
    mapping = {}
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            char, number = row
            mapping[number] = char
    return mapping


# Đường dẫn đến file mapping.csv
mapping_file = "./map/mapping.csv"

# Đường dẫn đến file output.txt
output_file = "./data/output.txt"

# Đọc dữ liệu từ file output.txt
with open(output_file, "r") as file:
    numbers = file.read().split()

# Tạo bảng ánh xạ từ file mapping.csv
mapping = load_mapping(mapping_file)
text = ""
# print(numbers)
# print(type(numbers))
numbers = numbers[0]
# print(numbers)
# print(type(numbers))
for i in range(0, len(numbers), 2):
    number = numbers[i] + numbers[i + 1]
    char = mapping.get("".join(number))
    if char is not None:
        text += char
    # print(text, " ", "\t", number, "\t", char)
# Lưu dữ liệu văn bản vào file text_out.txt
with open("run/text_out.txt", "w") as file:
    file.write(text)
