{"filter":false,"title":"forms_test.py","tooltip":"/bug/forms_test.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":32,"column":40},"action":"insert","lines":["from django.test import TestCase","from .forms import BugCommentForm, BugCreationForm","","class TestBugCommentForm(TestCase):","    ","    def test_users_can_comment(self):","        form = BugCommentForm({'comment': 'Test comment'})","        self.assertTrue(form.is_valid())","        ","    ","    def test_form_cant_be_blank(self):","        form = BugCommentForm({'comment': ''})","        self.assertFalse(form.is_valid())","        self.assertEqual(form.errors['comment'], ['This field is required.'])","","        ","","class TestBugCreationForm(TestCase):","    ","    def test_required_fields(self):","        form = BugCreationForm({'title':'', 'description': 'Bug description'})","        self.assertFalse(form.is_valid())","        self.assertEqual(form.errors['title'], ['This field is required.'])","        ","        form = BugCreationForm({'title': 'Test title', 'description': ''})","        self.assertFalse(form.is_valid())","        self.assertEqual(form.errors['description'], ['This field is required.'])","        ","        ","    def test_users_can_create_a_bug(self):","        form = BugCreationForm({'title': 'Bug Title',","                                'description': 'Bug description'})","        self.assertTrue(form.is_valid())"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":32,"column":40},"end":{"row":32,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566351408395,"hash":"02f8aebcb158eaf78e627b73a6c26a794a7c7154"}