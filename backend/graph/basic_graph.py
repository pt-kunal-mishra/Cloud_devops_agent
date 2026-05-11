from langgraph.graph import StateGraph,START,END
from backend.models.state import AgentState
from backend.graph.supervisor_node import supervisor_node

workflow=StateGraph(AgentState)
workflow.add_node("supervisor", supervisor_node)
workflow.add_edge(START, "supervisor")
workflow.add_edge("supervisor", END)

graph=workflow.compile()