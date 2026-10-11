<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: DataServiceRun  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataServiceRun/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전역 설명: **데이터 서비스(예: DataServiceDCAT-AP)의 특정 실행(run)에 대한 표현입니다.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 경우 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>  
- `alternateName[string]`: 이 항목의 대체 이름  - `configuration[array]`: 서비스의 기술적 구성입니다. 이 속성은 서비스 구성(출력 형식, URL 등)과 관련이 있지만 현재 이 모델에서 정의된 표준 속성으로 다루지 않는 매개변수를 캡처하는 속성 및 값의 배열로 의도되었습니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: 조화된 데이터 엔티티의 제공자를 식별하는 문자열  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 대개 스토리지 플랫폼에 의해 할당됩니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프. 이것은 일반적으로 저장 플랫폼에 의해 할당됩니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자(들)의 고유 ID를 참조하는 JSON 인코딩 문자열 시퀀스를 포함하는 목록  - `resultEntities[array]`: 서비스 실행 내에서 생성된 NGSI-LD 엔티티를 가리키는 참조 목록입니다.  - `resultExternal[array]`: 서비스 실행 내에서 생성된 외부 결과로 향하는 URI 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URI 목록  - `service[*]`: 해당 데이터 서비스를 나타내는 NGSI-LD 엔티티(예: DataServiceDCAT-AP 유형)를 가리키는 참조입니다.  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자열. 소스 제공자의 정규화된 도메인 이름 또는 소스 객체의 URL을 사용하는 것이 좋습니다.  - `sourceEntities[array]`: 서비스 실행 내에서 소스 역할을 한 NGSI-LD 엔티티를 가리키는 참조 목록입니다.  - `sourceExternal[array]`: 서비스 실행 내에서 소스 역할을 한 외부 결과로 향하는 URI 목록입니다.  - `type[string]`: NGSI 엔티티 유형입니다. DataServiceRun이어야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
이 데이터 모델은 DCAT 2.1.0 표준에 속하지 않으며, 채택을 위해 제안될 확장 모델입니다.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬됨 (자세한 내용은 클릭)  
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
      description: Technical configuration of the service. This attribute is intended to be an array of properties and their values which capture parameters which have to do with the configuration of a service (output format, URL, etc.) and which are not currently covered by the standard attributes defined by this model    
      items:    
        properties:    
          parameter:    
            description: Name of the parameter    
            format: text    
            type: string    
            x-ngsi:    
              type: Property    
          value:    
            description: Value of the parameter    
            type: string    
            x-ngsi:    
              type: Property    
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
        type: Relationship    
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
          type: Relationship    
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
        description: A uri pointing to external results that were generated within a service run    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
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
        description: A uri pointing to external results that acted as source within a service run    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
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
  x-derived-from: https://github.com/SEMICeu/DCAT-AP/blob/master/releases/2.1.1/dcat-ap_2.1.1.pdf    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
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
## 페이로드 예시  
#### DataServiceRun NGSI-v2 key-values 예시    
key-values 형식의 JSON-LD 형식 DataServiceRun 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### DataServiceRun NGSI-v2 정규화된 예시    
정규화된 JSON-LD 형식의 DataServiceRun 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataServiceRun:example-1234",  
  "type": "DataServiceRun",  
  "configuration": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:KeyPerformanceIndicator:example3",  
      "urn:ngsi-ld:KeyPerformanceIndicator:example4"  
    ]  
  },  
  "resultExternal": {  
    "type": "StructuredValue",  
    "value": [  
      "http://1.2.3.4:5678/files/example-file-3",  
      "http://1.2.3.4:5678/files/example-file-4"  
    ]  
  },  
  "sourceEntities": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Organization:example1",  
      "urn:ngsi-ld:Organization:example2"  
    ]  
  },  
  "sourceExternal": {  
    "type": "StructuredValue",  
    "value": [  
      "http://1.2.3.4:5678/files/example-file-1",  
      "http://1.2.3.4:5678/files/example-file-2"  
    ]  
  },  
  "service": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:DataServiceDCAT-AP:example"  
  }  
}  
```  
</details>  
#### DataServiceRun NGSI-LD key-values 예시    
key-values 형식의 JSON-LD 형식 DataServiceRun 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### DataServiceRun NGSI-LD 정규화된 예시    
정규화된 JSON-LD 형식의 DataServiceRun 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
