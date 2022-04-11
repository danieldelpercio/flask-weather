import requests

from flask import(
    Blueprint,render_template,request
)

bp = Blueprint('weather',__name__)

@bp.route('/', methods=['GET','POST'])
def index():
    city = 'Las Vegas' #initial default city
    
    if request.method == 'POST':
        city = request.form.get('city')

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1dbaf7baf220c461d9be1a59aebba09a'
    

    r = requests.get(url.format(city)).json()
    

    weather = {
        'city' : city,
        'temp' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
    }

    print(weather)

    return render_template('index.html',weather=weather)