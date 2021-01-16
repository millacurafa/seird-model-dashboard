# SEIRD-model-dashboard

Dashboard for analysis of Chilean Covid19 data, including SEIRD model

A live version is being constantly updated at [herokuapp.com](https://covid19-chile-dash.herokuapp.com/) (*currently fixing pip version conflicts*)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Requirements

USe `pip3 install -r requirements.txt`  to install all following libraries:

```python
# Python libraries to be installed

appdirs==1.4.4
Brotli==1.0.9
certifi==2020.12.5
click==7.1.2
dash==1.18.1
dash-bootstrap-components==0.11.1
dash-core-components==1.14.1
dash-html-components==1.1.1
dash-renderer==1.8.3
dash-table==4.11.1
distlib==0.3.1
filelock==3.0.12
Flask==1.1.2
Flask-Compress==1.8.0
future==0.18.2
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
numpy==1.19.5
pandas==1.2.0
pipenv==2020.11.15
plotly==4.14.3
python-dateutil==2.8.1
pytz==2020.5
retrying==1.3.3
scipy==1.6.0
six==1.15.0
virtualenv==20.3.1
virtualenv-clone==0.5.4
Werkzeug==1.0.1

```

### Installing

A step by step series of examples that tell you how to get a development env running

```
git clone https://github.com/millacurafa/seird-model-dashboard

or via SSH

git clone git@github.com:millacurafa/seird-model-dashboard.git
```

and run the ui.app 

```
cd seird-model-dashboard/
python ui.py
```


## Running the tests


```
Dash will run a local version on http://127.0.0.1:8050/ after proper deployment
```


### And coding style tests

```
Code is written using the snake_case standard for python apps.

```

## Deployment

For deployment into Heroku check current `pip` version for possible conflicts.

Last Heroku [update](https://devcenter.heroku.com/changelog-items/1740) includes pip version `20.0.2` the first you should downgrade your version if needed. *Remember to do this in a virtual environment*

```
pip install pip==20.0.2
```

## Built With

* Dash
* Plotly
* Pandas
* Scipy

## Contributing

Please read [CONTRIBUTING.md](https://github.com/millacurafa/CovidChile/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Git](https://git-scm.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/millacurafa/seird-model-dashboard/tags). 

## Authors


See the list of [contributors](https://github.com/millacurafa/seird-model-dashboard/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Felipe Millacura for creating this project and Cristobal Donoso for guidance.
* Epidemiological data obtained from the Chilean Health Ministry (MINSAL) and other official sources, documented and open for community analysis. Made available by the Chilean Science Ministry in the following [github repo](https://github.com/MinCiencia/Datos-COVID19/)





