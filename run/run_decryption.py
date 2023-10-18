import subprocess


def run_script(script_path):
    subprocess.run(["python", script_path])


def main():
    script_paths = ["./source/elgamal_decryption.py", "./source/trans2text.py"]
    for script_path in script_paths:
        run_script(script_path)


if __name__ == "__main__":
    main()
