"""
Code MVP for Contribution Protocol

Purpose:
- Verify expiration by time through executable code
- No human judgment
- No economic semantics

This is NOT a full implementation.
"""


import time

def is_valid(issued_at: float, expires_in: float) -> bool:
    """
    Determine whether a token is still valid based solely on time.

    :param issued_at: issuance time (epoch seconds)
    :param expires_in: validity duration in seconds
    :return: True if valid, False if expired
    """
    now = time.time()
    return now < issued_at + expires_in



if __name__ == "__main__":
    print("=== Code MVP check ===")

    issued_at = time.time()
    expires_in = 60  # ← 60sec (check only; minutes/months defined at higher layers)

    print("issued_at :", issued_at)
    print("expires_in:", expires_in, "seconds")

    print("\n[Immediately]")
    print("valid:", is_valid(issued_at, expires_in))

    time.sleep(expires_in + 1)

    print("\n[After expiration]")
    print("valid:", is_valid(issued_at, expires_in))

