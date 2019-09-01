{"filter":false,"title":"models.py","tooltip":"/ticket/models.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":37,"column":4},"end":{"row":37,"column":8},"action":"remove","lines":["    "],"id":7},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":38,"column":0},"end":{"row":48,"column":40},"action":"insert","lines":["class upVotes(models.Model):","    \"\"\"Bug upvotes\"\"\"","    upvote_user = models.ForeignKey(User, on_delete=models.CASCADE)","    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)","    created_date = models.DateTimeField(auto_now_add=True)","    ","    class Meta:","        verbose_name_plural = \"Up votes\"","    ","    def __str__(self):","        return self.upvote_user.username"],"id":9}],[{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"remove","lines":["g"],"id":10},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"remove","lines":["u"]},{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"remove","lines":["B"]}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["T"],"id":11},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["i"]},{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":["c"]},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":["k"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["e"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":7},"end":{"row":39,"column":10},"action":"remove","lines":["Bug"],"id":12},{"start":{"row":39,"column":7},"end":{"row":39,"column":13},"action":"insert","lines":["ticket"]},{"start":{"row":41,"column":4},"end":{"row":41,"column":7},"action":"remove","lines":["bug"]},{"start":{"row":41,"column":4},"end":{"row":41,"column":10},"action":"insert","lines":["ticket"]}],[{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["T"],"id":13},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["i"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["c"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["k"]},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["e"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":0},"end":{"row":48,"column":40},"action":"remove","lines":["class TicketupVotes(models.Model):","    \"\"\"ticket upvotes\"\"\"","    upvote_user = models.ForeignKey(User, on_delete=models.CASCADE)","    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)","    created_date = models.DateTimeField(auto_now_add=True)","    ","    class Meta:","        verbose_name_plural = \"Up votes\"","    ","    def __str__(self):","        return self.upvote_user.username"],"id":14}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":38,"column":0},"end":{"row":38,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":31,"state":"start","mode":"ace/mode/python"}},"timestamp":1567296926984,"hash":"b92f8e482aab99eaf51f814fa1f449b09a1dc69e"}