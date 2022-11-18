from robot.api import logger

def log_branch_coverage(composite_nodes):
    values = list(composite_nodes.values())
    total = len(values)
    passed_branches = 0
    execute_branches = 0
    for i in values:
        if i == True:
            passed_branches += 1
            execute_branches += 1
        elif i == False:
            execute_branches += 1
    logger.info(f'execute_branches:{execute_branches*100/total}%')
    logger.info(f'passed_branches:{passed_branches*100/total}%')

def log_line_coverage(keyword_nodes):
    values = list(keyword_nodes.values())
    total = len(values)
    passed_lines = 0
    execute_lines = 0
    for i in values:
        if i == True:
            passed_lines += 1
            execute_lines += 1
        elif i == False:
            execute_lines += 1
    logger.info(f'execute_lines:{execute_lines*100/total}%')
    logger.info(f'passed_lines:{passed_lines*100/total}%')
