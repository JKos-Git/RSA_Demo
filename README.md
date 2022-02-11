# RSA_Demo
A demo of RSA encryption using Python.

This module has four functions:
  
  generate_public_key(prime1, prime2)
    This function takes two distinct prime numbers and generates an RSA public key. 
    Arguments:
      prime1 (Integer) - The first prime number.
      prime2 (Integer) - The second prime number.
    Returns:
      public key (Tuple) - Returns the public key as a tuple with the following structure: (Exponent, Modulus).
      
  encryptor(message, public_key):
    This function takes a message and encrypts it using RSA to generate a cipher.
    (cipher = (message**exponent) mod modulus)
    Arguments:
      message (Integer) - This is the message to be encrypted. Because this is a simple script to demonstrate RSA encryption, this has to be an Integer.
      public_key (Tuple) - This is the public key used for encrypting. It must be a tuple with the following structure: (Exponent, Modulus).
    Return:
      cipher (Integer) - Returns the encrypted message.
  
  decryptor(cipher, prime1, prime2)
    This funcitons takes the encrypted cipher and the two prime numbers used to generate the public key that encrypted the message.
    It then calculates the private exponent which would be used for the private key (Private exponent, Modulus).
    It then decrypts the message.
    (message = (cipher**private exponent) mod modulus)
    Arguments:
      cipher (Integer) - The encrypted message.
      prime1 (Integer) - The first prime number.
      prime2 (Integer) - The second prime number.        
    Returns:
      message (Integer) - The decrypted message.
        
  main(message, prime1, prime2)
    This function is used to demonstrate the whole module and the operation of RSA encryption.
    Arguments:
      message (Integer) - This is the message to be encrypted. Because this is a simple script to demonstrate RSA encryption, this has to be an Integer.
      prime1 (Integer) - The first prime number.
      prime2 (Integer) - The second prime number.
      
