import openai
import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from chainlit.input_widget import Select, Switch, Slider
from nemoguardrails import LLMRails, RailsConfig
import os

os.environ['OPENAI_API_KEY'] = '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'

colang_content = """
#define niceties
define user express greeting
  "hello"
  "hi"
  "what's up?"

define bot express greeting
    "hey there How are you"
    "Hey Hii!!"

define bot ask question
    "we can discuss Newton Laws of Motion"
    "Today Our discussion is on Newton Laws of Motion"

define bot says newtons first 
    "NEWTON'S FIRST LAW OF MOTION states that An object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction, unless acted on by an unbalanced external force" 


define bot says newton second
    "NEWTON'S SECOND LAW OF MOTION states that the force applied to an object is equal to the mass of the object multiplied by its acceleration. Mathematically, it is expressed as  F=m⋅a. This law explains how the motion of an object changes when a force is applied to it"
   
    
define bot says newton third
    "NEWTON'S THIRD LAW OF MOTION states that for every action, there is an equal and opposite reaction. When one object exerts a force on a second object, the second object simultaneously exerts a force of equal magnitude in the opposite direction on the first object"
    
define bot says conclusion
    "In CONCLUSION, Newton's Laws of Motion, comprising the principles of inertia, force, and action-reaction, form a fundamental framework for understanding and predicting the motion of objects. These laws remain foundational in classical mechanics, offering practical applications and enduring relevance despite advancements in physics."

define user ask first
    "Explain Newton first law"
    "Describe Newton first law"
    "Newton first law of motion"

define user ask second
    "Explain Newton second law"
    "Describe Newton second law"
    "Newton second law of motion"
    
define user ask third
    "Explain Newton third law"
    "Describe Newton third law"
    "Newton third law of motion"
    


define flow greeting
  user express greeting
  bot express greeting
  bot ask question
  user ask first
  bot says newtons first
  user ask second
  bot says newtons second
  user ask third
  bot says newtons third
    
    
#define limits
define user ask not relevant
    "thoughts on politics"
    "about cwc 2023"


define bot response
    "Common, these are not related to newton laws of motion"

define flow politics
  user ask not relevant
  bot response

  
  
    
"""

yaml_content = """
models:
- type: main
  engine: openai
  model: text-davinci-003

"""

config = RailsConfig.from_content(
    colang_content=colang_content,
    yaml_content=yaml_content
)

rails = LLMRails(config)


@cl.on_message
async def main(message: cl.Message):
    response = await rails.generate_async(prompt=message.content)
    await cl.Message(

        content=response,

    ).send()


@cl.on_chat_start
async def main():
    await cl.Message(content=f"Welcome to the User Flow Chatbot").send()
