# StudyBuddy – System Architecture

StudyBuddy is an intelligent multi-agent system designed to convert raw syllabus text, deadlines, and tasks into a personalized adaptive weekly schedule.

This document describes the internal architecture and how agents collaborate.

---

## 🧠 1. Agent Overview

StudyBuddy uses **four core agents**, each with a dedicated role:

### **1. TaskExtractionAgent**
- Input: Natural language text like *“Complete Chapter 3 and finish assignment by Monday.”*
- Output: Parsed list of task objects:
  ```json
  [
    {"task": "Complete Chapter 3", "deadline": "Monday"},
    {"task": "Finish assignment", "deadline": "Monday"}
  ]
