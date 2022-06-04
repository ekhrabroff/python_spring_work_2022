class View:
    def __init__(self):
        pass

    def render(self, data):
        raise NotImplementedError('Метод должен быть перегружен')

class ListView(View):
    def __init__(self):
        pass
    def render(self, data):
        self.data = data
        print('Данные из класса ListView', self.data)

class QuestionView(View):
    def __init__(self):
        pass
    def render(self, data):
        self.data = data
        print('Данные из класса QuestionView', self.data)

class View_fabric:
    def __init__(self):
        pass
    def get_render(self, render_type):
        if render_type == 'list':
            return ListView
        elif render_type == 'question':
            return  QuestionView
        else:
            pass

obj = View_fabric()

rend = obj.get_render('list')
rend.render(rend, 'Test')

rend1 = obj.get_render('question')
rend3 = rend1.render(rend1, 'Test')
