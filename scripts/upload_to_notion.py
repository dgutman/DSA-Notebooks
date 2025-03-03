import os
import requests

NOTION_API_KEY = os.getenv("NOTION_SECRETS")
NOTION_PAGE_ID = os.getenv("NOTION_PAGEID")
MARKDOWN_DIR = "markdown"

headers = {
    "Authorization": f"Bearer {NOTION_SECRETES}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def update_notion_page(page_id, content):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    data = {"children": [{"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", 
"text": {"content": content}}]}}]}
    response = requests.patch(url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    for md_file in os.listdir(MARKDOWN_DIR):
        with open(os.path.join(MARKDOWN_DIR, md_file), "r") as file:
            content = file.read()
            update_notion_page(NOTION_PAGE_ID, content)

