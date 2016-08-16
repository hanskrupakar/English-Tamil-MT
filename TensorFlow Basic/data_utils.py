# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Utilities for downloading data from WMT, tokenizing, vocabularies."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import re
import tarfile

from six.moves import urllib

from tensorflow.python.platform import gfile

# Special vocabulary symbols - we always put them at the start.
_PAD = b"_PAD"
_GO = b"_GO"
_EOS = b"_EOS"
_UNK = b"_UNK"
_START_VOCAB = [_PAD, _GO, _EOS, _UNK]

PAD_ID = 0
GO_ID = 1
EOS_ID = 2
UNK_ID = 3

# Regular expressions used to tokenize.
_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")
_DIGIT_RE = re.compile(br"\d")

def basic_tokenizer(sentence):
  """Very basic tokenizer: split the sentence into a list of tokens."""
  words = []
  for space_separated_fragment in sentence.strip().split():
    words.extend(re.split(_WORD_SPLIT, space_separated_fragment))
  return [w for w in words if w]


def create_vocabulary(vocabulary_path, data_path, max_vocabulary_size,
                      tokenizer=None, normalize_digits=True):

  if not gfile.Exists(vocabulary_path):
    print("Creating vocabulary %s from data %s" % (vocabulary_path, data_path))
    vocab = {}
    with gfile.GFile(data_path, mode="rb") as f:
      counter = 0
      for line in f:
        counter += 1
        if counter % 100000 == 0:
          print("  processing line %d" % counter)
        tokens = tokenizer(line) if tokenizer else basic_tokenizer(line)
        for w in tokens:
          word = re.sub(_DIGIT_RE, b"0", w) if normalize_digits else w
          if word in vocab:
            vocab[word] += 1
          else:
            vocab[word] = 1
      vocab_list = _START_VOCAB + sorted(vocab, key=vocab.get, reverse=True)
      if len(vocab_list) > max_vocabulary_size:
        vocab_list = vocab_list[:max_vocabulary_size]
      with gfile.GFile(vocabulary_path, mode="wb") as vocab_file:
        for w in vocab_list:
          vocab_file.write(w + b"\n")


def initialize_vocabulary(vocabulary_path):

  if gfile.Exists(vocabulary_path):
    rev_vocab = []
    with gfile.GFile(vocabulary_path, mode="rb") as f:
      rev_vocab.extend(f.readlines())
    rev_vocab = [line.strip() for line in rev_vocab]
    vocab = dict([(x, y) for (y, x) in enumerate(rev_vocab)])
    return vocab, rev_vocab
  else:
    raise ValueError("Vocabulary file %s not found.", vocabulary_path)


def sentence_to_token_ids(sentence, vocabulary,
                          tokenizer=None, normalize_digits=True):
 
  if tokenizer:
    words = tokenizer(sentence)
  else:
    words = basic_tokenizer(sentence)
  if not normalize_digits:
    return [vocabulary.get(w, UNK_ID) for w in words]
  # Normalize digits by 0 before looking words up in the vocabulary.
  return [vocabulary.get(re.sub(_DIGIT_RE, b"0", w), UNK_ID) for w in words]


def data_to_token_ids(data_path, target_path, vocabulary_path,
                      tokenizer=None, normalize_digits=True):

  if not gfile.Exists(target_path):
    print("Tokenizing data in %s" % data_path)
    vocab, _ = initialize_vocabulary(vocabulary_path)
    with gfile.GFile(data_path, mode="rb") as data_file:
      with gfile.GFile(target_path, mode="w") as tokens_file:
        counter = 0
        for line in data_file:
          counter += 1
          if counter % 100000 == 0:
            print("  tokenizing line %d" % counter)
          token_ids = sentence_to_token_ids(line, vocab, tokenizer,
                                            normalize_digits)
          tokens_file.write(" ".join([str(tok) for tok in token_ids]) + "\n")

def prepare_wmt_data(data_dir, en_vocabulary_size, ta_vocabulary_size, tokenizer=None):
  
  en_vocab_path = os.path.join(data_dir,"vocabsize_%d.EN" % en_vocabulary_size)
  ta_vocab_path = os.path.join(data_dir,"vocabsize_%d.TA" % ta_vocabulary_size)
  en_data_path = os.path.join(data_dir,"ENGLISH_TRAIN")
  ta_data_path = os.path.join(data_dir,"TAMIL_TRAIN")
  en_test_path = os.path.join(data_dir,"ENGLISH_TEST")
  ta_test_path = os.path.join(data_dir,"TAMIL_TEST")
  create_vocabulary(ta_vocab_path, ta_data_path, ta_vocabulary_size, tokenizer)
  create_vocabulary(en_vocab_path, en_data_path, en_vocabulary_size, tokenizer)

  ta_train_ids_path = os.path.join(data_dir,"TRAIN_IDs%d.TA" % ta_vocabulary_size)
  en_train_ids_path = os.path.join(data_dir,"TRAIN_IDs%d.EN" % en_vocabulary_size)
  data_to_token_ids(ta_data_path, ta_train_ids_path, ta_vocab_path, tokenizer)
  data_to_token_ids(en_data_path, en_train_ids_path, en_vocab_path, tokenizer)

  ta_dev_ids_path = os.path.join(data_dir,"DEV_IDs%d.TA" % ta_vocabulary_size)
  en_dev_ids_path = os.path.join(data_dir,"DEV_IDs%d.EN" % en_vocabulary_size)
  data_to_token_ids(ta_test_path, ta_dev_ids_path, ta_vocab_path, tokenizer)
  data_to_token_ids(en_test_path, en_dev_ids_path, en_vocab_path, tokenizer)

  return (en_train_ids_path, ta_train_ids_path,
          en_dev_ids_path, ta_dev_ids_path,
          en_vocab_path, ta_vocab_path)