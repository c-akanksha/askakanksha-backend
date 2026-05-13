ALLOWED_BLOCKS = """
Allowed block types:

1. text
{
  "type": "text",
  "data": {
    "content": "string"
  }
}

2. bullets
{
  "type": "bullets",
  "data": {
    "title": "string",
    "items": ["item1", "item2"]
  }
}

3. tags
{
  "type": "tags",
  "data": {
    "label": "string",
    "items": ["React", "Node.js"]
  }
}

4. section
{
  "type": "section",
  "data": {
    "title": "string",
    "content": "string"
  }
}

5. steps
{
  "type": "steps",
  "data": {
    "items": [
      {
        "title": "string",
        "description": "string"
      }
    ]
  }
}

6. cards
{
  "type": "cards",
  "data": {
    "items": [
      {
        "title": "string",
        "subtitle": "string",
        "description": "string",
        "tags": ["React", "Node.js"],
        "link": "string",
        "meta": "optional"
      }
    ]
  }
}

7. timeline
{
  "type": "timeline",
  "data": {
    "items": [
      {
        "title": "string",
        "subtitle": "string",
        "duration": "string",
        "description": "optional"
      }
    ]
  }
}

8. stats
{
  "type": "stats",
  "data": {
    "items": [
      {
        "label": "Experience",
        "value": "5 years"
      }
    ]
  }
}

9. links
{
  "type": "links",
  "data": {
    "items": [
      {
        "label": "GitHub",
        "url": "https://..."
      }
    ]
  }
}

10. fallback
{
  "type": "fallback",
  "data": {
    "message": "Not mentioned in resume"
  }
}
"""
