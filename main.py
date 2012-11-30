import httplib2
import os


from apiclient.discovery import build
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from oauth2client.appengine import AppAssertionCredentials
from django.utils import simplejson as json

# BigQuery API Settings
SCOPE = 'https://www.googleapis.com/auth/bigquery'
PROJECT_NUMBER = 'xxxxxxxx' # REPLACE WITH YOUR Project ID

# Create a new API service for interacting with BigQuery
credentials = AppAssertionCredentials(scope=SCOPE)
httpss = credentials.authorize(httplib2.Http())
bigquery_service = build('bigquery', 'v2', http=httpss)


class GetTableData(webapp.RequestHandler):
  def get(self):
    inputData = self.request.get("inputData")
    queryData = {'query':'SELECT SUM(word_count) as sum_for_the,corpus_date,group_concat(corpus) FROM [publicdata:samples.shakespeare] WHERE word="' + inputData + '" and corpus_date>0 GROUP BY corpus_date ORDER BY sum_for_the ASC ignore case;','timeoutMs':'10000'}
    tableData = bigquery_service.jobs()
    listReply = tableData.query(projectId=PROJECT_NUMBER,body=queryData).execute()
    resp = []
    if 'rows' in listReply:
      for row in listReply['rows']:
        for key,dict_list in row.iteritems():
          count = dict_list[0]
          year = dict_list[1]
          corpus = dict_list[2]
          resp.append({'count': count['v'],'year':year['v'],'corpus':corpus['v']})
    else:
      resp.append({'count':'0','year':'0','corpus':'0'})
    
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(resp))
    
class ShowHome(webapp.RequestHandler):
  def get(self):
    template_data = {}
    template_path = 'index.html'
    self.response.out.write(template.render(template_path,template_data))

class ShowChart(webapp.RequestHandler):
  def get(self):
    template_data = {}
    template_path = 'ShowChart.html'
    self.response.out.write(template.render(template_path,template_data))

application = webapp.WSGIApplication(
                                     [('/chartPage',ShowChart),
				      ('/getTableData',GetTableData),
                                      ('/',ShowHome)
                                    ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
