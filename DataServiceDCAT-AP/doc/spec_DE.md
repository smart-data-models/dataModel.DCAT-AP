<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: DataServiceDCAT-AP  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataServiceDCAT-AP/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Datendienst angepasst an die DCAT-AP 2.0 Spezifikation, aber erweitert um zusätzliche Eigenschaften und kompatibel mit dem NGSI Standard**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `accessRights[string]`: Diese Eigenschaft KANN Informationen über den Zugang oder Einschränkungen aufgrund von Datenschutz-, Sicherheits- oder anderen Richtlinien enthalten.  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dataServiceDescription[array]`: Diese Eigenschaft enthält eine Freitextbeschreibung des Datendienstes. Diese Eigenschaft kann für parallele Sprachversionen der Beschreibung wiederholt werden  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `endPointDescription[array]`: Diese Eigenschaft enthält eine Beschreibung der über die Endpunkte verfügbaren Dienste, einschließlich ihrer Operationen, Parameter usw. Die Eigenschaft enthält spezifische Details zu den tatsächlichen Endpunktinstanzen, während dct:conformsTo verwendet wird, um den allgemeinen Standard oder die Spezifikation anzugeben, die die Endpunkte implementieren.  - `endPointURL[array]`: Der Hauptstandort oder primäre Endpunkt des Dienstes (ein IRI).  - `id[*]`: Eindeutiger Bezeichner der Entität  - `license[string]`: Diese Eigenschaft enthält die Lizenz, unter der der Datendienst zur Verfügung gestellt wird.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `servesDataset[array]`: Diese Eigenschaft bezieht sich auf eine Sammlung von Daten, die dieser Datendienst verteilen kann.  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `title[array]`: Diese Eigenschaft enthält einen Namen, der dem Datendienst gegeben wurde. Diese Eigenschaft kann für parallele Sprachversionen des Namens wiederholt werden.  - `type[string]`: NGSI-Entitätstyp. Es muss DataServiceDCAT-AP sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `endPointURL`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf). Einige Eigenschaften wurden umbenannt, um Konflikte mit anderen bestehenden Eigenschaften zu vermeiden. Zusätzlich wurden andere Eigenschaften hinzugefügt, um die Kompatibilität mit dem NGSI-Standard und anderen Datenmodellen zu gewährleisten.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataServiceDCAT-AP/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.DCAT-AP/edit/master/DataServiceDCAT-AP/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### DataServiceDCAT-AP NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen DataServiceDCAT-AP im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DataServiceDCAT-AP NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen DataServiceDCAT-AP im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DataServiceDCAT-AP NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen DataServiceDCAT-AP im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DataServiceDCAT-AP NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen DataServiceDCAT-AP im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DataServiceDCAT-AP:id:JBDJ:56257192",  
    "type": "DataServiceDCAT-AP",  
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
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "European union and beyond"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "European open data portal"  
    },  
    "dataServiceDescription": {  
        "type": "Property",  
        "value": [  
            "Digital resources for accessing to the end points of the EU open data portal for solar system.",  
            "Recursos digitales para el acceso a los puntos de interacci\u00f3n del portal europeo de datos abiertos del sistema solar."  
        ]  
    },  
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
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                72.564509,  
                11.125289  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": ""  
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
    "servesDataset": {  
        "type": "Property",  
        "value": [  
            "EU geographic map",  
            "EU physical map"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
