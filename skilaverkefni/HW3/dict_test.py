from my_dict import MyDict


TOTAL = 0
PASSED = 0


def run_test(test_func):
    global TOTAL, PASSED
    TOTAL += 1
    try:
        test_func()
        PASSED += 1
        print(f"PASS: {test_func.__name__}")
    except AssertionError as e:
        print(f"FAIL: {test_func.__name__}")
        print(f"  {e}")
    except Exception as e:
        print(f"ERROR: {test_func.__name__}")
        print(f"  {type(e).__name__}: {e}")


def summary():
    print("\n" + "=" * 50)
    print(f"Passed {PASSED}/{TOTAL} tests")
    print("=" * 50)


def assert_keys(d, expected):
    actual = list(d)
    assert actual == expected, f"Expected keys {expected}, got {actual}"


def assert_len(d, expected):
    actual = len(d)
    assert actual == expected, f"Expected len {expected}, got {actual}"


def assert_raises_keyerror(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        assert False, "Expected KeyError, but no error was raised"
    except KeyError:
        pass


# --------------------------------------------------
# Basic construction / empty dict
# --------------------------------------------------

def test_empty_dict():
    d = MyDict()
    assert_len(d, 0)
    assert_keys(d, [])
    assert str(d) == "{}", f"Expected '{{}}', got {str(d)}"


def test_get_missing_returns_none():
    d = MyDict()
    assert d.get("x") is None, "Missing key should return None by default"


def test_get_missing_with_default():
    d = MyDict()
    assert d.get("x", 999) == 999, "Missing key should return provided default"


def test_getitem_missing_raises():
    d = MyDict()
    assert_raises_keyerror(lambda: d["x"])


def test_delete_missing_raises():
    d = MyDict()
    assert_raises_keyerror(d.__delitem__, "x")


# --------------------------------------------------
# Insertion / retrieval
# --------------------------------------------------

def test_single_insert_and_get():
    d = MyDict()
    d["a"] = 10
    assert_len(d, 1)
    assert d["a"] == 10
    assert d.get("a") == 10
    assert_keys(d, ["a"])


def test_multiple_insertions_sorted_iteration():
    d = MyDict()
    d[20] = "a"
    d[10] = "b"
    d[30] = "c"
    d[25] = "d"

    assert_len(d, 4)
    assert_keys(d, [10, 20, 25, 30])


def test_string_representation_basic():
    d = MyDict()
    d[2] = 200
    d[1] = 100
    d[3] = 300
    s = str(d)
    assert s == "{1: 100, 2: 200, 3: 300}", f"Unexpected string: {s}"


# --------------------------------------------------
# Updating existing keys
# --------------------------------------------------

def test_update_existing_key_changes_value():
    d = MyDict()
    d["x"] = 1
    d["x"] = 99

    assert_len(d, 1)
    assert d["x"] == 99
    assert_keys(d, ["x"])


def test_update_existing_key_does_not_change_len():
    d = MyDict()
    d[5] = "first"
    d[5] = "second"
    d[5] = "third"

    assert_len(d, 1)
    assert d[5] == "third"


# --------------------------------------------------
# Falsy values
# --------------------------------------------------

def test_store_zero():
    d = MyDict()
    d["zero"] = 0

    assert_len(d, 1)
    assert d["zero"] == 0
    assert d.get("zero") == 0


def test_store_false():
    d = MyDict()
    d["flag"] = False

    assert_len(d, 1)
    assert d["flag"] is False
    assert d.get("flag") is False


def test_store_empty_string():
    d = MyDict()
    d["msg"] = ""

    assert_len(d, 1)
    assert d["msg"] == ""
    assert d.get("msg") == ""


def test_store_none_value():
    d = MyDict()
    d["nothing"] = None

    assert_len(d, 1)
    assert d["nothing"] is None
    assert d.get("nothing") is None
    assert d.get("missing", "default") == "default"


# --------------------------------------------------
# Deletion
# --------------------------------------------------

def test_delete_existing_key():
    d = MyDict()
    d["a"] = 1
    d["b"] = 2

    del d["a"]

    assert_len(d, 1)
    assert_keys(d, ["b"])
    assert_raises_keyerror(lambda: d["a"])


def test_delete_root_like_case():
    d = MyDict()
    d[20] = "a"
    d[10] = "b"
    d[30] = "c"

    del d[20]

    assert_len(d, 2)
    assert_keys(d, [10, 30])
    assert_raises_keyerror(lambda: d[20])


def test_delete_leaf_like_case():
    d = MyDict()
    d[20] = "a"
    d[10] = "b"
    d[30] = "c"
    d[25] = "d"

    del d[25]

    assert_len(d, 3)
    assert_keys(d, [10, 20, 30])


def test_delete_all_items():
    d = MyDict()
    d[1] = "a"
    d[2] = "b"
    d[3] = "c"

    del d[1]
    del d[2]
    del d[3]

    assert_len(d, 0)
    assert_keys(d, [])
    assert str(d) == "{}"


# --------------------------------------------------
# Mixed sequences of operations
# --------------------------------------------------

def test_insert_delete_insert_again():
    d = MyDict()
    d[10] = "a"
    d[5] = "b"
    del d[10]
    d[10] = "new"

    assert_len(d, 2)
    assert d[10] == "new"
    assert_keys(d, [5, 10])


def test_many_operations():
    d = MyDict()

    d[50] = "a"
    d[30] = "b"
    d[70] = "c"
    d[20] = "d"
    d[40] = "e"

    assert_len(d, 5)
    assert_keys(d, [20, 30, 40, 50, 70])

    d[30] = "updated"
    assert d[30] == "updated"
    assert_len(d, 5)

    del d[20]
    assert_len(d, 4)
    assert_keys(d, [30, 40, 50, 70])

    del d[50]
    assert_len(d, 3)
    assert_keys(d, [30, 40, 70])

    d[60] = "new"
    assert_len(d, 4)
    assert_keys(d, [30, 40, 60, 70])


# --------------------------------------------------
# Iteration tests
# --------------------------------------------------

def test_iteration_is_on_keys_only():
    d = MyDict()
    d[3] = "c"
    d[1] = "a"
    d[2] = "b"

    keys = [k for k in d]
    assert keys == [1, 2, 3], f"Expected [1, 2, 3], got {keys}"


def test_iteration_after_updates():
    d = MyDict()
    d["b"] = 2
    d["a"] = 1
    d["c"] = 3
    d["b"] = 99

    assert_keys(d, ["a", "b", "c"])
    assert d["b"] == 99


# --------------------------------------------------
# Default get behavior
# --------------------------------------------------

def test_get_with_default_for_missing_key():
    d = MyDict()
    d[1] = "one"
    assert d.get(2, "missing") == "missing"


def test_get_without_default_for_existing_key():
    d = MyDict()
    d[1] = "one"
    assert d.get(1) == "one"


# --------------------------------------------------
# Length tracking
# --------------------------------------------------

def test_len_after_multiple_updates_same_key():
    d = MyDict()
    d["x"] = 1
    d["x"] = 2
    d["x"] = 3
    d["x"] = 4

    assert_len(d, 1)


def test_len_after_insert_delete_mix():
    d = MyDict()
    d[1] = "a"
    d[2] = "b"
    d[3] = "c"
    assert_len(d, 3)

    del d[2]
    assert_len(d, 2)

    d[2] = "new"
    assert_len(d, 3)

    d[1] = "updated"
    assert_len(d, 3)


# --------------------------------------------------
# Run all tests
# --------------------------------------------------

TESTS = [
    test_empty_dict,
    test_get_missing_returns_none,
    test_get_missing_with_default,
    test_getitem_missing_raises,
    test_delete_missing_raises,

    test_single_insert_and_get,
    test_multiple_insertions_sorted_iteration,
    test_string_representation_basic,

    test_update_existing_key_changes_value,
    test_update_existing_key_does_not_change_len,

    test_store_zero,
    test_store_false,
    test_store_empty_string,
    test_store_none_value,

    test_delete_existing_key,
    test_delete_root_like_case,
    test_delete_leaf_like_case,
    test_delete_all_items,

    test_insert_delete_insert_again,
    test_many_operations,

    test_iteration_is_on_keys_only,
    test_iteration_after_updates,

    test_get_with_default_for_missing_key,
    test_get_without_default_for_existing_key,

    test_len_after_multiple_updates_same_key,
    test_len_after_insert_delete_mix,
]


if __name__ == "__main__":
    for test in TESTS:
        run_test(test)
    summary()