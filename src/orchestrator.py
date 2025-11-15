"""
orchestrator.py
Coordinates all agents and simulates a real multi-agent flow.

This follows the agent orchestration patterns taught
in the Google AI Agents Intensive course.
"""

from src.agents import (
    TaskExtractionAgent,
    PrioritizationAgent,
    SchedulerAgent,
    ReminderAgent
)

from src.memory import MemoryBank
from src.observability import Logger


class Orchestrator:
    """
    The Orchestrator runs the complete StudyBuddy pipeline:
      1. Task Extraction Agent
      2. Prioritization Agent
      3. Scheduler Agent
      4. Reminder Agent
      5. Saves final output to Memory
      6. Logs every step (observability)
    """

    def __init__(self):
        # Observability (logs)
        self.logger = Logger()

        # Long-term memory
        self.memory = MemoryBank()

        # Agents
        self.extractor = TaskExtractionAgent(logger=self.logger)
        self.prioritizer = PrioritizationAgent(logger=self.logger)
        self.scheduler = SchedulerAgent(logger=self.logger, memory=self.memory)
        self.reminder = ReminderAgent(logger=self.logger, memory=self.memory)

    def run(self, user_text: str):
        """
        Runs the entire multi-agent pipeline in sequence.
        Returns a dictionary with structured outputs.
        """

        self.logger.info("---- Orchestrator started ----")

        # Step 1: Extract tasks
        tasks = self.extractor.extract(user_text)
        self.logger.info(f"Extracted {len(tasks)} tasks.")

        # Step 2: Prioritize
        scored = self.prioritizer.score(tasks)
        self.logger.info("Prioritization complete.")

        # Step 3: Schedule blocks
        plan = self.scheduler.schedule(scored)
        self.logger.info("Scheduling complete.")

        # Step 4: Reminders
        reminders = self.reminder.create_reminders(plan)
        self.logger.info("Reminder creation complete.")

        # Step 5: Save everything
        self.memory.save_plan(plan)

        self.logger.info("---- Orchestrator finished ----")

        # Return structure
        return {
            "tasks": tasks,
            "scored": scored,
            "plan": plan,
            "reminders": reminders,
            "logs": self.logger.logs
        }
