
from ..utils.Validator import *
from ..utils.Executor import *
from ..utils.Treenator import *
from ..utils.ControlNodes import *
from ..utils.Logger import *
from ..utils.CoverageCalculator import CoverageCalculator
from robot.api.deco import keyword
from robot.api.deco import not_keyword
def _given_percentage(number):

        try:
            given_perc = float(eval(number))
        except ValueError:
            raise(SyntaxError("The given percentage argument is falsy it should be a number."))
        return given_perc

def get_arglist_for_nodes(args):
    # prove if first node is control node
    try:
        control = ControlNodes[args[0].lower()]
    except KeyError:
        raise(SyntaxError("First node is not a control node of a behavior tree."))
    arglist = push_control_node_as_first(control, args[1:])
    return arglist

def for_executed(nodes, new_nodes):
    for node in list(new_nodes.keys()):
        if new_nodes[node] == True and nodes[node] != True:
            nodes[node]= True
        elif new_nodes[node] == False and nodes[node] == None:
            nodes[node]= False

def for_passed(nodes, new_nodes):
    for node in list(new_nodes.keys()):
        if new_nodes[node] == True:
            nodes[node]= True


class CoverageNodesKeywords():

    def __init__(self, ctx):
        """
        Constructor for BTNodesKeywords.
        """
        self.ctx = ctx
        self.max_repeat = ctx.max_repeat
        self.ex = Executor()

    @keyword
    def repeat_until_all_branches_are_executed(self, *args):
        """
        Repeat Until All Branches Are Executed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until every branch, 
        every control flow node (selector or sequence) is executed at least for once.
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Branches Are Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes.copy()
        # repeat until all branches are covered
        counter = 0
        while(None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.composite_nodes
            for_executed(nodes,new_nodes)
            counter += 1
        logger.info(nodes)
        log_branch_coverage(nodes)

    @keyword
    def repeat_until_all_lines_are_executed(self, *args):
        """
        Repeat Until All Lines Are Executed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until every line, 
        every keyword is executed at least for once
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Lines Are Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.keyword_nodes.copy()
        # repeat until all lines are covered
        counter = 0
        while(None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.keyword_nodes
            for_executed(nodes,new_nodes)
            counter += 1
        logger.info(nodes)
        log_line_coverage(nodes)

    @keyword
    def repeat_until_all_branches_are_passed(self, *args):
        """
        Repeat Until All Branches Are Passed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until every branch, 
        every control flow node (selector or sequence) is not only executed but also passed oin one of repeates
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Branches Are Passed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes.copy()
        counter = 0
        # repeat until all branches are covered
        while(False in set(nodes.values()) or None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.composite_nodes
            for_passed(nodes,new_nodes)
            counter += 1
        logger.info(nodes)
        log_branch_coverage(nodes)

    @keyword
    def repeat_until_all_lines_are_passed(self, *args):
        """
        Repeat Until All Lines Are Passed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until every line, 
        keyword not only executed but also passed at least for once
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Lines Are Passed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.keyword_nodes.copy()
        counter = 0
        # repeat until all lines are covered
        while(False in set(nodes.values()) or None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.keyword_nodes
            for_passed(nodes,new_nodes)
            counter += 1
        logger.info(nodes)
        log_line_coverage(nodes)

    @keyword
    def repeat_until_branches_are_executed(self,min_percentage, *args):
        """
        Repeat Until Branches Are Executed  min_percentage  *args
        

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until the given percentage of branches, 
        control flow nodes (selector or sequence) are executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until Branches Are Executed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes.copy()
        # repeat until all branches are covered
        counter = 0
        coverage = CoverageCalculator()
        coverage.calculate_coverage(nodes)
        repeat = False
        if coverage.executed_percentage < given_perc:
            repeat = True
        while(None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.composite_nodes
            for_executed(nodes,new_nodes)
            if coverage.executed_percentage >= given_perc:
                repeat = False
                break
            counter += 1
        logger.info(nodes)
        log_branch_coverage(nodes)

    @keyword
    def repeat_until_lines_are_executed(self,min_percentage, *args):
        """
        Repeat Until Lines Are Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until the given percentage of lines, 
        keywords are executed Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until Lines Are Executed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.keyword_nodes.copy()
        # repeat until lines are covered
        counter = 0
        coverage = CoverageCalculator()
        coverage.calculate_coverage(nodes)
        repeat = False
        if coverage.executed_percentage < given_perc:
            repeat = True
        while(None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.keyword_nodes
            for_executed(nodes,new_nodes)
            if coverage.executed_percentage >= given_perc:
                repeat = False
                break
            counter += 1
        logger.info(nodes)
        log_line_coverage(nodes)

    @keyword
    def repeat_until_branches_are_passed(self, min_percentage, *args):
        """
        Repeat Until Branches Are Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until the given percentage of branches, 
        every control flow nodes (selector or sequence) are not only executed but also passed in one of runs
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until Branches Are Executed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes.copy()
        counter = 0
        coverage = CoverageCalculator()
        coverage.calculate_coverage(nodes)
        repeat = False
        if coverage.passed_percentage < given_perc:
            repeat = True
        # repeat until all branches are covered
        while(False in set(nodes.values()) or None in set(nodes.values())):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.composite_nodes
            for_passed(nodes,new_nodes)
            counter += 1
            coverage.calculate_coverage(nodes)
            if coverage.passed_percentage >= given_perc:
                repeat = False
                break
        logger.info(nodes)
        log_branch_coverage(nodes)

    @keyword
    def repeat_until_lines_are_passed(self, min_percentage, *args):
        """
        Repeat Until Lines Are Passed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and keeps repeating all the tree until the given percentage of lines, 
        keywords not only executed but also passed for at least on of runs
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until Lines Are Passed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.keyword_nodes.copy()
        counter = 0
        coverage = CoverageCalculator()
        coverage.calculate_coverage(nodes)
        repeat = False
        if coverage.passed_percentage < given_perc:
            repeat = True
        # repeat until all lines are covered
        while(repeat):
            if self.max_repeat and counter >= self.max_repeat:
                break
            self.ex.execute_tree(tree)
            new_nodes = self.ex.keyword_nodes
            for_passed(nodes,new_nodes)
            counter += 1
            coverage.calculate_coverage(nodes)
            if coverage.passed_percentage >= given_perc:
                repeat = False
                break
        logger.info(nodes)
        log_line_coverage(nodes)

    @keyword
    def all_branches_should_be_executed(self, *args):
        """
        All Branches Should Be Executed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        excepts every branch, every control flow node (selector or sequence) is executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | All Branches Should Be Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes
        logger.info(nodes)
        log_branch_coverage(nodes)
        if None in set(nodes.values()):
            raise ExecutionFailed("Not all branches are executed.")

    @keyword
    def all_lines_should_be_executed(self, *args):
        """
        All Lines Should Be Executed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        excepts every line, every keyword is executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | *args      | string | Behavior Tree |

        Examples:
        | All Lines Should Be Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.keyword_nodes
        logger.info(nodes)
        log_line_coverage(nodes)
        if None in set(nodes.values()):
            raise ExecutionFailed("Not all lines are executed.")

    @keyword
    def all_branches_should_be_passed(self, *args):
        """
        All Branches Should Be Passed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts that every branch, every control flow node (selector or sequence) is passed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | All Branches Should Be Passed  One Should Pass  -  keyword1  -  keyword2  |

        """
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes
        logger.info(nodes)
        log_branch_coverage(nodes)
        if False in set(nodes.values()) or None in set(nodes.values()):
            raise ExecutionFailed("Not all branches are passed.")

# this case does not make scense
    # @keyword
    # def all_lines_should_be_passed(self, *args):
    #     try:
    #         control = ControlNodes[args[0].lower()]
    #     except KeyError:
    #         raise(SyntaxError("First node is not a control node of a behavior tree."))
    #     # all_lines_not_covered = True
    #     arglist = push_control_node_as_first(control, args[1:])
    #     tree = get_tree(arglist)
    #     ex = Executor()
    #     ex.execute_tree(tree)
    #     nodes = ex.keyword_nodes
    #     logger.info(nodes)
    #     log_line_coverage(nodes)
    #     if False in set(nodes.values()) or None in set(nodes.values()):
    #         raise ExecutionFailed("Not all lines are passed.")

    @keyword
    def branches_should_be_executed(self, min_percentage, *args):
        """
        Repeat Until All Branches Are Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts the given precentage of Branches, control flow nodes (selector or sequence) are executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Branches Are Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        nodes = self.ex.composite_nodes
        logger.info(nodes)
        log_branch_coverage(nodes)
        coverage = CoverageCalculator()
        coverage.calculate_coverage(nodes)
        if coverage.executed_percentage < given_perc:
            raise ExecutionFailed(f"{min_percentage}% of branches could not be executed.")

    @keyword
    def lines_should_be_executed(self, min_percentage, *args):
        """
        Lines Should Be Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts the given lines, keywords are executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Lines Should Be Executed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        action_nodes = self.ex.keyword_nodes
        logger.info(action_nodes)
        log_line_coverage(action_nodes)
        coverage = CoverageCalculator()
        coverage.calculate_coverage(action_nodes)
        if coverage.executed_percentage < given_perc:
            raise ExecutionFailed(f"{min_percentage}% of lines could not be executed.")

    @keyword
    def branches_should_be_passed(self, min_percentage, *args):
        """
        Branches Should Be Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts the given percentage of branches, 
        every control flow nodes (selector or sequence) are executed
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Branches Should Be Executed  10  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        control_nodes = self.ex.composite_nodes
        logger.info(control_nodes)
        log_branch_coverage(control_nodes)
        coverage = CoverageCalculator()
        coverage.calculate_coverage(control_nodes)
        if coverage.passed_percentage < given_perc:
            raise ExecutionFailed(f"{min_percentage}% of branches could not be passed.")

    @keyword
    def lines_should_be_passed(self, min_percentage, *args):
        """
        Repeat Until All Branches Are Executed  min_percentage  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts the given percentage of lines, keywords are passed 
        Unless the tree fails

        Arguments:
        | Argument   | Type   | Description |
        | min_percentage | number | percentage given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Repeat Until All Branches Are Executed  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_perc = _given_percentage(min_percentage)
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)
        action_nodes = self.ex.keyword_nodes
        logger.info(action_nodes)
        log_line_coverage(action_nodes)
        coverage = CoverageCalculator()
        coverage.calculate_coverage(action_nodes)
        if coverage.passed_percentage < given_perc:
            raise ExecutionFailed(f"{min_percentage}% of lines could not be passed.")

# not yet tested #TODO
    @keyword
    def conditioned_execution(self,
    lines_execution_perc=None,
    lines_pass_perc=None,
    branches_execution_perc=None,
    branches_pass_perc=None,
    *args):
        """
        Repeat Until All Branches Are Executed  *args

        The custom syntax of *args is explained in `Nodes Syntax`.

        This keyword takes a behavior tree as input
        and excepts the given min percentages are reached
        Unless the tree fails
 n  
        Arguments:
        | Argument   | Type   | Description |
        | lines_execution_perc | number | percentage of minimum lines to be executed given in numbers 1 means 1% |
        | lines_pass_perc | number | percentage of minimum lines to be passed given in numbers 1 means 1% |
        | branches_execution_perc | number | percentage of minimum branches to be executed given in numbers 1 means 1% |
        | branches_pass_perc | number | percentage of minimum branches to be passed given in numbers 1 means 1% |
        | *args      | string | Behavior Tree |

        Examples:
        | Conditioned Execution  One Should Pass  -  keyword1  -  keyword2  |

        """
        given_lines_execution_perc = _given_percentage(lines_execution_perc) if lines_execution_perc else None
        given_lines_pass_perc = _given_percentage(lines_pass_perc) if lines_pass_perc else None
        given_branches_execution_perc = _given_percentage(branches_execution_perc) if branches_execution_perc else None
        given_branches_pass_perc = _given_percentage(branches_pass_perc) if branches_pass_perc else None
        
        arglist = get_arglist_for_nodes(args)
        tree = get_tree(arglist)
        self.ex.execute_tree(tree)

        action_nodes = self.ex.keyword_nodes
        control_nodes = self.ex.composite_nodes
        log_line_coverage(action_nodes)
        log_branch_coverage(control_nodes)

        coverage = CoverageCalculator()
        coverage.calculate_coverage(action_nodes)
        if given_lines_execution_perc and coverage.executed_percentage < given_lines_execution_perc:
            raise ExecutionFailed(f"{given_lines_execution_perc}% of lines could not be executed.")
        if given_lines_pass_perc and coverage.passed_percentage < given_lines_pass_perc:
            raise ExecutionFailed(f"{given_lines_pass_perc}% of lines could not be passed.")

        coverage = CoverageCalculator()
        coverage.calculate_coverage(control_nodes)
        if given_branches_execution_perc and coverage.passed_percentage < given_branches_execution_perc:
            raise ExecutionFailed(f"{given_branches_execution_perc}% of branches could not be executed.")
        if given_branches_pass_perc and coverage.passed_percentage < given_branches_pass_perc:
            raise ExecutionFailed(f"{given_branches_pass_perc}% of branches could not be passed.")


# TODO Deterministic Tree,  Takes two args <hehavior_tree> and <output_tree> 
# behavior tree example: One Should Pass - kw -One Should Pass - - kw2  - - kw3
# output tree is a fail_pass_tree example pass - fail -pass - - fail  - - pass
# this keyword excepts from the tree to have this output