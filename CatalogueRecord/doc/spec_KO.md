<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: CatalogueRecord  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/CatalogueRecord/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이것은 DCAT-AP 표준 2.1.1에 따른 데이터셋에 속하는 카탈로그 레코드입니다.**  
version: 1.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 경우 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 위치하고 해당 지역에 속하는 구역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 구역이 위치하고 국가에 속하는 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 구역은 일부 국가에서 지방 정부가 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 사서함 번호. 예를 들어, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호. 예를 들어, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 도로명 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 속성을 식별하는 번호    
- `areaServed[string]`: 서비스 또는 제공되는 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `conformsTo[string]`: 이 속성은 데이터셋의 메타데이터가 준수하는 애플리케이션 프로필을 참조합니다.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `description[array]`: 이 속성에는 레코드에 대한 자유 형식의 설명이 포함됩니다. 설명의 병렬 언어 버전을 위해 이 속성을 반복할 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `id[*]`: 엔티티의 고유 식별자  - `issued[date-time]`: 이 속성에는 데이터셋의 설명이 카탈로그에 포함된 날짜가 포함됩니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: 이 속성은 데이터셋의 제목, 설명 등을 기술하는 텍스트 메타데이터에 사용된 언어를 참조합니다. 메타데이터가 여러 언어로 제공되는 경우 이 속성을 반복할 수 있습니다.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `location[*]`: 항목에 대한 Geojson 참조. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon일 수 있습니다.  - `modified[date-time]`: 이 속성에는 카탈로그 항목이 변경되거나 수정된 가장 최근의 날짜가 포함됩니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `primaryTopic[string]`: 이 속성은 카탈로그 레코드를 레코드에 기술된 데이터셋, 데이터 서비스 또는 카탈로그에 연결합니다.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `source[string]`: 이 속성은 데이터셋의 메타데이터를 생성하는 데 사용된 원래의 메타데이터를 참조합니다.  . Model: [http://www.w3.org/ns/dcat#CatalogRecord](http://www.w3.org/ns/dcat#CatalogRecord)- `status[string]`: 이 속성은 카탈로그에 있는 데이터셋 항목의 최신 개정 유형을 참조합니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[array]`: 이 속성에는 카탈로그 레코드에 부여된 이름이 포함됩니다. 이름의 병렬 언어 버전을 위해 이 속성을 반복할 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: NGSI 엔티티 유형. CatalogueRecord여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `modified`  - `primaryTopic`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
[DCAT-AP 버전 2.1.1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211)에서 발췌하였습니다.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬됨 (자세한 내용은 클릭)  
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
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    conformsTo:    
      description: This property refers to an Application Profile that the Dataset's metadata conforms to    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    description:    
      description: This property contains a free-text account of the record. This property can be repeated for parallel language versions of the description    
      items:    
        description: Every language description    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
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
        type: Relationship    
    issued:    
      description: This property contains the date on which the description of the Dataset was included in the Catalogue    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    language:    
      description: This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Dataset. This property can be repeated if the metadata is provided in multiple languages    
      items:    
        description: Every language tag    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    modified:    
      description: This property contains the most recent date on which the Catalogue entry was changed or modified    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    primaryTopic:    
      description: This property links the Catalogue Record to the Dataset, Data service or Catalog described in the record    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Dataset    
        type: Property    
    source:    
      description: This property refers to the original metadata that was used in creating metadata for the Dataset    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#CatalogRecord    
        type: Property    
    status:    
      description: This property refers to the type of the latest revision of a Dataset's entry in the Catalogue    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#Concept    
        type: Property    
    title:    
      description: This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name    
      items:    
        description: Every title.    
        type: string    
        x-ngsi:    
          model: http://www.w3.org/2000/01/rdf-schema#Literal    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    type:    
      description: NGSI entity type. It has to be CatalogueRecord    
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
  x-derived-from: https://github.com/SEMICeu/DCAT-AP/blob/master/releases/2.1.1/dcat-ap_2.1.1.pdf    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/CatalogueRecord/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/CatalogueRecord/schema.json    
  x-model-tags: INTERSTAT, WATERVERSE    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### CatalogueRecord NGSI-v2 키-값 예시  
다음은 키-값 형식의 JSON-LD 형식의 CatalogueRecord 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecord:id:KFTL:88140679",  
  "type": "CatalogueRecord",  
  "description": [  
    "Catalogue record of the solar system open data portal"  
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
  "modified": "2021-07-02T18:37:55Z",  
  "conformsTo": "DCAT Application profile for data portals in Europe",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "title": [  
    "Example of catalogue record",  
    "Ejemplo de registro de cat\u00e1logo"  
  ]  
}  
```  
</details>  
#### CatalogueRecord NGSI-v2 정규화된 예시  
다음은 정규화된 형식의 JSON-LD 형식의 CatalogueRecord 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
    "value": "European Union and beyond"  
  },  
  "primaryTopic": {  
    "type": "Text",  
    "value": "Public administration"  
  },  
  "language": {  
    "type": "StructuredValue",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "title": {  
    "type": "StructuredValue",  
    "value": [  
      "Example of catalogue record",  
      "Ejemplo de registro de cat\u00e1logo"  
    ]  
  }  
}  
```  
</details>  
#### CatalogueRecord NGSI-LD 키-값 예시  
다음은 키-값 형식의 JSON-LD 형식의 CatalogueRecord 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
  "description": [  
    "Catalogue record of the solar system open data portal"  
  ],  
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
#### CatalogueRecord NGSI-LD 정규화된 예시  
다음은 정규화된 형식의 JSON-LD 형식의 CatalogueRecord 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
    "type": "Property",  
    "value": "2021-07-02T18:37:55Z"  
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
    "type": "Property",  
    "value": "2021-07-02T18:37:55Z"  
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
크기 단위를 다루는 방법에 대한 답을 얻으려면 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하십시오.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
