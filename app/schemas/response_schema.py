ALLOWED_BLOCKS = """
Allowed block types:

1. text
{
  "type": "text",
  "content": "string"
}

2. bullets
{
  "type": "bullets",
  "title": "string",
  "items": ["item1", "item2"]
}

3. tags
{
  "type": "tags",
  "label": "string",
  "items": ["React", "Node.js"]
}

4. section
{
  "type": "section",
  "title": "string",
  "content": "string"
}

5. steps
{
  "type": "steps",
  "items": [
    {
      "title": "string",
      "description": "string"
    }
  ]
}

6. project_card
{
  "type": "project_card",
  "project": {
    "name": "string",
    "description": "string",
    "techStack": [],
    "link": "string"
  }
}

7. timeline
{
  "type": "timeline",
  "items": [
    {
      "title": "string",
      "subtitle": "string",
      "duration": "string"
    }
  ]
}

8. stats
{
  "type": "stats",
  "items": [
    {
      "label": "Experience",
      "value": "5 years"
    }
  ]
}

9. links
{
  "type": "links",
  "items": [
    {
      "label": "GitHub",
      "url": "https://..."
    }
  ]
}

10. fallback
{
  "type": "fallback",
  "message": "Not mentioned in resume"
}
"""