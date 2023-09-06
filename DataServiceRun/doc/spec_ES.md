<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: DataServiceRun  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataServiceRun/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Representación de una ejecución específica de un servicio de datos (por ejemplo, DataServiceDCAT-AP).**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `configuration[array]`: Configuración técnica del servicio. Este atributo pretende ser una matriz de propiedades y sus valores que capturan parámetros que tienen que ver con la configuración de un servicio (formato de salida, URL, etc.) y que actualmente no están cubiertos por los atributos estándar definidos por este modelo  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `resultEntities[array]`: Una lista de referencias que apuntan a entidades NGSI-LD que se generaron dentro de una ejecución de servicio.  - `resultExternal[array]`: Una lista de uri que apuntan a resultados externos que se generaron dentro de una ejecución de servicio  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `service[*]`: una referencia a la entidad NGSI-LD que representa el servicio de datos correspondiente (por ejemplo, del tipo DataServiceDCAT-AP)  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `sourceEntities[array]`: Una lista de referencias que apuntan a entidades NGSI-LD que actuaron como fuente dentro de una ejecución de servicio.  - `sourceExternal[array]`: Una lista de uri que apuntan a resultados externos que actuaron como fuente dentro de una ejecución de servicio  - `type[string]`: Tipo de entidad NGSI. Tiene que ser DataServiceRun  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Este modelo de datos no pertenece a la norma DCAT 2.1.0, es una extensión que se propondrá para su adopción.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
      description: 'Technical configuration of the service. This attribute is intended to be an array of properties and their values which capture parameters which have to do with the configuration of a service (output format, URL, etc.) and which are not currently covered by the standard attributes defined by this model'    
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
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
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
      type: array    
      x-ngsi:    
        type: Property    
    resultEntities:    
      description: A list of references pointing to NGSI-LD entities that were generated within a service run    
      items:    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    resultExternal:    
      description: A list of uri pointing to external results that were generated within a service run    
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
      description: A reference pointing to the NGSI-LD entity representing the corresponding data service (e.g. of type DataServiceDCAT-AP)    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    sourceEntities:    
      description: A list of references pointing to NGSI-LD entities that acted as source within a service run    
      items:    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    sourceExternal:    
      description: A list of uri pointing to external results that acted as source within a service run    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be DataServiceRun    
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
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/DataServiceRun/schema.json    
  x-model-tags: SALTED    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### DataServiceRun NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un DataServiceRun en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### DataServiceRun NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un DataServiceRun en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### DataServiceRun NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un DataServiceRun en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
      "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### DataServiceRun NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un DataServiceRun en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
      "https://raw.githubusercontent.com/smart-data-models/dataModel.DataServices/master/context.jsonld"  
  ]  
  }  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
