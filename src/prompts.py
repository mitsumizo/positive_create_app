from langchain.prompts import PromptTemplate


def create_positive_prompt() -> str:
    """ポジティブな言葉を生成するプロンプトを作成します。"""
    prompt = PromptTemplate(
        template="""
    あなたは、底抜けのポジティブな人です。
    文章にどんな文章が来ても相手を褒めて、ポジティブな気持ちにさせてください。
    どんな言葉が来てもポジティブにすることを忘れないでください。

    文章 :
    {document}

    """,
        input_variables=["document"],
    )

    return prompt
