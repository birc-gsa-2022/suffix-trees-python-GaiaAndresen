import suffixTree as st
import tree



def positiveTest(gen):
    failIndex, failNode = yield from gen
    assert failIndex == -1, f"Did fail at index {failIndex}"

def negativeTest(gen, expIndex):
    failIndex, failNode = yield from gen
    assert failIndex != -1, "Did not fail"
    if expIndex is not None:
        assert failIndex == expIndex, f"Did not fail it index {expIndex}, but at {failIndex}"

def test_findExact():
    x = y = "aaa"
    leaf = tree.Leaf((0,3))
    t = tree.Tree({"a" : leaf}, (0, 0)) #Not true suffix tree
    res = list(positiveTest(st.findExact(y, x, t)))
    assert res == [0], f"findExact returned wrong item. Got {res}"

    y = "bbb"
    failIndex = 0
    res = list(negativeTest(st.findExact(y,x,t), failIndex))
    assert res == [], f"findExact did not return empty list. Got {res}"

    x = "aa"
    y = "a"
    leaf0 = tree.Leaf((2, 2))
    leaf1 = tree.Leaf((1, 2))
    leaf2 = tree.Leaf((0, 2))
    node1 = tree.Tree({"a": leaf2, "": leaf1}, (0, 1))
    root = tree.Tree({"a": node1, "": leaf0}, (0, 0))
    res = list(positiveTest(st.findExact(y,x,root)))
    assert res == [0, 1], f"findExact got incorrect result. Got {res}"

