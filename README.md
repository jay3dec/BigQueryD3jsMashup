Steps to Setting Up BigQueryD3js MashUp Online

1) First of all go to Google App Engine .Sign up if u haven’t yet and create an application. Lets name it simplemashup.appspot.com . This is where we will be hosting out Mash Up application.

2) Now go to the Application Dashboard and click on Application settings under Administration.Note the Service Account Name and Application Identifier. They will be required later on.

3) Now go to Google API Console .Sign up if u haven’t yet.

4) Now create a new project by clicking on the create link in the left side dropdown list.Lets name it Mashup.

5) In left side there might be Services tab.Click on it.Now it displays a list of Service offered by Google.Since we are fetching data from Google Big Query, enable BigQuery API.

6) Now click on the Team option in the left side and enter the Service Account Name from appengine that we noted down earlier with a can Edit permission.

7)Now go to the Overview option and note down the Project Number. It will be required later.

8) Ok now we are ready to deploy our application source.But before that we need to add a few things.Unzip the Source Code.And go to the app.yaml file and replace the application: applicationIdentifier with application: simplemashup (We have noted it down earlier, remember!)

9) Now go to main.py and replace the PROJECT_NUMBER with the Project Number that we had noted down earlier.

10) Now go to index.html page and search for http://bigqueryd3jsmashup.appspot.com/chartPage change it to http://simplemashup.appspot.com/chartPage. There might be one more link like this at the top in Home link.Please replace that too.

11) Now we are ready to deploy our application.Go to the Google App Engine SDK folder(GAE Python SDK Ver 1.7.3), and deploy it using the command ./appcfg.py update .

12)Thats it! Now try browsing simplemashup.appspot.com.