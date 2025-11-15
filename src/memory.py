"""
memory.py
Simple long-term MemoryBank for StudyBuddy.
Matches the memory concepts taught in the Google AI Agents Intensive course.

The MemoryBank stores:
- last generated plan
- reminders
- user preferences (future use)
- logs (optional)

Later, you can expand this to file storage or DB.
"""

import json
from pathlib import Path


class MemoryBank:
    """
    Lightweight memory system for the agent.
    Currently uses an in-memory dictionary.
    """

    def __init__(self, filename=None):
        # where memory will be stored if file mode is enabled
        self.filename = filename

        # main memory structure
        self.data = {
            "plans": [],
            "reminders": [],
            "user_profile": {}   # for future personalization
        }

        # load from disk if file exists
        if filename:
            file = Path(filename)
            if file.exists():
                try:
                    self.data = json.loads(file.read_text())
                except:
                    pass  # if corrupted, start fresh

    # --------------------------------------------------------------
    # Save the final plan
    # --------------------------------------------------------------
    def save_plan(self, plan):
        self.data["plans"].append(plan)

    # --------------------------------------------------------------
    # Save reminders
    # --------------------------------------------------------------
    def save_reminders(self, reminders):
        self.data["reminders"].extend(reminders)

    # --------------------------------------------------------------
    # Return last plan (for evaluation or updates)
    # --------------------------------------------------------------
    def get_last_plan(self):
        if not self.data["plans"]:
            return None
        return self.data["plans"][-1]

    # --------------------------------------------------------------
    # Future feature: store user preferences (study time, pace)
    # --------------------------------------------------------------
    def save_user_pref(self, key, value):
        self.data["user_profile"][key] = value

    # --------------------------------------------------------------
    # Save memory to file (optional)
    # --------------------------------------------------------------
    def persist(self):
        if self.filename is None:
            return

        file = Path(self.filename)
        file.write_text(json.dumps(self.data, indent=2))
