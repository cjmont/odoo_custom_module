<!-- PROJECT LOGO -->
<br />
<p>
  <h3>Consult an api-rest and save your pokemon in an own Odoo Module</h3>
  <img src="https://github.com/cjmont/odoo_custom_module/blob/main/img/pokemon.png" />
</p>


<!-- GETTING STARTED -->
## Table of contents

* [Description](#description)
* [Build with](#built-with)
* [REST API](#rest-api)



## Description

A custom module is required in Odoo that contains:

Scheduled task that consults the API https://pokeapi.co/api/v2/pokemon/ and stores the information in the custom module "Pokémon".

Create a View that lists the information stored in the Pokémon model


## REST API

A custom module is required in Odoo that contains:

A custom module is required in Odoo that contains a REST API service using Web Controllers and the native models: Partner, Order, Order Line and Product.

· List of Invoices (GET /invoices/)

· Create Invoice (POST /invoices/)

The JSON that the endpoints must receive and return is the following:

```sh
{

      "id": 1,
      "createtime": "2021-11-16 12:00",
      "document_number": "001-001-00001234", 
      "customer": {
          "document_type": "Cédula|RUC|Pasaporte", 
          "document_number": "0987654321", 
          "first_name": "Christian",
          "last_name": "Jaque", 
          "phone": "0987654321",
          "address": "Guayaquil, Urdesa", 
          "email": "cjaque@macronegocios.ec"
      },

      "items": [
          {
            "reference": "SKU1234", 
            "name": "Labial",
            "price": 10.50,
            "discount": 2.50,
            "subtotal": 8.50,
            "tax": 1.02,
            "total": 9.52
          },
      ]
}
```


## Built with

* [Python 3](https://www.python.org/downloads/)
* [Odoo 16](https://www.odoo.com/es_ES/blog/viajes-5/conoce-odoo-16-968)




 
