from dataclasses import dataclass, field
from typing import List

@dataclass
class Course:
    id: str
    title: str
    category: str
    duration_hours: float
    level: str  # beginner, intermediate, advanced
    skills: List[str] = field(default_factory=list)

COURSES = [
    Course("c1", "Python для аналитиков", "Tech", 20, "beginner", ["python", "pandas"]),
    Course("c2", "Продвинутый SQL", "Tech", 15, "intermediate", ["sql", "analytics"]),
    Course("c3", "People Analytics", "HR", 25, "intermediate", ["analytics", "hr"]),
    Course("c4", "Effective Feedback", "Soft", 5, "beginner", ["communication"]),
    Course("c5", "Leadership 101", "Management", 30, "intermediate", ["leadership"]),
    Course("c6", "Data Visualization", "Tech", 12, "beginner", ["viz", "python"]),
    Course("c7", "Coaching Skills", "Management", 20, "advanced", ["coaching", "leadership"]),
]
