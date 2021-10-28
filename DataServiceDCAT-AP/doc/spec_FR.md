Entité : DataServiceDCAT-AP  
===========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataServiceDCAT-AP/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Service de données adapté de la spécification DCAT-AP 2.0, mais étendu avec des propriétés supplémentaires et compatible avec la norme NGSI**.  
version : 0.0.1  

## Liste des propriétés  

- `accessRights`: Cette propriété PEUT inclure des informations concernant l'accès ou les restrictions basées sur la confidentialité, la sécurité ou d'autres politiques.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dataServiceDescription`: Cette propriété contient un compte rendu en texte libre du service de données. Cette propriété peut être répétée pour les versions en langage parallèle de la description.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `endPointDescription`: Cette propriété contient une description des services disponibles via les points de terminaison, y compris leurs opérations, paramètres, etc. La propriété donne des détails spécifiques sur les instances réelles des points de terminaison, tandis que dct:conformsTo est utilisé pour indiquer la norme ou la spécification générale que les points de terminaison mettent en œuvre.  - `endPointURL`: L'emplacement racine ou le point d'extrémité primaire du service (un IRI).  - `id`: Identifiant unique de l'entité  - `license`: Cette propriété contient la licence sous laquelle le service de données est mis à disposition.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `servesDataset`: Cette propriété fait référence à une collection de données que ce service de données peut distribuer.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `title`: Cette propriété contient un nom donné au service de données. Cette propriété peut être répétée pour les versions linguistiques parallèles du nom.  - `type`: Type d'entité NGSI. Il doit être DataServiceDCAT-AP.    
Propriétés requises  
- `endPointURL`  - `id`  - `title`  - `type`    
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf). Certaines propriétés ont été renommées afin d'éviter les conflits avec d'autres propriétés existantes. De plus, d'autres propriétés ont été ajoutées pour assurer la compatibilité avec la norme NGSI et d'autres modèles de données.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataServiceDCAT-AP:    
  description: 'Data Service adapted from DCAT-AP 2.0 specification, but extended with additional properties and compatible with NGSI standard'    
  properties:    
    accessRights:    
      description: 'This property MAY include information regarding access or restrictions based on privacy, security, or other policies'    
      type: string    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dataServiceDescription:    
      description: 'This property contains a free-text account of the Data Service. This property can be repeated for parallel language versions of the description'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endPointDescription:    
      description: 'This property contains a description of the services available via the end-points, including their operations, parameters etc. The property gives specific details of the actual endpoint instances, while dct:conformsTo is used to indicate the general standard or specification that the endpoints implement.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    endPointURL:    
      description: 'The root location or primary endpoint of the service (an IRI).'    
      items:    
        format: uri    
        minItems: 1    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &dataservicedcat-ap_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    license:    
      description: 'This property contains the licence under which the Data service is made available.'    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *dataservicedcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    servesDataset:    
      description: 'This property refers to a collection of data that this data service can distribute.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    title:    
      description: 'This property contains a name given to the Data Service. This property can be repeated for parallel language versions of the name.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be DataServiceDCAT-AP'    
      enum:    
        - DataServiceDCAT-AP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - endPointURL    
    - id    
    - title    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### DataServiceDCAT-AP Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de DataServiceDCAT-AP au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:DataServiceDCAT-AP:id:JBDJ:56257192",  
  "type": "DataServiceDCAT-AP",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "alternateName": "",  
  "areaServed": "European union and beyond",  
  "dataProvider": "European open data portal",  
  "dataServiceDescription": [  
    "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
    "Recursos digitales para el acceso a los puntos de interaccion del portal europeo de datos abiertos del sistema solar."  
  ],  
  "dateCreated": "2020-10-28T04:19:29Z",  
  "dateModified": "2021-10-06T16:31:26Z",  
  "description": "Data service for the solar system open data portal.",  
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
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:HGSY:92686457",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JCJR:29622597"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JDKD:53476147",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:XVJQ:09725114"  
  ],  
  "servesDataset": [  
    "EU geographic map",  
    "EU physical map"  
  ],  
  "source": "",  
  "title": [  
    "Data service of the european open data portal",  
    "Data service del portal europeo de datos abiertos"  
  ]  
}  
```  
#### DataServiceDCAT-AP NGSI-v2 normalisé Exemple  
Voici un exemple d'un DataServiceDCAT-AP au format JSON-LD tel que normalisé. Il est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:DataServiceDCAT-AP:id:JBDJ:56257192",  
  "type": "DataServiceDCAT-AP",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-10-28T04:19:29Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-10-06T16:31:26Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Data service for the solar system open data portal."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "European open data portal"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:HGSY:92686457",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JCJR:29622597"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JDKD:53476147",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:XVJQ:09725114"  
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
    "type": "PostalAddress",  
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
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
    ]  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Data service of the european open data portal",  
      "Data service del portal europeo de datos abiertos"  
    ]  
  },  
  "endPointDescription": {  
    "type": "array",  
    "value": [  
      "SPARQL end point without authentication",  
      "API compliant with CKAN specification"  
    ]  
  },  
  "servesDataset": {  
    "type": "array",  
    "value": [  
      "EU geographic map",  
      "EU physical map"  
    ]  
  },  
  "accessRights": {  
    "type": "Text",  
    "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
  },  
  "dataServiceDescription": {  
    "type": "array",  
    "value": [  
      "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
      "Recursos digitales para el acceso a los puntos de interacción del portal europeo de datos abiertos del sistema solar."  
    ]  
  },  
  "license": {  
    "type": "Text",  
    "value": "EUPL."  
  }  
}  
```  
#### DataServiceDCAT-AP Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un DataServiceDCAT-AP au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:DataServiceDCAT-AP:id:JBDJ:56257192",  
  "type": "DataServiceDCAT-AP",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "alternateName": "",  
  "areaServed": "European union and beyond",  
  "dataProvider": "European open data portal",  
  "dataServiceDescription": [  
    "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
    "Recursos digitales para el acceso a los puntos de interaccion del portal europeo de datos abiertos del sistema solar."  
  ],  
  "dateCreated": "2020-10-28T04:19:29Z",  
  "dateModified": "2021-10-06T16:31:26Z",  
  "description": "Data service for the solar system open data portal.",  
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
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:HGSY:92686457",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JCJR:29622597"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JDKD:53476147",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:XVJQ:09725114"  
  ],  
  "servesDataset": [  
    "EU geographic map",  
    "EU physical map"  
  ],  
  "source": "",  
  "title": [  
    "Data service of the european open data portal",  
    "Data service del portal europeo de datos abiertos"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### DataServiceDCAT-AP NGSI-LD normalisé Exemple  
Voici un exemple d'un DataServiceDCAT-AP au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:DataServiceDCAT-AP:id:JBDJ:56257192",  
  "type": "DataServiceDCAT-AP",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-28T04:19:29Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-10-06T16:31:26Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Data service for the solar system open data portal."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "European open data portal"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:HGSY:92686457",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JCJR:29622597"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JDKD:53476147",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:XVJQ:09725114"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        72.564509,  
        11.125289  
      ]  
    }  
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
  "endPointURL": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
    ]  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "Data service of the european open data portal",  
      "Data service del portal europeo de datos abiertos"  
    ]  
  },  
  "endPointDescription": {  
    "type": "Property",  
    "value": [  
      "SPARQL end point without authentication",  
      "API compliant with CKAN specification"  
    ]  
  },  
  "servesDataset": {  
    "type": "Property",  
    "value": [  
      "EU geographic map",  
      "EU physical map"  
    ]  
  },  
  "accessRights": {  
    "type": "Property",  
    "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
  },  
  "dataServiceDescription": {  
    "type": "Property",  
    "value": [  
      "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
      "Recursos digitales para el acceso a los puntos de interacciÃ³n del portal europeo de datos abiertos del sistema solar."  
    ]  
  },  
  "license": {  
    "type": "Property",  
    "value": "EUPL."  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
