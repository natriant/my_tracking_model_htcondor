import os

clean_flag = False # After each run, set this flag Flase to avoid deleting files by accident

if clean_flag:
	key_word = 'test'

	for filename in os.listdir():
		if key_word in filename and '.py' not in filename:
			os.remove(filename)
