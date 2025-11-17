# Evaluation & Testing

StudyBuddy includes simple but effective tests to validate agent correctness.

---

## 1. Unit Tests

### ✔ Task Extraction Test
Validates:
- Agent extracts at least one task  
- Deadlines are correctly recognized  

### ✔ Prioritization Test
Checks:
- Highest priority is assigned correctly  
- Sorting rules work  

### ✔ Scheduler Test
Ensures:
- Output includes "scheduled_day"  
- Schedule respects deadlines  

---

## 2. Manual Evaluation

We tested the system with:
- Large syllabus paragraphs  
- Mixed deadlines  
- Multi-step assignments  

Results showed:
- Correct task segmentation  
- Stable ordering  
- Balanced weekly distribution  

---

## 3. Performance Indicators

### ⭐ Correctness  
Tasks are interpreted accurately.

### ⭐ Consistency  
Same inputs → same output.

### ⭐ Efficiency  
Produces a schedule in under 1 second (depending on LLM runtime).

---

## 4. What Could Be Improved
- Add agent-level scoring  
- Add historical performance metrics  
- Integrate a feedback loop for user corrections  

---

# Summary
The system has strong baseline reliability, validated through unit tests and sample runs. Further improvements can make it more robust for larger academic workloads.
