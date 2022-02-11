# RSA_demo.py
# A Python script to demonstrate RSA encryption.
# This RSA demo uses the smallest possible exponent value.
# Part of the ArcTaurus technical challenge.
# Abbreviations:
#   e - Exponent
#   n - Modulus
#   PHI - Phi(n)
#   d - Private Exponent
# Author: Jakub Kosarzecki
# Python version: 3.9.2
# Feb 2022

from math import gcd
import sys


def generate_public_key(prime1, prime2):
    """ A function that takes two prime numbers to generate a RSA public key.
    This function prints out the modulus and exponents, and returns the public key as a tuple.

    Args:
        prime1 (int): First prime number.
        prime2 (int): Second prime number.
        
    Raises:
        ValueError: Value error is raised if the two user inputs are not distinct prime numbers.

    Returns:
        tuple: The public key as a tuple containing the exponent and modulus required for encryption.
    """
    try:
        if _validate(prime1, prime2):
            e, n, PHI = _get_key_components(
                prime1, prime2
            )  # PHI is not needed for public key.
            return (e, n)
        else:
            raise ValueError

    except TypeError:
        print("[-] Type error occured")

    except ValueError:
        print("[-] Value error occured")


def encryptor(message, public_key):
    """A function that takes an message and an RSA public key and encrypts it. 

    Args:
        msg (int): message too be encrypted. Must be an integer.
        public_key (tuple): The public key must be a tuple containing the exponent and modulus (e, n).

    Raises:
        ValueError: Value error is raised if public key is a tuple but not the right length.
        TypeError: Type error is raised if the user input is the wrong type.

    Returns:
        int: The encrypted message as an integer.
    """
    try:
        if len(public_key) == 2:  # Checking that the key has 2 components
            (e, n) = public_key
            return int(message ** e) % n  # Encrypting the message. (c = (m**e) mod n)
        elif isinstance(public_key, tuple):
            raise ValueError
        else:
            raise TypeError
    except TypeError:
        print("[-] Type error occured")

    except ValueError:
        print("[-] Value error occured")


def decryptor(encrypted_message, prime1, prime2):
    """ Function which takes an encrypted message and the two prime numbers used to generate
    the public key and it returns the unencrypted message.

    Args:
        encrypted_message (int): The encrypted message as an integer.
        prime1 (int): The first prime that was used to encrypt the message.
        prime2 (int): The second prime that was used to encrypt the message.

    Raises:
        ValueError: Value error is raised if the two user inputs are not distinct prime numbers.

    Returns:
        int: The unencrypted message.
    """
    try:
        if _validate(prime1, prime2):
            e, n, PHI = _get_key_components(prime1, prime2)
            # Calculating the private exponent. ((d*e) mod Phi(n) = 1)
            for i in range(2, PHI):
                if (i * e) % PHI == 1:
                    d = i
            # private key = (d, n)
            return (encrypted_message ** d) % n
        else:
            raise ValueError

    except TypeError:
        print("[-] Type error occured")

    except ValueError:
        print("[-] Value error occured")


def _validate(prime1, prime2):
    """ Function which takes a number and checks if it is prime number.

    Args:
        prime1 (int): First prime.
        prime2 (int): Second prime.

    Returns:
        Boolean: returns True if the numbers are primes and distinct.
    """
    if prime1 == prime2:
        return False  # False if the primes are not distinct
    else:
        for n in (prime1, prime2):
            for i in range(
                2, int(n ** 0.5) + 1
            ):  # Checking if the the user inputs are primes.
                if n % i == 0:
                    return False
    return True


def _get_key_components(prime1, prime2):
    """ Function which takes the two prime numbers and calculates the modulus,
    the PHI and the lowest exponent required for RSA encryption keys

    Args:
        prime1 (int): First prime number
        prime2 (int): Second prime number

    Returns:
        tuple: returns a tuple containing the exponent, modulus, and PHI. (e, n, PHI)
    """
    n = prime1 * prime2  # Calculating the modulus
    PHI = (prime1 - 1) * (prime2 - 1)  # Calculating Phi(n) = (p -1)(q -1)
    # Finding the lowset exponent which has no common factor with Phi(n)
    for e in range(2, PHI):
        if gcd(e, PHI) == 1:
            return (e, n, PHI)


def main(message=77, prime1=79, prime2=97):
    """ This is the main function which demonstrates the whole module and provides a demo of the RSA encryption.

    Args:
        message (int): The message to be encrypted. Must be an integer. Defaults to 77.
        prime1 (int): First prime number. Defaults to 79.
        prime2 (int): Second prime number. Defaults to 97.
    """
    try:
        print("[+] Message: ", message)
        print("[+] Prime 1: ", prime1)
        print("[+] Prime 2: ", prime2)
        e, n = generate_public_key(prime1, prime2)
        print("[+] The exponent: ", e)
        print("[+] The modulus: ", n)
        print(f"[+] Public key: ({e}, {n})")
        print("[+] Starting encryptor...")
        encrypted_message = encryptor(message, (e, n))
        print("[+] Encrypted message: ", encrypted_message)
        print("[+] Starting decryptor...")
        decrypted_message = decryptor(encrypted_message, prime1, prime2)
        print("[+] Decrypted message: ", decrypted_message)
    except:
        sys.exit(1)  # Script exits if an error occures.


if __name__ == "__main__":
    """ This is called if the script is run from the command line.

    Raises:
        TypeError: Type error is raised is the wrong number of arguments is given
    """
    try:
        if len(sys.argv) == 1:  # Checking if arguments are given.
            main()
        elif len(sys.argv) == 4:  # Checking if 3 arguemets were given.
            message, prime1, prime2 = sys.argv[1:]
            try:
                main(
                    int(message), int(prime1), int(prime2)
                )  # Calling main function with integer arguments.

            # Python raises a ValueError here if one of the arguements is not an integer. However, TypeError is more appropriate.
            except ValueError:
                print("[-] Type error occurd: Arguements are the wrong type.")
        else:
            raise TypeError
    except TypeError:
        print("[-] Type error occured: Wrong number of arguments.")
