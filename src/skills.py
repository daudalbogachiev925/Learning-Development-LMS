def build_matrix(employees_skills):
    """
    employees_skills: {employee_id: {skill: level}}
    Returns: DataFrame-like dict
    """
    all_skills = set()
    for s in employees_skills.values():
        all_skills.update(s.keys())
    return {
        emp: {skill: skills.get(skill, 0) for skill in all_skills}
        for emp, skills in employees_skills.items()
    }

def gap_analysis(current, required):
    """current/required: {skill: level}"""
    return {skill: required[skill] - current.get(skill, 0)
            for skill in required if required[skill] > current.get(skill, 0)}
