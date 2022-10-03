from tree import Tree as T, Leaf

def getSuffixTree(x: str) -> T:
    pass

def findExact(y: str, x: str, sufT: T | Leaf):
    node = sufT
    index = 0
    m = len(y)
    while node:
        start, end = node.label
        edgeLen = end-start
        for index in range(index, min(edgeLen, m)): #Long live python's ability to use global variables as loop variable 
            if y[index] != x[start+index]:
                return index, node # No match of y
        else:
            if index == edgeLen:
                match node:
                    case T(children):
                        node = children.get(y[index], None)
                    case Leaf():
                        return index, node
            if index == m-1: # y found, go to leaves 
                yield from findLeafLabels(node)
                return -1, node # Succesfully found string                

    return index, None
  

def findPartial(y: str, sufT: T | Leaf):
    pass

def findLeafLabels(subTree: T | Leaf):
    match subTree:
        case Leaf((start, _)):
            yield start
        case T(children, _):
            for n in children.values():
                yield from findLeafLabels(n) 
    
    #TODO make not recursive
    # node = sub
    # while
    # down, up, not self
