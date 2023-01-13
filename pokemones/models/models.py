from odoo import models, fields, api
import datetime
import requests

class Pokemones(models.Model):
    _name = 'pokemon.pokemones'
    _description = 'Consulta Pokemones'

    name = fields.Char(string='Nombre')
    url = fields.Char(string='Url de la imagen')


    def task_program(self):
        url = "https://pokeapi.co/api/v2/pokemon/"
        params = {'limit': 5}

        for offset in range(0, 100, 50):
            params['offset'] = offset  
            response = requests.get(url, params=params)

            if response.status_code != 200: 
                print(response.text)
            else:
                data = response.json()
                #pp.pprint(data)
                for item in data['results']:
                    print(item['name'])
                    print((item['url']))
                    pokemones = {
                        'name': item['name'],
                        'url' : item['url'],
                    }
                    self.env['pokemon.pokemones'].create(pokemones)