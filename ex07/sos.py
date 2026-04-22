import sys

def convert_to_morse(alp_str: str, morse_code_dict: dict[str, str]):
    """Convert a string consisted of alphabets and spaces to morse code"""
    ret = ""
    for char in alp_str:
        code = morse_code_dict.get(char)
        if code is None:
            raise AssertionError
        ret += code
    return ret[:-1]


def main() -> None:
    """Take a string as an argument and convert it to morse code."""
    morse_code_dict = {
        ' ': '/  ', 'A': '.- ', 'B': '-... ',
        'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ',
        'L': '.-.. ', 'M': '-- ', 'N': '-. ',
        'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
        'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ',
        'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
        'a': '.- ', 'b': '-... ',
        'c': '-.-. ', 'd': '-.. ', 'e': '. ',
        'f': '..-. ', 'g': '--. ', 'h': '.... ',
        'i': '.. ', 'j': '.--- ', 'k': '-.- ',
        'l': '.-.. ', 'm': '-- ', 'n': '-. ',
        'o': '--- ', 'p': '.--. ', 'q': '--.- ',
        'r': '.-. ', 's': '... ', 't': '- ',
        'u': '..- ', 'v': '...- ', 'w': '.-- ',
        'x': '-..- ', 'y': '-.-- ', 'z': '--.. ',
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError
        print(convert_to_morse(sys.argv[1], morse_code_dict))
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
