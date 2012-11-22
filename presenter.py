import os
import re
import subprocess


class Repository(object):

	@property
	def tree(self):
		for dirpath, dirnames, filenames in os.walk(self.toplevel):
			tree = {}

			if not self.gitignore.search(dirpath):
				tree[dirpath] = (
					[dirname for dirname in dirnames
						if not self.gitignore.search(dirname)],
					[filename for filename in filenames
						if not self.gitignore.search(filename)]
				)

			return tree

	@property
	def gitignore(self):
		"""Regular expression that emulates the behavior of .gitignore."""
		pattern = re.sub(
			'\*',
			'.*',
			'%s|/.git|^.git' % '|'.join(
				[regex.strip('\n') for regex
				 in open('%s/.gitignore' % self.toplevel).readlines()
				 if regex.strip('\n') is not '']
			)
		)
		return re.compile(pattern)

	@property
	def toplevel(self):
		"""The absolute path of the top-level directory."""
		toplevel, _ = subprocess.Popen(
			['git', 'rev-parse', '--show-toplevel'],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		).communicate()
		return toplevel.strip('\n')

	def list_objects(self, dirname):
		dirnames, filenames = self.tree[dirname]
		objects = [Tree(dirname) for dirname in dirnames] + \
			  [Blob(filename) for filename in filenames]
		return objects


class Object(object):
	def __init__(self, path):
		self.path = path

	@property
	def is_commit(self):
		return False

	@property
	def is_tree(self):
		return False

	@property
	def is_blob(self):
		return False

	@property
	def sha(self):
		sha, _ = subprocess.Popen(
			['git', 'hash-object', self.path],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		).communicate()
		return sha.strip('\n')

	def show(self):
		show, _ = subprocess.Popen(
			['git', 'show', self.sha],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		).communicate()
		return show.strip('\n') or open(self.path).read()


class Commit(Object):

	@property
	def is_commit(self):
		return True


class Tree(Object):

	@property
	def is_tree(self):
		return True


class Blob(Object):

	@property
	def is_blob(self):
		return True
