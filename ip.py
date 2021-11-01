import requests
from flask import Flask, request
import json

app = Flask(__name__)


def load_key():
    with open('config.json') as json_file:
        configs = json.load(json_file)
        key = configs['key']
        return key


@app.route('/')
def main():
    ip = request.args.get("ip", "")
    if ip:
        location = getIp(ip)
    else:
        location = ""
    return (
            """<form action="" method="get">
            <center>
                    <b><h2> Welcome to Geo Locator Application </b></h2>
                    <b>Insert IP: </b><input type="text" name="ip" value=""" + ip + """>
                <input type="submit" value="Check">
            </center>
            </form>"""
            + str(location)
    )


def getIp(ip):
    key = load_key()
    params = (
        ('apiKey', key),
        ('ip', ip),
    )
    response = requests.get("https://api.ipgeolocation.io/ipgeo", params=params)
    response = response.json()
    requested_answer = response['time_zone']['name']
    given_ip = response['ip']
    continent = response['continent_name']
    country = response['country_name']
    organization = response['organization']
    currency = response['currency']['name']
    time_zone = response['time_zone']['offset']
    return '''<center>
        <b> Details about given IP address {} :</b><br>
        <b> Requested Detail: {}.</b><br>
        <b> Continent: {}.</b><br>
        <b> Country:  {}.</b><br>
        <b> Organization:   {}.</b><br>
        <b> currency:   {}.</b><br>
        <b> time_zone:   {}.</b><br>
        </center>'''.format(given_ip, requested_answer, continent, country, organization, currency, time_zone)
