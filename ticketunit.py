def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def run_tests():

    test_cases = [

        (0,32),
        (100,212),
        (-40,-40),
        (25,77),
        (36.6,97.88),
        (1000,1832)

    ]

    passed = 0

    for c, expected in test_cases:

        result = celsius_to_fahrenheit(c)

        if abs(result - expected) < 0.001:

            print(f"PASS: {c}°C -> {result}°F")

            passed += 1

        else:

            print(
                f"FAIL: {c}°C expected {expected}, got {result}"
            )

    print(f"\n{passed}/{len(test_cases)} tests passed")


run_tests()
