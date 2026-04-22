import sys
from ft_filter import ft_filter


def main() -> None:
    """Accept two arguments: a string (S) and an integer (N)
    Output a list of words in S that have a length greater than N"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        length = int(sys.argv[2])
        print(ft_filter(lambda x: length < len(x), sys.argv[1].split()))
    except (ValueError, AssertionError):
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
