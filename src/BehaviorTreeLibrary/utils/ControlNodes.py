import py_trees

ControlNodes = {  
    "selector": 0, "one should pass":0, "fallback":0,
    "sequence":1, "all should pass":1,
    # here can be extended with custom control nodes or decorators.
    }

def get_selector_root(nameAddon = ""):
    name = "selector" + nameAddon
    root = py_trees.composites.Selector(name)
    return root

def get_sequence_root(nameAddon = ""):
    name = "sequence" + nameAddon
    root = py_trees.composites.Sequence(name)
    return root


# map the inputs to the function blocks
get_root = {
    0 : get_selector_root,
    1 : get_sequence_root,
}

def get_bt_root(composite:int,nameAddon = None):
    return get_root[composite](nameAddon)

###############
# node pusher #
###############
def _push_selector(args:list):
    arglist = list(["selector"])
    arglist.extend(args)
    return arglist

def _push_sequence(args:list):
    arglist = list(["sequence"])
    arglist.extend(args)
    return arglist

_push_control = {
    0 : _push_selector,
    1 : _push_sequence,
    }

def push_control_node_as_first(control:int, arglist:list):
    return _push_control[control](arglist)