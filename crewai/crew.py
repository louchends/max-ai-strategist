# Realistic implementation of Crew class
class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
    def kickoff(self):
        results = []
        for task in self.tasks:
            results.append(f"{task.agent.role} working on: {task.description}")
        return results