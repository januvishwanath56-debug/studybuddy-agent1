# How StudyBuddy Works

StudyBuddy transforms messy study information into an organized weekly schedule using three intelligent agents.

---

## Step 1 — User Input
The user gives any of the following:
- A list of tasks  
- A syllabus paragraph  
- Deadlines  
- Exam preparation topics  

Example input:
```
Finish math homework by Monday, study chapter 5, complete lab report by Friday.
```

---

## Step 2 — Task Extraction
Handled by **TaskExtractionAgent**.

It:
- Reads the raw text  
- Identifies tasks  
- Detects dates  
- Splits combined sentences  

Example output:
```json
[
  {"task": "Finish math homework", "deadline": "Monday"},
  {"task": "Study chapter 5", "deadline": null},
  {"task": "Complete lab report", "deadline": "Friday"}
]
```

---

## Step 3 — Prioritization  
Handled by **PrioritizationAgent**.

Rules include:
- Earlier deadlines → higher priority  
- Harder tasks → higher rank  
- Lengthy tasks get sliced first  

Example output:
```json
[
  {"task": "Finish math homework", "deadline": "Monday"},
  {"task": "Complete lab report", "deadline": "Friday"},
  {"task": "Study chapter 5", "deadline": null}
]
```

---

## Step 4 — Scheduling  
Handled by **SchedulerAgent**.

It assigns each task a suitable day:
- Distributes workload evenly  
- Avoids putting everything on the same day  
- Meets deadline constraints  

Example output:
```json
[
  {"task": "Finish math homework", "scheduled_day": "Monday"},
  {"task": "Complete lab report", "scheduled_day": "Wednesday"},
  {"task": "Study chapter 5", "scheduled_day": "Thursday"}
]
```

---

## Step 5 — Final Output  
A nice, clean weekly plan.

---

## Step 6 — Memory + Observability
- MemoryBank stores patterns (e.g., recurring subjects).  
- Observability logs every decision so debugging is easy.  

---

## Summary
StudyBuddy runs a complete agent pipeline that:
1) Extracts  
2) Prioritizes  
3) Schedules  
4) Learns  
5) Retrieves  
6) Explains  

This makes it a highly powerful productivity assistant.
