from backend.config.llm import llm

async def supervisor_node(state) :
    messages = state['messages']
    response=await llm.ainvoke(messages)
    
    return {
        "messages":[
            response
        ]
    }