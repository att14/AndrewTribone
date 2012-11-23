import os
import unittest

from att import presenter


class RepositoryTestCase(unittest.TestCase):

	def setUp(self):
		self.repo = presenter.Repository()

	def test_toplevel(self):
		self.assertEqual(
			self.repo.toplevel,
			os.path.abspath('..'))

	def test_gitignore(self):
		self.assertEqual(self.repo.gitignore.match('src/'), None)
		self.assertNotEqual(self.repo.gitignore.match('/.git'), None)

	def test_tree(self):
		self.assertIn(os.path.abspath('.'), self.repo.tree)

		dirnames, filenames = self.repo.tree[self.repo.toplevel]
		self.assertTrue(
			all(
				[dirname in os.listdir(os.path.abspath('..'))
				 for dirname in dirnames]))
		self.assertTrue(
			all(
				[filename in os.listdir(os.path.abspath('..'))
				 for filename in filenames]))

	def test_list_objects(self):
		objects = self.repo.list_objects(self.repo.toplevel)
		for o in objects:
			assert isinstance(o, presenter.Object)


class ObjectTestCase(unittest.TestCase):

	def setUp(self):
		self.path = os.path.abspath('../.gitignore')

	def test_object(self):
		presenter.Object(self.path)

	def test_commit(self):
		self.assertEqual(presenter.Commit(self.path).is_commit, True)

	def test_tree(self):
		self.assertEqual(presenter.Tree(self.path).is_tree, True)

	def test_blob(self):
		self.assertEqual(presenter.Blob(self.path).is_blob, True)

	def test_sha(self):
		self.assertEqual(len(presenter.Object(self.path).sha), 40)

	def test_show(self):
		self.assertEqual(
			presenter.Object(self.path).show(),
			open(self.path).read())


if __name__ == '__main__':
	unittest.main()
