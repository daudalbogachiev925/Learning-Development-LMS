def completion_rate(records):
    """records: [{employee, course, completed}]"""
    if not records:
        return 0
    done = sum(1 for r in records if r["completed"])
    return round(done / len(records) * 100, 1)

def hours_per_employee(records):
    by_emp = {}
    for r in records:
        if r["completed"]:
            by_emp[r["employee"]] = by_emp.get(r["employee"], 0) + r["hours"]
    return by_emp

def top_learners(records, top_n=5):
    hours = hours_per_employee(records)
    return sorted(hours.items(), key=lambda x: -x[1])[:top_n]
