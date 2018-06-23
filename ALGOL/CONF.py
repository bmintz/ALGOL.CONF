#!/usr/bin/env python3
# encoding: utf-8

def load(fp):
	result = {}
	for line in fp:
		line = line.strip()
		if line.startswith('#') or not line:
			continue

		xs = line.split('=')
		if len(xs) == 1:
			continue

		key = xs[0]
		value = '='.join(xs[1:])
		result[key] = value

	return result

def decode(str):
	return load(str.splitlines())
