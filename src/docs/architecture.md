# StudyBuddy Agent – System Architecture

## 1. Overview
StudyBuddy is a multi-agent system that converts raw study inputs—tasks, deadlines, syllabus text—into a clean, adaptive study schedule. The system uses modular agents that collaborate through a centralized Orchestrator.

---

## 2. Agent Architecture

### **1. TaskExtractionAgent**
- Input: Natural language task descriptions.
- Output: Structured tasks with `{task, deadline, metadata}`.
- Capabilities:
  - Extracts tasks using rule-based parsing + LLM refinement.
  - Detects deadlines.
  - Splits multi-part tasks.

---

### **2. PrioritizationAgent**
- Input: List of structured tasks.
- Output: List of tasks sorted by importance/urgency.
- Capabilities:
  - Deadline-based ranking.
  - Difficulty estimation.
  - Load balancing for long schedules.

---

### **3. SchedulerAgent**
- Input: Prioritized tasks.
- Output: Schedule with assigned days `{task, scheduled_day}`.
- Logic:
  - Distributes tasks across the week.
  - Avoids task clustering.
  - Ensures deadlines are respected.

---

## 3. Memory Architecture

### **Short-term memory (in Orchestrator)**
Stores:
- Current task list  
- Prioritized output  
- Intermediate schedule

### **Long-term memory**
Implemented using `MemoryBank`:
- Saves past tasks
- Helps recognize recurring patterns
- Supports consistency across sessions

---

## 4. Observability Layer

Provides:
- Logging  
- Debug tracing  
- Inspection of agent decisions  

Each agent logs:
- Inputs received  
- Outputs produced  
- Internal decisions  

---

## 5. Orchestrator Flow

The Orchestrator coordinates the entire workflow:

```
User Input → TaskExtractionAgent
              ↓
      PrioritizationAgent
              ↓
        SchedulerAgent
              ↓
         Final Schedule
```

---

## 6. Summary
The architecture is designed to be:
- Modular  
- Extensible  
- Easy to use  
- LLM-ready  

This makes StudyBuddy a scalable multi-agent workflow suitable for academic productivity.
