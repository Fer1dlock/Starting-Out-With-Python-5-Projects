def binary_2_decimal(bin_num: int) -> int:
    return sum(2 ** idx for idx, i in enumerate(str(bin_num)[::-1]) if i == '1')


def main():
    assert binary_2_decimal(10011101) == 157


if __name__ == '__main__':
    main()
