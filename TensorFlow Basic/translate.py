from __future__ import print_function
import os
import sys
import argparse
from itertools import islice
import tensorflow as tf
import numpy as np
import time
import pickle
import h5py
import math
import random

parser = argparse.ArgumentParser(description='English - Tamil Neural MT System')
parser.add_argument("-en_size", "--en_size", help="Max Size (No. of words) of the English Vocabulary", default=50000)
parser.add_argument("-ta_size", "--ta_size", help="Max Size (No. of words) of the Tamil Vocabulary", default=50000)
parser.add_argument("-en_path", "--en_path", help="Location of English part of Bilingual Sentences", default='dataset/src-train.txt')
parser.add_argument("-ta_path", "--ta_path", help="Location of Tamil part of Bilingual Sentences", default='dataset/targ-train.txt')
parser.add_argument("-en_devpath", "--en_devpath", help="Location of English Dev Bilingual Sentences", default='dataset/src-val.txt')
parser.add_argument("-ta_devpath", "--ta_devpath", help="Location of Tamil Dev Bilingual Sentences", default='dataset/targ-val.txt')
parser.add_argument("-en_vocab_path", "--en_vocab_path", help="Location to save/retrieve English Vocabulary", default='vocab/en')
parser.add_argument("-ta_vocab_path", "--ta_vocab_path", help="Location to save/retrieve Tamil Vocabulary", default='vocab/ta')
parser.add_argument("-lr", "--lr", help="Learning Rate", default=0.5)
parser.add_argument("-decay","--decay",help="Learning Rate Decay Factor", default=0.75)
parser.add_argument("-softmax_sample","--softmax_sample",help="Sample Size for Sampled SoftMax to account for Large Target Vocabulary", default=256)
parser.add_argument("-hidden_layer_size","--hidden_layer_size",help="No. of neurons in hidden layer(s)", default=325)
parser.add_argument("-no_of_layers","--no_of_layers",help="No. of hidden layer(s) in the encoder and decoder", default=4)
parser.add_argument("-test","--test",help="If present - Testing phase", action='store_true')
parser.add_argument("-grad_norm","--grad_norm",help="Gradient Clipping Limit", default=5.0)
parser.add_argument("-batch_size","--batch_size",help="No of sentences per batch", default=16)
parser.add_argument("-ckpt_path","--ckpt_path",help="Path to checkpoint files directory for model restore", default='checkpoints/')
parser.add_argument("-steps_per_checkpoint","--steps_per_checkpoint",help="No. of steps per checkpoint", default=50)

args = parser.parse_args()
parser.print_help()

def extract_vocab():

	if not os.path.exists('vocab/save.en.pkl') or not os.path.exists('vocab/save.ta.pkl'):
		envocab={}
		tavocab={}
	
		with open(args.en_path,'r') as f:

			for line in f.readlines():
				for word in line.strip().split(' '):
					if(word.strip()):
						if(word.strip() not in envocab):
							envocab[str(word)]=1
						else:
							envocab[str(word)]+=1
			envocab=['PAD', 'GO', 'EOS', 'UNK'] + sorted(envocab, key=envocab.__getitem__, reverse=True)
			ev = envocab
			if(len(envocab)>(args.en_size+4)):
				envocab=envocab[:args.en_size+4]

		k=1
		if(not os.path.exists(args.en_vocab_path)):
			with open(args.en_vocab_path,'w+') as f:
				for k,t in enumerate(envocab):
					print(k,t,file=f)
					k+=1
	
		with open(args.ta_path,'r') as f:

			for line in f.readlines():
				for word in line.strip().split(' '):
					if(word.strip()):
						if(word.strip() not in tavocab):
							tavocab[word]=1
						else:
							tavocab[word]+=1
			tavocab=['PAD', 'GO', 'EOS', 'UNK'] + sorted(tavocab, key=tavocab.__getitem__, reverse=True)
			tv = tavocab
			if(len(tavocab)>(args.ta_size+4)):
				tavocab=tavocab[:args.ta_size+4]

		k=1
		if(not os.path.exists(args.ta_vocab_path)):
			with open(args.ta_vocab_path,'w+') as f:
				for k,t in enumerate(tavocab):
					print(k,t,file=f)
					k+=1	
	
		if(not os.path.exists('vocab/ta.train.ids') and not os.path.exists('vocab/en.train.ids')):
				
			with open('vocab/en.train.ids','w+') as f, open('vocab/ta.train.ids', 'w+') as g, open(args.en_path, 'r') as c, open(args.ta_path, 'r') as d:
				for line1, line2 in zip(c.readlines(),d.readlines()):
					if line1.strip() and line2.strip():
						print(' '.join([str(tv.index(x.strip())) if x.strip() and tv.index(x.strip())<min(len(tavocab), (args.ta_size+3)) else '3' for x in line2.strip().split(' ')]), file=g)
						print(' '.join([str(ev.index(x.strip())) if x.strip() and ev.index(x.strip())<min(len(envocab), (args.en_size+3)) else '3' for x in line1.strip().split(' ')]), file=f)
								
		if(not os.path.exists('vocab/ta.dev.ids') and not os.path.exists('vocab/en.dev.ids')):
		
			with open('vocab/en.dev.ids', 'w+') as f, open('vocab/ta.dev.ids', 'w+') as g, open(args.en_devpath, 'r') as c, open(args.ta_devpath, 'r') as d:
				for line1, line2 in zip(c.readlines(),d.readlines()):
					if line1.strip() and line2.strip():
						print(' '.join([str(tv.index(x.strip())) if x.strip() in tv and x.strip() and tv.index(x.strip())<min((args.ta_size+3), len(tavocab)) else '3' for x in line2.strip().split(' ')]), file=g)
						print(' '.join([str(ev.index(x.strip())) if x.strip() in ev and x.strip() and ev.index(x.strip())<min((args.en_size+3), len(envocab)) else '3' for x in line1.strip().split(' ')]), file=f)
	
	
		with open('vocab/save.en.pkl', 'wb') as f:
			pickle.dump(envocab, f, pickle.HIGHEST_PROTOCOL)
			
		with open('vocab/save.ta.pkl', 'wb') as f:
			pickle.dump(tavocab, f, pickle.HIGHEST_PROTOCOL)
	
		if(not os.path.exists('embedding/data.h5')):
			from embedding import word2vec
			with open('vocab/en') as f:
				content = [unicode(x.split(' ')[1].strip(),'utf-8') for x in f.readlines()]
				encvectors = word2vec.return_english(content, args.hidden_layer_size)

			with open('vocab/ta') as f:
				content = [unicode(x.split(' ')[1].strip(),'utf-8') for x in f.readlines()]
				word2vec.create_tamil(args.hidden_layer_size)
				decvectors = word2vec.return_tamil(content, args.hidden_layer_size)
		
			h5f = h5py.File('embedding/data.h5', 'w')
			h5f.create_dataset('en', data=encvectors)
			h5f.create_dataset('ta', data=decvectors)
			h5f.close()
	
	else:
		with open('vocab/save.en.pkl', 'rb') as f:
			envocab = pickle.load(f)
		with open('vocab/save.ta.pkl', 'rb') as f:
			tavocab = pickle.load(f)
					
	return envocab, tavocab
						
def model_desc(buckets, tavocab):
	
	global_timestep = tf.get_variable('timestep', initializer=0, trainable=False, dtype=tf.float32)
	lr = tf.get_variable("lr", initializer=float(args.lr), trainable=False, dtype=tf.float32)
	lr_decay = lr.assign(lr * args.decay)
	wb_pair = None
	softmax = None
	if(args.softmax_sample>0 and args.softmax_sample<min((args.ta_size+4), len(tavocab))):
	
		W = tf.get_variable("w_output", [args.hidden_layer_size, min((args.ta_size+4), len(tavocab))], dtype=tf.float32)
		W_S = tf.transpose(W)
		B = tf.get_variable("b_output", [min((args.ta_size+4), len(tavocab))], dtype=tf.float32)
		projection = (W, B)
		
		def SS(X, Y):
			Y_S = tf.reshape(Y, [-1, 1])
			B_S = tf.cast(B, tf.float32)
			X_S = tf.cast(X, tf.float32)
			return tf.cast(tf.nn.sampled_softmax_loss(W_S, B_S, X_S, Y_S, args.softmax_sample, min(args.ta_size+4, len(tavocab))), tf.float32)
		
		sampled_softmax = SS
		
	RNNCell = tf.nn.rnn_cell.BasicLSTMCell(args.hidden_layer_size)
	if(args.no_of_layers>1):
		RNNCell = tf.nn.rnn_cell.MultiRNNCell([RNNCell] * args.no_of_layers)
	
	def s2s(X, C):
		return tf.nn.seq2seq.embedding_attention_seq2seq(X, C, RNNCell, num_encoder_symbols=(args.en_size+4), num_decoder_symbols=min((args.ta_size+4), len(tavocab)), embedding_size=args.hidden_layer_size, output_projection=projection, feed_previous=True, dtype=tf.float32)
	
	X = []
	Y = []
	TW = []
	
	for x in xrange(buckets[-1][0]):
		X.append(tf.placeholder(tf.int32, shape=[None], name="X.{0}".format(x)))
	
	for y in xrange(buckets[-1][1] + 1): 
		Y.append(tf.placeholder(tf.int32, shape=[None], name="Y.{0}".format(y)))
		TW.append(tf.placeholder(tf.float32, shape=[None], name="W.{0}".format(y)))
	
	T = [Y[i + 1] for i in xrange(len(Y) - 1)]
	
	Ydash, L = tf.nn.seq2seq.model_with_buckets(X, Y, T, TW, buckets, lambda x, y: s2s(x, y), softmax_loss_function=sampled_softmax)
	
	if projection is not None:
		for i in xrange(len(buckets)):
			Ydash[i] = [tf.matmul(O, projection[0]) + projection[1] for O in Ydash[i]]
	if not args.test:
	
		gn = []
		u = []
		optimizer = tf.train.GradientDescentOptimizer(args.lr)
		
		for i in xrange(len(buckets)):
			grads = tf.gradients(L[i], tf.trainable_variables())
	 		clipped_grads, norm = tf.clip_by_global_norm(grads, args.grad_norm)
	 		gn.append(norm)
	 		u.append(optimizer.apply_gradients(zip(clipped_grads, tf.trainable_variables()), global_step=global_timestep))

	save = tf.train.Saver(tf.all_variables())
	if not args.test:
		return X, Y, TW, save, u, gn, L, lr, lr_decay, Ydash, global_timestep
	else:
		return X, Y, TW, save, None, None, L, lr, lr_decay, Ydash, global_timestep
	
def step(sess, X, Y, TW, bucket_no, test, buckets, u, gn, L, Ydash,Xt, Yt, TWt):
	
	es, ds = buckets[bucket_no]
	if not (es==len(X) and ds==len(Y) and ds==len(TW)):
		print("LENGTH MISMATCH")
	
	feed = {}
	for e in xrange(es):
		feed[Xt[e].name] = X[e]
	for d in xrange(ds):
		feed[Yt[d].name] = Y[d]
		feed[TWt[d].name] = TW[d]
	last = Yt[ds].name
	feed[last] = np.zeros([args.batch_size], dtype=np.int32)
		
	if not test:
		out = [u[bucket_no], gn[bucket_no], L[bucket_no]] 
	else:
 		out = [L[bucket_no]]
 		for l in xrange(ds): 
	 			out.append(Ydash[bucket_no][l])
	
	outputs = sess.run(out, feed)
	if not args.test:
		return outputs[1],outputs[2], None
	else:
		return None, outputs[0], outputs[1:]
	
def rand_batch(data, bucket_no, buckets):
	es, ds = buckets[bucket_no]
	X, Y = [], []
	for _ in xrange(args.batch_size):
 		X1, Y1 = random.choice(data[bucket_no])
	 	epad = [0] * (es - len(X1))
	 	X.append(list(reversed(X1 + epad)))
		dpad_size = ds - len(Y1) - 1
	 	Y.append([1] + Y1 + [0] * dpad_size)
	 	
 	X_B, Y_B, WT_B = [], [], []
 	for lid in xrange(es):
		X_B.append(np.array([X[bid][lid] for bid in xrange(args.batch_size)], dtype=np.int32))
	for lid in xrange(ds):
		Y_B.append(np.array([Y[bid][lid] for bid in xrange(args.batch_size)], dtype=np.int32))
		W_B = np.ones(args.batch_size, dtype=np.float32)
		for bid in xrange(args.batch_size):
			if lid < ds - 1:
				target = Y[bid][lid + 1]
			if lid == ds - 1 or target == 0:
				W_B[bid] = 0.0
		WT_B.append(W_B)
	return X_B, Y_B, WT_B

def train(buckets):
	envocab, tavocab = extract_vocab()
	data_set = [[] for _ in buckets]
	dev_set = [[] for _ in buckets]
	with tf.Session() as sess:
	
		Xt, Yt, TWt, saver, u, gn, L, lr, lr_decay, Ydash, global_timestep = model_desc(buckets, tavocab)
		ckpt = tf.train.get_checkpoint_state(args.ckpt_path)
		if ckpt and os.path.exists(ckpt.model_checkpoint_path):
			print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
			saver.restore(sess, ckpt.model_checkpoint_path)
		else:
			print("Created model with fresh parameters.")
			sess.run(tf.initialize_all_variables())
		
		with open('vocab/en.train.ids', 'r') as e, open('vocab/ta.train.ids', 'r') as t, open('vocab/en.dev.ids', 'r') as ed, open('vocab/ta.dev.ids', 'r') as td: 
			for line1, line2 in zip(e.readlines(), t.readlines()):
				s_ids, t_ids = [int(x) for x in line1.split(' ')], [int(x) for x in line2.split(' ')]
				t_ids.append(int('2'))
				for bucket_no, (e_size, t_size) in enumerate(buckets):
					if len(s_ids) < e_size and len(t_ids) < t_size:
						data_set[bucket_no].append([s_ids, t_ids])			
			for line1, line2 in zip(ed.readlines(), td.readlines()):
				s_ids, t_ids = [int(x) for x in line1.split(' ')], [int(x) for x in line2.split(' ')]
				t_ids.append(int('2'))
				for bucket_no, (e_size, t_size) in enumerate(buckets):
					if len(s_ids) < e_size and len(t_ids) < t_size:
						dev_set[bucket_no].append([s_ids, t_ids])
			
			train_bucket_sizes = [len(data_set[b]) for b in xrange(len(buckets))]
			train_total_size = float(sum(train_bucket_sizes))
			train_buckets_scale = [sum(train_bucket_sizes[:i + 1]) / train_total_size for i in xrange(len(train_bucket_sizes))]
			step_time, loss = 0.0, 0.0
			current_step = 0
			previous_losses = []
			
			while True:
				
				rand = np.random.random_sample()
				bucket_no = min([i for i in xrange(len(train_buckets_scale)) if train_buckets_scale[i] > rand])
				start_time = time.time()
				X, Y, TW = rand_batch(data_set, bucket_no, buckets)
				_, step_loss, _ = step(sess, X, Y, TW, bucket_no, args.test, buckets, u, gn, L, Ydash,Xt, Yt, TWt)
				step_time += (time.time() - start_time) / args.steps_per_checkpoint
				loss += step_loss / args.steps_per_checkpoint
				current_step += 1
				if current_step % args.steps_per_checkpoint == 0:
					perplexity = math.exp(loss) if loss < 300 else float('inf')
					checkpoint_path = os.path.join(args.ckpt_path, "translate.ckpt")
					saver.save(sess, args.ckpt_path, global_step=global_timestep)
					print ("global step %d learning rate %.4f step-time %.2f perplexity %.2f" % (global_timestep.eval(), lr.eval(), step_time, perplexity))
				if len(previous_losses) > 2 and loss > max(previous_losses[-3:]):
					sess.run(lr_decay)
				previous_losses.append(loss)
				step_time, loss = 0.0, 0.0
				for bucket_no in xrange(len(buckets)):
					if len(dev_set[bucket_no]) == 0:
						print("	eval: empty bucket %d" % (bucket_no))
						continue
					X, Y, TW = rand_batch(dev_set, bucket_no, buckets)
					_, eval_loss, _ = step(sess, X, Y, TW, bucket_no, args.test, buckets, u, gn, L, Ydash, Xt, Yt, TWt)
					eval_ppx = math.exp(eval_loss) if eval_loss < 300 else float('inf')
					print(" eval: bucket %d perplexity %.2f" % (bucket_no, eval_ppx))
				sys.stdout.flush()

def test(buckets):
	
	envocab, tavocab = extract_vocab()
	Xt, Yt, TWt, saver, u, gn, L, lr, lr_decay, Ydash, _ = model_desc(buckets, tavocab)
	
	with tf.Session() as sess:
		
		ckpt = tf.train.get_checkpoint_state(args.ckpt_path)
		if ckpt and os.path.exists(ckpt.model_checkpoint_path):
			print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
			saver.restore(sess, ckpt.model_checkpoint_path)
		else:
			print("Created model with fresh parameters.")
			sess.run(tf.initialize_all_variables()) 
		
		with open('dataset/src-test.txt', 'r') as f:
			for sentence in f.readlines(): 
				token_ids, bucket_no, encoder_inputs, decoder_inputs, target_weights, outputs, output = None, None, None, None, None, None, None 
				words = sentence.split(' ')
		  		token_ids = [envocab.index(w.strip()) for w in words]
		  		bucket_no = min([b for b in xrange(len(buckets)) if buckets[b][0] > len(token_ids)])
				encoder_inputs, decoder_inputs, target_weights = rand_batch({bucket_no: [(token_ids, [])]}, bucket_no, buckets)
				_,_,output = step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_no, args.test, buckets, u, gn, L, Ydash, Xt, Yt, TWt)
				outputs = [int(np.argmax(logit[0])) for logit in output]
				if 2 in outputs:
					outputs = outputs[:outputs.index(int('2'))]
				print("INPUT SENTENCE: ", sentence)
				print("OUTPUT SENTENCE: ", " ".join([tf.compat.as_str(tavocab[output]) for output in outputs]))
				print("\n\t\t\t................................................\n\n")

if __name__=='__main__':

	buckets = [(5, 5), (10, 12), (12, 12), (14, 13), (18,15), (20,17), (24,25), (30,30), (45,50), (85,80)]
	if not args.test:
		train(buckets)
	else:
		test(buckets)
