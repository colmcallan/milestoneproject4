{"filter":false,"title":"forms.py","tooltip":"/ticket/forms.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":11,"column":41},"action":"insert","lines":["from django import forms","from .models import FeatureComment, Feature","","class FeatureCommentForm(forms.ModelForm):","    class Meta:","        model = FeatureComment","        fields = ('comment',)","        ","class FeatureCreationForm(forms.ModelForm):","    class Meta:","        model = Feature","        fields = ('title', 'description')"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":22,"column":41},"action":"remove","lines":["from django import forms","from .models import FeatureComment, Feature","","class FeatureCommentForm(forms.ModelForm):","    class Meta:","        model = FeatureComment","        fields = ('comment',)","        ","class FeatureCreationForm(forms.ModelForm):","    class Meta:","        model = Feature","        fields = ('title', 'description')from django import forms","from .models import FeatureComment, Feature","","class TicketCommentForm(forms.ModelForm):","    class Meta:","        model = FeatureComment","        fields = ('comment',)","        ","class FeatureCreationForm(forms.ModelForm):","    class Meta:","        model = Feature","        fields = ('title', 'description')"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":11,"column":41},"action":"insert","lines":["from django import forms","from .models import FeatureComment, Feature","","class FeatureCommentForm(forms.ModelForm):","    class Meta:","        model = FeatureComment","        fields = ('comment',)","        ","class FeatureCreationForm(forms.ModelForm):","    class Meta:","        model = Feature","        fields = ('title', 'description')"],"id":4}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["e"],"id":5},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":["r"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["u"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["t"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["a"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["e"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"remove","lines":["F"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["T"],"id":6},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["i"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["c"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["k"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["e"],"id":7},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["r"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["u"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["t"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["a"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"remove","lines":["e"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["F"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["T"],"id":8},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["i"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["c"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["k"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["e"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["e"],"id":10},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["r"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["u"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["t"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["a"]}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["e"],"id":11},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["F"]}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["T"],"id":12},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["i"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["c"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["k"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["e"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":23},"action":"remove","lines":["Feature"],"id":15},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["T"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["i"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["c"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["k"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["e"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":41},"end":{"row":11,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566251573982,"hash":"829e78dad16b31ee6d76fb29ea8d2d4cb47c4e59"}