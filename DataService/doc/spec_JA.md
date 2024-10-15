<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティデータサービス    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DataService/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**データサービスは DCAT-AP 2.1.1 仕様に準拠しているが、追加プロパティで拡張され、NGSI 標準と互換性がある。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `accessRights[string]`: このプロパティには、プライバシー、セキュリティ、またはその他のポリシーに基づくアクセスまたは制限に関する情報を含めることができる。  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[array]`: このプロパティには、データサービスに関するフリーテキストの説明が含まれる。このプロパティは、並列言語版の説明のために繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `endPointDescription[array]`: このプロパティには、エンドポイントを介して利用可能なサービスの説明（操作、パラメータなど）が含まれる。dct:conformsToはエンドポイントが実装する一般的な標準や仕様を示すために使用されます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `endPointURL[array]`: サービスのルート・ロケーションまたはプライマリ・エンドポイント（IRI）  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `id[*]`: エンティティの一意識別子  - `license[string]`: このプロパティには、データサービスが利用可能なライセンスが含まれます。  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `servesDataset[array]`: このプロパティは、このデータサービスが配布できるデータのコレクションを指す。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `title[array]`: このプロパティには、データサービスに与えられた名前が含まれる。このプロパティは、並列言語版の名前のために繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: NGSIエンティティタイプ。DataServiceでなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `endPointURL`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
DCAT-APバージョン2.1.1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211)からの引用。いくつかのプロパティは、他の既存のプロパティとの衝突を防ぐために名前が変更されている。さらに、NGSI標準や他のデータモデルとの互換性を維持するために、他のプロパティが追加されている。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
より幅広い使い方ができるように、いくつかのプロパティが追加されました。contactPoint、assetProvider、configurationなどです。    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### DataService NGSI-v2 キー値の例    
JSON-LD形式のDataServiceのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### DataService NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のDataServiceの例である。これは、NGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
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
#### DataService NGSI-LD キー値の例    
JSON-LD形式のDataServiceのkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### DataService NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のDataServiceの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
