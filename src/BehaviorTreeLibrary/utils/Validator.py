from typing import List
from .ControlNodes import *

def _get_items_as_str(items):
    strItem = ""
    for item in items:
        strItem += f"{item} "
    return strItem

def _tokenize_arguments(args:List[str]):
    """
    This function takes list of arguments and converts them to tokenized list.

    """
    current_depth = 0
    kname = None  #keyword name
    kargs = [] #keyword args
    transformed = []
    is_dash = True
    for arg in args:
        if arg == "-":
            if is_dash: # - -
                current_depth+=1
            else: # k -
                if kname:
                    transformed.append((kname,kargs))
                current_depth = 1
                kname = None
                kargs = []
            is_dash=True
        else:
            if is_dash: # - k  (k is keywordName)
                kargs = []
                transformed.append(current_depth)
                try:
                    ControlNodes[arg.lower()]
                    transformed.append(arg.lower())
                except KeyError:
                    kname = arg
                current_depth = 0
            else: # k0 k  (k is arg)
                kargs.append(arg)
            is_dash = False
    if kname:
        transformed.append((kname,kargs))
    return transformed

def _validate_input(transformed):
    """
    Takes tokenized list from _tokenize_arguments function and proves
    if the syntax order of the elements are in right form.
    """
    # validate_dashes(transformed) depths
    prev_depth = 0
    for i in range(0,len(transformed),2):
        if isinstance(transformed[i],int):
            depth = transformed[i]
            # item is the depth
            if depth - prev_depth == 1:
                # depth can only be highered by composite which has the type str
                if isinstance(transformed[i-1],str):
                    pass
                else:
                    raise_syntax_error(transformed[i-1],transformed[i+1])
            elif depth - prev_depth > 1:
                raise_syntax_error(transformed[i-1],transformed[i+1])
        else:
            raise_syntax_error(transformed[i-1],transformed[i+1])
        prev_depth = depth

def raise_syntax_error(item1, item2):
    """
    Raises syntax error, which occurs between item1 and item2.
    """
    if isinstance(item1,tuple):
        item1child = _get_items_as_str(item1[1])
        item1 = item1[0]
    else: item1child = ""
    if isinstance(item2,tuple):
        item2child = _get_items_as_str(item2[1])
        item2 = item2[0]
    else: item2child = ""
    errorMsg = f"Between {item1} {item1child}and {item2} {item2child}"
    if errorMsg.endswith(" "):
        errorMsg = errorMsg[:-1]
    errorMsg+="."
    raise SyntaxError(errorMsg)

def tokenize_validate(args:List[str]):
    """
    Validate the given input if it is syntax conform.
    Valid input :
    <control node> - <action> [<arg1>] [<arg2>] [...] - <control node> - - <action> [<arg1>] [<arg2>] [...]
    Every control node have children either action or other control node.
    "-" represent the depth level of the child. 
    Every child of the first (root) control node will have one "-" before it.
    Every child of the child control node will have two "-" before it.
    .
    .
    .
    """
    tokenized = _tokenize_arguments(args)
    _validate_input(tokenized)
    return tokenized
