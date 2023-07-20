<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : CatalogueRecord  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/CatalogueRecord/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Il s'agit d'une fiche de catalogue appartenant à un ensemble de données conformément à la norme DCAT-AP 2.1.1**.  
version : 1.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `conformsTo[string]`: Propriété. Modèle : "http://purl.org/dc/terms/Standard". Cette propriété fait référence à un profil d'application auquel les métadonnées de l'ensemble de données sont conformes.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `description[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient un compte rendu en texte libre de l'enregistrement. Cette propriété peut être répétée pour les versions en langues parallèles de la description  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `id[*]`: Identifiant unique de l'entité  - `issued[string]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient la date à laquelle la description du jeu de données a été incluse dans le catalogue.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: Propriété. Modèle : "http://purl.org/dc/terms/LinguisticSystem". Cette propriété fait référence à une langue utilisée dans les métadonnées textuelles décrivant les titres, les descriptions, etc. de l'ensemble de données. Cette propriété peut être répétée si les métadonnées sont fournies en plusieurs langues  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `modified[string]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient la date la plus récente à laquelle l'entrée du catalogue a été changée ou modifiée.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `primaryTopic[string]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Dataset". Cette propriété relie la fiche du catalogue à l'ensemble de données, au service de données ou au catalogue décrit dans la fiche.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `source[string]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#CatalogRecord". Cette propriété fait référence aux métadonnées originales qui ont été utilisées pour créer les métadonnées de l'ensemble de données.  . Model: [http://www.w3.org/ns/dcat#CatalogRecord](http://www.w3.org/ns/dcat#CatalogRecord)- `status[string]`: Propriété. Modèle : "http://www.w3.org/2004/02/skos/core#Concept". Cette propriété fait référence au type de la dernière révision de l'entrée d'un jeu de données dans le catalogue.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient un nom donné à la notice du catalogue. Cette propriété peut être répétée pour les versions linguistiques parallèles du nom.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Propriété. Type d'entité NGSI. Il doit s'agir d'un CatalogueRecord  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `modified`  - `primaryTopic`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de [DCAT-AP version 2.1.1] (https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CatalogueRecord:    
  description: This is a Catalogue Record belonging to a dataset according to the DCAT-AP standard 2.1.1    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
    conformsTo:    
      description: 'Property. Model:''http://purl.org/dc/terms/Standard''. This property refers to an Application Profile that the Dataset''s metadata conforms to'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    description:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a free-text account of the record. This property can be repeated for parallel language versions of the description"    
      items:    
        description: Property. Every language description    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    id:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    issued:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the date on which the description of the Dataset was included in the Catalogue."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    language:    
      description: 'Property. Model:''http://purl.org/dc/terms/LinguisticSystem''. This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Dataset. This property can be repeated if the metadata is provided in multiple languages'    
      items:    
        description: Property. Every language tag    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    modified:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the most recent date on which the Catalogue entry was changed or modified."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    primaryTopic:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Dataset'. This property links the Catalogue Record to the Dataset, Data service or Catalog described in the record."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    source:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#CatalogRecord'. This property refers to the original metadata that was used in creating metadata for the Dataset."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#CatalogRecord"    
        type: Property    
    status:    
      description: "Property. Model:'http://www.w3.org/2004/02/skos/core#Concept'. This property refers to the type of the latest revision of a Dataset's entry in the Catalogue."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    title:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name."    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    type:    
      description: Property. NGSI entity type. It has to be CatalogueRecord    
      enum:    
        - CatalogueRecord    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - primaryTopic    
    - modified    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/CatalogueRecord/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/CatalogueRecord/schema.json    
  x-model-tags: ""    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### CatalogueRecord Valeurs clés NGSI-v2 Exemple  
Voici un exemple de CatalogueRecord au format JSON-LD en tant que valeurs clés. Il est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecord:id:KFTL:88140679",  
  "type": "CatalogueRecord",  
  "description": ["Catalogue record of the solar system open data portal"],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      36.633152,  
      -85.183315  
    ]  
  },  
  "address": {  
    "streetAddress": "2, rue Mercier",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "addressCountry": "Luxembourg",  
    "postalCode": "2985",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "European Union and beyond",  
  "primaryTopic": "Public administration",  
  "modified": "2021-07-02T18:37:55Z",  
  "conformsTo": "DCAT Application profile for data portals in Europe",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "title": [  
    "Example of catalogue record",  
    "Ejemplo de registro de catálogo"  
  ]  
}  
```  
</details>  
#### CatalogueRecord NGSI-v2 normalisé Exemple  
Voici un exemple de CatalogueRecord au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecord:id:KFTL:88140679",  
  "type": "CatalogueRecord",  
  "modified": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        36.633152,  
        -85.183315  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAdress",  
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
    "value": "European Union and beyond"  
  },  
  "primaryTopic": {  
    "type": "Text",  
    "value": "Public administration"  
  },  
  "language": {  
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Example of catalogue record",  
      "Ejemplo de registro de catálogo"  
    ]  
  }  
}  
```  
</details>  
#### CatalogueRecord Valeurs clés NGSI-LD Exemple  
Voici un exemple de CatalogueRecord au format JSON-LD en tant que key-values. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CatalogueRecord:id:KFTL:88140679",  
    "type": "CatalogueRecord",  
    "address": {  
        "streetAddress": "2, rue Mercier",  
        "addressLocality": "Luxembourg",  
        "addressRegion": "Luxembourg",  
        "addressCountry": "Luxembourg",  
        "postalCode": "2985",  
        "postOfficeBoxNumber": ""  
    },  
    "areaServed": "European Union and beyond",  
    "modified": "2021-07-02T18:37:55Z",  
    "description": ["Catalogue record of the solar system open data portal"],  
    "language": [  
        "EN",  
        "ES"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            36.633152,  
            -85.183315  
        ]  
    },  
    "primaryTopic": "Public administration",  
    "title": [  
        "Example of catalogue record",  
        "Ejemplo de registro de cat\u00e1logo"  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### CatalogueRecord NGSI-LD normalisé Exemple  
Voici un exemple de CatalogueRecord au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecord:id:KFTL:88140679",  
  "type": "CatalogueRecord",  
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
  "language": {  
    "type": "Property",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "listingDate": {  
    "type": {  
      "@type": "Property",  
      "@value": "2021-07-02T18:37:55Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        36.633152,  
        -85.183315  
      ]  
    }  
  },  
  "modified": {  
    "type": {  
      "@type": "Property",  
      "@value": "2021-07-02T18:37:55Z"  
    }  
  },  
  "primaryTopic": {  
    "type": "Property",  
    "value": "Public administration"  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "Example of catalogue record",  
      "Ejemplo de registro de cat\u00e1logo"  
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
