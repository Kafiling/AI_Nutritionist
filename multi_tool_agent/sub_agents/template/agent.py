"""Short description of the module here."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

data_analyst_agent = Agent(
    model=MODEL,
    name="data_analyst_agent",
    instruction="",
    output_key="market_data_analysis_output",
    tools=[google_search],
)