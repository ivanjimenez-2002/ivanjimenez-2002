from langchain_core.utils import secret_from_env
from newsapi import NewsApiClient
import datetime
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Initialize the News API client
# The NewsApiClient is initialized with the API key stored in the environment variable 'NEWS_API_KEY'.
# This function takes a string of topics as input and fetches news articles related to those topics.
# The function returns a JSON string containing the articles.
def get_news(topics: str):
    newsapi = NewsApiClient(os.environ.get('NEWS_API_KEY'))
    yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    all_articles = newsapi.get_everything(q=topics,
                                      from_param=yesterday_date,
                                      language='en',
                                      sort_by='relevancy',
                                      page=3,
                                      page_size=3)

    return json.dumps(all_articles, indent=2)


from jinja2 import Template # Library for rendering HTML templates
from weasyprint import HTML # Library for converting HTML to PDF

# Function to generate a PDF from the entries
# The function takes a list of entries, each containing information about a news article.
def generate_pdf(entries):
    # Define the HTML template for the PDF
    # The template uses Jinja2 syntax to dynamically insert data into the HTML structure.
    template_html = """<html>
    <head>
    <style>
        .header {
        text-align: center;
        font-size: 24px;
        margin: 20px 0;
        }

        .entry {
        width: 90%;
        margin: 0 auto 20px auto;  /* auto left & right centers it */
        border: 1px solid #ccc;
        padding: 16px;
        border-radius: 5px;
        }

        .entry img {
        display: block;
        margin: 0 auto;
        max-width: 70%;
        height: auto;
        }

        .entry p {
        margin: 8px 0;
        line-height: 2;
        font-size: 16px;
        }

        .URL {
        margin: 8px 0;
        line-height: 2;
        font-size: 16px;
        text-decoration: underline;
        color: blue;
        }

        .page-break {
        page-break-after: always;
        }
    </style>
    </head>
    <body>
    <h1 class="header">News Reports</h1>
    {% for item in entries %}
        <div class="entry">
        <h2>{{ item.title }}</h2>
        <img src="{{ item.url_image }}" alt="News image">
        <p><strong>Topic:</strong> {{ item.topic }}</p>
        <p><strong>Description:</strong> {{ item.description }}</p>
        <p><strong>Date:</strong> {{ item.date }}</p>
        <a href="{{ item.url }}" class="URL">You can read more here!</a>
        <p><strong>Comment:</strong> {{ item.comment }}</p>
        <p><strong>Outlook:</strong> {{ item.outlook }}</p>
        </div>
        {% if not loop.last %}
            <div class="page-break"></div>
        {% endif %}
    {% endfor %}
    </body>
    </html>
    """
    # Create a Jinja2 Template object from the HTML string
    # This allows us to render the HTML with dynamic data.
    template = Template(template_html)
    rendered_html = template.render(entries=entries)

    # Convert the rendered HTML to a PDF file using WeasyPrint
    # The PDF is saved with the name "news_report.pdf"
    # HTML(string=rendered_html).write_pdf("news_report.pdf") # This one saves in the current directory

    # Save the PDF to the user's Desktop
    # The path is constructed using os.path.join to ensure compatibility across different operating systems.
    # The PDF will be saved in the "Desktop" folder of the user's home directory.
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    pdf_path = os.path.join(desktop_path, "news_report.pdf")
    HTML(string=rendered_html).write_pdf(pdf_path)
    print(f"PDF saved to: {pdf_path}")

# search_tool = Tool(
#         name="get_news",
#         func=get_news,
#         description="Get the latest news articles related to AI and ML. The output is a JSON string containing the articles.",
# )

# save_tool = Tool(
#         name="save_to_text",
#         func=save_to_text,
#         description="Saves the output to a text file. The output is a string.",
# )
