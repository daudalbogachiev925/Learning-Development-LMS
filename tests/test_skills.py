from src.skills import gap_analysis

def test_gap_analysis():
    current = {"python": 3, "sql": 2}
    required = {"python": 5, "sql": 2, "leadership": 4}
    gaps = gap_analysis(current, required)
    assert gaps == {"python": 2, "leadership": 4}
