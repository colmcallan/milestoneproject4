{"filter":false,"title":"models_test.py","tooltip":"/bug/models_test.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":45},"action":"insert","lines":["from django.test import TestCase","from .models import Bug, BugComment","","","class BugEntryTest(TestCase):","    ","    def test_string_representation(self):","        bug = Bug(title=\"TestBug\")","        self.assertEqual(str(bug), bug.title)"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":45},"end":{"row":8,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566351502104,"hash":"c067cc999cd61e6f6071b4d03840b8299a15d62c"}