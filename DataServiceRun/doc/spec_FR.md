<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : DataServiceRun  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataServiceRun/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- Aucune propriété requise  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ce modèle de données ne fait pas partie de la norme DCAT 2.1.0, il s'agit d'une extension qui sera proposée pour adoption.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataServiceRun:    
  description: A representation of one specific run of a data service (e.g. DataServiceDCAT-AP).    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    configuration:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Technical configuration of the service. This attribute is intended to be an array of properties and their values which capture parameters which have to do with the configuration of a service (output format, URL, etc.) and which are not currently covered by the standard attributes defined by this model.'    
      items:    
        properties:    
          parameter:    
            format: text    
            type: string    
          value:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &dataservicerun_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *dataservicerun_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    resultEntities:    
      description: Relationship. A list of references pointing to NGSI-LD entities that were generated within a service run.    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    resultExternal:    
      description: Property. A list of uri pointing to external results that were generated within a service run.    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    service:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Relationship. A reference pointing to the NGSI-LD entity representing the corresponding data service (e.g. of type DataServiceDCAT-AP).    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    sourceEntities:    
      description: Relationship. A list of references pointing to NGSI-LD entities that acted as source within a service run.    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    sourceExternal:    
      description: Property. A list of uri pointing to external results that acted as source within a service run.    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI entity type. It has to be DataServiceRun    
      enum:    
        - DataServiceRun    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataServiceRun/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.DCAT-AP/master/DataServiceRun/schema.json    
  x-model-tags: SALTED    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### DataServiceRun Valeurs clés NGSI-v2 Exemple  
Voici un exemple de DataServiceRun au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataServiceRun:example-1234",  
  "type": "DataServiceRun",  
  "configuration": [  
    {  
      "parameter": "param1",  
      "value": "10"  
    },  
    {  
      "parameter": "param2",  
      "value": "3"  
    }  
  ],  
  "dateCreated": "2022-06-21T08:24:35.905712+02:00",  
  "dateModified": "2022-06-22T09:24:35.905712+02:00",  
  "description": "This is a representation of one specific run of a data service.",  
  "resultEntities": [  
    "urn:ngsi-ld:KeyPerformanceIndicator:example3",  
    "urn:ngsi-ld:KeyPerformanceIndicator:example4"  
  ],  
  "resultExternal": [  
    "http://1.2.3.4:5678/files/example-file-3",  
    "http://1.2.3.4:5678/files/example-file-4"  
  ],  
  "sourceEntities": [  
    "urn:ngsi-ld:Organization:example1",  
    "urn:ngsi-ld:Organization:example2"  
  ],  
  "sourceExternal": [  
    "http://1.2.3.4:5678/files/example-file-1",  
    "http://1.2.3.4:5678/files/example-file-2"  
  ],  
  "service": "urn:ngsi-ld:DataServiceDCAT-AP:example"  
}  
```  
</details>  
#### DataServiceRun NGSI-v2 normalisé Exemple  
Voici un exemple de DataServiceRun au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataServiceRun:example-1234",  
  "type": "DataServiceRun",  
  "configuration": {  
    "type": "array",  
    "value": [  
      {  
        "parameter": "param1",  
        "value": "10"  
      },  
      {  
        "parameter": "param2",  
        "value": "3"  
      }  
    ]  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-06-21T08:24:35.905712+02:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-06-22T09:24:35.905712+02:00"  
  },  
  "description": {  
    "type": "Text",  
    "value": "This is a representation of one specific run of a data service."  
  },  
  "resultEntities": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:KeyPerformanceIndicator:example3",  
      "urn:ngsi-ld:KeyPerformanceIndicator:example4"  
    ]  
  },  
  "resultExternal": {  
    "type": "array",  
    "value": [  
      "http://1.2.3.4:5678/files/example-file-3",  
      "http://1.2.3.4:5678/files/example-file-4"  
    ]  
  },  
  "sourceEntities": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Organization:example1",  
      "urn:ngsi-ld:Organization:example2"  
    ]  
  },  
  "sourceExternal": {  
    "type": "array",  
    "value": [  
      "http://1.2.3.4:5678/files/example-file-1",  
      "http://1.2.3.4:5678/files/example-file-2"  
    ]  
  },  
  "service": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:DataServiceDCAT-AP:example"  
  },      
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
]  
}  
```  
</details>  
#### DataServiceRun Valeurs clés NGSI-LD Exemple  
Voici un exemple de DataServiceRun au format JSON-LD en tant que valeurs-clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataServiceRun:example-1234",  
  "type": "DataServiceRun",  
  "configuration": [  
    {  
      "parameter": "param1",  
      "value": "10"  
    },  
    {  
      "parameter": "param2",  
      "value": "3"  
    }  
  ],  
  "dateCreated": "2022-06-21T08:24:35.905712+02:00",  
  "dateModified": "2022-06-22T09:24:35.905712+02:00",  
  "description": "This is a representation of one specific run of a data service.",  
  "resultEntities": [  
    "urn:ngsi-ld:KeyPerformanceIndicator:example3",  
    "urn:ngsi-ld:KeyPerformanceIndicator:example4"  
  ],  
  "resultExternal": [  
    "http://1.2.3.4:5678/files/example-file-3",  
    "http://1.2.3.4:5678/files/example-file-4"  
  ],  
  "sourceEntities": [  
    "urn:ngsi-ld:Organization:example1",  
    "urn:ngsi-ld:Organization:example2"  
  ],  
  "sourceExternal": [  
    "http://1.2.3.4:5678/files/example-file-1",  
    "http://1.2.3.4:5678/files/example-file-2"  
  ],  
  "service": "urn:ngsi-ld:DataServiceDCAT-AP:example",  
  "@context": [  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### DataServiceRun NGSI-LD normalisé Exemple  
Voici un exemple de DataServiceRun au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DataServiceRun:example-1234",  
    "type": "DataServiceRun",  
    "configuration": {  
        "type": "Property",  
        "value": [  
            {  
                "parameter": "param1",  
                "value": "10"  
            },  
            {  
                "parameter": "param2",  
                "value": "3"  
            }  
        ]  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": "2022-06-21T08:24:35.905712+02:00"  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": "2022-06-22T09:24:35.905712+02:00"  
    },  
    "description": {  
        "type": "Property",  
        "value": "This is a representation of one specific run of a data service."  
    },  
    "resultEntities": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:KeyPerformanceIndicator:example3",  
            "urn:ngsi-ld:KeyPerformanceIndicator:example4"  
        ]  
    },  
    "resultExternal": {  
        "type": "Property",  
        "value": [  
            "http://1.2.3.4:5678/files/example-file-3",  
            "http://1.2.3.4:5678/files/example-file-4"  
        ]  
    },  
    "sourceEntities": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Organization:example1",  
            "urn:ngsi-ld:Organization:example2"  
        ]  
    },  
    "sourceExternal": {  
        "type": "Property",  
        "value": [  
            "http://1.2.3.4:5678/files/example-file-1",  
            "http://1.2.3.4:5678/files/example-file-2"  
        ]  
    },  
    "service": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:DataServiceDCAT-AP:example"  
    },  
    "@context": [  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.DataServices/master/context.jsonld"  
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
