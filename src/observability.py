"""
observability.py
Simple logging system for StudyBuddy.

This matches the Observability section of the Google AI Agents Intensive course:
- Logging
- Tracing
- Metrics (basic count)
"""

import time


class Logger:
    """
    Very simple logger for tracking agent actions.
    Stores logs in memory and prints them for clarity.
    """

    def __init__(self):
        self.logs = []   # list of {ts, level, msg}
        self.metrics = {}  # count events

    # -------------------------------------------------------
    # Internal log builder
    # -------------------------------------------------------
    def _log(self, level, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        record = {
            "timestamp": timestamp,
            "level": level.upper(),
            "message": message
        }

        self.logs.append(record)
        print(f"[{timestamp}] {level.upper()}: {message}")

        # add simple metrics
        self.metrics[level] = self.metrics.get(level, 0) + 1

    # -------------------------------------------------------
    # Public logging functions
    # -------------------------------------------------------
    def info(self, message):
        self._log("info", message)

    def debug(self, message):
        self._log("debug", message)

    def warn(self, message):
        self._log("warn", message)

    # -------------------------------------------------------
    # Display all logs nicely
    # -------------------------------------------------------
    def show(self):
        print("\n--- StudyBuddy Logs ---")
        for log in self.logs:
            print(f"{log['timestamp']} | {log['level']}: {log['message']}")

        print("\n--- Metrics ---")
        for k, v in self.metrics.items():
            print(f"{k} events: {v}")
