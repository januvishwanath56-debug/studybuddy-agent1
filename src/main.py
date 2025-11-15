"""
StudyBuddy - Main Program
Beginner-friendly runnable version.
This file will collect user input and run the study planner.
"""

from datetime import datetime, timedelta

def extract_tasks(user_text):
    """
    A very simple task extractor for beginners.
    Example input:
    "Math homework due 2025-12-01, 3 hours"
    """
    tasks = []
    lines = user_text.strip().split("\n")
    for line in lines:
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
                due_str, hours_str = tail.split(",", 1)
                due_date = due_str.strip()
                hours = int("".join([c for c in hours_str if c.isdigit()]) or 1)
            else:
                due_date = tail.strip()

        tasks.append({
            "title": title,
            "due_date": due_date,
            "hours": hours
        })

    return tasks


def prioritize(tasks):
    """
    Sort tasks by due date.
    """
    def score(task):
        try:
            due = datetime.fromisoformat(task["due_date"])
            days_left = (due - datetime.now()).days
        except:
            days_left = 999
        
        return days_left
    
    return sorted(tasks, key=score)


def create_plan(tasks):
    """
    Create a simple schedule:
    - Assign 2 hour study blocks
    - Spread over days
    """
    plan = []
    start = datetime.now().replace(hour=18, minute=0)

    for task in tasks:
        hours_needed = int(task["hours"])
        blocks = []

        day = start
        while hours_needed > 0:
            block = {
                "task": task["title"],
                "start": day.strftime("%Y-%m-%d %H:%M"),
                "duration": min(2, hours_needed)
            }
            blocks.append(block)
            hours_needed -= 2
            day += timedelta(days=1)

        plan.append({
            "task": task["title"],
            "blocks": blocks
        })

    return plan


def demo():
    print("Running StudyBuddy demo...\n")

    sample = """
    Math homework due 2025-12-01, 3 hours
    History essay due 2025-11-30, 2 hours
    Presentation slides due 2025-12-05, 4 hours
    """

    tasks = extract_tasks(sample)
    tasks = prioritize(tasks)
    plan = create_plan(tasks)

    print("\nGenerated Study Plan:\n")
    for item in plan:
        print("Task:", item["task"])
        for block in item["blocks"]:
            print("   -", block)
        print()


if __name__ == "__main__":
    demo()
