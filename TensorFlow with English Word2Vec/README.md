The implementation of this model was left out to be the same code as the one used in [this](https://www.tensorflow.org/versions/master/tutorials/seq2seq/) tutorial. Here, I have used LSTM activated RNNs with a simple encoder and attention decoder.

To run the program, use the invoke command based on this example that uses the best possible parameters for a 2 GB NVIDIA GeForce 650M graphics card:

python -m src.translate --data_dir . --train_dir checkpoints/ --en_vocab_size=75000 --fr_vocab_size=80000 --size=340 --batch_size=32 --num_layers=4 --steps_per_checkpoint=500 

Here,

data_dir: $PWD
train_dir: Location to store(d) checkpoints
en_vocab_size: No. of words to use in the English vocabulary of the trained model
ta_vocab_size: No. of words to use in the Tamil vocabulary of the trained model
size: No. of neurons in the hidden layer of RNNs
batch_size: No. of bilingual pairs of sentences per mini-batch
num_layers: No. of RNN layers for encoder and decoder
steps_per_checkpoint: Save periodically in this many steps
