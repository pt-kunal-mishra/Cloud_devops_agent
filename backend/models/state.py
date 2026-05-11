from typing import TypedDict
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    incident_id: str
    severity: str
    analysis: str
    remediation: str