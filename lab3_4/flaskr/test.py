from flaskr import app, db
import flaskr
import unittest

from flask_testing import TestCase


class FlaskrTestCase(unittest.TestCase):
	
		# '/login' test

	# url /login повертає код 200
	def test_login_code(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	# '/login' містить слово 'Login'
	def test_login_page1(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertTrue(b'Login' in response.data)

	# '/login' містить титульний напис 'Notes.Noodles'
	def test_login_page2(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertTrue(b'Notes.Noodles' in response.data)

	# '/login' містить 'username' та 'password'	
	def test_login_page3(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertTrue(b'username'and b'password' in response.data)

	# коли залогінився правильно редіректнуло на добру сторінку
	def test_login_correct(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'admin', password = 'default'), follow_redirects = True)
		self.assertTrue(b'u were logged in' in response.data)

	# коли неправильний username не редіректнуло на добру сторінку
	def test_login_incorrect_username(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'incorrect', password = 'default'), follow_redirects = True)
		self.assertTrue(b'Bad username' in response.data)

	# коли неправильний password не редіректнуло на добру сторінку
	def test_login_incorrect_password(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'admin', password = 'incorrect'), follow_redirects = True)
		self.assertTrue(b'Bad password' in response.data)

	# '/' містить logout here коли залогінений
	def test_logout_in_logined(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'admin', password = 'default'), follow_redirects = True)
		self.assertTrue(b'loGout here' in response.data)

	# '/' містить форму для створення замітки коли залогінений
	def test_form_in_logined(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'admin', password = 'default'), follow_redirects = True)
		self.assertTrue(b'Name:'and b'Title:'and b'Text:'and b'Share' in response.data)


		# '/logout' test

	# logout працює добре
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.post('/login', data = dict(username = 'admin', password = 'default'), follow_redirects = True)
		response = tester.get('/logout', follow_redirects = True)
		self.assertTrue(b'logout succeded' in response.data)


		# '/' test

	# '/' містить login here
	def test_index_login(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertTrue(b'loGin here' in response.data)

	# '/' містить титульний напис
	def test_index_title(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertTrue(b'Notes.Noodles' in response.data)






if __name__ == '__main__':
	unittest.main()