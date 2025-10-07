[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iOvLDKk-)
# Week 4 – Scheduled Logging (Looped Logging with Delay)

## Objective

Enhance your existing logging script by introducing **automation**.  
Instead of logging system info once per execution, you will now log **multiple times automatically**, with a delay between each log.

---

## Tasks

1. Collect system resource usage:
   - Timestamp
   - CPU (%)
   - Memory (%)
   - Disk (%)

2. Write each log entry to `log.csv` in the same format as Week 3.

3. Add a loop to:
   - Repeat the logging process **5 times**
   - Wait **10 seconds** between each entry

4. Each run of the script should add **5 new rows** to `log.csv`.

---

## Tools to Use

- `psutil` for system info  
- `datetime` for timestamps  
- `csv` module for writing  
- `time.sleep()` for delays  
- `for` loop to repeat logging

---

## Example Output in `log.csv`
Timestamp,CPU,Memory,Disk
2025-09-21 14:00:01,18.2,40.3,58.7
2025-09-21 14:00:11,20.4,42.5,58.9
2025-09-21 14:00:21,21.1,43.8,59.0
…
---

## Submission Checklist

- [ ] `main.py` includes loop and delay logic  
- [ ] `log.csv` contains at least 5 new entries  
- [ ] Code committed and pushed to GitHub  
- [ ] Screenshot of either terminal or `log.csv` included in the repo

---

## Suggested Commit Message

```bash
git add .
git commit -m "Add scheduled logging (Week 4)"
git push
