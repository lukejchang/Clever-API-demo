# Luke Chang
# Clever API demo: getting average number of students per section
# 10/4/2016

import sys

import requests

def assert_status(status_code):
  if status_code != 200:
    print 'API request not successful, status:', error_code
    sys.exit()

def get_sections_data(params=None):
  request_url = 'https://api.clever.com/v1.1/sections'
  if params is not None:
    request_url += params
  r = requests.get(request_url, headers={'Authorization':'Bearer DEMO_TOKEN'})
  assert_status(r.status_code)
  return r.json()

# Get the number of sections so we can set the paging limit correctly
count_data = get_sections_data('?count=true')
section_count = count_data['count']
sections_data = get_sections_data('?limit=' + str(section_count))
sections = sections_data['data']
student_count = 0
for section in sections:
  student_count += len(section['data']['students'])

average_student_count = (student_count + 0.0) / len(sections)

print "Average students per section:", average_student_count