### How to Use

#### Note: Please Remove the .gitignore files from data/fonts and data/output before using this repository


#### Step 1: Fill the file config.yaml

language : tam
fontlist : Vijaya
maxpages : 250


Give the language code for "language"
Give the fontlist in "fontlist"
maxpage can be vary from 10 to 250. Read the docs for its details.


- change the page from 10 (which was used for testing) to 250 which seems to be a good number to avoid overfitting


#### Step 2: Generate the scripts

Run the below command

python3 generate_scripts.py




#### Step 3: Setting Up The Structure for the Repository

    .
    ├── data
    |     ├── fonts
    |     ├── lang_data
    |     ├── output
    |     └── tess_data
    └── generate_training_data.sh
  
  
#### Note: if you're training an english font, you can skip step 4.

#### Step 4: Downloading Relavent Data
- Place the font you want to train in the fonts folder
- download from link: https://github.com/tesseract-ocr/langdata and place the data inside the lang_data
- go to link: https://github.com/tesseract-ocr/ download one specific language from either tessdata_best or tessdata_fast based on your application requirement and place that inside the data/tess_data folder


#### Step 5: Running the pipeline
run the command: `execute_train_pipeline.sh`

The pipeline will do the following things:
1. Construct the data from the font
2. Extract the Model for further fine tuning
3. train the model on the new font, the new model will be saved in finetuned_model
