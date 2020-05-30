import yaml

lang_info = yaml.load(open('config.yaml'),Loader=yaml.FullLoader)

language = lang_info['language']
fontlist = lang_info['fontlist']
maxpages = lang_info['maxpages']


evaluate_sh_content = '''lstmeval --model data/model/'''+ language + '''.lstm \\
  --traineddata data/tess_data/''' + language + '''.traineddata \ \
  --eval_listfile data/output/''' + language + '''.training_files.txt


#--model_dat takes the extracted model as input
#--traineddata takes the data it was trained on
#--eval_listfile takes the files that are to be evaluated
'''

evaluate_file = open("evaluate.sh","w")
evaluate_file.write(evaluate_sh_content)
evaluate_file.close()


extract_model_content = """combine_tessdata -e data/tess_data/"""  + language + """.traineddata data/model/""" + language + """.lstm

#after flag -e the first path takes the pre-existing data it was trained on
#the second path specified the output path for the model
"""

extract_model_file = open("extract_model.sh","w")
extract_model_file.write(extract_model_content)
extract_model_file.close()


generate_training_data_content = """rm -rf data/output/*
tesstrain.sh --fonts_dir data/fonts \\
	     --fontlist '""" + fontlist + """' \\
	     --lang """ + language + """ \\
	     --linedata_only \\
	     --langdata_dir data/lang_data \\
	     --tessdata_dir data/tess_data \\
	     --save_box_tiff \\
	     --maxpages """ + str(maxpages) + """ \\
	     --output_dir data/output

#the max pages will enter the amount of pages to be rendered for training purpose
"""

generate_training_data_file = open("generate_training_data.sh","w")
generate_training_data_file.write(generate_training_data_content)
generate_training_data_file.close()




train_content = """rm -rf data/finetuned_model/*
OMP_THREAD_LIMIT=8 lstmtraining \\
	--continue_from data/model/""" + language + """.lstm \\
	--model_output data/finetuned_model/ \\
	--traineddata data/tess_data/""" + language + """.traineddata \\
	--train_listfile data/output/""" + language + """.training_files.txt \\
	--max_iterations 100
"""

train_file = open("train.sh","w")
train_file.write(train_content)
train_file.close()


