import re
from typing import Callable


def generator_numbers(text: str):
    """
    Generate all valid floating-point numbers from the text.
    Numbers must be surrounded by spaces.

    Args:
        text (str): Input text containing numbers separated by spaces

    Yields:
        float: Valid numbers found in the text
    """

    pattern = r'\s(\d+\.?\d*)\s'

    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group(1))


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculate the total sum of numbers extracted from the text using the provided generator function.

    Args:
        text (str): Input text containing numbers
        func (Callable): Generator function that yields numbers from the text

    Returns:
        float: Sum of all numbers found in the text
    """
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

    test_text = "Numbers: 10.5 20.75 30.0 end"
    total = sum_profit(test_text, generator_numbers)
    print(f"Test total: {total}")
