from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

with open("Prompter.txt") as f:     ## great way to read files with open("txt") as f:   text = f.read()
    text = f.read()

template = """Based on the following instrutions, help me write a good prompt TEMPLATE for the following task:

{objective}

Notably, this prompt TEMPLATE expects that additional information will be provided by the end user of the prompt you are writing. For the piece(s) of information that they are expected to provide, please write the prompt in a format where they can be formatted into as if a Python f-string.

When you have enough information to create a good prompt, return the prompt in the following format:\n\n```prompt\n\n...\n\n```

Instructions for a good prompt:

{text}
"""

# prompt = PromptTemplate.from_template(template)                                                 # translates the text template to a prompt 
# prompt = prompt.partial(text = text)                                                            # since text is something that doesnt change we can add it here instead of chain.invoke({"text":text,...}) so now we can remove it form the invoke

# or the more propper way to do it :            This is better since the PromptTepmplate only builds a single text whiche the Chatprompt you can add system user and assistance ... so better for longer agenst
prompt = ChatPromptTemplate.from_messages([
    ("system", template)
]).partial(text=text)

chain  = prompt | ChatOpenAI(model="gpt-4-1106-preview", temperature=0) | StrOutputParser()     # usually model =ChatOpenAI(.....) then ...| model |...


## THE REST IS WILL BE PROVIDED FROM THE SERVER

# objective = "answer a question based on provided, and ONLY on that context."

# for token in chain.stream({"objective":objective}):
#     print(token, end="")