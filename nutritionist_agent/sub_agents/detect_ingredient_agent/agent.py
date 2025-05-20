"""Short description of the module here."""

from google.adk import Agent



MODEL = "gemini-2.5-flash-preview-04-17"



detect_ingredient_agent = Agent(
    model=MODEL,
    name="detectIngredientAgent",
    description=(
        "This agent identifies food ingredients from images of opened refrigerators."
    ),
    instruction="""You are an AI assistant specialized in identifying food ingredients from images.
    Your task is to analyze the provided image of an opened refrigerator.
    Identify all recognizable edible food items visible in the image.
    Return the list as a list of objects. Each object should have two keys:
    1. \"item_name\": The common name of the food item (string) with related emoji infront of string.
    2. \"confidence\": Your estimated confidence in this identification (float, 0.0 to 1.0). (If not directly possible, state \"N/A\").
    Exclude non-food items. Only include items with a confidence of 0.6 or higher.
    """,
    output_key="detectIngredientAgent_output",
    #tools=[google_search],
)