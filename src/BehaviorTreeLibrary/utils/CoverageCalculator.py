class CoverageCalculator:

    def __init__(self):
        self.passed = 0
        self.executed = 0
        self.passed_percentage = 0
        self.executed_percentage = 0

    def calculate_coverage(self, nodes):
        values = list(nodes.values())
        total = len(values)
        passed = 0
        executed = 0
        for i in values:
            if i == True:
                passed += 1
                executed += 1
            elif i == False:
                executed += 1
        self.passed = passed
        self.executed = executed
        self.passed_percentage = passed*100/total
        self.executed_percentage = executed*100/total