from binary_search_tree import Pair, BinarySearchTree


# ============================================================
# Small testing framework
# ============================================================

TOTAL_TESTS = 0
PASSED_TESTS = 0


def run_test(fn):
    global TOTAL_TESTS, PASSED_TESTS
    TOTAL_TESTS += 1
    print(f"\n--- RUNNING {fn.__name__} ---")
    try:
        fn()
        PASSED_TESTS += 1
        print(f"PASS: {fn.__name__}")
    except AssertionError as e:
        print(f"FAIL: {fn.__name__}")
        print("AssertionError:", e)
    except Exception as e:
        print(f"ERROR: {fn.__name__}")
        print(type(e).__name__ + ":", e)


def summary():
    print("\n" + "=" * 60)
    print(f"PASSED {PASSED_TESTS} / {TOTAL_TESTS} TESTS")
    print("=" * 60)


# ============================================================
# Generic helper assertions
# ============================================================

def tree_keys(tree: BinarySearchTree):
    return [pair.key for pair in tree]


def tree_keys_reversed(tree: BinarySearchTree):
    return [pair.key for pair in reversed(tree)]


def assert_inorder(tree: BinarySearchTree, expected_keys):
    actual = tree_keys(tree)
    assert actual == expected_keys, f"inorder keys wrong\nexpected: {expected_keys}\nactual:   {actual}"


def assert_reverse_inorder(tree: BinarySearchTree, expected_keys):
    actual = tree_keys_reversed(tree)
    assert actual == expected_keys, f"reverse inorder keys wrong\nexpected: {expected_keys}\nactual:   {actual}"


def assert_pairs_match(tree: BinarySearchTree, expected_pairs):
    actual = [(pair.key, pair.value) for pair in tree.pairs()]
    assert actual == expected_pairs, f"pairs wrong\nexpected: {expected_pairs}\nactual:   {actual}"


def assert_keys_method(tree: BinarySearchTree, expected_keys):
    actual = tree.keys()
    assert actual == expected_keys, f"keys() wrong\nexpected: {expected_keys}\nactual:   {actual}"


def assert_membership(tree: BinarySearchTree, present_keys, absent_keys):
    for key in present_keys:
        assert tree.is_in(key) is True, f"is_in({key}) should be True"
    for key in absent_keys:
        assert tree.is_in(key) is False, f"is_in({key}) should be False"


def assert_get_values(tree: BinarySearchTree, expected):
    """
    expected = dict: key -> value
    """
    for key, value in expected.items():
        actual = tree.get(key)
        assert actual == value, f"get({key}) wrong, expected {value}, got {actual}"


def assert_empty_tree(tree: BinarySearchTree):
    assert tree.is_empty() is True, "empty tree should report is_empty() == True"
    assert tree.keys() == [], f"empty tree keys() should be [], got {tree.keys()}"
    assert tree.pairs() == [], f"empty tree pairs() should be [], got {tree.pairs()}"
    assert list(tree) == [], f"iterating empty tree should give []"
    assert list(reversed(tree)) == [], f"reversed empty tree should give []"
    assert tree.get(123456) is None, "get on empty tree should return None"
    assert tree.is_in(123456) is False, "is_in on empty tree should be False"


def build_tree_from_keys(keys):
    tree = BinarySearchTree()
    for key in keys:
        tree.insert_key(key)
    return tree


def build_tree_from_pairs(pairs):
    tree = BinarySearchTree()
    for key, value in pairs:
        tree.insert(Pair(key, value))
    return tree


def assert_sorted_property_after_build(keys):
    tree = build_tree_from_keys(keys)
    expected = sorted(set(keys))
    assert_inorder(tree, expected)
    assert_reverse_inorder(tree, list(reversed(expected)))
    assert_keys_method(tree, expected)


def assert_delete_result(tree, key, expected_bool, expected_keys_after):
    actual = tree.delete(key)
    assert actual == expected_bool, f"delete({key}) returned {actual}, expected {expected_bool}"
    assert_inorder(tree, expected_keys_after)
    assert_reverse_inorder(tree, list(reversed(expected_keys_after)))


# ============================================================
# Basic / empty tree tests
# ============================================================

def test_empty_tree_initial_state():
    tree = BinarySearchTree()
    assert_empty_tree(tree)


def test_clear_on_empty_tree():
    tree = BinarySearchTree()
    tree.clear()
    assert_empty_tree(tree)


def test_delete_on_empty_tree():
    tree = BinarySearchTree()
    assert tree.delete(10) is False, "delete on empty tree should return False"
    assert_empty_tree(tree)


def test_string_on_empty_tree():
    tree = BinarySearchTree()
    s = str(tree)
    assert isinstance(s, str), "__str__ should return a string"
    assert s == "-", f"empty tree string should be '-', got {s}"


# ============================================================
# Single node tests
# ============================================================

def test_single_insert_key():
    tree = BinarySearchTree()
    assert tree.insert_key(10) is True
    assert tree.is_empty() is False
    assert_inorder(tree, [10])
    assert_reverse_inorder(tree, [10])
    assert_keys_method(tree, [10])
    assert_pairs_match(tree, [(10, None)])
    assert tree.get(10) is None
    assert_membership(tree, [10], [5, 15, 0])


def test_single_insert_pair():
    tree = BinarySearchTree()
    assert tree.insert(Pair(10, "a")) is True
    assert_inorder(tree, [10])
    assert_pairs_match(tree, [(10, "a")])
    assert tree.get(10) == "a"


def test_single_duplicate_insert_key():
    tree = BinarySearchTree()
    assert tree.insert_key(10) is True
    assert tree.insert_key(10) is False
    assert_inorder(tree, [10])
    assert_pairs_match(tree, [(10, None)])


def test_single_duplicate_insert_pair_updates_value():
    tree = BinarySearchTree()
    assert tree.insert(Pair(10, "old")) is True
    assert tree.insert(Pair(10, "new")) is False
    assert_inorder(tree, [10])
    assert_pairs_match(tree, [(10, "new")])
    assert tree.get(10) == "new"


def test_single_delete_root():
    tree = BinarySearchTree()
    tree.insert_key(10)
    assert tree.delete(10) is True
    assert_empty_tree(tree)


def test_single_delete_missing():
    tree = BinarySearchTree()
    tree.insert_key(10)
    assert tree.delete(20) is False
    assert_inorder(tree, [10])


# ============================================================
# Small shape tests
# ============================================================

def test_two_nodes_left():
    tree = BinarySearchTree()
    tree.insert_key(10)
    tree.insert_key(5)
    assert_inorder(tree, [5, 10])
    assert_reverse_inorder(tree, [10, 5])


def test_two_nodes_right():
    tree = BinarySearchTree()
    tree.insert_key(10)
    tree.insert_key(15)
    assert_inorder(tree, [10, 15])
    assert_reverse_inorder(tree, [15, 10])


def test_three_nodes_balanced():
    tree = BinarySearchTree()
    for key in [10, 5, 15]:
        tree.insert_key(key)
    assert_inorder(tree, [5, 10, 15])
    assert_reverse_inorder(tree, [15, 10, 5])
    assert_membership(tree, [5, 10, 15], [1, 6, 20])


def test_three_nodes_left_chain():
    tree = BinarySearchTree()
    for key in [30, 20, 10]:
        tree.insert_key(key)
    assert_inorder(tree, [10, 20, 30])
    assert_reverse_inorder(tree, [30, 20, 10])


def test_three_nodes_right_chain():
    tree = BinarySearchTree()
    for key in [10, 20, 30]:
        tree.insert_key(key)
    assert_inorder(tree, [10, 20, 30])
    assert_reverse_inorder(tree, [30, 20, 10])


# ============================================================
# Iterator / reverse iterator tests
# ============================================================

def test_iterator_matches_keys():
    tree = build_tree_from_keys([20, 30, 40, 10])
    assert tree_keys(tree) == [10, 20, 30, 40]


def test_reverse_iterator_matches_keys():
    tree = build_tree_from_keys([20, 30, 40, 10])
    assert tree_keys_reversed(tree) == [40, 30, 20, 10]


def test_iterator_empty():
    tree = BinarySearchTree()
    assert list(tree) == []


def test_reversed_empty():
    tree = BinarySearchTree()
    assert list(reversed(tree)) == []


def test_iterator_single():
    tree = BinarySearchTree()
    tree.insert_key(7)
    assert tree_keys(tree) == [7]
    assert tree_keys_reversed(tree) == [7]


def test_iterator_after_clear():
    tree = build_tree_from_keys([5, 2, 8, 1, 3])
    tree.clear()
    assert list(tree) == []
    assert list(reversed(tree)) == []


# ============================================================
# Public method correctness tests
# ============================================================

def test_keys_method_basic():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    assert tree.keys() == [20, 30, 40, 50, 60, 70, 80]


def test_pairs_method_with_values():
    pairs = [(20, "a"), (10, "b"), (30, "c"), (25, "d")]
    tree = build_tree_from_pairs(pairs)
    assert_pairs_match(tree, [(10, "b"), (20, "a"), (25, "d"), (30, "c")])


def test_get_missing_returns_none():
    tree = build_tree_from_pairs([(10, "x"), (5, "y"), (15, "z")])
    assert tree.get(100) is None


def test_is_in_basic():
    tree = build_tree_from_keys([8, 3, 10, 1, 6])
    assert tree.is_in(8) is True
    assert tree.is_in(1) is True
    assert tree.is_in(99) is False


def test_clear_nonempty_tree():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    tree.clear()
    assert_empty_tree(tree)


# ============================================================
# Update-value tests
# ============================================================

def test_update_root_value():
    tree = BinarySearchTree()
    tree.insert(Pair(50, "old"))
    tree.insert(Pair(50, "new"))
    assert tree.get(50) == "new"
    assert_pairs_match(tree, [(50, "new")])


def test_update_leaf_value():
    tree = build_tree_from_pairs([(50, "a"), (30, "b"), (70, "c"), (20, "d")])
    assert tree.insert(Pair(20, "updated")) is False
    assert tree.get(20) == "updated"
    assert_pairs_match(tree, [(20, "updated"), (30, "b"), (50, "a"), (70, "c")])


def test_update_internal_value():
    tree = build_tree_from_pairs([(50, "a"), (30, "b"), (70, "c"), (60, "d"), (80, "e")])
    assert tree.insert(Pair(70, "updated")) is False
    assert tree.get(70) == "updated"
    assert_pairs_match(tree, [(30, "b"), (50, "a"), (60, "d"), (70, "updated"), (80, "e")])


# ============================================================
# Build-order tests
# ============================================================

def test_randomish_build_order_1():
    assert_sorted_property_after_build([50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55])


def test_randomish_build_order_2():
    assert_sorted_property_after_build([8, 3, 10, 1, 6, 14, 4, 7, 13])


def test_randomish_build_order_3():
    assert_sorted_property_after_build([15, 10, 20, 8, 12, 17, 25, 6, 11, 16, 27])


def test_sorted_insert_order():
    assert_sorted_property_after_build([1, 2, 3, 4, 5, 6, 7, 8, 9])


def test_reverse_sorted_insert_order():
    assert_sorted_property_after_build([9, 8, 7, 6, 5, 4, 3, 2, 1])


def test_duplicate_heavy_build():
    tree = build_tree_from_keys([5, 3, 7, 3, 7, 5, 3, 5, 7, 4, 6])
    assert_inorder(tree, [3, 4, 5, 6, 7])
    assert_reverse_inorder(tree, [7, 6, 5, 4, 3])


# ============================================================
# Delete leaf tests
# ============================================================

def test_delete_leaf_left():
    tree = build_tree_from_keys([20, 10, 30])
    assert_delete_result(tree, 10, True, [20, 30])


def test_delete_leaf_right():
    tree = build_tree_from_keys([20, 10, 30])
    assert_delete_result(tree, 30, True, [10, 20])


def test_delete_leaf_deeper():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80, 35])
    assert_delete_result(tree, 35, True, [20, 30, 40, 50, 60, 70, 80])


def test_delete_leaf_smallest():
    tree = build_tree_from_keys([50, 30, 70, 20, 40])
    assert_delete_result(tree, 20, True, [30, 40, 50, 70])


def test_delete_leaf_largest():
    tree = build_tree_from_keys([50, 30, 70, 60, 80])
    assert_delete_result(tree, 80, True, [30, 50, 60, 70])


# ============================================================
# Delete one-child tests
# ============================================================

def test_delete_node_with_only_left_child():
    tree = build_tree_from_keys([20, 10, 5])
    assert_delete_result(tree, 10, True, [5, 20])


def test_delete_node_with_only_right_child():
    tree = build_tree_from_keys([20, 30, 40])
    assert_delete_result(tree, 30, True, [20, 40])


def test_delete_root_with_only_left_child():
    tree = build_tree_from_keys([20, 10])
    assert_delete_result(tree, 20, True, [10])


def test_delete_root_with_only_right_child():
    tree = build_tree_from_keys([20, 30])
    assert_delete_result(tree, 20, True, [30])


def test_delete_internal_with_one_child_left():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 35])
    assert_delete_result(tree, 40, True, [20, 30, 35, 50, 70])


def test_delete_internal_with_one_child_right():
    tree = build_tree_from_keys([50, 30, 70, 60, 80, 65])
    assert_delete_result(tree, 60, True, [30, 50, 65, 70, 80])


# ============================================================
# Delete two-children tests
# ============================================================

def test_delete_root_two_children_small():
    tree = build_tree_from_keys([20, 10, 30])
    assert tree.delete(20) is True
    assert_inorder(tree, [10, 30])


def test_delete_root_two_children_medium():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    assert tree.delete(50) is True
    assert_inorder(tree, [20, 30, 40, 60, 70, 80])
    assert_reverse_inorder(tree, [80, 70, 60, 40, 30, 20])


def test_delete_internal_two_children_left_subtree():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 35, 45])
    assert tree.delete(30) is True
    assert_inorder(tree, [20, 35, 40, 45, 50, 70])


def test_delete_internal_two_children_right_subtree():
    tree = build_tree_from_keys([50, 30, 70, 60, 80, 55, 65])
    assert tree.delete(70) is True
    assert_inorder(tree, [30, 50, 55, 60, 65, 80])


def test_delete_two_children_complex():
    tree = build_tree_from_keys([50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55])
    assert tree.delete(50) is True
    assert_inorder(tree, [20, 25, 30, 35, 40, 55, 60, 65, 70, 80])


# ============================================================
# Delete missing key tests
# ============================================================

def test_delete_missing_from_nonempty_1():
    tree = build_tree_from_keys([20, 10, 30])
    assert_delete_result(tree, 999, False, [10, 20, 30])


def test_delete_missing_from_nonempty_2():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    assert_delete_result(tree, 65, False, [20, 30, 40, 50, 60, 70, 80])


def test_delete_missing_after_some_deletes():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    tree.delete(20)
    tree.delete(80)
    assert_delete_result(tree, 999, False, [30, 40, 50, 60, 70])


# ============================================================
# Repeated delete sequence tests
# ============================================================

def test_delete_many_sequence_1():
    tree = build_tree_from_keys([50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55])
    expected_sequences = [
        (55, [20, 25, 30, 35, 40, 50, 60, 65, 70, 80]),
        (20, [25, 30, 35, 40, 50, 60, 65, 70, 80]),
        (70, [25, 30, 35, 40, 50, 60, 65, 80]),
        (50, [25, 30, 35, 40, 60, 65, 80]),
    ]
    for key, expected in expected_sequences:
        assert tree.delete(key) is True, f"delete({key}) should be True"
        assert_inorder(tree, expected)


def test_delete_many_sequence_2():
    tree = build_tree_from_keys([10, 5, 15, 3, 7, 12, 17, 1, 4, 6, 8])
    deletes = [1, 4, 7, 10, 12, 17]
    expected = [
        [3, 4, 5, 6, 7, 8, 10, 12, 15, 17],
        [3, 5, 6, 7, 8, 10, 12, 15, 17],
        [3, 5, 6, 8, 10, 12, 15, 17],
        [3, 5, 6, 8, 12, 15, 17],
        [3, 5, 6, 8, 15, 17],
        [3, 5, 6, 8, 15],
    ]
    for key, exp in zip(deletes, expected):
        assert tree.delete(key) is True
        assert_inorder(tree, exp)


def test_delete_until_empty_from_balanced_tree():
    keys = [4, 2, 6, 1, 3, 5, 7]
    tree = build_tree_from_keys(keys)

    for key in [1, 3, 2, 5, 7, 6, 4]:
        assert tree.delete(key) is True

    assert_empty_tree(tree)


def test_delete_until_empty_from_right_chain():
    tree = build_tree_from_keys([1, 2, 3, 4, 5, 6])
    for key in [6, 5, 4, 3, 2, 1]:
        assert tree.delete(key) is True
    assert_empty_tree(tree)


def test_delete_until_empty_from_left_chain():
    tree = build_tree_from_keys([6, 5, 4, 3, 2, 1])
    for key in [1, 2, 3, 4, 5, 6]:
        assert tree.delete(key) is True
    assert_empty_tree(tree)


# ============================================================
# Root-focused tests
# ============================================================

def test_root_changes_after_delete_1():
    tree = build_tree_from_keys([20, 10, 30, 5, 15])
    assert tree.delete(20) is True
    assert_inorder(tree, [5, 10, 15, 30])
    assert tree.is_in(20) is False


def test_root_changes_after_delete_2():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    assert tree.delete(50) is True
    assert_inorder(tree, [20, 30, 40, 60, 70, 80])
    assert tree.is_in(50) is False


def test_delete_root_repeatedly():
    tree = build_tree_from_keys([40, 20, 60, 10, 30, 50, 70])
    for key, expected in [
        (40, [10, 20, 30, 50, 60, 70]),
        (30, [10, 20, 50, 60, 70]),
        (20, [10, 50, 60, 70]),
        (10, [50, 60, 70]),
        (50, [60, 70]),
        (60, [70]),
        (70, []),
    ]:
        assert tree.delete(key) is True
        assert_inorder(tree, expected)


# ============================================================
# Value-preservation tests during delete
# ============================================================

def test_delete_preserves_other_values():
    pairs = [
        (50, "a"),
        (30, "b"),
        (70, "c"),
        (20, "d"),
        (40, "e"),
        (60, "f"),
        (80, "g")
    ]
    tree = build_tree_from_pairs(pairs)
    assert tree.delete(30) is True
    assert tree.get(20) == "d"
    assert tree.get(40) == "e"
    assert tree.get(50) == "a"
    assert tree.get(60) == "f"
    assert tree.get(70) == "c"
    assert tree.get(80) == "g"


def test_delete_root_preserves_values():
    pairs = [
        (20, "root"),
        (10, "left"),
        (30, "right"),
        (5, "ll"),
        (15, "lr"),
    ]
    tree = build_tree_from_pairs(pairs)
    assert tree.delete(20) is True
    remaining = tree.keys()
    assert remaining == [5, 10, 15, 30]
    assert tree.get(5) == "ll"
    assert tree.get(10) == "left"
    assert tree.get(15) == "lr"
    assert tree.get(30) == "right"


# ============================================================
# Membership checks after updates/deletes
# ============================================================

def test_membership_after_deletes():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 60, 80])
    tree.delete(20)
    tree.delete(70)
    assert_membership(tree, [30, 40, 50, 60, 80], [20, 70, 999])


def test_membership_after_clear():
    tree = build_tree_from_keys([1, 2, 3, 4, 5])
    tree.clear()
    assert_membership(tree, [], [1, 2, 3, 4, 5])


# ============================================================
# String sanity tests
# ============================================================

def test_string_nonempty_is_string():
    tree = build_tree_from_keys([20, 10, 30])
    s = str(tree)
    assert isinstance(s, str)
    assert "20" in s
    assert "10" in s
    assert "30" in s


def test_string_changes_after_delete():
    tree = build_tree_from_keys([20, 10, 30])
    before = str(tree)
    tree.delete(10)
    after = str(tree)
    assert before != after, "string representation should change after structural change"
    assert "10" not in after or after.count("10") < before.count("10")


# ============================================================
# Many small specific shape tests
# ============================================================

def test_shape_case_1():
    tree = build_tree_from_keys([4, 2, 6, 1, 3, 5, 7])
    assert_inorder(tree, [1, 2, 3, 4, 5, 6, 7])


def test_shape_case_2():
    tree = build_tree_from_keys([7, 6, 5, 4, 3, 2, 1])
    assert_inorder(tree, [1, 2, 3, 4, 5, 6, 7])


def test_shape_case_3():
    tree = build_tree_from_keys([1, 7, 2, 6, 3, 5, 4])
    assert_inorder(tree, [1, 2, 3, 4, 5, 6, 7])


def test_shape_case_4():
    tree = build_tree_from_keys([100, 50, 150, 25, 75, 125, 175])
    assert_inorder(tree, [25, 50, 75, 100, 125, 150, 175])


def test_shape_case_5():
    tree = build_tree_from_keys([10, 5, 1, 7, 40, 50])
    assert_inorder(tree, [1, 5, 7, 10, 40, 50])


# ============================================================
# More delete scenarios
# ============================================================

def test_delete_predecessor_is_direct_child_case():
    tree = build_tree_from_keys([20, 10, 30, 5, 15])
    assert tree.delete(20) is True
    assert_inorder(tree, [5, 10, 15, 30])


def test_delete_predecessor_has_left_child_case():
    tree = build_tree_from_keys([50, 30, 70, 20, 40, 35])
    assert tree.delete(50) is True
    assert_inorder(tree, [20, 30, 35, 40, 70])


def test_delete_node_then_reinsert_same_key():
    tree = build_tree_from_keys([20, 10, 30])
    assert tree.delete(10) is True
    assert tree.insert_key(10) is True
    assert_inorder(tree, [10, 20, 30])


def test_delete_all_then_rebuild():
    tree = build_tree_from_keys([8, 3, 10, 1, 6, 14, 4, 7, 13])
    for key in [1, 4, 7, 6, 3, 13, 14, 10, 8]:
        assert tree.delete(key) is True
    assert_empty_tree(tree)

    for key in [5, 2, 9, 1, 3]:
        assert tree.insert_key(key) is True
    assert_inorder(tree, [1, 2, 3, 5, 9])


def test_delete_same_key_twice():
    tree = build_tree_from_keys([20, 10, 30])
    assert tree.delete(10) is True
    assert tree.delete(10) is False
    assert_inorder(tree, [20, 30])


# ============================================================
# Pair/value-oriented tests
# ============================================================

def test_pairs_after_deletes():
    tree = build_tree_from_pairs([
        (50, "a"),
        (30, "b"),
        (70, "c"),
        (20, "d"),
        (40, "e"),
        (60, "f"),
        (80, "g"),
    ])
    tree.delete(20)
    tree.delete(70)
    assert_pairs_match(tree, [(30, "b"), (40, "e"), (50, "a"), (60, "f"), (80, "g")])


def test_insert_none_values():
    tree = build_tree_from_pairs([
        (10, None),
        (5, None),
        (15, None)
    ])
    assert_pairs_match(tree, [(5, None), (10, None), (15, None)])
    assert tree.get(10) is None


def test_mixed_value_types():
    tree = build_tree_from_pairs([
        (10, "hello"),
        (5, 123),
        (15, [1, 2, 3]),
        (12, {"x": 1}),
    ])
    assert tree.get(10) == "hello"
    assert tree.get(5) == 123
    assert tree.get(15) == [1, 2, 3]
    assert tree.get(12) == {"x": 1}


# ============================================================
# Bulk checks on several datasets
# ============================================================

def test_dataset_1():
    keys = [12, 5, 18, 2, 9, 15, 19, 13, 17]
    tree = build_tree_from_keys(keys)
    expected = sorted(keys)
    assert_inorder(tree, expected)
    for k in expected:
        assert tree.is_in(k) is True


def test_dataset_2():
    keys = [42, 21, 84, 10, 30, 63, 95, 25, 35, 60, 70]
    tree = build_tree_from_keys(keys)
    expected = sorted(keys)
    assert_inorder(tree, expected)
    assert_reverse_inorder(tree, list(reversed(expected)))


def test_dataset_3():
    keys = [90, 80, 70, 60, 50, 40, 30, 20]
    tree = build_tree_from_keys(keys)
    expected = sorted(keys)
    assert_inorder(tree, expected)


def test_dataset_4():
    keys = [11, 7, 3, 9, 8, 10, 15, 13, 20, 18]
    tree = build_tree_from_keys(keys)
    expected = sorted(keys)
    assert_inorder(tree, expected)


def test_dataset_5():
    keys = [100, 90, 110, 85, 95, 105, 115, 83, 87, 93, 97]
    tree = build_tree_from_keys(keys)
    expected = sorted(keys)
    assert_inorder(tree, expected)
    assert_keys_method(tree, expected)


# ============================================================
# Stress-ish but still reasonable tests
# ============================================================

def test_insert_1_to_20():
    keys = list(range(1, 21))
    tree = build_tree_from_keys(keys)
    assert_inorder(tree, keys)
    assert_reverse_inorder(tree, list(reversed(keys)))


def test_insert_20_to_1():
    keys = list(range(20, 0, -1))
    tree = build_tree_from_keys(keys)
    assert_inorder(tree, list(range(1, 21)))
    assert_reverse_inorder(tree, list(range(20, 0, -1)))


def test_delete_even_numbers_from_1_to_20():
    keys = list(range(1, 21))
    tree = build_tree_from_keys(keys)
    for key in range(2, 21, 2):
        assert tree.delete(key) is True
    assert_inorder(tree, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])


def test_delete_odd_numbers_from_1_to_20():
    keys = list(range(1, 21))
    tree = build_tree_from_keys(keys)
    for key in range(1, 21, 2):
        assert tree.delete(key) is True
    assert_inorder(tree, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])


def test_delete_all_from_1_to_15():
    keys = list(range(1, 16))
    tree = build_tree_from_keys(keys)
    for key in range(1, 16):
        assert tree.delete(key) is True
    assert_empty_tree(tree)


# ============================================================
# Regression-like tests based on your earlier examples
# ============================================================

def test_user_style_test0_but_with_asserts():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    tree.insert_key(10)

    assert_inorder(tree, [10, 20, 30, 40])
    assert_reverse_inorder(tree, [40, 30, 20, 10])
    assert tree.is_in(10) is True
    assert tree.is_in(50) is False
    assert_pairs_match(tree, [(10, None), (20, None), (30, None), (40, None)])
    assert_keys_method(tree, [10, 20, 30, 40])


def test_user_style_test1_but_with_asserts():
    tree = BinarySearchTree()
    keys = [50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55]
    for key in keys:
        tree.insert_key(key)

    assert tree.delete(55) is True
    assert_inorder(tree, [20, 25, 30, 35, 40, 50, 60, 65, 70, 80])

    assert tree.delete(20) is True
    assert_inorder(tree, [25, 30, 35, 40, 50, 60, 65, 70, 80])

    assert tree.delete(70) is True
    assert_inorder(tree, [25, 30, 35, 40, 50, 60, 65, 80])

    assert tree.delete(50) is True
    assert_inorder(tree, [25, 30, 35, 40, 60, 65, 80])
    assert_reverse_inorder(tree, [80, 65, 60, 40, 35, 30, 25])


def test_user_style_test2_but_with_asserts():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    tree.insert_key(10)

    pairs = [a for a in tree]
    assert [p.key for p in pairs] == [10, 20, 30, 40]


# ============================================================
# Extra sanity tests around repeated methods
# ============================================================

def test_call_keys_multiple_times():
    tree = build_tree_from_keys([5, 2, 8, 1, 3])
    k1 = tree.keys()
    k2 = tree.keys()
    k3 = tree.keys()
    assert k1 == [1, 2, 3, 5, 8]
    assert k2 == [1, 2, 3, 5, 8]
    assert k3 == [1, 2, 3, 5, 8]


def test_call_pairs_multiple_times():
    tree = build_tree_from_pairs([(5, "a"), (2, "b"), (8, "c"), (1, "d"), (3, "e")])
    p1 = [(p.key, p.value) for p in tree.pairs()]
    p2 = [(p.key, p.value) for p in tree.pairs()]
    assert p1 == p2 == [(1, "d"), (2, "b"), (3, "e"), (5, "a"), (8, "c")]


def test_get_after_delete():
    tree = build_tree_from_pairs([(10, "a"), (5, "b"), (15, "c")])
    assert tree.delete(5) is True
    assert tree.get(5) is None
    assert tree.get(10) == "a"
    assert tree.get(15) == "c"


def test_is_in_after_reinsert():
    tree = build_tree_from_keys([10, 5, 15])
    assert tree.delete(5) is True
    assert tree.is_in(5) is False
    assert tree.insert_key(5) is True
    assert tree.is_in(5) is True
    assert_inorder(tree, [5, 10, 15])


# ============================================================
# Run all tests
# ============================================================

TESTS = [
    test_empty_tree_initial_state,
    test_clear_on_empty_tree,
    test_delete_on_empty_tree,
    test_string_on_empty_tree,

    test_single_insert_key,
    test_single_insert_pair,
    test_single_duplicate_insert_key,
    test_single_duplicate_insert_pair_updates_value,
    test_single_delete_root,
    test_single_delete_missing,

    test_two_nodes_left,
    test_two_nodes_right,
    test_three_nodes_balanced,
    test_three_nodes_left_chain,
    test_three_nodes_right_chain,

    test_iterator_matches_keys,
    test_reverse_iterator_matches_keys,
    test_iterator_empty,
    test_reversed_empty,
    test_iterator_single,
    test_iterator_after_clear,

    test_keys_method_basic,
    test_pairs_method_with_values,
    test_get_missing_returns_none,
    test_is_in_basic,
    test_clear_nonempty_tree,

    test_update_root_value,
    test_update_leaf_value,
    test_update_internal_value,

    test_randomish_build_order_1,
    test_randomish_build_order_2,
    test_randomish_build_order_3,
    test_sorted_insert_order,
    test_reverse_sorted_insert_order,
    test_duplicate_heavy_build,

    test_delete_leaf_left,
    test_delete_leaf_right,
    test_delete_leaf_deeper,
    test_delete_leaf_smallest,
    test_delete_leaf_largest,

    test_delete_node_with_only_left_child,
    test_delete_node_with_only_right_child,
    test_delete_root_with_only_left_child,
    test_delete_root_with_only_right_child,
    test_delete_internal_with_one_child_left,
    test_delete_internal_with_one_child_right,

    test_delete_root_two_children_small,
    test_delete_root_two_children_medium,
    test_delete_internal_two_children_left_subtree,
    test_delete_internal_two_children_right_subtree,
    test_delete_two_children_complex,

    test_delete_missing_from_nonempty_1,
    test_delete_missing_from_nonempty_2,
    test_delete_missing_after_some_deletes,

    test_delete_many_sequence_1,
    test_delete_many_sequence_2,
    test_delete_until_empty_from_balanced_tree,
    test_delete_until_empty_from_right_chain,
    test_delete_until_empty_from_left_chain,

    test_root_changes_after_delete_1,
    test_root_changes_after_delete_2,
    test_delete_root_repeatedly,

    test_delete_preserves_other_values,
    test_delete_root_preserves_values,

    test_membership_after_deletes,
    test_membership_after_clear,

    test_string_nonempty_is_string,
    test_string_changes_after_delete,

    test_shape_case_1,
    test_shape_case_2,
    test_shape_case_3,
    test_shape_case_4,
    test_shape_case_5,

    test_delete_predecessor_is_direct_child_case,
    test_delete_predecessor_has_left_child_case,
    test_delete_node_then_reinsert_same_key,
    test_delete_all_then_rebuild,
    test_delete_same_key_twice,

    test_pairs_after_deletes,
    test_insert_none_values,
    test_mixed_value_types,

    test_dataset_1,
    test_dataset_2,
    test_dataset_3,
    test_dataset_4,
    test_dataset_5,

    test_insert_1_to_20,
    test_insert_20_to_1,
    test_delete_even_numbers_from_1_to_20,
    test_delete_odd_numbers_from_1_to_20,
    test_delete_all_from_1_to_15,

    test_user_style_test0_but_with_asserts,
    test_user_style_test1_but_with_asserts,
    test_user_style_test2_but_with_asserts,

    test_call_keys_multiple_times,
    test_call_pairs_multiple_times,
    test_get_after_delete,
    test_is_in_after_reinsert,
]


if __name__ == "__main__":
    for test in TESTS:
        run_test(test)
    summary()