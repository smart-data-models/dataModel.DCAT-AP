<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 에이전트  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Agent/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **DCAT-AP 2.1.1 사양을 충족하는 에이전트 스키마**.  
버전: 1.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `Type[string]`: 이 속성은 카탈로그 또는 데이터셋을 사용할 수 있게 하는 에이전트 유형을 나타냅니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[array]`: 이 속성에는 상담원의 이름이 포함됩니다.  이 속성은 다른 버전의 이름(예: 다른 언어로 된 이름)에 대해 반복할 수 있습니다.  . Model: [dct:description](dct:description)- `type[string]`: NGSI 엔티티 유형. 에이전트여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
DCAT-AP 버전 2.1.1](https://codeload.github.com/SEMICeu/DCAT-AP/zip/refs/tags/v2.1.1)에서 수정되었습니다. DCAT 2.1.1의 원래 유형 속성이 NGSI-LD와 함께 사용할 수 있도록 유형으로 이름이 변경되었습니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Agent:    
  description: Agent Schema meeting DCAT-AP 2.1.1 specification    
  properties:    
    Type:    
      description: This property refers to a type of the agent that makes the Catalogue or Dataset available    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
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
    name:    
      description: This property contains a name of the agent.  This property can be repeated for different  versions of the name (e.g. the name in  different languages)    
      items:    
        description: Every name in different languages    
        minItems: 1    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: dct:description    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Agent    
      enum:    
        - Agent    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Agent/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Agent/schema.json    
  x-model-tags: ""    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 에이전트 NGSI-v2 키 값 예제  
다음은 JSON-LD 형식의 에이전트를 키-값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:id:ZLHO:07918336",  
  "type": "Agent",  
  "name": "Agent 10.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.934074,  
      -149.532943  
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
  "name": [  
    "Agent 10",  
    "Agente 10"  
  ],  
  "Type": "EU Publications office"  
}  
```  
</details>  
#### 에이전트 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 에이전트 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:id:ZLHO:07918336",  
  "type": "Agent",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        12.934074,  
        -149.532943  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
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
  "name": {  
    "type": "array",  
    "value": [  
      "Agent 10",  
      "Agente 10"  
    ]  
  },  
  "Type": {  
    "type": "Text",  
    "value": "EU Publications office"  
  }  
}  
```  
</details>  
#### 에이전트 NGSI-LD 키 값 예제  
다음은 JSON-LD 형식의 에이전트를 키-값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:id:ZLHO:07918336",  
    "type": "Agent",  
    "address": {  
        "streetAddress": "2 Rue Mercier",  
        "addressLocality": "Luxembourg",  
        "addressRegion": "Luxembourg",  
        "addressCountry": "Luxembourg",  
        "postalCode": "2985 ",  
        "postOfficeBoxNumber": "",  
        "areaServed": "European Union"  
    },  
    "name": [  
        "Agent 10",  
        "Agente 10"  
    ],  
    "Type": "EU Publications office",  
    "description": "organization the Agent 10 belongs to.",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            12.934074,  
            -149.532943  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 에이전트 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 에이전트 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:id:ZLHO:07918336",  
    "type": "Agent",  
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
    "name": {  
        "type": "Property",  
        "value": [  
            "Agent 10",  
            "Agente 10"  
        ]  
    },  
    "Type": {  
        "type": "Property",  
        "value": "EU Publications office"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                12.934074,  
                -149.532943  
            ]  
        }  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
