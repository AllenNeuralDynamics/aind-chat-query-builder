"""Script to call query builder class"""

from typing import Literal

from aind_chat_query_builder.prompts.complex_v2 import get_complex_v2_prompt
from aind_chat_query_builder.prompts.simple_v1 import get_v1_prompt
from aind_chat_query_builder.prompts.simple_v2 import get_simple_v2_prompt
from aind_chat_query_builder.utils import complex_agent_v2, simple_agent


class ChatQueryBuilder:
    """
    Class that calls query builders for different schema versions,
    with differing levels of complexity
    """

    def __init__(
        self,
        query: str,
        version: Literal["v1", "v2"],
        selectors: dict = None
    ):
        """Init class"""
        self.query = query
        self.version = version
        self.selectors = selectors

    async def simple_query_builder(self):
        """
        Simple query builder method with toggles for v1 and v2
        Returns filter dictionary to be input into MongoDB
        """

        if self.version == "v1":
            prompt = get_v1_prompt(query=self.query)

        else:
            prompt = get_simple_v2_prompt(query=self.query)

        response = await simple_agent.ainvoke(prompt)

        answer = response.tool_calls[0]["args"]["filter"]
        return answer

    async def complex_query_builder(self):
        """
        Complex query builder method, only applicable to v2
        Returns list of the aggregation pipeline
        """

        prompt = get_complex_v2_prompt(
            query=self.query,
            selectors = self.selectors
            )
        response = await complex_agent_v2.ainvoke(prompt)
        if "agg_pipeline" in response.tool_calls[0]["args"]:
            answer = response.tool_calls[0]["args"]["agg_pipeline"]

        return answer
