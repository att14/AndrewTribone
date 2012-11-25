import os
import unittest

from tribone.lib import presenter


class RepositoryTestCase(unittest.TestCase):

	def setUp(self):
		self.repo = presenter.Repository()

	def test_toplevel(self):
		self.assertTrue('AndrewTribone' in self.repo.toplevel)

	def test_gitignore(self):
		self.assertEqual(self.repo.gitignore.match('.gitignore'), None)
		self.assertNotEqual(self.repo.gitignore.match('/.git'), None)

	def test_tree(self):
		self.assertIn(os.path.abspath('tribone'), self.repo.tree)

		dirnames, filenames = self.repo.tree['%s/tribone' % self.repo.toplevel]
		self.assertTrue(
			all(
				[dirname in os.listdir(os.path.abspath('tribone'))
				 for dirname in dirnames]))
		self.assertTrue(
			all(
				[filename in os.listdir(os.path.abspath('tribone'))
				 for filename in filenames]))

	def test_list_objects(self):
		objects = self.repo.list_objects(self.repo.toplevel)
		for obj in objects:
			assert isinstance(obj, presenter.Object)


class ObjectTestCase(unittest.TestCase):

	def setUp(self):
		self.dirpath = os.path.abspath(os.path.dirname(__file__))
		self.filename = 'presenter_test.py'

	def test_object(self):
		presenter.Object(self.dirpath, self.filename)

	def test_commit(self):
		self.assertEqual(
			presenter.Commit(
				self.dirpath,
				self.filename).is_commit,
			True)

	def test_tree(self):
		self.assertEqual(
			presenter.Tree(
				self.dirpath,
				self.filename).is_tree,
			True)

	def test_blob(self):
		self.assertEqual(
			presenter.Blob(
				self.dirpath,
				self.filename).is_blob,
			True)

	def test_sha(self):
		self.assertEqual(
			len(presenter.Object(
				self.dirpath,
				self.filename).sha),
			40)

	def test_show(self):
		self.assertEqual(
			presenter.Blob(self.dirpath, self.filename).show(),
			open('%s/%s' % (self.dirpath, self.filename)).read().strip())
		self.assertEqual(
			len(presenter.Tree(
				os.path.abspath('%s/..' % self.dirpath),
				'test').show()),
			len(os.listdir(self.dirpath)))

	def test_nav_list_html(self):
		self.assertNotIn(
			'..',
			presenter.Tree(
				'/Users/atribone/code/AndrewTribone/tribone',
				'..').nav_list_html)
		self.assertIn(
			'__init__.py',
			presenter.Tree(
				'/Users/atribone/code/AndrewTribone/tribone',
				'test').nav_list_html)


if __name__ == '__main__':
	unittest.main()
