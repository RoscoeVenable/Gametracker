from flask import Blueprint, render_template

bp = Blueprint('searching', __name__)


@bp.route('/videogame')
def video_game():
    message = "This text is coming from the 'VIDEOGAME.PY' module, not the html file!"
    phrase = "Python is ...... ok!"
    return render_template('videogame/index.html', message=message, word=phrase)

#class Search:
    #def __init__(self, game_value):
       # self.value
       # self.found = True

    #def search_By_Name(self):
        #pass

# video_game.py
# register a blueprint
# create one endpoint
# visit it, go from there