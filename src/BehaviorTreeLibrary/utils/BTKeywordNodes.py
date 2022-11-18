import py_trees
import random
from .Logger import logger
from robot.libraries.BuiltIn import register_run_keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.running.model import Keyword
from robot.errors import ExecutionFailed
from robot.errors import KeywordError
from os import error

class BTKeywordNode(py_trees.behaviour.Behaviour):

    def _run_keyword_under_robot(self, name, args):
        return self.builtin.run_keyword(name, *args)
  
    def __init__(self, name, args=[]):
        """
        Minimal one-time initialisation. A good rule of thumb is
        to only include the initialisation relevant for being able
        to insert this behaviour in a tree for offline rendering to
        dot graphs.

        Other one-time initialisation requirements should be met via
        the setup() method.
        """
        super(BTKeywordNode, self).__init__(name.lower())
        self.args = args
        self.builtin = BuiltIn()
        register_run_keyword('BTKeywordNode', '_run_keyword_under_robot', 1)

    def setup(self):
        """
        When is this called?
          This function should be either manually called by your program
          to setup this behaviour alone, or more commonly, via
          :meth:`~py_trees.behaviour.Behaviour.setup_with_descendants`
          or :meth:`~py_trees.trees.BehaviourTree.setup`, both of which
          will iterate over this behaviour, it's children (it's children's
          children ...) calling :meth:`~py_trees.behaviour.Behaviour.setup`
          on each in turn.

          If you have vital initialisation necessary to the success
          execution of your behaviour, put a guard in your
          :meth:`~py_trees.behaviour.Behaviour.initialise` method
          to protect against entry without having been setup.

        What to do here?
          Delayed one-time initialisation that would otherwise interfere
          with offline rendering of this behaviour in a tree to dot graph
          or validation of the behaviour's configuration.

          Good examples include:

          - Hardware or driver initialisation
          - Middleware initialisation (e.g. ROS pubs/subs/services)
          - A parallel checking for a valid policy configuration after
            children have been added or removed
        """
        logger.debug("  %s [Foo::setup()]" % self.name)

    def initialise(self):
        """
        When is this called?
          The first time your behaviour is ticked and anytime the
          status is not RUNNING thereafter.

        What to do here?
          Any initialisation you need before putting your behaviour
          to work.
        """
        logger.debug("  %s [Foo::initialise()]" % self.name)

    def update(self):
        """
        When is this called?
          Every time your behaviour is ticked.

        What to do here?
          - Triggering, checking, monitoring. Anything...but do not block!
          - Set a feedback message
          - return a py_trees.common.Status.[RUNNING, SUCCESS, FAILURE]
        """
        logger.debug("  %s [Foo::update()]" % self.name)
        try:
            self._run_keyword_under_robot(self.name, self.args)
        except ExecutionFailed as e:
            if e.message.startswith("No keyword with name '"):
                raise e
            self.status = py_trees.common.Status.FAILURE
            return self.status
        self.status = py_trees.common.Status.SUCCESS
        return self.status
        # return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        """
        When is this called?
           Whenever your behaviour switches to a non-running state.
            - SUCCESS || FAILURE : your behaviour's work cycle has finished
            - INVALID : a higher priority branch has interrupted, or shutting down
        """
        logger.debug("  %s [Foo::terminate().terminate()][%s->%s]" % (self.name, self.status, new_status))