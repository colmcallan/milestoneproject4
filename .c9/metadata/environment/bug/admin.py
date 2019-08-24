{"filter":false,"title":"admin.py","tooltip":"/bug/admin.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":16,"column":28},"action":"insert","lines":["from django.contrib import admin","from .models import Bug, BugComment, upVotes","","# Register your models here.","","class BugAdmin(admin.ModelAdmin):","    list_display = ['title', 'description', 'status', 'creator',","                    'created_date', 'bug_upvotes']","    list_filter = ('status',)","    ","class BugCommentAdmin(admin.ModelAdmin):","    list_display = ['bug', 'comment', 'creator', 'created_date']","    list_filter = ('bug', 'creator')","","admin.site.register(Bug, BugAdmin)","admin.site.register(BugComment, BugCommentAdmin)","admin.site.register(upVotes)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":28},"end":{"row":16,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566350882726,"hash":"05bbdfc2b00f022cbc0d7bf5cc83bef00357de95"}