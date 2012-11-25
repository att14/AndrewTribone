import os
import re
import subprocess


class Repository(object):
	"""Information associated with the repository.

	>>> r = Repository()

	>>> r.toplevel
	'/Users/atribone/code/AndrewTribone'

	>>> r.tree
	{'/Users/atribone/code/AndrewTribone': (['static', 'templates'],
	  ['andrewtribone.py',
	   'presenter.py',
	   'Procfile',
	   'requirements.txt']),
	 '/Users/atribone/code/AndrewTribone/static': (['css', 'img', 'js'], []),
	 '/Users/atribone/code/AndrewTribone/static/css': ([],
	  ['atribone.css',
	   'bootstrap-responsive.css',
	   'bootstrap-responsive.min.css',
	   'bootstrap.css',
	   'bootstrap.min.css',
	   'prettify.css']),
	 '/Users/atribone/code/AndrewTribone/static/img': ([],
	  ['glyphicons-halflings-white.png', 'glyphicons-halflings.png']),
	 '/Users/atribone/code/AndrewTribone/static/js': ([],
	  ['bootstrap.js', 'bootstrap.min.js', 'prettify.js']),
	 '/Users/atribone/code/AndrewTribone/templates': ([],
	  ['index.html', 'layout.html']),

	>>> r.list_objects(r.toplevel)
	[<presenter.Tree at 0x107ec4910>,
	 <presenter.Tree at 0x10802c690>,
	 <presenter.Tree at 0x10802c650>,
	 <presenter.Blob at 0x10802c910>,
	 <presenter.Blob at 0x10802c6d0>,
	 <presenter.Blob at 0x10802c610>,
	 <presenter.Blob at 0x10802cd50>,
	 <presenter.Blob at 0x10802c890>]
	"""

	@property
	def tree(self):
		"""Representation of the repository's file structure."""
		tree = {}

		for dirpath, dirnames, filenames in os.walk(self.toplevel):
			if not self.gitignore.search(dirpath):
				tree[dirpath] = (
					[dirname for dirname in dirnames
					 if not self.gitignore.search(dirname)],
					[filename for filename in filenames
					 if not self.gitignore.search(filename)])

		return tree

	@property
	def gitignore(self):
		"""Regular expression that emulates the behavior of .gitignore."""
		pattern = re.sub(
			'\*',
			'.*',
			'%s|/.git|^.git$' % '|'.join(
				[regex.strip('\n') for regex
				 in open('%s/.gitignore' % self.toplevel).readlines()
				 if regex.strip('\n') is not '']))
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

	def list_objects(self, dirpath):
		dirnames, filenames = self.tree[dirpath]
		objects = [Blob(dirpath, filename)
			   for filename in filenames] + \
			  [Tree(dirpath, dirname)
			   for dirname in dirnames]
		return objects


class Object(object):

	def __init__(self, dirpath, filename):
		self.dirpath = dirpath
		self.filename = filename

	@property
	def path(self):
		return os.path.abspath('%s/%s' % (self.dirpath, self.filename))

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
		return sha.strip()


class Commit(Object):

	@property
	def is_commit(self):
		return True


class Tree(Object):

	@property
	def is_tree(self):
		return True

	@property
	def nav_list_html(self):
		# TODO: Need to find a way so this fucntion does not know about Repository
		repo = Repository()

		nav_list = '<li class="nav-header">att14/AndrewTribone</li>'
		if self.path != repo.toplevel:
			link_id = 'tree'
			icon_class = 'icon-folder-close'
			nav_list += '<li><a href=# id="%s" data-dirpath="%s"><i class="%s"></i>%s</a>' \
				% (link_id, self.path, icon_class, '..')

		for obj in self.show():
			if not repo.gitignore.search(obj.path):
				link_id = 'tree' if obj.is_tree else 'blob'
				icon_class = 'icon-folder-close' if obj.is_tree else 'icon-file'
				nav_list += '<li><a href=# id="%s" data-dirpath="%s"><i class="%s"></i>%s</a>' \
					% (link_id, obj.dirpath, icon_class, obj.filename)

		return nav_list

	def show(self):
		return [Tree(self.path, filename)
			if os.path.isdir('%s/%s' % (self.path, filename))
			else Blob(self.path, filename)
			for filename in os.listdir(self.path)]

class Blob(Object):

	@property
	def is_blob(self):
		return True

	def show(self):
		show, _ = subprocess.Popen(
			['git', 'show', self.sha],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		).communicate()
		return show.strip() or open(self.path).read().strip()
