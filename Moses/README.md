Set Up mosesdecoder, giza-pp and compile them: http://www.statmt.org/moses/?n=Development.GetStarted

Get train, dev and test corpora respectively inside Corpus folder: ADD.en, ADD.ta, dev.en, dev.ta test.en, test.ta

PWD: Master Directory (Current Directory)

PROJECT DIRECTORY STRUCTURE:

Moses/
├── Corpus
│	├── ADD.en
│   ├── ADD.ta
│   ├── dev.en
│   ├── dev.ta
│   ├── test.en
│   ├── test.ta
│   ├── lowercase.py
│   └── tokenize.py
│
├── giza-pp
│   ├── bin
│   │   ├── GIZA++
│   │   ├── mkcls
│   │   └── snt2cooc.out
│   ├── GIZA++
│   ├── Makefile
│   ├── mkcls-v2
│   └── README
├── log
├── mert.out
├── mert-work
├── mosesdecoder
├── README.md
└── output_model

CORPUS: Train: ADD.en and ADD.ta, Dev: dev.en and dev.ta, Test: test.en and test.ta
DIR: Corpus/

	cd corpus/

Clean, tokenize and lowercase the train corpora:

	python tokenize.py ADD.en > ADD.tok.en
	
	python tokenize.py ADD.ta > ADD.tok.ta
	
	python lowercase.py ADD.tok.en 
	
	mosesdecoder/scripts/training/clean-corpus-n.perl \
    Corpus/ADD.tok en ta \
    Corpus/ADD.clean.tok 1 20


Clean and tokenize the language model corpus: TA-LM

	python tokenize.py TA-LM > lm.tok.ta
	
	python shorten.py lm.tok.ta 20

Language Model: 

	Create n-gram language model (3 used here)
		mosesdecoder/bin/lmplz -o 3 <Corpus/ADD.tok.ta > Corpus/LM  

	Binarize the LM for faster access:
		mosesdecoder/bin/build_binary Corpus/LM Corpus/LM_BINARY

Train the model:
	
	./mosesdecoder/scripts/training/train-model.perl -root-dir output_model -external-bin-dir giza-pp/bin/ -corpus Corpus/OUT.clean.tok -f en -e ta -alignment grow-diag-final-and -reordering msd-bidirectional-fe --parallel -lm 0:3:$PWD/Corpus/LM_BINARY > log


Clean, tokenize and lowercase the dev corpora for tuning:

	python tokenize.py dev.en > dev.tok.en
	
	python tokenize.py dev.ta > dev.tok.ta
	
	python lowercase.py dev.tok.en

	mosesdecoder/scripts/training/clean-corpus-n.perl \
    Corpus/dev.tok en ta \
    Corpus/dev.clean.tok 1 20

Tune the model to improve test set BLEU score:

	$PWD/mosesdecoder/scripts/training/mert-moses.pl $PWD/Corpus/dev.clean.tok.en $PWD/Corpus/dev.clean.tok.ta $PWD/mosesdecoder/bin/moses $PWD/output_model/model/moses.ini --mertdir $PWD/mosesdecoder/bin/ > mert.out

Clean, tokenize and lowercase the test corpora for decoding:

	python tokenize.py test.en > test.tok.en
	
	python tokenize.py test.ta > test.tok.ta
	
	python lowercase.py test.tok.en

	mosesdecoder/scripts/training/clean-corpus-n.perl \
    Corpus/test.tok en ta \
    Corpus/test.clean.tok 1 20

To run the decoder with STDOUT input:

	mosesdecoder/bin/moses -f mert-work/moses.ini

	Copy paste sentences from the test set to check and verify results

To make the test process instantaneously available:
	
	mkdir output_model/binary
 	
 	cd output_model
 	
 	mkdir binarised-model

 	../mosesdecoder/bin/processPhraseTableMin \
   	-in output_model/model/phrase-table.gz -nscores 4 \
   	-out binarised-model/phrase-table
 	
 	../mosesdecoder/bin/processLexicalTableMin \
   	-in train/model/reordering-table.wbe-msd-bidirectional-fe.gz \
   	-out binarised-model/reordering-table

   	cp ../mert-work/moses.ini binarised-model

   	gedit binarised-model/moses.ini

   	Make the following changes:

    Change PhraseDictionaryMemory to PhraseDictionaryCompact
    
    Set the path of the PhraseDictionary feature to point to $ROOT_DIR/output_model/binary/binarised-model/phrase-table.minphr
    
    Set the path of the LexicalReordering feature to point to $ROOT_DIR/output_model/binary/binarised-model/reordering-table 

Run the decoder again to see the difference:

	cd ..

	mosesdecoder/bin/moses -f mert-work/moses.ini