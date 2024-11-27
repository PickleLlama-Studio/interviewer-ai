from operator import itemgetter

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import Runnable, RunnablePassthrough, RunnableLambda
from langchain.schema.runnable.config import RunnableConfig
from langchain.memory import ConversationBufferMemory

from chainlit.types import ThreadDict
from typing import Dict, Optional
import chainlit as cl
from system_prompts import system_prompts
from codeflo_interview_content import project_overview, opening_summary, opening_call_to_action

def setup_runnable():
    memory = cl.user_session.get("memory")  # type: ConversationBufferMemory
    model = ChatOpenAI(model="gpt-4o" ,streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompts["interview_me"]),
            ("system", f"""
                Please interview the user about this project: 
                {project_overview} 
            """),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    runnable = (
        RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        )
        | prompt
        | model
        | StrOutputParser()
    )
    cl.user_session.set("runnable", runnable)


@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("memory", ConversationBufferMemory(return_messages=True))
    
    welcome_message = "If you're a solo developer or a small agency, managing multiple software projects, we really need to talk!"
    
    welcome_elements = [
        cl.Text(name="Welcome!", content=welcome_message, display="inline")
    ]
    
    await cl.Message(
        content="Building CodeFlo: An AI-Powered SaaS for Code Maintenance and Feature Development",
        elements=welcome_elements,
    ).send()
    
    res = await cl.AskActionMessage(
        content="Ready to go?",
        actions=[
            cl.Action(name="continue", value="continue", label="✅ Continue"),
            cl.Action(name="cancel", value="cancel", label="❌ Cancel"),
        ],
    ).send()

    if res and res.get("value") == "continue":
        elements = [
            cl.Text(name="Here's some context...", content=opening_summary, display="inline")
        ]

        await cl.Message(
            content="Let's get started!",
            elements=elements,
        ).send()
        
        res = await cl.AskActionMessage(
            content="Ready to start the interview?",
            actions=[
                cl.Action(name="continue", value="continue", label="✅ Let's start"),
                cl.Action(name="cancel", value="cancel", label="❌ Cancel"),
            ],
        ).send()
        if res and res.get("value") == "continue":
            elements = [
                cl.Text(name="First things first...", content=opening_call_to_action, display="inline")
            ]

            await cl.Message(
                content="Let's get started!",
                elements=elements,
            ).send()
            
            setup_runnable()
    else:
        await cl.Message(
            content="Alright, let me know if you change your mind!",
        ).send()
    
    


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    memory = ConversationBufferMemory(return_messages=True)
    root_messages = [m for m in thread["steps"] if m["parentId"] == None]
    for message in root_messages:
        if message["type"] == "user_message":
            memory.chat_memory.add_user_message(message["output"])
        else:
            memory.chat_memory.add_ai_message(message["output"])

    cl.user_session.set("memory", memory)

    setup_runnable()


@cl.on_message
async def on_message(message: cl.Message):
    memory = cl.user_session.get("memory")  # type: ConversationBufferMemory

    runnable = cl.user_session.get("runnable")  # type: Runnable

    res = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await res.stream_token(chunk)

    await res.send()

    memory.chat_memory.add_user_message(message.content)
    memory.chat_memory.add_ai_message(res.content)