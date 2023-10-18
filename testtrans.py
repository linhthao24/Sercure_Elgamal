import json
import csv

# kiểm tra file json
# Kiểm tra xem data có được mã hóa thành công không
file_path = "./data/data_send.json"


def check_empty_json_file_data_send(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not data:
                raise ValueError("Empty JSON file data_send")
    except FileNotFoundError:
        raise FileNotFoundError("File not found data_send")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file data_send")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra khoa cong khai

file_path = "./data/key_public.json"


def check_empty_json_file_key_public(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not data:
                raise ValueError("Empty JSON file key_public")
    except FileNotFoundError:
        raise FileNotFoundError("File not found key_public")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file key_public")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra khoa bi mat
file_path = "./data/key_secret.json"


def check_empty_json_file_key_secret(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not data:
                raise ValueError("Empty JSON file key_secret")
    except FileNotFoundError:
        raise FileNotFoundError("File not found key_secret")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file key_secret")
    except ValueError as e:
        raise ValueError(str(e))


# Kiem tra file text
# kiem tra file input
file_path = "./data/input.txt"


def check_empty_text_file_input(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file input")
    except FileNotFoundError:
        raise FileNotFoundError("File not found input")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file output
file_path = "./data/output.txt"


def check_empty_text_file_output(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file output")
    except FileNotFoundError:
        raise FileNotFoundError("File not found output")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file key_trans
file_path = "./data/key_trans.txt"


def check_empty_text_file_key_trans(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file key_trans")
    except FileNotFoundError:
        raise FileNotFoundError("File not found key_trans")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file prime_numbers
file_path = "./number/prime_numbers.txt"


def check_empty_text_file_prime_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file prime_numbers")
    except FileNotFoundError:
        raise FileNotFoundError("File not found prime_numbers")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file tex_in
file_path = "./run/text_in.txt"


def check_empty_text_file_text_in(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file text_in")
    except FileNotFoundError:
        raise FileNotFoundError("File not found text_in")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file text_out
file_path = "./run/text_out.txt"


def check_empty_text_file_text_out(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("Empty text file text_out")
    except FileNotFoundError:
        raise FileNotFoundError("File not found text_out")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra file csv
# file mappping
file_path = "./map/mapping.csv"


def check_empty_csv_file_mapping(file_path):
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.reader(file)
            if not any(row for row in reader):
                raise ValueError("Empty CSV file mapping")
    except FileNotFoundError:
        raise FileNotFoundError("File not found mapping")
    except ValueError as e:
        raise ValueError(str(e))


# kiem tra generator
file_path = "./number/mapping.csv"


def check_empty_csv_file_generator(file_path):
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.reader(file)
            if not any(row for row in reader):
                raise ValueError("Empty CSV file generator")
    except FileNotFoundError:
        raise FileNotFoundError("File not found generator")
    except ValueError as e:
        raise ValueError(str(e))
