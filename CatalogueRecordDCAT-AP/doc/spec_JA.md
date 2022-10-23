<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティカタログレコードDCAT-AP  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/CatalogueRecordDCAT-AP/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**DCAT-AP規格2.0.1に準拠したデータセットに属するカタログレコードである**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `applicationProfile[string]`: このプロパティは、データセットのメタデータが準拠するアプリケーションプロファイルを参照する。  . Model: [dct:conformsTo](dct:conformsTo)- `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `changeType[string]`: このプロパティは、カタログのデータセットエントリの最新リビジョンのタイプを参照します。  . Model: [adms:status](adms:status)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `language[array]`: このプロパティは、データセットのタイトルや説明などを記述するテキストメタデータで使用される言語を参照する。このプロパティは、メタデータが複数の言語で提供される場合、繰り返すことができる。  . Model: [dct:language](dct:language)- `listingDate[string]`: このプロパティは、データセットの記述がカタログに含まれるようになった日付を含む。  . Model: [dct:issued](dct:issued)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `modificationDate[string]`: このプロパティは、カタログエントリが変更または修正された最新の日付を含んでいます。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `primaryTopic[string]`: このプロパティは、カタログレコードを、そのレコードに記述されたデータセット、データサービス、またはカタログにリンクします。  . Model: [foaf:primaryTopic](foaf:primaryTopic)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `sourceMetadata[string]`: このプロパティは、データセットのメタデータを作成する際に使用されたオリジナルのメタデータを参照する。  . Model: [dct:source](dct:source)- `title[array]`: このプロパティは、カタログレコードに付けられた名前を含む。このプロパティは、名前の並行言語版のために繰り返すことができる。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSIエンティティタイプ。これはCatalogueRecordDCAT-APでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `modificationDate`  - `primaryTopic`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CatalogueRecordDCAT-AP:    
  description: 'This is a Catalogue Record belonging to a dataset according to the DCAT-AP standard 2.0.1'    
  properties:    
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
    applicationProfile:    
      description: 'This property refers to an Application Profile that the Dataset’s metadata conforms to'    
      type: string    
      x-ngsi:    
        model: dct:conformsTo    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    changeType:    
      description: 'This property refers to the type of the latest revision of a Dataset''s entry in the Catalogue.'    
      type: string    
      x-ngsi:    
        model: adms:status    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
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
    id:    
      anyOf: &cataloguerecorddcat-ap_-_properties_-_owner_-_items_-_anyof    
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
    language:    
      description: 'This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Dataset. This property can be repeated if the metadata is provided in multiple languages'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dct:language    
        type: Property    
    listingDate:    
      description: 'This property contains the date on which the description of the Dataset was included in the Catalogue.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: dct:issued    
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
    modificationDate:    
      description: 'This property contains the most recent date on which the Catalogue entry was changed or modified..'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *cataloguerecorddcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    primaryTopic:    
      description: 'This property links the Catalogue Record to the Dataset, Data service or Catalog described in the record.'    
      type: string    
      x-ngsi:    
        model: foaf:primaryTopic    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    sourceMetadata:    
      description: 'This property refers to the original metadata that was used in creating metadata for the Dataset.'    
      type: string    
      x-ngsi:    
        model: dct:source    
        type: Property    
    title:    
      description: 'This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be CatalogueRecordDCAT-AP'    
      enum:    
        - CatalogueRecordDCAT-AP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - primaryTopic    
    - modificationDate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/CatalogueRecordDCAT-AP/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT_AP/CatalogueRecordDCAT-AP/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### CatalogueRecordDCAT-AP NGSI-v2 key-value 例  
以下は、CatalogueRecordDCAT-APをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": "2020-11-02T21:25:54Z",  
  "dateModified": "2021-07-02T18:37:55Z",  
  "source": "",  
  "name": "",  
  "alternateName": "",  
  "description": "Catalogue record of the solar system open data portal",  
  "dataProvider": "european open data portal",  
  "owner": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
  ],  
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
  "modificationDate": "2021-07-02T18:37:55Z",  
  "applicationProfile": "DCAT Application profile for data portals in Europe",  
  "changeType": "First version",  
  "listingDate": "2021-07-02T18:37:55Z",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "sourceMetadata": "",  
  "title": [  
    "Example of catalogue record",  
    "Ejemplo de registro de catálogo"  
  ]  
}  
```  
</details>  
#### CatalogueRecordDCAT-AP NGSI-v2 正規化例  
以下は、CatalogueRecordDCAT-APをJSON-LD形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-11-02T21:25:54Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
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
    "value": "Catalogue record of the solar system open data portal"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "european open data portal"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
    ]  
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
  "modificationDate": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "applicationProfile": {  
    "type": "Text",  
    "value": "DCAT Application profile for data portals in Europe"  
  },  
  "changeType": {  
    "type": "Text",  
    "value": "First version"  
  },  
  "listingDate": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "language": {  
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "sourceMetadata": {  
    "type": "Text",  
    "value": ""  
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
#### CatalogueRecordDCAT-AP NGSI-LD key-value 例  
以下は、CatalogueRecordDCAT-APをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
    "type": "CatalogueRecordDCAT-AP",  
    "address": {  
        "streetAddress": "2, rue Mercier",  
        "addressLocality": "Luxembourg",  
        "addressRegion": "Luxembourg",  
        "addressCountry": "Luxembourg",  
        "postalCode": "2985",  
        "postOfficeBoxNumber": ""  
    },  
    "alternateName": "",  
    "applicationProfile": "DCAT Application profile for data portals in Europe",  
    "areaServed": "European Union and beyond",  
    "changeType": "First version",  
    "dataProvider": "european open data portal",  
    "dateCreated": "2020-11-02T21:25:54Z",  
    "dateModified": "2021-07-02T18:37:55Z",  
    "description": "Catalogue record of the solar system open data portal",  
    "language": [  
        "EN",  
        "ES"  
    ],  
    "listingDate": "2021-07-02T18:37:55Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            36.633152,  
            -85.183315  
        ]  
    },  
    "modificationDate": "2021-07-02T18:37:55Z",  
    "name": "",  
    "owner": [  
        "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
        "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
    ],  
    "primaryTopic": "Public administration",  
    "seeAlso": [  
        "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
        "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
    ],  
    "source": "",  
    "sourceMetadata": "",  
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
#### CatalogueRecordDCAT-AP NGSI-LD 正規化例  
以下は、CatalogueRecordDCAT-APをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
    "type": "CatalogueRecordDCAT-AP",  
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
    "applicationProfile": {  
        "type": "Property",  
        "value": "DCAT Application profile for data portals in Europe"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "European Union and beyond"  
    },  
    "changeType": {  
        "type": "Property",  
        "value": "First version"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "european open data portal"  
    },  
    "dateCreated": {  
        "type": {  
            "@type": "Property",  
            "@value": "2020-11-02T21:25:54Z"  
        }  
    },  
    "dateModified": {  
        "type": {  
            "@type": "Property",  
            "@value": "2021-07-02T18:37:55Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Catalogue record of the solar system open data portal"  
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
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                36.633152,  
                -85.183315  
            ]  
        }  
    },  
    "modificationDate": {  
        "type": {  
            "@type": "Property",  
            "@value": "2021-07-02T18:37:55Z"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": ""  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
            "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
        ]  
    },  
    "primaryTopic": {  
        "type": "Property",  
        "value": "Public administration"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
            "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "sourceMetadata": {  
        "type": "Property",  
        "value": ""  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
