rm -rf data/finetuned_model/*
OMP_THREAD_LIMIT=8 lstmtraining \
	--continue_from data/model/tam.lstm \
	--model_output data/finetuned_model/ \
	--traineddata data/tess_data/tam.traineddata \
	--train_listfile data/output/tam.training_files.txt \
	--max_iterations 100
