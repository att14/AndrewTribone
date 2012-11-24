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
		for o in objects:
			assert isinstance(o, presenter.Object)


class ObjectTestCase(unittest.TestCase):

	def setUp(self):
		self.path = os.path.abspath(__file__)

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
			presenter.Blob(self.path).show(),
			open(self.path).read().strip())
		self.assertEqual(
			len(presenter.Tree(os.path.abspath('tribone')).show()),
			len(os.listdir('tribone')))


if __name__ == '__main__':
	unittest.main()
