# from time import perf_counter
from os import get_terminal_size
# from time import sleep


# start = perf_counter()


def ft_tqdm(lst: range) -> None:
    """This function simulates the behavior of tqdm
    filling a progress bar by showing:
        Percentage of the bar being filled
        The bar itself being filled with => symbols till 100%
        Showing elapsed time and iterations per second"""
    term_width = get_terminal_size().columns
    reserved_space = 39
    bar_len = max(10, term_width - reserved_space)
    iterations = len(lst)
    for i, item in enumerate(lst, 1):
        step = i / iterations
        percent = int(step * 100)
        filled = int(bar_len * step)
        # elapsed = perf_counter() - start
        # speed = i / elapsed if elapsed > 0 else 0
        # eta = (100 - i) / speed if speed > 0 else 0
        bar_status = f"|{filled * '='}>{(bar_len - filled) * ' '}|"
        # time = f"{elapsed:05.2f}<{eta:05.2f}"
        data = f"{i}/{iterations}"
        # Add this above if you want more stats [{time}, {speed:06.2f}it/s]
        print(f"\r{percent}%{bar_status} {data}", end="", flush=True)
        yield item
    print()


def main():
    # for elem in ft_tqdm(range(90)):
    #     sleep(0.005)
    print()


if __name__ == "__main__":
    main()
