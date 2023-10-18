import hashlib
import math
import random


def create_signature(message, private_key, alpha, p):
    # Tính giá trị hàm băm
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    H = int(hashed_message, 16)

    # Chọn số ngẫu nhiên K
    K = random.randint(1, p - 1)
    while math.gcd(K, p - 1) != 1:
        K = random.randint(1, p - 1)

    # Tính S1 và S2
    S1 = pow(alpha, K, p)
    K_inverse = pow(K, -1, p - 1)
    S2 = (K_inverse * (H - private_key * S1)) % (p - 1)

    signature = (S1, S2)
    return (signature, K, H, K_inverse)


def verify_signature(message, signature, public_key, alpha, p):
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    H = int(hashed_message, 16)

    S1, S2 = signature

    # Tính V1 và V2
    V1 = pow(alpha, H, p)
    V2 = (pow(public_key, S1, p) * pow(S1, S2, p)) % p

    if V1 == V2:
        return True, V1, V2
    else:
        return False


p = 23
alpha = 5
private_key = 7
public_key = pow(alpha, private_key, p)
print(public_key)
message = "BTLN9"

signature, K, H, K_inverse = create_signature(message, private_key, alpha, p)
print("Signature:", signature)
print(K, " ", H, " ", K_inverse)

is_valid, V1, V2 = verify_signature(message, signature, public_key, alpha, p)
print("Is Valid:", is_valid)
print(V1, " ", V2)
