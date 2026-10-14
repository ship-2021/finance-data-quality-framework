def generate_test_cases():
    """
    Simulated AI-driven test case generator for finance data validation
    """

    test_cases = [
        "Check transaction amount is not negative",
        "Validate no duplicate transaction IDs",
        "Ensure total reconciliation matches source and warehouse",
        "Validate transaction amount < 10000 threshold"
    ]

    return test_cases


if __name__ == "__main__":
    tests = generate_test_cases()
    for t in tests:
        print("AI Generated Test:", t)