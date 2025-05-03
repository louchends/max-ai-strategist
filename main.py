from crewai import Agent, Task, Crew
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

with open('max_tone.txt', 'r') as f:
    max_tone = f.read()

planner = Agent(
    role='Content Strategist',
    goal='Plan 3 Instagram post ideas per week that reflect Max’s underground DJ life and cultural reality.',
    backstory=f"You’re Max’s strategist. Tone: playful, grounded, meme-aware. {max_tone}",
    verbose=True,
    llm=llm
)

stylist = Agent(
    role='Caption Stylist',
    goal='Rewrite ideas into Max’s tone: ironic, grounded, minimal but punchy.',
    backstory=f"You’re Max’s ghostwriter. Keep it authentic, not influencer-y. {max_tone}",
    verbose=True,
    llm=llm
)

critic = Agent(
    role='Creative Director',
    goal='Critique all posts. Delete anything bland or off-brand.',
    backstory="You’re the final filter. No clichés. Just strong, underground energy.",
    verbose=True,
    llm=llm
)

task1 = Task(description='Create 3 content ideas for Max’s Instagram.', agent=planner)
task2 = Task(description='Rewrite ideas in Max’s tone.', agent=stylist)
task3 = Task(description='Review and filter captions.', agent=critic)

crew = Crew(agents=[planner, stylist, critic], tasks=[task1, task2, task3])
result = crew.kickoff()
print(result)
