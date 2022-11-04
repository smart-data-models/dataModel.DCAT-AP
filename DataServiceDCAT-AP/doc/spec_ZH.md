<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。数据服务DCAT-AP  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataServiceDCAT-AP/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**数据服务改编自DCAT-AP 2.0规范，但扩展了额外的属性并与NGSI标准兼容**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `accessRights[string]`: 该属性可能包括基于隐私、安全或其他政策的访问或限制信息。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dataServiceDescription[array]`: 此属性包含数据服务的自由文本说明。此属性可重复用于平行语言版本的描述  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `endPointDescription[array]`: 此属性包含对通过端点提供的服务的描述，包括其操作、参数等。该属性给出了实际端点实例的具体细节，而dct:conformsTo则用于指示端点实现的一般标准或规范。  - `endPointURL[array]`: 服务的根位置或主要端点（一个IRI）。  - `id[*]`: 实体的唯一标识符  - `license[string]`: 此属性包含提供数据服务的许可。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `servesDataset[array]`: 此属性指的是此数据服务可以分发的数据集合。  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `title[array]`: 此属性包含给予数据服务的名称。此属性可重复用于该名称的平行语言版本。  - `type[string]`: NGSI实体类型。它必须是DataServiceDCAT-AP  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `endPointURL`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf).一些属性已经被重新命名，以防止与其他现有的属性冲突。此外，还增加了其他属性以保持与NGSI标准和其他数据模型的兼容性。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
## ＃＃＃＃有效载荷的例子  
#### DataServiceDCAT-AP NGSI-v2关键值示例  
这里有一个以JSON-LD格式作为key-values的DataServiceDCAT-AP的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### DataServiceDCAT-AP NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的DataServiceDCAT-AP的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### DataServiceDCAT-AP NGSI-LD关键值示例  
下面是一个以JSON-LD格式作为key-values的DataServiceDCAT-AP的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### DataServiceDCAT-AP NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的DataServiceDCAT-AP的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
