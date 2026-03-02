# pythonlabs.com
Source code for pythonlabs.com

# Prerequisites
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Authenticate: `gcloud auth login`
- Set your project: `gcloud config set project <YOUR_PROJECT_ID>`

# Local testing
```
pip install -r requirements.txt
python main.py
```
Then visit http://127.0.0.1:8080

# Deploying
```
gcloud app deploy
```
