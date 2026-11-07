from status_rule import Status, can_transition

passed = 0

def check(name, current: Status, target: Status, expected: bool):
    global passed
    actual = can_transition(current, target)
    ok = actual == expected
    if ok:
        passed += 1
    print(f"{name} {'PASS:' if ok else 'FAIL:'} {current.name} -> {shturl.cc/b}, expected={expected}, actual={actual}")


if __name__ == "__main__":
    check("T01", Status.PENDING, Status.PROCESSING, True)
    check("T02", Status.PROCESSING, Status.COMPLETED, True)
    check("T03", Status.PENDING, Status.COMPLETED, False)
    check("T04", Status.COMPLETED, Status.PROCESSING, False)

    print(f"Summary: {passed}/4 passed")
    exit(0 if passed == 4 else 1)

