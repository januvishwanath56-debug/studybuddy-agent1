from src.agents import TaskExtractionAgent, PrioritizationAgent, SchedulerAgent

def test_task_extraction():
    agent = TaskExtractionAgent()
    tasks = agent.run("Finish math homework by Monday")
    assert len(tasks) > 0

def test_prioritization():
    agent = PrioritizationAgent()
    tasks = [{"task": "Finish math", "deadline": "Monday"}]
    prioritized = agent.run(tasks)
    assert prioritized[0]["task"] == "Finish math"

def test_scheduler():
    agent = SchedulerAgent()
    schedule = agent.run(
        [{"task": "Finish math", "deadline": "Monday"}]
    )
    assert "scheduled_day" in schedule[0]
