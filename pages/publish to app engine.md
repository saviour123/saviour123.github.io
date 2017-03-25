title: Deploy A Flask App to Google App Engine
date: 2017-03-25
tags: [deployment, cloud, linux]
subtitle: Deploying to Google appspot should not be difficult but can be if you don't get help in the beginning. Follow this guide to deploy your Flask App to google appengine.

### Install Cloud components

<code class="prettyprint">$ gclould components install app-engine-python</code> #you can use

<code class="prettyprint">`$ sudo`</code> if you need elevated permissions
<br>
you can list the components to see if they are properly install.

<code class="prettyprint">`$ gclould components list`</code>

Proceed to login:

<code class="prettyprint">`$ gcloud login auth login`</code>

follow your browser and login

visit your cloud console and retrieve your project name
set or make your project ready for deployment:

<code class="prettyprint">`$ gcloud config set project projectname`</code>

with no errors,
lets verify if its running locally.

<code class="prettyprint">`$ gcloud app browse`</code>

lets deploy our app to app engine
<code class="prettyprint">$ gcloud app deploy</code>

lets make this version of the app visible to the world if this is **not** your first
version.
