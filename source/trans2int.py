import csv


def load_mapping(filename):
    mapping = {}
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            char, number = row
            mapping[char] = number
    return mapping


def convert_text_to_number(text, mapping):
    numbers = [mapping.get(char, char) for char in text]
    return "".join(numbers)


# Đường dẫn đến file mapping.csv
mapping_file = "./map/mapping.csv"

# Đường dẫn đến file text_in.txt
text_in_file = "run/text_in.txt"

# Đọc dữ liệu từ file text_in.txt
with open(text_in_file, "r") as file:
    text = file.read()

# Tạo bảng ánh xạ từ file mapping.csv
mapping = load_mapping(mapping_file)

# Chuyển đổi văn bản sang dạng số
numbers = convert_text_to_number(text, mapping)

# Lưu dữ liệu số vào file input.txt
with open("./data/input.txt", "w") as file:
    file.write(numbers)
