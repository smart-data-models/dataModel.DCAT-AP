<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: Catalogue  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Catalogue/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전체 설명: **DCAT-AP 사양 버전 2.1.1을 준수하는 데이터 세트 카탈로그.**  
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
- `areaServed[string]`: 서비스 또는 제공되는 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `catalog[array]`: 이 속성은 이 카탈로그의 문맥에서 내용이 유의미한 카탈로그를 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `creator[array]`: 카탈로그 제작에 주된 책임을 지는 엔티티들  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `dataset[array]`: 이 속성은 카탈로그의 일부인 데이터 세트를 카탈로그와 연결합니다.  . Model: [http://www.w3.org/ns/dcat#dataset](http://www.w3.org/ns/dcat#dataset)- `description[array]`: 이 속성은 카탈로그에 대한 자유 형식의 설명을 포함합니다. 이 속성은 설명의 병렬 언어 버전을 위해 반복될 수 있습니다. 다국어 문제에 대한 자세한 내용은 pdf 문서 https://codeload.github.com/SEMICeu/DCAT-AP/zip/refs/tags/v2.1.1의 8절을 참조하십시오.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `hasPart[array]`: 이 속성은 설명된 카탈로그의 일부인 관련 카탈로그를 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `homepage[uri]`: 이 속성은 카탈로그의 메인 페이지 역할을 하는 웹 페이지를 나타냅니다.  . Model: [http://xmlns.com/foaf/0.1/homepage](http://xmlns.com/foaf/0.1/homepage)- `id[*]`: 엔티티의 고유 식별자  - `isPartOf[uri]`: 이 속성은 설명된 카탈로그가 물리적 또는 논리적으로 포함된 관련 카탈로그를 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `issued[date-time]`: 이 속성은 카탈로그의 공식 발행(예: 출판) 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: 이 속성은 카탈로그 내 데이터 세트의 제목, 설명 등을 기술하는 텍스트 메타데이터에 사용된 언어를 나타냅니다. 메타데이터가 여러 언어로 제공되는 경우 이 속성을 반복할 수 있습니다.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: 이 속성은 카탈로그를 사용하거나 재사용할 수 있는 라이선스를 나타냅니다.  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: 항목에 대한 Geojson 참조. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon일 수 있습니다.  - `modified[date-time]`: 이 속성은 카탈로그가 수정된 가장 최근 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `publisher[string]`: 이 속성은 카탈로그를 사용할 수 있도록 제공하는 책임을 지는 엔티티(조직)를 나타냅니다.  . Model: [http://xmlns.com/foaf/0.1/#term_Agent](http://xmlns.com/foaf/0.1/#term_Agent)- `record[array]`: 이 속성은 카탈로그의 일부인 카탈로그 레코드를 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#CatalogRecord](http://www.w3.org/ns/dcat#CatalogRecord)- `rights[string]`: 이 속성은 카탈로그와 관련된 권리를 명시하는 문구를 나타냅니다.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `service[array]`: 이 속성은 카탈로그에 나열된 사이트 또는 엔드포인트(데이터 서비스)를 나타냅니다. 빈 카탈로그는 보통 문제를 나타내므로, 빈 카탈로그 확인 기능을 구현하기 위해 이 속성은 이전 속성인 dataset과 결합되어야 합니다.  . Model: [http://www.w3.org/ns/dcat#DataService](http://www.w3.org/ns/dcat#DataService)- `spatial[array]`: 이 속성은 카탈로그가 다루는 지리적 영역을 나타냅니다.  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `themeTaxonomy[array]`: 이 속성은 카탈로그의 데이터 세트를 분류하는 데 사용되는 지식 조직 체계를 나타냅니다.  . Model: [http://www.w3.org/2004/02/skos/core#ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)- `title[array]`: 이 속성은 카탈로그에 부여된 이름을 포함합니다. 이 속성은 이름의 병렬 언어 버전을 위해 반복될 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Catalogue여야 합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `description`  - `id`  - `publisher`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
이 데이터 모델과 DCAT-AP의 다른 주제들은 사용을 위해 조정되고 있으며, 추가적인 컨텍스트가 포함되는 것이 권장됩니다. [https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld" ](https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld)  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬됨 (자세한 내용은 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Catalogue:    
  description: Catalogue of datasets compliant with DCAT-AP specification version 2.1.1.    
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
    catalog:    
      description: This property refers to a catalog whose contents are of interest in the context of this catalog    
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
        description: Every link to the contents of interest to the catalog    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Catalog    
        type: Relationship    
    creator:    
      description: The entities primarily responsible for producing the catalogue    
      items:    
        description: The link to an entity primarily responsible for producing the catalogue    
        type: string    
        x-ngsi:    
          model: http://xmlns.com/foaf/0.1/Agent    
          type: Relationship    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Relationship    
    dataset:    
      description: This property links the Catalogue with a Dataset that is part of the Catalogue    
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
        model: http://www.w3.org/ns/dcat#dataset    
        type: Relationship    
    description:    
      description: This property contains a free-text account of the Catalogue. This property can be repeated for parallel language versions of the description. For further information on multilingual issues, please refer to section 8 of the pdf document https://codeload.github.com/SEMICeu/DCAT-AP/zip/refs/tags/v2.1.1    
      items:    
        description: Catalogue description in different languages    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    hasPart:    
      description: This property refers to a related Catalogue that is part of the described Catalogue    
      items:    
        description: Every link to the related catalog    
        format: uri    
        type: string    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Catalog    
        type: Relationship    
    homepage:    
      description: This property refers to a web page that acts as the main page for the Catalogue    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/homepage    
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
    isPartOf:    
      description: This property refers to a related Catalogue in which the described Catalogue is physically or logically included    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Catalog    
        type: Relationship    
    issued:    
      description: This property contains the date of formal issuance (e.g., publication) of the Catalogue    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    language:    
      description: This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. This property can be repeated if the  metadata is provided in multiple languages    
      items:    
        description: Individual identifiers of the language    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    license:    
      description: This property refers to the licence under which the Catalogue can be used or reused    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/LicenseDocument    
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
      description: This property contains the most recent date on which the Catalogue was modified    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    publisher:    
      description: This property refers to an entity (organisation) responsible for making the Catalogue available    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/#term_Agent    
        type: Property    
    record:    
      description: This property refers to a Catalogue Record that is part of the Catalogue    
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
        description: Link to the catalog record    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#CatalogRecord    
        type: Relationship    
    rights:    
      description: This property refers to a statement that specifies rights associated with the Catalogue    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    service:    
      description: This property refers to a site or end-point (Data Service) that is listed in the Catalogue. As empty Catalogues are usually indications of problems, this property should be combined with the previous property dataset to implement an empty Catalogue check    
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
        description: NGSI-LD id of the different services linked to the catalogue    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#DataService    
        type: Relationship    
    spatial:    
      description: This property refers to a geographical area covered by the Catalogue    
      items:    
        description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
        oneOf:    
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items: {}    
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
        x-ngsi:    
          type: GeoProperty    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Location    
        type: GeoProperty    
    themeTaxonomy:    
      description: This property refers to a knowledge organization system used to classify the Catalogue's Datasets    
      items:    
        description: The value to be used for this property is the URI of the vocabulary itself, i.e. the concept scheme, not the URIs of the concepts in the vocabulary.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#ConceptScheme    
        type: Property    
    title:    
      description: This property contains a name given to the Catalogue. This property can be repeated for parallel language versions of the name    
      items:    
        description: Title in different languages    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    type:    
      description: It has to be Catalogue    
      enum:    
        - Catalogue    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - description    
    - publisher    
    - title    
  type: object    
  x-derived-from: https://github.com/SEMICeu/DCAT-AP/blob/master/releases/2.1.1/dcat-ap_2.1.1.pdf    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Catalogue/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Catalogue/schema.json    
  x-model-tags: INTERSTAT, WATERVERSE    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### Catalogue NGSI-v2 key-values 예시  
다음은 key-values 형식의 JSON-LD 포맷 카탈로그 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "description": [  
    "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
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
    "postOfficeBoxNumber": ""  
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
  "license": "Creative Commons 3.0 International",  
  "issued": "2004-08-22T22:32:47Z",  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  ],  
  "themeTaxonomy": [  
    "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
    "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
  ],  
  "modified": "1982-09-02T03:16:28Z",  
  "hasPart": [  
    "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
  ],  
  "isPartOf": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287",  
  "record": [  
    "Catalogue.items.HLGA.73285516",  
    "Catalogue.items.IHOB.85266800"  
  ],  
  "rights": "",  
  "catalog": [  
    "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
    "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
  ],  
  "creator": [  
    ""  
  ]  
}  
```  
</details>  
#### Catalogue NGSI-v2 normalized 예시  
다음은 normalized 형식의 JSON-LD 포맷 카탈로그 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "description": {  
    "type": "StructuredValue",  
    "value": [  
      "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
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
      "streetAddress": "2 Rue Mercier",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "2985 ",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "dataset": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ]  
  },  
  "publisher": {  
    "type": "Text",  
    "value": "spanish open data portal"  
  },  
  "title": {  
    "type": "StructuredValue",  
    "value": [  
      "Hair commercial free civil. Figure American film despite few. Box watch cold act mean thank music people. Third fill us.",  
      "Technology life low standard second."  
    ]  
  },  
  "homepage": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Catalogue:homepage:ZFAW:13633782"  
  },  
  "language": {  
    "type": "StructuredValue",  
    "value": [  
      "Town size computer way. Since challenge phone state listen south low.",  
      "Eight once single. Build every kid."  
    ]  
  },  
  "license": {  
    "type": "Text",  
    "value": "Improve social simply court week debate bad. Structure ago cup head point. Above much can own course."  
  },  
  "issued": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
  },  
  "spatial": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "type": "Point",  
        "coordinates": [  
          57.234944,  
          52.840273  
        ]  
      }  
    ]  
  },  
  "themeTaxonomy": {  
    "type": "StructuredValue",  
    "value": [  
      "Tourism",  
      "Economy"  
    ]  
  },  
  "modified": {  
    "type": "DateTime",  
    "value": "1982-09-02T03:16:28Z"  
  },  
  "hasPart": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
    ]  
  },  
  "isPartOf": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287"  
  },  
  "record": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:HLGA:73285516",  
      "urn:ngsi-ld:Catalogue:items:IHOB:85266800"  
    ]  
  },  
  "rights": {  
    "type": "Text",  
    "value": "Open source"  
  },  
  "catalog": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "StructuredValue",  
    "value": [  
      "Role fact sport shoulder blue direction probably order."  
    ]  
  }  
}  
```  
</details>  
#### Catalogue NGSI-LD key-values 예시  
다음은 key-values 형식의 JSON-LD 포맷 카탈로그 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "address": {  
    "streetAddress": "2 Rue Mercier",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "addressCountry": "Luxembourg",  
    "postalCode": "2985 ",  
    "postOfficeBoxNumber": ""  
  },  
  "catalog": [  
    "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
    "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
  ],  
  "creator": [  
    "Role fact sport shoulder blue direction probably order."  
  ],  
  "dataset": [  
    "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
  ],  
  "description": [  
    "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
  ],  
  "hasPart": [  
    "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
  ],  
  "homepage": "ngsi-ld:Catalogue:homepage:ZFAW:13633782",  
  "isPartOf": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287",  
  "language": [  
    "ES",  
    "DE"  
  ],  
  "license": "Creative Commons 3.0 International",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -83.400987,  
      0.152532  
    ]  
  },  
  "modified": "1982-09-02T03:16:28Z",  
  "publisher": "Spanish data portal",  
  "record": [  
    "Catalogue.items.HLGA.73285516",  
    "Catalogue.items.IHOB.85266800"  
  ],  
  "issued": "2004-08-22T22:32:47Z",  
  "rights": "",  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  ],  
  "themeTaxonomy": [  
    "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
    "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
  ],  
  "title": [  
    "title first",  
    "Secondary title."  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Catalogue NGSI-LD normalized 예시  
다음은 normalized 형식의 JSON-LD 포맷 카탈로그 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "2 Rue Mercier",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "2985 ",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "catalog": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "Relationship",  
    "object": [""]  
  },  
  "dataset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": [""]  
  },  
  "hasPart": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"  
    ]  
  },  
  "homepage": {  
    "type": "Property",  
    "value": "Catalogue:homepage:ZFAW:13633782"  
  },  
  "isPartOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Catalogue:isPartOf:NXBZ:88517287"  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      "ES",  
      "DE"  
    ]  
  },  
  "license": {  
    "type": "Property",  
    "value":  
      "Creative Commons 3.0 International"  
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
  "modified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1982-09-02T03:16:28Z"  
    }  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Spain open data portal"  
  },  
  "record": {  
    "type": "Relationship",  
    "object": [  
      "Catalogue.items.HLGA.73285516",  
      "Catalogue.items.IHOB.85266800"  
    ]  
  },  
  "issued": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2004-08-22T22:32:47Z"  
    }  
  },  
  "rights": {  
    "type": "Property",  
    "value": ""  
  },  
  "spatial": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  },  
  "themeTaxonomy": {  
    "type": "Property",  
    "value": [  
      "Tourism",  
      "Economy"  
    ]  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "New catalogue",  
      "Nuevo catalogo"  
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
