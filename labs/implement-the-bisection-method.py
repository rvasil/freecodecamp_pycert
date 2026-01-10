def square_root_bisection(
    number: float, tolerance: float = 0.01, max_iterations: int = 10
):
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )
    if number in [0, 1]:
        print(f"The square root of {number} is {number}")
        return number

    iteration = 0
    low = 0.0
    mid = 0.0
    high = max(1.0, number)

    while iteration < max_iterations:
        iteration += 1
        diff = high - low
        if diff <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        mid = (high + low) / 2
        squared_mid = mid * mid

        if squared_mid > number:
            high = mid
        else:
            low = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None


# square_root_bisection(16, 0.5, 10)
# square_root_bisection(225, 1e-7, 10)
# square_root_bisection(0.25, 1e-7, 50)
t = square_root_bisection(0.001, 1e-7, 50)
