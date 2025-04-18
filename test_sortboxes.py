from sort_boxes import sort

def run_tests():
    assert sort(100, 100, 100, 10) == "SPECIAL"
    assert sort(50, 50, 50, 25) == "SPECIAL"
    assert sort(160, 10, 10, 21) == "REJECTED"
    assert sort(40, 40, 40, 10) == "STANDARD"
    assert sort(200, 20, 20, 19) == "SPECIAL"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()