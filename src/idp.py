from src.courses import COURSES

def recommend_courses(gaps):
    """gaps: {skill: gap}"""
    recommendations = []
    for course in COURSES:
        matches = [s for s in course.skills if s in gaps]
        if matches:
            recommendations.append({
                "course": course.title,
                "matches": matches,
                "priority": sum(gaps[s] for s in matches)
            })
    return sorted(recommendations, key=lambda x: -x["priority"])
