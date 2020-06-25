import web

render = web.template.render('views')

class hello:
    def GET(self):
        try:
            return render.index()
        except Exception as e:
            return "Error "+str(e.args)