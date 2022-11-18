from .ControlNodes import *
from robot.api import *
from robot.errors import ExecutionFailed
import py_trees
from py_trees.common import Status
from .Logger import logger
from .BTKeywordNodes import BTKeywordNode

class Executor:

    def __init__(self):
        self.composite_nodes = {}
        self.keyword_nodes = {}

    def _fill_dict(self, name, status, nodes_dic):
        try:
            if nodes_dic[name] == None:
                if status == Status.SUCCESS:
                    nodes_dic[name] = True
                elif status == Status.FAILURE:
                    nodes_dic[name] = False
            elif nodes_dic[name] == False:
                if status == Status.SUCCESS:
                    nodes_dic[name] = True
        except KeyError:
            if status == Status.SUCCESS:
                nodes_dic[name] = True
            elif status == Status.INVALID:
                nodes_dic[name] = None
            elif status == Status.FAILURE:
                nodes_dic[name] = False

    def _set_nodes_keywords(self, behaviour_tree):
        composite_nodes = {}
        keyword_nodes = {}
        counter = 0
        for node in behaviour_tree.root.iterate():
            if isinstance(node,BTKeywordNode):
                name = node.name + str(counter)
                self._fill_dict(name,node.status,keyword_nodes)
            else:
                name =  node.name
                self._fill_dict(name,node.status,composite_nodes)
            counter += 1
        self.composite_nodes = composite_nodes
        self.keyword_nodes = keyword_nodes
        logger.info(composite_nodes)
        logger.info(keyword_nodes)

    def execute_tree(self, pytree):
        behaviour_tree = py_trees.trees.BehaviourTree(root=pytree)
        behaviour_tree.tick_tock(1,1)
        logger.info(py_trees.display.xhtml_tree(pytree, show_status=True),html=True)
        if behaviour_tree.tip().status == py_trees.common.Status.FAILURE:
            raise ExecutionFailed("The tree has failed.")
        self._set_nodes_keywords(behaviour_tree)

