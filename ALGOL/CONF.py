#!/usr/bin/env python3
# encoding: utf-8

import itertools

def load(fp):
	result = {}
	lines = list(fp)
	i = 0
	while i < len(lines):
		line = lines[i].strip()
		i += 1
		if line.startswith('#') or not line:
			continue

		line = line.split(' ')
		if line[0] == 'NEST':
			key = ' '.join(line[1:])
			nested = list(itertools.takewhile(lambda line: not line.strip().startswith('TSEN'), lines[i:]))
			i += len(nested)
			result[key] = load(nested)
		elif line[0] == 'STRING':
			key = ' '.join(line[1:])
			string = list(itertools.takewhile(lambda line: line.rstrip() != 'GRINTS', lines[i:]))
			i += len(string)
			result[key] = '\n'.join(string)
		else:
			line = ' '.join(line).split('=')
			if len(line) == 1:
				continue

			key = line[0]
			value = '='.join(line[1:])
			result[key] = value

	return result

def decode(str):
	return load(str.splitlines())
