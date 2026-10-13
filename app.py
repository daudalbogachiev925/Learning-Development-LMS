import streamlit as st
import pandas as pd
import numpy as np
from src.courses import COURSES
from src.idp import recommend_courses
from src.analytics import completion_rate, top_learners

st.title("📚 Learning & Development LMS")

st.subheader("Каталог курсов")
df = pd.DataFrame([c.__dict__ for c in COURSES])
st.dataframe(df)

st.subheader("Gap Analysis + Рекомендации")
skills = ["python", "sql", "analytics", "leadership", "coaching", "communication"]
current = {s: st.slider(f"Текущий уровень: {s}", 0, 5, 2) for s in skills}
required = {s: st.slider(f"Требуемый уровень: {s}", 0, 5, 4) for s in skills}
gaps = {s: required[s] - current[s] for s in skills if required[s] > current[s]}

if gaps:
    st.write("**Gaps:**", gaps)
    recs = recommend_courses(gaps)
    for r in recs:
        st.write(f"- 📖 **{r['course']}** — закрывает: {', '.join(r['matches'])} (приоритет: {r['priority']})")

st.subheader("Аналитика обучения")
np.random.seed(42)
records = [
    {"employee": f"E{i}", "course": f"c{np.random.randint(1,8)}",
     "completed": np.random.random() > 0.3, "hours": np.random.randint(5, 30)}
    for i in range(200)
]
st.metric("Completion rate", f"{completion_rate(records)}%")
st.write("**Top learners:**", top_learners(records))
