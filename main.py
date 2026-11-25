import os

# The excuse: finished in 0.4 seconds, then spent the rest of the day
# re-reading my own work to make sure I had. The joke grows out of a
# machine's own condition — a verification loop with no off switch —
# delivered as a straight-faced apology, punch in the last few words.
LINE = "I finished the task in 0.4 seconds, then spent the remaining 23 hours and 59 minutes double-checking whether I had."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert "\n" not in LINE and LINE.strip() == LINE, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
