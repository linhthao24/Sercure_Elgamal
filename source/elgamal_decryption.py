import json


def decrypt(key_receive, key_know, data_receive, key_trans):
    Information_receive = data_receive
    R_receive = key_trans
    K = pow(R_receive, key_know, key_receive[0])
    K1 = pow(K, -1, key_receive[0])
    M = ""
    for i in range(len(Information_receive)):
        temp = (Information_receive[i] * K1) % key_receive[0]
        M1 = str(temp)
        M += M1
    return M


def main_output():
    key_receive_file = "./data/key_public.json"
    key_know_file = "./data/key_secret.json"

    # Nhận dữ liệu
    with open("./data/data_send.json", "r") as file:
        data_receive = json.load(file)
    # Đọc key_receive từ file key_public.json
    # print(data_receive)
    with open("./data/key_trans.txt", "r") as file:
        key_trans = json.load(file)
    # print(key_trans)
    with open(key_receive_file, "r") as file:
        key_receive = json.load(file)
    # print(key_receive)
    # Đọc key_know từ file key_secret.json
    with open(key_know_file, "r") as file:
        key_know = json.load(file)[1]
    # print(key_know)
    # Giai mã
    result = decrypt(key_receive, key_know, data_receive, key_trans)
    print()
    # Ghi vào tệp tin đầu ra
    output_Name = "./data/output.txt"
    with open(output_Name, "w") as file:
        file.write(result)


if __name__ == "__main__":
    main_output()
