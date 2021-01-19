source code used to analyze [how to run a subprocess inside google cloud function](https://stackoverflow.com/questions/54938099/how-to-run-a-subprocess-inside-google-cloud-function-in-python).

## running locally
To run locally, type:
```
pipenv install
pipenv run functions_framework --target exec &
curl http://localhost:8080
```

As the local environment does not run in a Cloud Function environment, it will behave differently

## running in Cloud Function
to run as a Cloud Function, type:

```
gcloud functions deploy  \
    --region europe-west1 \
    --entry-point exec \
    --runtime python39 exec \
    --trigger-http \
    --allow-unauthenticated

URL=$(gcloud functions describe exec  --region europe-west1 --format 'value(httpsTrigger.url)')
curl $URL
```
