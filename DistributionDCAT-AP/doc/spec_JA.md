エンティティディストリビューションDCAT-AP  
========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DistributionDCAT-AP/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明。**このディストリビューションは、DCAT-AP規格2.0.1に準拠したデータセットに属するものです。  
バージョン: 0.0.1  

## プロパティのリスト  

- `accessService`: このプロパティは、データセットの配布にアクセスするためのデータサービスを指します。  - `accessUrl`: このプロパティには、データセットの配布物にアクセスするための URL が含まれます。アクセスURLのリソースには、データセットの入手方法に関する情報が含まれている場合があります。  - `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `availability`: 本プロパティは、本データセットの配信をいつまで維持するかを示す。  - `byteSize`: このプロパティは、Distribution のサイズをバイト単位で表したものである。  - `checksum`: このプロパティは、ディストリビューションのコンテンツが変更されていないことを確認するために使用できるメカニズムを提供します。チェックサムは、downloadURLに関連しています。  - `compressionFormat`: 本プロパティは、ダウンロードするファイルのサイズを小さくするために、データを圧縮して含 むファイルの形式を示す。IANAが管理するメディアタイプの公式レジスタに定義されているメディアタイプを使用して表現すべきである（SHOULD）。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `documentation`: このプロパティは、このDistributionに関するページやドキュメントを指します。  - `downloadURL`: このプロパティは、指定されたフォーマットのダウンロード可能なファイルへのダイレクトリンクであるURLを含みます。  - `format`: 本プロパティは、Distribution のファイル形式を示す。  - `hasPolicy`: このプロパティは、ODRL ボキャブラリーを使用している場合、配布に関連する権利を表現するポリシーを指します。  - `id`: エンティティのユニークな識別子  - `language`: 本プロパティは、本ディストリビューションで使用されている言語を示す。メタデータが複数の言語で提供されている場合は、このプロパティを繰り返すことができる。  - `license`: このプロパティは、データセットの配布にアクセスするためのデータサービスを指します。  - `linkedSchemas`: 本プロパティは、記述された Distribution が準拠している確立されたスキーマを指す。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `mediaType`: 本プロパティは、IANA が管理するメディアタイプの公式登録簿で定義されている Distribution のメディアタイプを指す。  - `modifiedDate`: このプロパティには、Distribution の変更または修正が行われた最新の日付が含まれる。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `packagingFormat`: 本プロパティは、関連するファイルをまとめてダウンロードするために、1 つ以上のデー タファイルをまとめたファイルの形式を示すものである。IANAが管理するメディアタイプの公式登録簿で定義されているメディアタイプを用いて表現すべきである（SHOULD）。  - `releaseDate`: 本プロパティには、Distribution の正式な発行日（公開日など）が含まれる。  - `rights`: 本プロパティは、"Distribution "に関連する権利を指定する記述を指す。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `spatialResolution`: このプロパティは、データセットの分布において解決可能な最小の空間分離を示すもので、単位はメートルです。  - `status`: このプロパティは、ディストリビューションの成熟度を示す。Completed」、「Deprecated」、「Under Development」、「Withdrawn」のいずれかの値を取らなければなりません。  - `temporalResolution`: このプロパティは、データセットの配布で解決可能な最小の時間帯を示す。  - `title`: このプロパティには、Distribution に付けられた名前が含まれる。このプロパティは、説明の並列言語バージョンのために繰り返すことができる。    
必須項目  
- `id`  - `type`    
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf).  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DistributionDCAT-AP:    
  description: 'this is a distribution belonging ot a dataset according to the DCAT-AP standard 2.0.1'    
  properties:    
    accessService:    
      description: 'This property refers to a data service that gives access to the distribution of the dataset'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    accessUrl:    
      description: 'This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset.'    
      items:    
        minitems: 1    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    availability:    
      description: 'This property indicates how long it is planned to keep the Distribution of the Dataset available.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    byteSize:    
      description: 'This property contains the size of a Distribution in bytes.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    checksum:    
      description: 'This property provides a mechanism that can be used to verify that the contents of a distribution have not changed. The checksum is related to the downloadURL.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    compressionFormat:    
      description: 'This property refers to the format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    documentation:    
      description: 'This property refers to a page or document about this Distribution.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    downloadURL:    
      description: 'This property contains a URL that is a directlink to a downloadable file in a givenformat.'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    format:    
      description: 'This property refers to the file format of the Distribution.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hasPolicy:    
      description: 'This property refers to the policy expressing the rights associated with the distribution if using the ODRL vocabulary'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &distributiondcat-ap_-_properties_-_owner_-_items_-_anyof    
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
      description: 'This property refers to a language used in the Distribution. This property can be repeated if the metadata is provided in multiple languages.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    license:    
      description: 'This property refers to a data service that gives access to the distribution of the dataset'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    linkedSchemas:    
      description: 'This property refers to an established schema to which the described Distribution conforms.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    mediaType:    
      description: 'This property refers to the media type of the Distribution as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modifiedDate:    
      description: 'This property contains the most recent date on which the Distribution was changed or modified.'    
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
        anyOf: *distributiondcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    packagingFormat:    
      description: 'This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    releaseDate:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Distribution.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    rights:    
      description: 'This property refers to a statement that specifies rights associated with the Distribution.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    spatialResolution:    
      description: 'This property refers to the minimum spatial separation resolvable in a dataset distribution, measured in meters'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
        units: Meters    
    status:    
      description: 'This property refers to the maturity of the Distribution. It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn'    
      enum:    
        - Completed    
        - Deprecated    
        - 'Under Development'    
        - Withdrawn    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    temporalResolution:    
      description: 'This property refers to the minimum time period resolvable in the dataset distribution'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    title:    
      description: 'This property contains a name given to the Distribution. This property can be repeated for parallel language versions of the description.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### DistributionDCAT-AP NGSI-v2 key-valuesの例。  
DistributionDCAT-APをkey-valuesとしてJSON-LD形式で出力した例です。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "type": "DistributionDCAT-AP",  
  "accessService": [  
    ""  
  ],  
  "accessUrl": [  
    ""  
  ],  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "24004",  
    "streetAddress": "Luxembourg platz 2"  
  },  
  "alternateName": "csv",  
  "areaServed": "European Union.",  
  "availability": "yes",  
  "byteSize": 43503,  
  "checksum": "H3FR.",  
  "compressionFormat": "",  
  "dataProvider": "Meloda.org",  
  "dateCreated": "1993-08-16T05:35:56Z",  
  "dateModified": "1970-07-14T10:48:19Z",  
  "description": "Distribution of open data portals in csv",  
  "documentation": [],  
  "downloadURL": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:HVWX:12201868",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:ICPI:96947751"  
  ],  
  "format": " text/csv",  
  "hasPolicy": "Open data policy.",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "license": "CC-BY",  
  "linkedSchemas": [],  
  "location": {  
    "coordinates": [  
      -67.057831,  
      67.968509  
    ],  
    "type": "Point"  
  },  
  "mediaType": "",  
  "modifiedDate": "1986-03-28T19:56:43Z",  
  "name": "csv portals distribution",  
  "owner": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
  ],  
  "packagingFormat": "zip",  
  "releaseDate": "1997-05-06T05:04:10Z",  
  "rights": "copyleft",  
  "seeAlso": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
  ],  
  "source": "",  
  "spatialResolution": [  
    0.5,  
    0.5  
  ],  
  "status": "Withdrawn",  
  "temporalResolution": [  
    2,  
    10  
  ],  
  "title": [  
    "Dataset base"  
  ]  
}  
```  
#### ディストリビューションDCAT-AP NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のDistributionDCAT-APの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1993-08-16T05:35:56Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1970-07-14T10:48:19Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "csv portals distribution"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "csv"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Distribution of open data portals in csv"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Meloda.org"  
  },  
  "owner": {  
    "type": "Text",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -67.057831,  
        67.968509  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Luxembourg platz 2",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "24004",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "European Union."  
  },  
  "accessUrl": {  
    "type": "array",  
    "value": [  
      ""  
    ]  
  },  
  "availability": {  
    "type": "Text",  
    "value": "yes"  
  },  
  "format": {  
    "type": "Text",  
    "value": " text/csv"  
  },  
  "license": {  
    "type": "Text",  
    "value": "CC-BY"  
  },  
  "accessService": {  
    "type": "array",  
    "value": [  
      ""  
    ]  
  },  
  "byteSize": {  
    "type": "array",  
    "value": 43503  
  },  
  "checksum": {  
    "type": "Text",  
    "value": "H3FR."  
  },  
  "compressionFormat": {  
    "type": "Text",  
    "value": ""  
  },  
  "documentation": {  
    "type": "array",  
    "value": [  
    ]  
  },  
  "downloadURL": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HVWX:12201868",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:ICPI:96947751"  
    ]  
  },  
  "hasPolicy": {  
    "type": "Text",  
    "value": "Open data policy."  
  },  
  "language": {  
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "linkedSchemas": {  
    "type": "array",  
    "value": [  
    ]  
  },  
  "mediaType": {  
    "type": "Text",  
    "value": ""  
  },  
  "packagingFormat": {  
    "type": "Text",  
    "value": "zip"  
  },  
  "releaseDate": {  
    "type": "DateTime",  
    "value": "1997-05-06T05:04:10Z"  
  },  
  "rights": {  
    "type": "Text",  
    "value": "copyleft"  
  },  
  "spatialResolution": {  
    "type": "array",  
    "value": [  
      0.5,  
      0.5  
    ]  
  },  
  "status": {  
    "type": "Text",  
    "value": "Withdrawn"  
  },  
  "temporalResolution": {  
    "type": "array",  
    "value": [  
      2,  
      10  
    ]  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Dataset base"  
    ]  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "1986-03-28T19:56:43Z"  
  }  
}  
```  
#### ディストリビューションDCAT-AP NGSI-LDのキーバリューの例  
DistributionDCAT-APをkey-valuesとしてJSON-LD形式で出力した例です。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "type": "DistributionDCAT-AP",  
  "accessService": [  
    ""  
  ],  
  "accessUrl": [  
    ""  
  ],  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "24004",  
    "streetAddress": "Luxembourg platz 2"  
  },  
  "alternateName": "csv",  
  "areaServed": "European Union.",  
  "availability": "yes",  
  "byteSize": 43503,  
  "checksum": "H3FR.",  
  "compressionFormat": "",  
  "dataProvider": "Meloda.org",  
  "dateCreated": "1993-08-16T05:35:56Z",  
  "dateModified": "1970-07-14T10:48:19Z",  
  "description": "Distribution of open data portals in csv",  
  "documentation": [],  
  "downloadURL": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:HVWX:12201868",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:ICPI:96947751"  
  ],  
  "format": " text/csv",  
  "hasPolicy": "Open data policy.",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "license": "CC-BY",  
  "linkedSchemas": [],  
  "location": {  
    "coordinates": [  
      -67.057831,  
      67.968509  
    ],  
    "type": "Point"  
  },  
  "mediaType": "",  
  "modifiedDate": "1986-03-28T19:56:43Z",  
  "name": "csv portals distribution",  
  "owner": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
  ],  
  "packagingFormat": "zip",  
  "releaseDate": "1997-05-06T05:04:10Z",  
  "rights": "copyleft",  
  "seeAlso": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
  ],  
  "source": "",  
  "spatialResolution": [  
    0.5,  
    0.5  
  ],  
  "status": "Withdrawn",  
  "temporalResolution": [  
    2,  
    10  
  ],  
  "title": [  
    "Dataset base"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### ディストリビューションDCAT-AP NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のDistributionDCAT-APの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1993-08-16T05:35:56Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-07-14T10:48:19Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "csv portals distribution"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "csv"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Distribution of open data portals in csv"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Meloda.org"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -67.057831,  
        67.968509  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Luxembourg platz 2",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "24004",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "European Union."  
  },  
  "accessUrl": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "availability": {  
    "type": "Property",  
    "value": "yes"  
  },  
  "format": {  
    "type": "Property",  
    "value": " text/csv"  
  },  
  "license": {  
    "type": "Property",  
    "value": "CC-BY"  
  },  
  "accessService": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "byteSize": {  
    "type": "Property",  
    "value": 43503  
  },  
  "checksum": {  
    "type": "Property",  
    "value": "H3FR."  
  },  
  "compressionFormat": {  
    "type": "Property",  
    "value": ""  
  },  
  "documentation": {  
    "type": "Property",  
    "value": [  
    ]  
  },  
  "downloadURL": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HVWX:12201868",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:ICPI:96947751"  
    ]  
  },  
  "hasPolicy": {  
    "type": "Property",  
    "value": "Open data policy."  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "linkedSchemas": {  
    "type": "Property",  
    "value": [  
    ]  
  },  
  "mediaType": {  
    "type": "Property",  
    "value": ""  
  },  
  "packagingFormat": {  
    "type": "Property",  
    "value": "zip"  
  },  
  "releaseDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1997-05-06T05:04:10Z"  
    }  
  },  
  "rights": {  
    "type": "Property",  
    "value": "copyleft"  
  },  
  "spatialResolution": {  
    "type": "Property",  
    "value": [  
      0.5,  
      0.5  
    ]  
  },  
  "status": {  
    "type": "Property",  
    "value": "Withdrawn"  
  },  
  "temporalResolution": {  
    "type": "Property",  
    "value": [  
      2,  
      10  
    ]  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "Dataset base"  
    ]  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1986-03-28T19:56:43Z"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
