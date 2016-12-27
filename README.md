# English-Tamil-MT
English Tamil MT is part of a project carried out for ADD (Acoustic Dialect Decoder). It implements Moses based SMT and Neural MT in TensorFlow.

How to set-up:

LINUX DEBIAN:

Install pip (Python package manager):

    sudo apt-get install python-pip

Install TensorFlow r0.8 (backward compatibility problematic for some TensorFlow releases):

  For GPU training (GPU and CUDA required):
  For more help, refer NVIDIA website to install cuda.

    sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl

  For CPU training:

    sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl

Install the gensim module:

    sudo -H pip install --upgrade gensim
    
Now cd to the respective models' root dir, whichever one you want to train. 

This repo contains the following root dirs for various models as specified:

1. Tensorflow Basic - RNN GRU Embedding Attention Encoder Decoder Model 
2. Tensorflow with English Word2Vec - RNN LSTM Embedding Attention Encoder Decoder model with word2vec embedding for the English sentences.
3. Tensorflow with Eng and Tam Word2Vec - RNN LSTM Embedding Attention Encoder Decoder model with Word2Vec encoding for both English and Tamil Corpora. (Best Performance)
4. Moses - Instructions and Results of using Moses Phrase-Based SMT model.


I have re-implemented the same model implemented in the Tensorflow Tutorial for Seq2Seq API from [here](https://www.tensorflow.org/versions/master/tutorials/seq2seq/) for Model 3.

I think that the stateful class-style programming is best suited to handle all the different variables involved through the training. Also, the functional style (like the one I've used) is cumbersome with a lot of arguments for every function. But I have written the code to speed up the preprocessing a little and familiarize myself with the API. 

Instructions to use the models can be found in the dirs. 

'Invoke command' is used to invoke the programs from terminal.

To test the translation models from the most recent checkpoint, use the --decode flag with the 'Invoke Command'

Thanks to TensorFlow's API and Tutorials: https://www.tensorflow.org/versions/r0.8/tutorials/index.html

BEST RESULTS: [3 Layers, Model Number 3.]

Trisha is the heroine.  
_UNK த்ரிஷா நடிக்கிறார் .

ONGC, has made an investment of $_NUMBER billion, which is expected to go up to $_NUMBER billion later this year.
பில்லியன் டாலர்கள் கடன் _UNK பில்லியன் _UNK பில்லியன் _UNK . பில்லியன் டாலராக ஆயிற்று .

Meeting the press people, the group criticized the opposition severely.
இந்தக் செய்தி ஊடக _UNK மக்கள் _UNK , _UNK எதிர்ப்பை தெரிவித்தது .

This is not my duty, I am not carrying any official role or leading position.
எனது தனிப்பட்ட , தனிப்பட்ட , தனிப்பட்ட , எந்த _UNK நான் எந்த முக்கியமான பங்கைக் கொள்ளவில்லை .

Confronting a worsening foreign exchange crisis, the Sri Lankan government is seeking a $US_NUMBER billion loan from the International Monetary Fund IMF to bail out the country.
ஒரு நிதிய நெருக்கடியில் இருந்து , இலங்கை அரசாங்கம் நாட்டை எதிர்கொண்டுள்ள கடன் கொடுக்கும் நிலைமையை ஒட்டி _UNK _UNK . பில்லியன் டாலர்கள் கடன் கொடுப்பதில் சர்வதேச நாணய நிதியம் கொடுத்துள்ளது .

And whoever touches any thing that was under him shall be unclean until the even: and he that bears any of those things shall wash his clothes, and bathe himself in water, and be unclean until the even.
ஒருவன் ஒன்றையும் _UNK தன் வஸ்திரங்களைத் தோய்த்து , தன் வஸ்திரங்களைத் தோய்த்து , தன் வஸ்திரங்களைத் தோய்த்து , தண்ணீரில் முழுகி , பின்பு சுத்தமாயிருப்பான் . பின்பு , அவன் சுத்தமாயிருப்பான் .

DM: We are currently looking at offers from some other states and so we hope that there will be no more trouble, but I am determined to make this film.
இன்னும் பல இடங்களில் இந்த முன்னேற்றம் இப்பொழுது நாம் இங்கே நடக்கும் ; எனவே இந்த பிரச்சினைகளை நாம் இங்கு _UNK என்று நம்பிக்கை உண்டு .

And David said to Abigail, Blessed be the LORD God of Israel, which sent you this day to meet me:
அப்படியே தாவீது தன் ஊழியக்காரரை நோக்கி : நீங்கள் இன்று ஐந்தாம் மாதம் _UNK ; அவன் தேவனாகிய கர்த்தருக்கு ஆலயத்தைக் _UNK ;

French capitalism needs another prop
பிரெஞ்சு முதலாளித்துவம் _UNK

He is a father now.
இவர் தந்தை .

you know what you want.
என்ன _UNK என்று நீங்கள் நினைக்கிறீர்கள் .

They are tamil fans.
ரசிகர்கள் .

People are against many political parties.
இடது கட்சிகளின் மீது _UNK இருக்கின்றனர் .

Indian men and US armed forces are fighting in Iraq.
இந்திய மற்றும் அமெரிக்க _UNK இந்த சண்டையில் ஈடுபட்டுள்ளன .

American administration is more strong than any other country.
வேறு எங்கும் விட அதிகமாக அமெரிக்க அரசு வேறு புஷ் நிர்வாகம் உள்ளது .

director acts in film about police officials.
போலீஸ் _UNK நேரடியாக போலீஸ் அதிகாரியாக நடிக்கிறார் .

Indian Democratic party won the elections.
இந்திய தேர்தல்களில் இந்த கட்சி தேர்தல்களில் வெற்றி கொண்டுள்ளது .

This international agreement supports world peace.
சர்வதேச சமாதானம் மற்றும் _UNK வேண்டும் என்று அமெரிக்கா கோருகிறது .

this international agreement support world peace.
இந்த சக்திகள் உலக சமாதானம் என்று _UNK .

political parties run.            
அரசியல் கட்சிகள் இருக்கின்றன .

political parties run it.
அரசியல் கட்சிகள் இயங்குகின்றன .

Egypt is a country.
எகிப்து ஒரு நாடு .

Iran is a country.
ஈரான் ஒரு நாடு .

India has more military troops
இந்தியா இராணுவ ரீதியாக _UNK

India has a powerful military base.
இந்திய இராணுவ சக்தி வாய்ந்த சக்திவாய்ந்த சக்தியாக விளங்குகிறது .

God is our creator.
தேவன் எங்கள் _UNK .

Pakistan is against India.
பாகிஸ்தான் சீனாவும் இந்தியாவிற்கு எதிராக உள்ளது .

Lord Jesus had an after life.
_UNK மரணத்திற்கு _UNK .

Congress is an international political Party.
_UNK ஒரு அனைத்துலக அரசியல் கட்சி ஆகும் .

Pakistan has a million weapons to fight a war against India.
_UNK எதிராக ஒரு மில்லியன் _UNK பாக்கிஸ்தான் இந்தியாவிற்கு _UNK .

what method is it?
இந்த முறை என்ன ?

you want a win.
நீங்கள் ஒரு திறமையான அரசாங்கத்தை செய்து நிற்க வேண்டும் .

He is not American.
அவர் ஒன்றும் _UNK அல்ல .

American army won the war.
அமெரிக்க இராணுவ வீரர்கள் வெற்றி பெற்றது .

American policy is freedom.
அமெரிக்காவின் கொள்கை அடிப்படையில் .

Government said there would be war.
பிராந்திய நாடுகள் போர் எதிர்ப்பு ஆர்ப்பாட்டங்கள் _UNK என்று கூறினார் .

Economic growth problem is of prime importance in India.
இந்தியாவில் வளர்ச்சி தொடர்பான பிரச்சினை முக்கியம் .

The film is directed by mani ratnam.
படத்தை _UNK இயக்குகிறார் .

Every year he gave a party at his house. 
அவர் ஒரு குடும்பத்தில் இருந்து ஒரு _UNK தொடங்கினார் .

India has peace now.
இந்தியா இப்பொழுது சமாதான நாடாக உள்ளது .

He is opposition to the campaign.
அவர் எதிர்க் கட்சி .

People in the US support their president.
அமெரிக்க மக்கள் நிபந்தனையற்ற ஆதரவு கொடுத்து வந்து விட்டது .

We are the ruling party.
நாங்கள் ஆளும் கட்சியில் தலைமை தாங்கி கொண்டிருக்கிறோம் .

Police fired at the workers.
தொழிலாளர்கள் மீது _UNK .

The police were attacked.
போலீஸ் தாக்குதலுக்கு முன் வைத்திருந்தனர் .

Police officers put him in jail.    
பொலிஸ் அவரை கைது செய்தார் .

Bush was against American Oil policies.
புஷ் அமெரிக்க கொள்கைகளுக்கு எதிரான ஒரு கொள்கையை மேற்கொண்டனர் .

Bush fought against American policies.
புஷ் அமெரிக்க கொள்கைகளுக்கு எதிராக _UNK .

Indian troops lose their support.
இந்திய துருப்புக்கள் தங்கள் ஆதரவையும் இழந்து விட்டனர் .

We are going to war.
நாங்கள் யுத்தத்திற்கு சென்றோம் .

The media is against the government.
செய்தி ஊடகம் அரசாங்கத்தின் எதிராக எதிர்ப்புத் கொண்டது .

News is broadcast from television and Social media.
பத்திரிகை , _UNK மற்றும் _UNK பேட்டி என செய்தி ஊடகம் .

People voted against the ruling party.
ஆளும் _UNK எதிராக மக்கள் வாக்களித்துள்ளனர் .

If we maintain peace, there will be no war.
நாங்கள் மீண்டும் சமாதானம் _UNK , போர் _UNK கூடாது .

Her children are soldiers.
பிள்ளைகள் _UNK இராணுவத்தில் .

The working class hate the government policies.
தொழிலாள வர்க்கம் அரசாங்கத்தின் கொள்கைகளை _UNK .

Government should make things right.
அரசாங்க சலுகைகள் தருமாறு மத்திய அரசாங்கத்தை நாங்கள் _UNK .

Government is responsible for the people.
மக்கள் பொறுப்பு என்ற பொறுப்பை கொண்டுள்ளது .

There would be peace when the war is over.
போருக்கு _UNK எதிர்காலம் உண்டு .
