#!/usr/bin/env python3
import sys

from PIL import Image

RED_RATIO_THRESHOLD = 0.02
SIZE = (256, 256)


def is_red(r: int, g: int, b: int) -> bool:
    return r > 150 and g < 100 and b < 100


def red_ratio(path: str) -> float:
    img = Image.open(path).convert("RGB").resize(SIZE)
    data = img.tobytes()
    total = len(data) // 3
    red = sum(
        1 for i in range(0, len(data), 3)
        if is_red(data[i], data[i + 1], data[i + 2])
    )
    return red / total


def classify(path: str) -> str:
    return "DEFECT" if red_ratio(path) >= RED_RATIO_THRESHOLD else "OK"


def main() -> int:
    if len(sys.argv) != 2:
        print("Использование: python defect_check.py <путь_к_картинке>", file=sys.stderr)
        return 2
    try:
        print(classify(sys.argv[1]))
    except (FileNotFoundError, OSError) as e:
        print(f"Не удалось открыть файл: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
