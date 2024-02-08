export PROJECT_ID="sandbox-athevenot"
gcloud builds submit --tag eu.gcr.io/${PROJECT_ID}/bigsigths/bigquery/dataset:latest .

docker push eu.gcr.io/${PROJECT_ID}/bigsigths/bigquery/dataset:latest



# docker run \
#     -v /Users/athevenot/:/Users/athevenot/ \
#     -e GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS \
#     eu.gcr.io/${PROJECT_ID}/bigsigths/bigquery/dataset:latest
