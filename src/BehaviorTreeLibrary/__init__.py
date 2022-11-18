
from robotlibcore import DynamicCore

from .keywords import (
    BTNodesKeywords,
    CoverageNodesKeywords,
    HelperKeywords,
)
from .version import VERSION


class BehaviorTreeLibrary(DynamicCore):
    """BehaviorTreeLibrary is a web testing library for Robot Framework.
     new library or hacking the source code. See
    [https://github.com/robotframework/BehaviorTreeLibrary/blob/master/docs/extending/extending.rst#Plugins|plugin API]
    documentation for further details.

    Plugin API is new BehaviorTreeLibrary 4.0
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(
        self,
        max_repeat=0,
    ):
        """BehaviorTreeLibrary can be imported with several optional arguments.
        - ``max_repeat``:
          Default value for `timeouts` used with ``Repeat ...`` keywords.
          max_repeat = 0 means that there is no limit in this case it is possible that the repeat keyword can land in an endless loop.
        """
        self.max_repeat = max_repeat
        libraries = [
          BTNodesKeywords(self),
          CoverageNodesKeywords(self),
          HelperKeywords(self),
        ]
        self._running_keyword = None
        DynamicCore.__init__(self, libraries)
