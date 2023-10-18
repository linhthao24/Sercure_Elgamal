def compare_input_output():
    with open("./data/input.txt", "r") as input_file:
        input_data = input_file.read()

    with open("./data/output.txt", "r") as output_file:
        output_data = output_file.read()

    if input_data == output_data:
        print("Dữ liệu trong input.txt và output.txt giống nhau.")
    else:
        print("Dữ liệu trong input.txt và output.txt không giống nhau.")


if __name__ == "__main__":
    compare_input_output()
