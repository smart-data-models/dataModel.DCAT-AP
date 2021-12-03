エンティティカタログDCAT-AP  
=================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/CatalogueDCAT-AP/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明です。**DCAT-AP仕様に準拠したデータセットのカタログです。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `catalogue`: このプロパティは、このカタログの文脈で関心のある内容のカタログを参照している  - `creator`: 本プロパティは、カタログの作成に主に責任を持つエンティティを指す。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dataset`: このプロパティは、カタログと、カタログの一部であるデータセットをリンクします。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `hasPart`: このプロパティは、記述されたカタログの一部である関連カタログを参照する。  - `homepage`: 本プロパティは、「カタログ」のメインページとなる Web ページを指す。  - `id`: エンティティのユニークな識別子  - `isPartOf`: このプロパティは、記述されたカタログが物理的または論理的に含まれている関連カタログを指す。  - `language`: このプロパティは、カタログ中のデータセットのタイトルや説明などを記述したテキ ストのメタデータに使用される言語を示すものである。メタデータが複数の言語で提供されている場合は、このプロパティを繰り返すことができる。  - `licence`: このプロパティは、「カタログ」を使用または再利用するためのライセンスを示す。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `modificationDate`: このプロパティには、「カタログ」が変更された最新の日付が含まれる。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `publisher`: 本プロパティは、カタログを利用可能にする責任を負うエンティティ（組織）を指す。  - `record`: このプロパティは、カタログの一部である「カタログレコード」を参照する。  - `releaseDate`: このプロパティには、カタログの正式な発行（出版）日が含まれる。  - `rights`: 本プロパティは、カタログに関連する権利を指定する記述を指す。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `service`: このプロパティは、カタログに掲載されているサイトやエンドポイントを参照しています。  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `spatial_geographic`: このプロパティは、カタログでカバーされている地理的領域を指します。  - `themes`: 本プロパティは、カタログのデータセットを分類するための知識体系を示す。  - `title`: このプロパティには、カタログに与えられた名前が含まれる。このプロパティは、名前の並列言語バージョンのために繰り返すことができる  - `type`: カタログDCAT-APでなければならない    
必須項目  
- `dataset`  - `description`  - `id`  - `publisher`  - `title`  - `type`    
このデータモデルやDCAT-APの対象となる他のものは、彼らの使用のために適応されており、追加のコンテキストが含まれることが推奨されます。[https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld" ](https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld)  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CatalogueDCAT-AP:    
  description: 'Catalogue of datasets compliant with DCAT-AP specification.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties: &cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_properties_-_address_-_properties    
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
    catalogue:    
      description: 'This property refers to a catalog whose contents are of interest in the context of this catalog'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: dcat:catalog    
        type: Relationship    
    creator:    
      description: 'This property refers to the entity primarily responsible for producing the catalogue'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dataset:    
      description: 'This property links the Catalogue with a Dataset that is part of the Catalogue'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: dcat:Dataset    
        type: Relationship    
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
    hasPart:    
      description: 'This property refers to a related Catalogue that is part of the described Catalogue'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    homepage:    
      description: 'This property refers to a web page that acts as the main page for the Catalogue.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: foaf:homepage    
        type: Property    
    id:    
      anyOf: &cataloguedcat-ap_-_properties_-_owner_-_items_-_anyof    
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
    isPartOf:    
      description: 'This property refers to a related Catalogue in which the described Catalogue is physically or logically included.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    language:    
      description: 'This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. This property can be repeated if the  metadata is provided in multiple languages.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dct:language    
        type: Property    
    licence:    
      description: 'This property refers to the licence under which the Catalogue can be used or reused.'    
      type: string    
      x-ngsi:    
        model: dct:license    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_properties_-_location_-_oneof    
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
      description: 'This property contains the most recent date on which the Catalogue was modified.'    
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
        anyOf: *cataloguedcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    publisher:    
      description: 'This property refers to an entity (organisation) responsible for making the Catalogue available'    
      type: string    
      x-ngsi:    
        model: dct:publisher    
        type: Property    
    record:    
      description: 'This property refers to a Catalogue Record that is part of the Catalogue'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    releaseDate:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Catalogue.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    rights:    
      description: 'This property refers to a statement that specifies rights associated with the Catalogue.'    
      type: string    
      x-ngsi:    
        model: dct:rights    
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
    service:    
      description: 'This property refers to a site or end-point that is listed in the catalog'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dcat:DataService    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    spatial_geographic:    
      description: 'This property refers to a geographical area covered by the Catalogue'    
      items:    
        properties:    
          address:    
            description: 'Property. The mailing address. Model:''https://schema.org/address'''    
            properties: *cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_properties_-_address_-_properties    
            type: object    
          areaServed:    
            description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
            type: string    
          location:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_properties_-_location_-_oneof    
        type: object    
      type: array    
      x-ngsi:    
        model: dct:spatial    
        type: Geoproperty    
    themes:    
      description: 'This property refers to a knowledge organization system used to classify the Catalogue''s Datasets.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dcat:themeTaxonomy    
        type: Property    
    title:    
      description: 'This property contains a name given to the Catalogue. This property can be repeated for parallel language versions of the name'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: rdfs:Literal    
        type: Property    
    type:    
      description: 'It has to be CatalogueDCAT-AP'    
      enum:    
        - CatalogueDCAT-AP    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - dataset    
    - description    
    - publisher    
    - title    
  type: object    
```  
</details>    
## ペイロードの例  
#### カタログDCAT-AP NGSI-v2 キーバリューの例  
JSON-LD形式でkey-valuesとしてCatalogDCAT-APを作成した例です。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
  "dateCreated": "1980-03-03T10:01:24Z",  
  "dateModified": "1987-12-04T10:44:40Z",  
  "source": "",  
  "name": "Catalogue",  
  "alternateName": "",  
  "description": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size.",  
  "dataProvider": "european open data portal",  
  "owner": [  
    "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Catalogue:ILBA:60770941"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -83.400987,  
      0.152532  
    ]  
  },  
  "address": {  
    "streetAddress": "2 Rue Mercier",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "addressCountry": "Luxembourg",  
    "postalCode": "2985 ",  
    "postOfficeBoxNumber": "",  
    "areaServed": "European Union"  
  },  
  "dataset": [  
    "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
  ],  
  "publisher": "Spanish data portal",  
  "title": [  
    "title first",  
    "Secondary title."  
  ],  
  "homepage": "ngsi-ld:Catalogue:homepage:ZFAW:13633782",  
  "language": [  
    "ES",  
    "DE"  
  ],  
  "licence": "Creative Commons 3.0 International",  
  "releaseDate": "2004-08-22T22:32:47Z",  
  "spatial_geographic": [  
    {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  ],  
  "themes": [  
    "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
    "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
  ],  
  "modificationDate": "1982-09-02T03:16:28Z",  
  "hasPart": [  
    "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
  ],  
  "isPartOf": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287",  
  "record": [  
    "Catalogue.items.HLGA.73285516",  
    "Catalogue.items.IHOB.85266800"  
  ],  
  "rights": "",  
  "catalogue": [  
    "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
    "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
  ],  
  "creator": "Role fact sport shoulder blue direction probably order."  
}  
```  
#### カタログDCAT-AP NGSI-v2 正規化例  
正規化されたJSON-LD形式のCatalogDCAT-APの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1980-03-03T10:01:24Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1987-12-04T10:44:40Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Catalogue"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "european open data portal"  
  },  
  "owner": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ILBA:60770941"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -83.400987,  
        0.152532  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": [  
        "2 Rue Mercier"  
      ],  
      "addressLocality": [  
        "Luxembourg"  
      ],  
      "addressRegion": [  
        "Luxembourg"  
      ],  
      "addressCountry": [  
        "Luxembourg"  
      ],  
      "postalCode": [  
        "2985 "  
      ],  
      "postOfficeBoxNumber": [  
        ""  
      ],  
      "areaServed": [  
        "European Union"  
      ]  
    }  
  },  
  "dataset": {  
    "type": "object",  
    "value": "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "spanish open data portal"  
  },  
  "title": {  
    "type": "Array",  
    "value": [  
      [  
        "Hair commercial free civil. Figure American film despite few. Box watch cold act mean thank music people. Third fill us."  
      ],  
      [  
        "Technology life low standard second."  
      ]  
    ]  
  },  
  "homepage": {  
    "type": "string",  
    "value": "urn:ngsi-ld:Catalogue:homepage:ZFAW:13633782"  
  },  
  "language": {  
    "type": "Array",  
    "value": [  
      [  
        "Town size computer way. Since challenge phone state listen south low."  
      ],  
      [  
        "Eight once single. Build every kid."  
      ]  
    ]  
  },  
  "licence": {  
    "type": "Property",  
    "value": "Improve social simply court week debate bad. Structure ago cup head point. Above much can own course."  
  },  
  "releaseDate": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
  },  
  "spatial_geographic": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  },  
  "themes": {  
    "type": "Array",  
    "value": [  
      [  
        "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member."  
      ],  
      [  
        "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
      ]  
    ]  
  },  
  "modificationDate": {  
    "type": "DateTime",  
    "value": "1982-09-02T03:16:28Z"  
  },  
  "hasPart": {  
    "type": "object",  
    "value": "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
  },  
  "isPartOf": {  
    "type": "object",  
    "value": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287"  
  },  
  "record": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:HLGA:73285516",  
      "urn:ngsi-ld:Catalogue:items:IHOB:85266800"  
    ]  
  },  
  "rights": {  
    "type": "Property",  
    "value": "Open source"  
  },  
  "catalogue": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "Text",  
    "value": "Role fact sport shoulder blue direction probably order."  
  }  
}  
```  
#### カタログDCAT-AP NGSI-LDのキーバリューの例  
ここではCatalogDCAT-APをkey-valuesとしてJSON-LD形式で記述した例を紹介します。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
  "dateCreated": "1980-03-03T10:01:24Z",  
  "dateModified": "1987-12-04T10:44:40Z",  
  "source": "",  
  "name": "Catalogue",  
  "alternateName": "",  
  "description": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size.",  
  "dataProvider": "european open data portal",  
  "owner": [  
    "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Catalogue:ILBA:60770941"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -83.400987,  
      0.152532  
    ]  
  },  
  "address": {  
    "streetAddress": "2 Rue Mercier",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "addressCountry": "Luxembourg",  
    "postalCode": "2985 ",  
    "postOfficeBoxNumber": "",  
    "areaServed": "European Union"  
  },  
  "dataset": [  
    "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
  ],  
  "publisher": "Spanish data portal",  
  "title": [  
    "title first",  
    "Secondary title."  
  ],  
  "homepage": "ngsi-ld:Catalogue:homepage:ZFAW:13633782",  
  "language": [  
    "ES",  
    "DE"  
  ],  
  "licence": "Creative Commons 3.0 International",  
  "releaseDate": "2004-08-22T22:32:47Z",  
  "spatial_geographic": [  
    {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  ],  
  "themes": [  
    "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
    "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
  ],  
  "modificationDate": "1982-09-02T03:16:28Z",  
  "hasPart": [  
    "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
  ],  
  "isPartOf": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287",  
  "record": [  
    "Catalogue.items.HLGA.73285516",  
    "Catalogue.items.IHOB.85266800"  
  ],  
  "rights": "",  
  "catalogue": [  
    "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
    "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
  ],  
  "creator": "Role fact sport shoulder blue direction probably order.",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld"  
  ]  
}  
```  
#### カタログDCAT-AP NGSI-LD 正規化例  
正規化されたJSON-LD形式のCatalogDCAT-APの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-03T10:01:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-04T10:44:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Catalogue"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "European open data portal"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ILBA:60770941"  
    ]  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -83.400987,  
        0.152532  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "2 Rue Mercier",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "2985 ",  
      "postOfficeBoxNumber": "",  
      "areaServed": "European Union"  
    }  
  },  
  "dataset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ]  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Spain open data portal"  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      [  
        "New catalogue"  
      ],  
      [  
        "Nuevo catalogo"  
      ]  
    ]  
  },  
  "homepage": {  
    "type": "Property",  
    "value": "Catalogue:homepage:ZFAW:13633782"  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      [  
        "ES"  
      ],  
      [  
        "DE"  
      ]  
    ]  
  },  
  "licence": {  
    "type": "Property",  
    "value": [  
      "Creative Commons 3.0 International"  
    ]  
  },  
  "releaseDate": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
  },  
  "spatial_geographic": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  },  
  "themes": {  
    "type": "Property",  
    "value": [  
      [  
        "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member."  
      ],  
      [  
        "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
      ]  
    ]  
  },  
  "modificationDate": {  
    "type": "DateTime",  
    "value": "1982-09-02T03:16:28Z"  
  },  
  "hasPart": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
    ]  
  },  
  "isPartOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287"  
  },  
  "record": {  
    "type": "Property",  
    "value": [  
      "Catalogue.items.HLGA.73285516",  
      "Catalogue.items.IHOB.85266800"  
    ]  
  },  
  "rights": {  
    "type": "Property",  
    "value": ""  
  },  
  "catalogue": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "Property",  
    "value": ""  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。