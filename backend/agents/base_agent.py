from abc import ABC
from typing import Type

from pydantic import BaseModel

from llm import llm


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(self, prompt, output_schema: Type[BaseModel]):
        self.prompt = prompt
        self.output_schema = output_schema

        self.structured_llm = llm.with_structured_output(
            output_schema
        )

        self.chain = self.prompt | self.structured_llm

    def invoke(self, inputs: dict):
        """
        Execute the LangChain pipeline.
        """
        return self.chain.invoke(inputs)