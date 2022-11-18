from BehaviorTreeLibrary.utils.Validator import *
from BehaviorTreeLibrary.utils.Executor import *
from BehaviorTreeLibrary.utils.Treenator import *
from BehaviorTreeLibrary.utils.BTKeywordNodes import BTKeywordNode
import py_trees

def _get_tree_from_btlibrary(args_input):
    created_tree = get_tree(args_input)
    return created_tree

def _compare_trees(tree1,tree2):
    t1 = py_trees.display.ascii_tree(tree1, show_status=True)
    t2 = py_trees.display.ascii_tree(tree2, show_status=True)
    assert (t1 == t2)

# test tree 1
input1 = ['selector', '-', 'Log to console', 'hurraa', '-', 'Fail', 'fail2']
created_tree = _get_tree_from_btlibrary(input1)
# create the tree manually
child1 = BTKeywordNode('Log to console',['hurraa'])
child2 = BTKeywordNode('Fail', ['fail2'])
deep1 = py_trees.composites.Selector("selector0",children=[child1,child2])
_compare_trees(deep1,created_tree)

# test tree 2
input2 = ['selector', '-', 'a', 'arg1', 'arg2', '-', 'b', 'arg1', '-', 'c', '-', 'd', '-', 'All Should Pass', '-', '-', 'e', '-', '-', 'f', '-', '-', 'Fail', 'fail2', '-', 'g']
created_tree = _get_tree_from_btlibrary(input2)
# create the tree manually
child1 = BTKeywordNode('e',['hurraa'])
child2 = BTKeywordNode('f', ['fail2'])
child3 = BTKeywordNode('Fail', ['fail2'])
deep2 = py_trees.composites.Sequence("sequence0",children=[child1,child2,child3])
child1 = BTKeywordNode('a',['arg1','arg2'])
child2 = BTKeywordNode('b',['arg1'])
child3 = BTKeywordNode('c',[])
child4 = BTKeywordNode('d',[])
child5 = BTKeywordNode('g',[])
deep1 = py_trees.composites.Selector("selector1",children=[child1,child2,child3,child4,deep2,child5])
_compare_trees(deep1,created_tree)


# test tree 3
input2 = ['selector', '-', 'a', '-', 'b', '-', 'c', '-', 'sequence', '-', '-', 'd', '-', '-', 'e', '-', '-', 'selector','-', '-', '-', 'f', '-', '-', '-', 'g', '-', 'c']
created_tree = _get_tree_from_btlibrary(input2)
# create the tree manually
child1 = BTKeywordNode('f',[])
child2 = BTKeywordNode('g', [])
deep3 = py_trees.composites.Selector("selector0",children=[child1,child2])
child1 = BTKeywordNode('d',[])
child2 = BTKeywordNode('e', [])
deep2 = py_trees.composites.Sequence("sequence1",children=[child1,child2,deep3])
child1 = BTKeywordNode('a',[])
child2 = BTKeywordNode('b',[])
child3 = BTKeywordNode('c',[])
child4 = BTKeywordNode('c',[])
deep1 = py_trees.composites.Selector("selector2",children=[child1,child2,child3,deep2,child4])
_compare_trees(deep1,created_tree)

