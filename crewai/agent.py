# Realistic implementation of Agent class
class Agent:
    def __init__(self, role, goal, backstory, verbose, llm):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose
        self.llm = llm