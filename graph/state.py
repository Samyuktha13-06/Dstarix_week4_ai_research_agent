from typing import TypedDict, List


class ResearchState(TypedDict):
    question: str
    search_results: str
    summary: str
    route: str
    history: List[str]