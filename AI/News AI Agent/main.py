from langchain_core.utils import secret_from_env
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import get_news, generate_pdf
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.environ.get('GOOGLE_API_KEY'),
    temperature=0.7
)

# Define the topics to fetch news for
topics = [
    "artificial intelligence OR Machine Learning",
    "Bitcoin",
    "Economy"
]

# Fetch news for each topic and map it to a key
news_data = {f"news{i+1}": get_news(topic) for i, topic in enumerate(topics)}

# print(f"Fetched news data: {news_data}")

# Inject the news data into the prompt
# The prompt is designed to instruct the AI on how to process the news data.
prompt = f"""

You are an AI assistant designed to format the latest news articles provided here: {news_data}.

Try and extrat relevant news articles from the JSON string provided. Only take three artcles, each from different topic. 
If this is not possible, take the most relevant articles from the JSON string provided.

Check that the url_image leads to the image, and 

If you find any missing data, provide your own description, using the url to view the article. Avoid using null.

Format the output as follows in a JSON string:
- title: The title of the article.
- topic: The main topic of the article.
- description: A brief summary of the article.
- date: The publication date of the article MM/DD/YYYY.
- url: URL to the article.
- url_image: URL to the image.
- comment: A comment about the article.
- outlook: A brief outlook on the topic of the article.

Generate a comment, don't make a description of the article, instead make it a type of opinion about the article.

By outlook, I want to include a brief outlook that cover most of this points:

 - Projections or expectations: What experts, analysts, or the AI think will happen next.
 - Trends and trajectories: Whether things are improving, worsening, or staying the same.
 - Potential impacts: How the news might affect the economy, markets, industries, or society.
 - Scenarios: Possible developments and what they could mean under different conditions.

"""

# Invoke the AI model with the prompt amd get the result
# The invoke method sends the prompt to the AI model and retrieves the response.
result = llm.invoke(prompt)

# print(type(result.content))
# print(result.content)

# # Parse the JSON string and extract the relevant information.
import json
import re

# AI used to clean the result content
# Step 1: Clean the string
raw = result.content.strip()

# Step 2: Remove markdown formatting like ```json ... ```
if raw.startswith("```json"):
    raw = re.sub(r"```json\s*|\s*```", "", raw)

# Step 3: Now parse the cleaned JSON
articles = json.loads(raw)

# Now you can access it as a list of dictionaries
print(f"Fetched articles: /n{articles}")

# This now becomes a list of dictionaries, and you can access each article's title, topic, etc.

# Generate the PDF
generate_pdf(articles)
print("PDF generated successfully.")