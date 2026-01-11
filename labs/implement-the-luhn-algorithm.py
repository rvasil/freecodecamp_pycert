def verify_card_number(number: str):
    all_digits = all([c.isdigit() for c in number.replace("-", "").replace(" ", "")])
    if not all_digits:
        return "INVALID!"
    digits = [int(d) for d in number if d.isdigit()]

    for i in range(-2, -len(digits) - 1, -2):
        digit = digits[i]
        digits[i] = digit * 2 if digit * 2 < 10 else (digit * 2) - 9
        print(i, digit, digits[i])

    checksum = sum(digits)
    return "VALID!" if checksum % 10 == 0 else "INVALID!"


# print(verify_card_number('453914881'))
# print(verify_card_number('453914889'))
print(verify_card_number("4111-1111-1111-1111"))
# print(verify_card_number('1234 5678 9012 3456'))
