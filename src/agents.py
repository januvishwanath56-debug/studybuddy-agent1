"""
agents.py
StudyBuddy Agents - Easy, beginner-friendly version.

This file contains:
1. TaskExtractionAgent  - understands the raw text
2. PrioritizationAgent  - ranks tasks
3. SchedulerAgent       - creates study blocks
4. ReminderAgent        - simulates reminders

This matches the multi-agent concepts from the Google AI Agents Intensive course.
"""

from datetime import datetime, timedelta
from dateutil import parser as dateparser


# --------------------------------------------------------------------
# 1) TASK EXTRACTION AGENT
# --------------------------------------------------------------------

class TaskExtractionAgent:
    """
    Turns user text into structured tasks.
    Example:
      "Math homework due 2025-12-01, 3 hours"
    """

    def __init__(self, logger=None):
        self.logger = logger

    def extract(self, text: str):
        tasks = []

        for line in text.strip().split("\n"):
            line = line.strip()
            if not line:
                continue

            parts = line.split("due")
            title = parts[0].strip()

            due_date = None
            hours = 1

            if len(parts) > 1:
                tail = parts[1].strip()

                if "," in tail:
                    due_str, hr_str = tail.split(",", 1)
                    due_date = due_str.strip()

                    digits = "".join([c for c in hr_str if c.isdigit()])
                    hours = int(digits) if digits else 1
                else:
                    due_date = tail.strip()

            tasks.append({
                "title": title,
                "due_date": due_date,
                "hours": hours
            })

        if self.logger:
            self.logger.info(f"TaskExtractionAgent: extracted {len(tasks)} tasks.")

        return tasks


# --------------------------------------------------------------------
# 2) PRIORITIZATION AGENT
# --------------------------------------------------------------------

class PrioritizationAgent:
    """
    Gives each task a priority score.
    Lower score = more important.
    """

    def __init__(self, logger=None):
        self.logger = logger

    def score(self, tasks):
        scored = []

        for t in tasks:
            due_val = t.get("due_date")
            hours = t.get("hours", 1)

            try:
                due_dt = dateparser.parse(due_val).date()
                days_left = (due_dt - datetime.now().date()).days
            except:
                days_left = 999   # no proper due date

            score = days_left + (hours * 0.2)

            new_t = t.copy()
            new_t["priority_score"] = score
            scored.append(new_t)

        scored.sort(key=lambda x: x["priority_score"])

        if self.logger:
            self.logger.info("PrioritizationAgent: tasks scored and sorted.")

        return scored


# --------------------------------------------------------------------
# 3) SCHEDULER AGENT
# --------------------------------------------------------------------

class SchedulerAgent:
    """
    Creates a study plan of 1–2 hour blocks.
    Each block is placed on a new day.
    """

    def __init__(self, logger=None, memory=None):
        self.logger = logger
        self.memory = memory

    def schedule(self, tasks):
        plan = []
        start = datetime.now().replace(hour=18, minute=0)

        for task in tasks:
            hrs = task.get("hours", 1)
            day = start
            blocks = []

            while hrs > 0:
                duration = min(2, hrs)

                blocks.append({
                    "task": task["title"],
                    "start": day.strftime("%Y-%m-%d %H:%M"),
                    "duration": duration
                })

                hrs -= duration
                day += timedelta(days=1)

            plan.append({
                "task": task["title"],
                "blocks": blocks
            })

        if self.logger:
            self.logger.info("SchedulerAgent: schedule created.")

        return plan


# --------------------------------------------------------------------
# 4) REMINDER AGENT (long-running operation simulation)
# --------------------------------------------------------------------

class ReminderAgent:
    """
    Creates reminder times for each task.
    In a real system, this could trigger alerts or notifications.
    """

    def __init__(self, logger=None, memory=None):
        self.logger = logger
        self.memory = memory

    def create_reminders(self, plan):
        reminders = []

        for item in plan:
            first_block_time = item["blocks"][0]["start"]
            first_dt = dateparser.parse(first_block_time)
            remind_dt = first_dt - timedelta(hours=24)

            reminders.append({
                "task": item["task"],
                "remind_at": remind_dt.strftime("%Y-%m-%d %H:%M")
            })

        if self.memory:
            self.memory.save_reminders(reminders)

        if self.logger:
            self.logger.info("ReminderAgent: reminders created.")

        return reminders
