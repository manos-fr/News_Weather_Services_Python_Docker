import json
from sys import argv, exit
from flask import Flask, request
import requests

def main(argv):

    if len(argv) > 3 or len(argv) < 2:
        print(f'Usage: {argv[0]} <City name> or/and <Country News>')
        exit(1)

    cityStr = argv[1]
    countryStr = argv[2]

    if len(argv) == 2:    
        weather(cityStr)
    elif len(argv) == 3:
        news(countryStr) 
        weather(cityStr)
 
def weather(city):
    cityStr = city
    if cityStr.isdigit():
        print("\nCity name must be string e.g. 'Amsterdam, Berlin' ")
        exit(1)
    response = requests.get("http://localhost:3001/weather?city="+ cityStr)
    weather = response.json() 
    print(f"\nWeather of {cityStr}: {weather}")    
    return weather

def news(country):
    countryStr = country
    if countryStr.isdigit() or len(countryStr) > 2 :
        print("Country name must be string. Choose from below: \n\nThe 2-letter ISO 3166-1 code of the country you want to get headlines for.\nPossible options: ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za")
        return
    response = requests.get("http://localhost:3001/news?country="+ countryStr)
    news = response.json() 
    print(f"{countryStr} News: {news}")
    return news

if __name__ == '__main__':
    main(argv)