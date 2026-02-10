"""シンプルな数値計算ツール"""


def add(a: float, b: float) -> float:
    """2つの数値を加算する"""
    return a + b


def subtract(a: float, b: float) -> float:
    """2つの数値を減算する"""
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数値を乗算する"""
    return a * b


def divide(a: float, b: float) -> float:
    """2つの数値を除算する

    Raises:
        ValueError: 0で割ろうとした場合
    """
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def average(numbers: list[float]) -> float:
    """数値リストの平均値を計算する

    Raises:
        ValueError: リストが空の場合
    """
    if not numbers:
        raise ValueError("空のリストの平均は計算できません")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("=== Calculator ===")
    print(f"1 + 2 = {add(1, 2)}")
    print(f"10 - 3 = {subtract(10, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"average([1, 2, 3, 4, 5]) = {average([1, 2, 3, 4, 5])}")
