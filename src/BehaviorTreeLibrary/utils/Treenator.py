from .BTKeywordNodes import BTKeywordNode
from .ControlNodes import *
from .Validator import *

def _get_deepest(tokenized):
    """ This function takes a tokenized tree and returns the indexes of first and last element of the deepest tree member"""
    prev_depth = 0
    first_index = 0
    for i in range(0,len(tokenized),2):
        depth = tokenized[i]
        if prev_depth < depth:
            first_index = i - 1
        elif prev_depth > depth:
            return [first_index , i - 1]
        prev_depth = depth
    return [first_index , len(tokenized)]

def _make_tree(tokenized):
    """
    This function gets a tokenized tree structure and converts it to a py_trees root
    """
    # The construction of the tree is easier to start from deepest member 
    deepest = _get_deepest(tokenized)
    # until there is no deeper element than the main parent itself
    # pack the deepest child to its parent
    counter = 0
    while(deepest !=[0,2]):
        first = deepest[0]
        last = deepest[1]
        root = get_bt_root(ControlNodes[tokenized[first]],str(counter))
        for i in range(first+2,last+1,2):
            keyword = tokenized[i]
            if isinstance(tokenized[i],tuple):
                keyword = BTKeywordNode(tokenized[i][0],tokenized[i][1])
            root.add_child(keyword)
        tmp = tokenized[:first].copy()
        tmp.append(root)
        if tokenized[last+1:]:
            tmp.extend(tokenized[last+1:])
        tokenized = tmp
        deepest = _get_deepest(tokenized)
        counter += 1
    # the first element is always 0 which resembles the first depth
    # the second element will be containing the whole tree
    tree = tokenized[1]
    return tree

def get_tree(arglist):
    tokenized = tokenize_validate(arglist)
    tree = _make_tree(tokenized)
    return tree
