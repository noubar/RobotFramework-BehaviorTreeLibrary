
from ..utils.Validator import *
from ..utils.Executor import *
from ..utils.Treenator import *
from ..utils.ControlNodes import *
from ..utils.Logger import *
from robot.api.deco import keyword
from robot.api.deco import not_keyword

def _make_and_execute(controlNode : int ,args):
    tree_args = push_control_node_as_first(controlNode, args)
    tree = get_tree(tree_args)
    ex = Executor()
    ex.execute_tree(tree)
    log_branch_coverage(ex.composite_nodes)
    log_line_coverage(ex.keyword_nodes)

class BTNodesKeywords():

    def __init__(self, ctx):
        """
        Constructor for BTNodesKeywords.
        """
        self.ctx = ctx

    @keyword
    def one_should_pass(self, *args):
        """
        One Should Pass *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        One Should Pass is alias of `Selector`.

        Arguments:
        | Argument   | Type   | Description                     |
        | *args      | string | Children nodes in custom syntax |

        Examples:
        | One Should Pass  -  keyword1  -  keyword2 |

        """
        _make_and_execute(ControlNodes['selector'],list(args))

    @keyword
    def fallback(self, *args):
        """
        Fallback *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        Fallback is alias of `Selector`.

        Arguments:
        | Argument   | Type   | Description                     |
        | *args      | string | Children nodes in custom syntax |

        Examples:
        | Fallback  -  keyword1  -  keyword2 |

        """
        _make_and_execute(ControlNodes['selector'],list(args))

    @keyword
    def selector(self, *args):
        """
        Selector *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        Selector corresponds the control node of Behavior Tree.
        It will pass as keyword if one of given children passes.

        Arguments:
        | Argument   | Type   | Description                     |
        | *args      | string | Children nodes in custom syntax |

        Examples:
        | Selector  -  keyword1  -  keyword2 |

        """
        _make_and_execute(ControlNodes['selector'],list(args))

    @keyword
    def all_should_pass(self, *args):
        """
        All Should Pass *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        All Should Pass is alias of `Sequence`.

        Arguments:
        | Argument   | Type   | Description                     |
        | *args      | string | Children nodes in custom syntax |

        Examples:
        | All Should Pass  -  keyword1  -  keyword2 |

        """
        _make_and_execute(ControlNodes['sequence'],list(args))

    @keyword
    def sequence(self, *args):
        """
        Sequence *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        Sequence corresponds the control node of Behavior Tree.
        It will pass as keyword if all the given children pass.

        Arguments:
        | Argument   | Type   | Description                     |
        | *args      | string | Children nodes in custom syntax |

        Examples:
        | Sequence  -  keyword1  -  keyword2 |

        """
        _make_and_execute(ControlNodes['sequence'],list(args))