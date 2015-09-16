#!/usr/bin/env python3

stories = []

with open('stories_links_logs') as f:
  lines = f.readlines()

  for i in range(0, len(lines), 2):
    stories += [{
      'info_url': lines[i],
      'matching_html_pages': eval(lines[i+1])
    }]

for story in stories:
  if len(story['matching_html_pages']) != 1:
    print(story)