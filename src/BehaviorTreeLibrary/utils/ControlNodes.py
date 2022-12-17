import py_trees

ControlNodes = {
    # Controls
    "selector": 0, "one should pass":0, "fallback":0,
    "sequence":1, "all should pass":1,

    # here can be extended with custom control nodes.
    }

DecoratorNodes = {
    "inverter":0
    # here can be extended with custom decorators.
    }

def _get_selector_root(nameAddon = ""):
    name = "selector" + nameAddon
    root = py_trees.composites.Selector(name)
    return root

def _get_sequence_root(nameAddon = ""):
    name = "sequence" + nameAddon
    root = py_trees.composites.Sequence(name)
    return root

def _get_inverter_node(nameAddon = "",child=None):
    name = "inverter" + nameAddon
    root = py_trees.decorators.Inverter(child=child,name=name)
    return root


# map the inputs to the function blocks
_get_root = {
    0 : _get_selector_root,
    1 : _get_sequence_root,
}
# map the inputs to the function blocks
_get_decorator = {
    0 : _get_inverter_node,
}

def get_bt_root(composite:int,nameAddon = None):
    return _get_root[composite](nameAddon)

def get_bt_deco(composite:int,nameAddon = None,child=None):
    return _get_decorator[composite](nameAddon,child)

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