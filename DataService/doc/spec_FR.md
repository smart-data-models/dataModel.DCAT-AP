<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : DataService    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataService/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Service de données adapté de la spécification DCAT-AP 2.1.1, mais enrichi de propriétés supplémentaires et compatible avec la norme NGSI**.    
version : 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `accessRights[string]`: Cette propriété PEUT inclure des informations concernant l'accès ou les restrictions basées sur la vie privée, la sécurité ou d'autres politiques.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[array]`: Cette propriété contient un compte rendu en texte libre du service de données. Cette propriété peut être répétée pour les versions en langues parallèles de la description.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `endPointDescription[array]`: Cette propriété contient une description des services disponibles via les points finaux, y compris leurs opérations, leurs paramètres, etc. La propriété donne des détails spécifiques sur les instances des points d'extrémité, tandis que dct:conformsTo est utilisé pour indiquer la norme générale ou la spécification que les points d'extrémité mettent en œuvre.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `endPointURL[array]`: L'emplacement racine ou le point d'arrivée principal du service (un IRI)  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `id[*]`: Identifiant unique de l'entité  - `license[string]`: Cette propriété contient la licence sous laquelle le service de données est mis à disposition.  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `servesDataset[array]`: Cette propriété fait référence à une collection de données que ce service de données peut distribuer  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `title[array]`: Cette propriété contient le nom donné au service de données. Cette propriété peut être répétée pour les versions linguistiques parallèles du nom.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'un DataService  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `endPointURL`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Adapté de [DCAT-AP version 2.1.1] (https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211). Certaines propriétés ont été renommées afin d'éviter les conflits avec d'autres propriétés existantes. En outre, d'autres propriétés ont été ajoutées pour assurer la compatibilité avec la norme NGSI et d'autres modèles de données.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
DataService:      
  description: 'Data Service adapted from DCAT-AP 2.1.1 specification, but extended with additional properties and compatible with NGSI standard'      
  properties:      
    accessRights:      
      description: 'This property MAY include information regarding access or restrictions based on privacy, security, or other policies'      
      type: string      
      x-ngsi:      
        model: http://purl.org/dc/terms/RightsStatement      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    description:      
      description: This property contains a free-text account of the Data Service. This property can be repeated for parallel language versions of the description      
      items:      
        description: Every description in a language      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"      
        type: Property      
    endPointDescription:      
      description: 'This property contains a description of the services available via the end-points, including their operations, parameters etc. The property gives specific details of the actual endpoint instances, while dct:conformsTo is used to indicate the general standard or specification that the endpoints implement'      
      items:      
        description: Every service available at an end-point      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"      
        type: Property      
    endPointURL:      
      description: The root location or primary endpoint of the service (an IRI)      
      items:      
        description: Every root location      
        format: uri      
        minItems: 1      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    license:      
      description: This property contains the licence under which the Data service is made available      
      type: string      
      x-ngsi:      
        model: http://purl.org/dc/terms/LicenseDocument      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    servesDataset:      
      description: This property refers to a collection of data that this data service can distribute      
      items:      
        description: Every dataset distributed      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: "http://www.w3.org/ns/dcat#Dataset"      
        type: Property      
    title:      
      description: This property contains a name given to the Data Service. This property can be repeated for parallel language versions of the name      
      items:      
        description: The title in one language      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be DataService      
      enum:      
        - DataService      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - endPointURL      
    - id      
    - title      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataService/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
Certaines propriétés ont été ajoutées pour permettre un plus large éventail d'utilisations. Il s'agit de contactPoint, assetProvider et configuration.    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### DataService NGSI-v2 key-values Exemple    
Voici un exemple de DataService au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "areaServed": "European union and beyond",  
  "description": [  
    "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
    "Recursos digitales para el acceso a los puntos de interaccion del portal europeo de datos abiertos del sistema solar."  
  ],  
  "endPointDescription": [  
    "SPARQL end point without authentication",  
    "API compliant with CKAN specification"  
  ],  
  "endPointURL": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
  ],  
  "license": "EUPL.",  
  "location": {  
    "coordinates": [  
      72.564509,  
      11.125289  
    ],  
    "type": "Point"  
  },  
  "servesDataset": [  
    "EU geographic map",  
    "EU physical map"  
  ],  
  "title": [  
    "Data service of the european open data portal",  
    "Data service del portal europeo de datos abiertos"  
  ]  
}  
```  
</details>    
#### DataService NGSI-v2 normalisé Exemple    
Voici un exemple de DataService au format JSON-LD tel que normalisé. Il est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "description": {  
    "type": "StructuredValue",  
    "value": [  
      "Data service for the solar system open data portal."  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        72.564509,  
        11.125289  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "2, rue Mercier",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "2985",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "European union and beyond"  
  },  
  "endPointURL": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
    ]  
  },  
  "title": {  
    "type": "StructuredValue",  
    "value": [  
      "Data service of the european open data portal",  
      "Data service del portal europeo de datos abiertos"  
    ]  
  },  
  "endPointDescription": {  
    "type": "StructuredValue",  
    "value": [  
      "SPARQL end point without authentication",  
      "API compliant with CKAN specification"  
    ]  
  },  
  "servesDataset": {  
    "type": "StructuredValue",  
    "value": [  
      "EU geographic map",  
      "EU physical map"  
    ]  
  },  
  "accessRights": {  
    "type": "Text",  
    "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
  },  
  "license": {  
    "type": "Text",  
    "value": "EUPL."  
  }  
}  
```  
</details>    
#### DataService Valeurs clés NGSI-LD Exemple    
Voici un exemple de DataService au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "areaServed": "European union and beyond",  
  "description": [  
    "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
    "Recursos digitales para el acceso a los puntos de interaccion del portal europeo de datos abiertos del sistema solar."  
  ],  
  "modified": "2021-10-06T16:31:26Z",  
  "endPointDescription": [  
    "SPARQL end point without authentication",  
    "API compliant with CKAN specification"  
  ],  
  "endPointURL": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
  ],  
  "license": "EUPL.",  
  "location": {  
    "coordinates": [  
      72.564509,  
      11.125289  
    ],  
    "type": "Point"  
  },  
  "servesDataset": [  
    "EU geographic map",  
    "EU physical map"  
  ],  
  "title": [  
    "Data service of the european open data portal",  
    "Data service del portal europeo de datos abiertos"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### DataService NGSI-LD normalisé Exemple    
Voici un exemple de DataService au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
    "type": "DataService",  
    "accessRights": {  
        "type": "Property",  
        "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "2, rue Mercier",  
            "addressLocality": "Luxembourg",  
            "addressRegion": "Luxembourg",  
            "addressCountry": "Luxembourg",  
            "postalCode": "2985",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "European union and beyond"  
    },  
    "modified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-10-06T16:31:26Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Data service for the solar system open data portal."  
    },  
    "endPointDescription": {  
        "type": "Property",  
        "value": [  
            "SPARQL end point without authentication",  
            "API compliant with CKAN specification"  
        ]  
    },  
    "endPointURL": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
            "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
        ]  
    },  
    "license": {  
        "type": "Property",  
        "value": "EUPL."  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                72.564509,  
                11.125289  
            ]  
        }  
    },  
    "servesDataset": {  
        "type": "Property",  
        "value": [  
            "EU geographic map",  
            "EU physical map"  
        ]  
    },  
    "title": {  
        "type": "Property",  
        "value": [  
            "Data service of the european open data portal",  
            "Data service del portal europeo de datos abiertos"  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
