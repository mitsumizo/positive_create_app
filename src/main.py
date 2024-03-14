import chainlit as cl
import configs
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI
from prompts import create_positive_prompt

chat = ChatOpenAI(model=configs.AOAI_MODEL)


@cl.on_chat_start
async def onchat_start():
    await cl.Message(
        content="何でも入力してね。ポジティブな言葉に変換してあなたを応援するよ！"
    ).send()


@cl.on_message
async def on_message(input_message: cl.Message):
    result = chat(
        [
            HumanMessage(
                content=create_positive_prompt().format(document=input_message.content)
            )
        ]
    )
    await cl.Message(content=result.content).send()
