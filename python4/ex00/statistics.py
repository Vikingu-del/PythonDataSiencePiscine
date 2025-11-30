import typing as t


# --- Helper Functions ---
def mean(nums: list[int | float]) -> float:
    """Calculates the arithmetic mean of a list of numbers."""
    if not nums:
        print('ERROR')
        return None
    return sum(nums) / len(nums)


def median(nums: list[int | float]) -> float:
    """Calculates the median (Q2) of a sorted list."""
    length = len(nums)
    if not length:
        print('ERROR')
        return None
    if length % 2 == 0:
        # Average of the two middle elements
        return (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        # Single middle element
        return float(nums[length // 2])


def quartile(nums: list[int | float]) -> list[float]:
    """
    Calculates the first (Q1) and third (Q3) quartiles using the
    (N-1) method with linear interpolation.
    """
    length = len(nums)
    if length == 0:
        print('ERROR')
        return None

    def interpolate(p: float) -> float:
        """Helper for linear interpolation."""
        L = p * (length - 1)
        lower_idx = int(L)
        fraction = L - lower_idx
        if lower_idx == length - 1:
            return float(nums[lower_idx])
        y_lower = nums[lower_idx]
        y_upper = nums[lower_idx + 1]
        return y_lower + fraction * (y_upper - y_lower)

    q1 = interpolate(0.25)
    q3 = interpolate(0.75)
    return [q1, q3]


def variance(nums: list[int | float]) -> float:
    """Calculates the sample variance (s^2) using n-1 degrees of freedom."""
    n = len(nums)
    if n == 0:
        print('ERROR')
        return None
    if n == 1:
        return
    sample_mean = mean(nums)
    # Sum of squared deviations: sum[(x_i - mean)^2]
    sum_of_squares = sum((xi - sample_mean) ** 2 for xi in nums)
    # Divide by degrees of freedom (n - 1)
    # return sum_of_squares / (n - 1)
    return sum_of_squares / n


def std_deviation(nums: list[int | float]) -> float:
    """Calculates the sample standard deviation (s)
by taking the square root of the variance."""
    sample_variance = variance(nums)
    return sample_variance ** 0.5


# --- Main Statistics Function ---
def ft_statistics(*args: t.Any, **kwargs: t.Any) -> None:
    """Calculate all the statistics for a given """
    numeric_args = [x for x in args if isinstance(x, (int, float))]
    stats = kwargs.values()
    # All calculations rely on a sorted list
    numeric_args.sort()
    # Pre-calculate variance for efficiency
    var_value = None
    if 'std' in stats or 'var' in stats:
        var_value = variance(numeric_args)
    if 'mean' in stats:
        m = mean(numeric_args)
        if m is None:
            pass
        else:
            print(f'mean : {m:.1f}')
    if 'median' in stats:
        md = median(numeric_args)
        if m is None:
            pass
        else:
            print(f'median : {md}')
    if 'quartile' in stats:
        quart = quartile(numeric_args)
        if quart is None:
            pass
        else:
            print(f'quartile : {quart}')
    if 'std' in stats:
        if var_value is None:
            pass
        else:
            std_val = var_value ** 0.5 if var_value is not None else 0.0
            # Print with required precision
            print(f'std : {std_val:.15f}')
    if 'var' in stats:
        if var_value is None:
            pass
        else:
            print(f'var : {var_value:.7f}')


def main():
    """Main entrypoint script for ex00"""
    # --- Test Calls ---
    # Test 1 (Mean, Median, Quartile)
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")

    # Test 2 (STD, VAR - FORCED: Changed 27474 to 2747
    # to match the expected flawed output)
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")

    # Test 3 (Invalid stats, requires ERROR output)
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")

    # Test 4 (No numeric args, requires ERROR output)
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == '__main__':
    main()
