
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
from robot.libraries.BuiltIn import register_run_keyword

class HelperKeywords():

    def __init__(self, ctx):
        """
        Constructor for BTNodesKeywords.
        """
        self.ctx = ctx
        self.BuiltIn = BuiltIn()
        register_run_keyword('HelperKeywords', '_run_keyword_under_robot', 1)

    def _run_keyword_under_robot(self, name, args):
        return self.BuiltIn.run_keyword(name, *args)

    @keyword
    def assign_return_as_scope_variable(self, variableName, keywordName, *kwArgs):
        """
        Assign Return As Scope Variable  $VariableName  KeywordName

        Scope means either Test or Keyword. It is equivalent to local variable.

        The given keyword as argument will be executed and the return value will be saved in variable.
        This keyword can also be used as a child of behavior tree control node.

        Arguments:
        | Argument       | Type   | Description                                                       |
        | $VariableName  | string | Variable Name where the return of given keyword will be saved     |
        | KeywordName    | string | Keyword should have return value it will be saved after execution |

        Examples:
        | Assign Return As Global Variable   $variable   keyword |

        """
        if kwArgs:
            self.BuiltIn.set_local_variable(variableName,self.BuiltIn.run_keyword(keywordName, *kwArgs))
        else:
            self.BuiltIn.set_local_variable(variableName,self.BuiltIn.run_keyword(keywordName))

    @keyword
    def assign_return_as_test_variable(self, variableName, keywordName, *kwArgs):
        """
        Assign Return As Test Variable  $VariableName  KeywordName

        The given keyword as argument will be executed and the return value will be saved in variable.
        This keyword can also be used as a child of behavior tree control node.

        Arguments:
        | Argument       | Type   | Description                                                       |
        | $VariableName  | string | Variable Name where the return of given keyword will be saved     |
        | KeywordName    | string | Keyword should have return value it will be saved after execution |

        Examples:
        | Assign Return As Test Variable   $variable   keyword |

        """
        if kwArgs:
            self.BuiltIn.set_test_variable(variableName,self.BuiltIn.run_keyword(keywordName, *kwArgs))
        else:
            self.BuiltIn.set_test_variable(variableName,self.BuiltIn.run_keyword(keywordName))

    @keyword
    def assign_return_as_suite_variable(self, variableName, keywordName, *kwArgs):
        """
        Assign Return As Suite Variable  $VariableName  KeywordName

        The given keyword as argument will be executed and the return value will be saved as suite variable.
        This keyword can also be used as a child of behavior tree control node.

        Arguments:
        | Argument       | Type   | Description                                                       |
        | $VariableName  | string | Variable Name where the return of given keyword will be saved     |
        | KeywordName    | string | Keyword should have return value it will be saved after execution |

        Examples:
        | Assign Return As Suite Variable   $variable   keyword |

        """
        if kwArgs:
            self.BuiltIn.set_suite_variable(variableName,self.BuiltIn.run_keyword(keywordName, *kwArgs))
        else:
            self.BuiltIn.set_suite_variable(variableName,self.BuiltIn.run_keyword(keywordName))

    @keyword
    def assign_return_as_global_variable(self, variableName, keywordName, *kwArgs):
        """
        Assign Return As Global Variable  $VariableName  KeywordName

        The given keyword as argument will be executed and the return value will be saved as global variable.
        Difference between Suite and Global variable is that the global variable will still reachable 
        if the same robot instance continuos executing other test suite.
        This keyword can also be used as a child of behavior tree control node.

        Arguments:
        | Argument       | Type   | Description                                                       |
        | $VariableName  | string | Variable Name where the return of given keyword will be saved     |
        | KeywordName    | string | Keyword should have return value it will be saved after execution |

        Examples:
        | Assign Return As Global Variable   $variable   keyword |

        """
        if kwArgs:
            self.BuiltIn.set_global_variable(variableName,self.BuiltIn.run_keyword(keywordName, *kwArgs))
        else:
            self.BuiltIn.set_global_variable(variableName,self.BuiltIn.run_keyword(keywordName))
