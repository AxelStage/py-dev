"""
Encrypt and decrypt messages using the Caesar cipher.
A mono alphabetic substitution cipher where each letter
is replaced by another letter in the alphabet.

Classes:
    None

Functions:
    encode_message(str, int)
    decode_message(str, int)

Notes:
    Capital letters are not maintained after encoding!
"""

# preparations
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encode_message(message, offset):
    """Encodes any alphabet characters string by a numeric offset"""

    encoded_message = ""

    for symbol in list(message):
        if symbol in alphabet:
            index = alphabet.index(symbol)
            if len(alphabet) - 1 - index >= offset:
                encoded_message += alphabet[index + offset]
            elif offset < 2 * len(alphabet):
                encoded_message += alphabet[offset - (len(alphabet) - 1 - index)]
            else:
                encoded_message += alphabet[
                    (offset - (len(alphabet) - 1 - index)) % len(alphabet) - 1
                ]
        else:
            encoded_message += symbol

    print(encoded_message)


def decode_message(message, offset):
    """Decodes an encoded message by a known numeric offset"""

    decoded_message = ""

    for symbol in list(message):
        if symbol in alphabet:
            index = alphabet.index(symbol)
            if index >= offset:
                decoded_message += alphabet[index - offset]
            # elif len(alphabet) + index <= offset:
            elif offset < 2 * len(alphabet):
                decoded_message += alphabet[len(alphabet) + index - offset - 1]
            else:
                decoded_message += alphabet[
                    len(alphabet) + index - (offset % len(alphabet))
                ]
        else:
            decoded_message += symbol

    print(decoded_message)

def main(running=True):
    """main program logic"""

    while running:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encode_message(text, shift)
        elif direction == "decode":
            decode_message(text, shift)

        repeat = input(
            "Run again? Type y for yes or press any other button to exit.\n"
        ).lower()

        if repeat != "y":
            running = False

if __name__ == "__main__":
    main()
