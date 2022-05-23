def mean(numbers: list, dropna=False) -> float:
    """Compute the mean for a list of numbers"""

    # Check input is list or tuple
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Numbers must be provided as a list or tuple!")

    # Count includes missing values
    count = len(numbers)
    numbers = [nr for nr in numbers if nr is not None]

    # When dropping missing, update count
    if dropna:
        count = len(numbers)

    return sum(numbers) / count
