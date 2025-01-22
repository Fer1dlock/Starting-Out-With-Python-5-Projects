def binary_2_decimal(bin_num: str) -> int:
    return sum(2 ** idx for idx, i in enumerate(bin_num[::-1]) if i == '1')


def decimal_2_binary(dec_num: int) -> str:
    result = ''
    while dec_num != 0:
        result += '1' if dec_num % 2 != 0 else '0'

        dec_num //= 2

    return result[::-1]


def main():
    assert binary_2_decimal('10011101') == 157
    assert decimal_2_binary(157) == '10011101'


if __name__ == '__main__':
    main()
