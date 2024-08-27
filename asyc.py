import os
import argparse
import multiprocessing as mp
import re

def compile_asy(file):
	os.system(f'asy {file}')

if __name__ == '__main__':
	# set up arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', nargs = '?', help = 'Filename to compile asy for')
	parser.add_argument('--processes', help = 'Number of processes to use', default = mp.cpu_count() // 2)
	args = parser.parse_args()

	# process arguments
	filename = args.filename
	if filename is not None:
		if os.path.isfile(filename):
			filename = os.path.splitext(filename)[0]
		if filename.startswith('.\\'):
			filename = filename[2:]
	num_processes = max(int(args.processes), 1)

	# find asy files to compile
	# if no filename given, compile *.asy
	asy_files = []
	if filename is None:
		for file in os.listdir('.'):
			if file.endswith('.asy'):
				asy_files.append(file)
	else:
		for file in os.listdir('.'):
			search = re.search(f'{filename}-[0-9]+.asy', file)
			if search is not None:
				i, j = search.span()
				if (i == 0) and (j == len(file)):
					asy_files.append(file)

	# run asy compilation in parallel
	with mp.Pool(num_processes) as p:
		p.map(compile_asy, asy_files)
