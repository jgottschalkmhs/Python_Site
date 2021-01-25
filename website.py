from bottle import run, route, view, static_file, request
from datetime import date
import requests

# functions go here

# copes with extra / after url name
@route('/static/<filepath:path>')
def load_static(filepath):

    return static_file(filepath, root='./static')

# displays index
@route('/')
@view('index')
def index():

    today = date.today()
    formatted_date = today.strftime('%A')

    pass
    return dict(
        day = formatted_date
    )

# displays age guessing form...
@route('/age-form')
@view('age-form')
def age_form():
    pass

# displays age based on name...
@route('/age-result', method='POST')
@view('age-result')
def age_result():

    # get name from form...
    first_name = request.forms.get('name')

    # query api to get possible age

    api_result = requests.get('https://api.agify.io/?name=' + first_name)
    agify_data = api_result.json()

    return dict(
    name = first_name,
    age = agify_data['age']
    )
    pass


# Start the website
run(host='localhost', port=8080, reloader=True, debug=True)