from . import web




@web.route('/')
def index():
    return 'hi'


@web.route('/personal')
def personal_center():
    pass
