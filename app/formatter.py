import re

def format_llm_text(text: str) -> str:
    """
    Identifies markdown-like patterns in a block of text and converts them
    to consistently formatted HTML.

    Args:
        text: A string containing the raw text with markdown.

    Returns:
        A string containing the formatted HTML.
    """
    html_output = ""
    # Split text into lines, stripping leading/trailing whitespace from the block
    lines = text.strip().split('\n')
    in_list = False

    for line in lines:
        # Handle Headings (e.g., ## My Heading)
        match_h2 = re.match(r'^##\s(.*)', line)
        if match_h2:
            if in_list:
                html_output += "</ul>\n"
                in_list = False
            html_output += f"<h2>{match_h2.group(1).strip()}</h2>\n"
            continue

        match_h3 = re.match(r'^###\s(.*)', line)
        if match_h3:
            if in_list:
                html_output += "</ul>\n"
                in_list = False
            html_output += f"<h3>{match_h3.group(1).strip()}</h3>\n"
            continue

        # Handle Bullet Points (e.g., * My Item)
        match_li = re.match(r'^\*\s(.*)', line)
        if match_li:
            if not in_list:
                html_output += "<ul>\n"
                in_list = True
            html_output += f"  <li>{match_li.group(1).strip()}</li>\n"
            continue

        # If a line is not a special format and not empty, it's a paragraph
        if line.strip():
            if in_list:
                html_output += "</ul>\n"
                in_list = False
            html_output += f"<p>{line.strip()}</p>\n"

    # Close any open list tag at the end of the document
    if in_list:
        html_output += "</ul>\n"

    # Handle inline formatting like **bold** using a global substitution
    html_output = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_output)

    return html_output