# -*- coding: utf-8 -*-
import os
import codecs
import random
from tqdm import tqdm
from collections import defaultdict


def enc_dec_generator(ask, response, TESTSET_SIZE = 8000):
	train_enc = codecs.open('dataset/{}'.format('train_enc'), 'w', 'utf-8')
	train_dec = codecs.open('dataset/{}'.format('train_dec'), 'w', 'utf-8')
	test_enc = codecs.open('dataset/{}'.format('test_enc'), 'w', 'utf-8')
	test_dec = codecs.open('dataset/{}'.format('test_dec'), 'w', 'utf-8')

	test_index = random.sample([i for i in range(len(ask))], TESTSET_SIZE)

	for i in tqdm(range(len(ask)), total = len(ask), ncols = 70, leave = False, unit = 'b'):
		if i in test_index:
			test_enc.write(ask[i] + '\n')
			test_dec.write(response[i] + '\n')
		else:
			train_enc.write(ask[i] + '\n')
			train_dec.write(response[i] + '\n')

	train_enc.close()
	train_dec.close()
	test_enc.close()
	test_dec.close()


def vocabulary_generator(inputfile, outputfile):
	vocabulary = defaultdict(int)
	with codecs.open('dataset/{}'.format(inputfile), 'r', 'utf-8') as f:
		count = 0
		for line in f:
			count += 1
			tokens = [i for i in line.strip('\n')]
			for word in tokens:
				if word in vocabulary:
					vocabulary[word] += 1
				else:
					vocabulary[word] = 1
		vocabulary_list = START_VOCAB + sorted(vocabulary, key = vocabulary.get, reverse = True)
		if len(vocabulary_list) > 5000:
			vocabulary_list = vocabulary_list[: 5000]
		with codecs.open('vocab/{}'.format(outputfile), 'w', 'utf-8') as wf:
			for word in vocabulary_list:
				wf.write(word + '\n')


def convert_to_tokens(inputfile, vocabularyfile, outputfile):
	temp_vocab = [line.strip() for line in codecs.open('vocab/{}'.format(vocabularyfile), 'r', 'utf-8').read().splitlines()]
	word2idx = {word: idx for idx, word in enumerate(temp_vocab)}
	output_f = codecs.open('dataset/{}'.format(outputfile), 'w', 'utf-8')
	with codecs.open('dataset/{}'.format(inputfile), 'r', 'utf-8') as f:
		for line in f:
			line_vec = []
			for word in line.strip():
				line_vec.append(word2idx.get(word, 3)) # UNK_ID
			output_f.write(' '.join([str(tokens) for tokens in line_vec]) + '\n')
	output_f.close()


if __name__ == '__main__':

	# Step 1 : split train & test, enc & dec 
	data_path = 'dataset/dgk_shooter_min.conv'

	if not os.path.exists(data_path):
		print('MSG : Dataset Error!')
		exit()

	convs = []
	with codecs.open(data_path, 'r', 'utf-8') as f:
		datasets = []
		for line in f:
			line = line.strip('\n').replace('/', '')
			if line == '':
				continue
			if line[0] == 'E':
				if datasets:
					convs.append(datasets)
				datasets = []
			elif line[0] == 'M':
				datasets.append(line.split(' ')[1])

	# print(convs[:5])

	ask = []
	response = []
	for conv in convs:
		if len(conv) == 1:
			continue
		if len(conv) % 2 != 0:
			conv = conv[: -1]
		for i in range(len(conv)):
			if i % 2 == 0:
				ask.append(conv[i])
			else:
				response.append(conv[i])

	# print(ask[0], response[0])

	enc_dec_generator(ask, response)
	print('MSG : (Step1) build enc & dec files for train & test Done!')

	# Step 2 : train & test vocabulary
	PAD = "<PAD>"
	GO = "<GO>"
	EOS = "<EOS>"
	UNK = "<UNK>"
	START_VOCAB = [PAD, GO, EOS, UNK]
	VOCAB_SIZE = 5000

	train_enc_file = 'train_enc'
	train_dec_file = 'train_dec'
	test_enc_file = 'test_enc'
	test_dec_file = 'test_dec'

	print('MSG : Start generating vocabulary file......')
	vocabulary_generator(train_enc_file, 'train_enc_vocab')
	vocabulary_generator(train_dec_file, 'train_dec_vocab')

	print("MSG : (Step2) Build vocabulary file for train_enc & dec Done!")

	train_enc_vocab_file = 'train_enc_vocab'
	train_dec_vocab_file = 'train_dec_vocab'

	print("MSG : Start converting datasets to tokens......")

	convert_to_tokens(train_enc_file, train_enc_vocab_file, 'train_enc.vec')
	convert_to_tokens(train_dec_file, train_dec_vocab_file, 'train_dec.vec')
	convert_to_tokens(test_enc_file, train_enc_vocab_file, 'test_enc.vec')
	convert_to_tokens(test_dec_file, train_dec_vocab_file, 'test_dec.vec')
	print("MSG : (Step3) Build tokens for enc & dec Done!")













