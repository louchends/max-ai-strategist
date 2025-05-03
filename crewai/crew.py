
class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks

    def kickoff(self):
        results = []
        for task in self.tasks:
            result = f"{task.agent.role} working on: {task.description}"
            results.append(result)
        return results
