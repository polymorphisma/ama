# chat-adex-minified

## configurations:
1. use python 3.10.12 <br>

## Instructions
1. Store each model's folder inside trainables/ folder, example trainables/HR/doc1.pdf <br>
2. run `train.py` to train for model and input model name, which should be directory name of each model in trainables/
3. to run the server use `sudo uvicorn server:app --host 127.0.0.1 --port 80 --workers 3`

## For workflow:
1. `sudo pip3 install -r requirements.txt`
2. First run `sudo aws s3 cp s3://<bucket_name>/chunkDB/ chunkDB/ --recursive`
2. run `sudo aws s3 cp s3://<bucket_name>/augment_data/ augment_data/ --recursive`
3. run `sudo uvicorn server:app --host 0.0.0.0 --port 80 --workers 2 --log-config logging_config.ini`

## Project Structure

### Folders

1. **trainables/**
   - This directory contains the trainable models and associated files necessary for the machine learning models in the project.

2. **chunkDB/**
   - The `chunkDB` folder stores the chunked data or segmented information, facilitating efficient data handling and retrieval.

3. **raw_text/**
   - In the `raw_text` directory, you'll find the raw textual data used in the project. This can include original documents, transcripts, or any other unprocessed text data.

4. **database/**
   - The `database` folder houses the project's database-related files. This may include schema definitions, queries, or other database-specific elements.

5. **augment_data/**
   - In the `augment_data` directory, you can find files and scripts related to data augmentation. Data augmentation is often crucial for enhancing model performance by increasing the diversity of the training dataset.

### .env 
LOCAL_ENV = 0
REGION_NAME = us-east-1
S3_BUCKET_NAME =
COGNITO_SIGNIN_URL = 
CLIENT_ID=your_cognito_client_id_here
USERPOOL_ID=your_userpool_id_here
REGION=your_aws_region_here
HOSTED_UI_COGNITO_DOMAIN=your_cognito_domain_here
REDIRECT_URI=your_redirect_uri_after_login