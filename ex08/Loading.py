import os
import sys


def ft_tqdm(lst: range):
    """A function imitating tqdm"""
    count = 0
    terminal_size = os.get_terminal_size()
    start_time = os.times().elapsed
    last_print = 0
    interval = 0.1

    def convert_time_str(time: int):
        """format int type time to string xx:xx"""
        return f"{(int(time/60)) % 60:02d}:{time % 60:02d}"

    def get_suffix(time: float):
        """create a string for the right side of the bar"""
        time_passed = time - start_time
        if count == 0:
            left_str = "?"
            speed = "?it/s"
        else:
            left_str = convert_time_str(
                int(time_passed / count * (len(lst) - count)))
            if time_passed < count:
                speed = f"{count / time_passed:5.2f}it/s"
            else:
                speed = f"{time_passed / count:5.2f}s/it"
        passed_str = convert_time_str(int(time_passed))
        return f"| {count}/{len(lst)} [{passed_str}<{left_str}, {speed}]"

    def print_stat():
        """print the task progress"""
        nonlocal last_print
        time = os.times().elapsed
        if count < len(lst) and time - last_print < interval:
            return
        last_print = time
        finish_rate = count / len(lst) * 100
        prefix = f"{int(finish_rate):3d}%|"
        suffix = get_suffix(time)
        bar_count = int((terminal_size.columns -
                         len(prefix) - len(suffix)) * count / len(lst))
        empty_count = terminal_size.columns -\
            len(prefix) - len(suffix) - bar_count
        print(f"\r{prefix}" + "█" * bar_count
              + " " * empty_count + suffix, end="", file=sys.stderr)

    for obj in lst:
        print_stat()
        yield obj
        count += 1
    print_stat()
    print(file=sys.stderr)
