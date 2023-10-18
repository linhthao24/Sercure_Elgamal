import subprocess


def run_script(script_path):
    subprocess.run(["python", script_path])


def main():
    script_paths = ["./source/trans2int.py", "./source/elgamal_encryption.py"]
    for script_path in script_paths:
        run_script(script_path)


if __name__ == "__main__":
    main()
