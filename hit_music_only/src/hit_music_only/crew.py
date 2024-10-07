from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from hit_music_only.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class HitMusicOnlyCrew():
	"""HitMusicOnly crew"""

	@agent
	def songwriter(self) -> Agent:
		return Agent(
			config=self.agents_config['songwriter'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def producer(self) -> Agent:
		return Agent(
			config=self.agents_config['producer'],
			verbose=True
		)

	@task
	def songwriting(self) -> Task:
		return Task(
			config=self.tasks_config['songwriting'],
		)

	@task
	def producing(self) -> Task:
		return Task(
			config=self.tasks_config['producing'],
			output_file='song.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the HitMusicOnly crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)