To perform the translation, first run:
    python preprocess.py <filename> <lang>
    <lang> - 'en', 'xx' where en refers to english (for lowercasing) and xx is (any) morphologically rich language


After this, run the following to train the model:

    python translate.py
    
To make changes to the model in terms of the hyper-parameters used:


usage: translate.py [-h] [-en_size EN_SIZE] [-ta_size TA_SIZE]
                    [-en_path EN_PATH] [-ta_path TA_PATH]
                    [-en_devpath EN_DEVPATH] [-ta_devpath TA_DEVPATH]
                    [-en_vocab_path EN_VOCAB_PATH]
                    [-ta_vocab_path TA_VOCAB_PATH] [-lr LR] [-decay DECAY]
                    [-softmax_sample SOFTMAX_SAMPLE]
                    [-hidden_layer_size HIDDEN_LAYER_SIZE]
                    [-no_of_layers NO_OF_LAYERS] [-test]
                    [-grad_norm GRAD_NORM] [-batch_size BATCH_SIZE]
                    [-ckpt_path CKPT_PATH]
                    [-steps_per_checkpoint STEPS_PER_CHECKPOINT]

Help Section

  -en_size EN_SIZE, --en_size EN_SIZE:  Max Size (No. of words) of the English Vocabulary
  -ta_size TA_SIZE, --ta_size TA_SIZE:  Max Size (No. of words) of the Tamil Vocabulary
  -en_path EN_PATH, --en_path EN_PATH:  Location of English part of Bilingual Sentences
  -ta_path TA_PATH, --ta_path TA_PATH:  Location of Tamil part of Bilingual Sentences
  -en_devpath EN_DEVPATH, --en_devpath EN_DEVPATH:  Location of English Dev Bilingual Sentences
  -ta_devpath TA_DEVPATH, --ta_devpath TA_DEVPATH:  Location of Tamil Dev Bilingual Sentences
  -en_vocab_path EN_VOCAB_PATH, --en_vocab_path EN_VOCAB_PATH:  Location to save/retrieve English Vocabulary
  -ta_vocab_path TA_VOCAB_PATH, --ta_vocab_path TA_VOCAB_PATH:  Location to save/retrieve Tamil Vocabulary
  -lr LR, --lr LR:  Learning Rate
  -decay DECAY, --decay DECAY:  Learning Rate Decay Factor
  -softmax_sample SOFTMAX_SAMPLE, --softmax_sample SOFTMAX_SAMPLE:  Sample Size for Sampled SoftMax to account for Large:  Target Vocabulary
  -hidden_layer_size HIDDEN_LAYER_SIZE, --hidden_layer_size HIDDEN_LAYER_SIZE:  No. of neurons in hidden layer(s)
  -no_of_layers NO_OF_LAYERS, --no_of_layers NO_OF_LAYERS:  No. of hidden layer(s) in the encoder and decoder
  -test, --test:  If present - Testing phase
  -grad_norm GRAD_NORM, --grad_norm GRAD_NORM:  Gradient Clipping Limit
  -batch_size BATCH_SIZE, --batch_size BATCH_SIZE:  No of sentences per batch
  -ckpt_path CKPT_PATH, --ckpt_path CKPT_PATH:  Path to checkpoint files directory for model restore
  -steps_per_checkpoint STEPS_PER_CHECKPOINT, --steps_per_checkpoint STEPS_PER_CHECKPOINT:  No. of steps per checkpoint
