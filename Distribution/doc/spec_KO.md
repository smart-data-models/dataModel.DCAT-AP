<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: Distribution  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Distribution/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이것은 DCAT-AP 표준 2.1.1에 따른 데이터셋에 속하는 distribution입니다**  
version: 1.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 경우 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>  
- `accessService[array]`: 이 속성은 데이터셋의 Distribution에 대한 액세스를 제공하는 데이터 서비스를 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#DataService](http://www.w3.org/ns/dcat#DataService)- `accessURL[array]`: 이 속성은 데이터셋의 Distribution에 액세스할 수 있는 URL을 포함합니다. 액세스 URL의 리소스에는 데이터셋을 가져오는 방법에 대한 정보가 포함될 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 위치하고 해당 지역에 속하는 구역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 구역이 위치하고 국가에 속하는 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 구역은 일부 국가에서 지방 정부가 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 사서함 번호. 예를 들어, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호. 예를 들어, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 도로명 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 속성을 식별하는 번호    
- `areaServed[string]`: 서비스 또는 제공되는 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: 이 속성은 데이터셋의 Distribution을 얼마나 오래 사용할 수 있도록 유지할 계획인지 나타냅니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `belongsToDataset[*]`: Distribution을 부모 데이터셋에 연결합니다. 참고: 이 속성은 현재 버전인 DCAT-AP 2.1.1에 속하지 않습니다.  . Model: [https://www.w3.org/ns/dcat#Dataset](https://www.w3.org/ns/dcat#Dataset)- `byteSize[number]`: 이 속성은 바이트 단위의 Distribution 크기를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `checksum[string]`: 이 속성은 Distribution의 내용이 변경되지 않았음을 확인하는 데 사용할 수 있는 메커니즘을 제공합니다. 체크섬은 downloadURL과 관련이 있습니다.  . Model: [http://spdx.org/rdf/terms#Checksum](http://spdx.org/rdf/terms#Checksum)- `compressionFormat[string]`: 이 속성은 다운로드 가능한 파일 크기를 줄이기 위해 데이터가 압축된 파일 형식을 나타냅니다. IANA에서 관리하는 공식 미디어 유형 레지스트리에 정의된 미디어 유형을 사용하여 표현해야 합니다.  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `conformsTo[array]`: 이 속성은 설명된 Distribution이 준수하는 확립된 스키마를 나타냅니다.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `description[array]`: 이 속성은 Distribution에 대한 자유 형식의 설명을 포함합니다. 설명의 병렬 언어 버전에 대해 이 속성을 반복해서 사용할 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `downloadURL[array]`: 이 속성은 특정 형식의 다운로드 가능한 파일로 직접 연결되는 URL을 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `format[string]`: 이 속성은 Distribution의 파일 형식을 나타냅니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasPolicy[string]`: 이 속성은 ODRL 어휘를 사용하는 경우 Distribution과 관련된 권리를 나타내는 정책을 의미합니다.  . Model: [http://www.w3.org/ns/odrl/2/hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy)- `issued[date-time]`: 이 속성은 Distribution의 공식 발행(예: 출판) 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: 이 속성은 Distribution에 사용된 언어를 나타냅니다. 메타데이터가 여러 언어로 제공되는 경우 이 속성을 반복해서 사용할 수 있습니다.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: 이 속성은 데이터셋의 Distribution에 대한 액세스를 제공하는 데이터 서비스를 나타냅니다.  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: 항목에 대한 Geojson 참조. Point, LineString, Polygon, MultiPoint, MultiLineString 또는 MultiPolygon일 수 있습니다.  - `mediaType[string]`: 이 속성은 IANA에서 관리하는 공식 미디어 유형 레지스트리에 정의된 Distribution의 미디어 유형을 나타냅니다.  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `modified[date-time]`: 이 속성은 Distribution이 변경되거나 수정된 가장 최근 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `packageFormat[string]`: 이 속성은 관련 파일 세트를 함께 다운로드할 수 있도록 하나 이상의 데이터 파일을 그룹화한 파일 형식을 나타냅니다. IANA에서 관리하는 공식 미디어 유형 레지스트리에 정의된 미디어 유형을 사용하여 표현해야 합니다.  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `packagingFormat[string]`: 이 속성은 관련 파일 세트를 함께 다운로드할 수 있도록 하나 이상의 데이터 파일을 그룹화한 파일 형식을 나타냅니다. IANA에서 관리하는 공식 미디어 유형 레지스트리에 정의된 미디어 유형을 사용하여 표현해야 합니다. 카디널리티 (0..1)  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `page[array]`: 이 속성은 이 Distribution에 관한 페이지 또는 문서를 나타냅니다.  . Model: [http://xmlns.com/foaf/0.1/#term_Document](http://xmlns.com/foaf/0.1/#term_Document)- `rights[string]`: 이 속성은 Distribution과 관련된 권리를 지정하는 문구를 나타냅니다.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `spatialResolutionInMeters[array]`: 이 속성은 미터 단위로 측정된, Distribution에서 식별 가능한 최소 공간 분해능을 나타냅니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `status[string]`: 이 속성은 Distribution의 성숙도를 나타냅니다. 반드시 Completed, Deprecated, Under Development, Withdrawn 중 하나의 값을 가져야 합니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `temporalResolution[duration]`: 이 속성은 데이터셋에서 식별 가능한 최소 시간 단위를 나타냅니다.  . Model: [http://www.w3.org/2001/XMLSchema#duration](http://www.w3.org/2001/XMLSchema#duration)- `title[array]`: 이 속성은 Distribution에 부여된 이름을 포함합니다. 설명의 병렬 언어 버전에 대해 이 속성을 반복해서 사용할 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: NGSI 엔티티 유형. 반드시 Distribution이어야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `accessURL`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
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
Distribution:    
  description: This is a distribution belonging ot a dataset according to the DCAT-AP standard 2.1.1    
  properties:    
    accessService:    
      description: This property refers to a data service that gives access to the distribution of the dataset    
      items:    
        description: Every Data service providing access to the distribution    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#DataService    
        type: Property    
    accessURL:    
      description: This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset    
      items:    
        description: URL that gives access to a Distribution of the Dataset    
        minItems: 1    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Property    
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
    availability:    
      description: This property indicates how long it is planned to keep the Distributio of the Dataset available    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#Concept    
        type: Property    
    belongsToDataset:    
      anyOf:    
        - description: Link to the dataset    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Link to the dataset    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'It links the Distribution to its parent Dataset. Note: this attribute does not belong to the current version of DCAT-AP, 2.1.1'    
      x-ngsi:    
        model: https://www.w3.org/ns/dcat#Dataset    
        type: Relationship    
    byteSize:    
      description: This property contains the size of a Distribution in bytes    
      type: number    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    checksum:    
      description: This property provides a mechanism that can be used to verify that the contents of a distribution have not changed. The checksum is related to the downloadURL    
      type: string    
      x-ngsi:    
        model: http://spdx.org/rdf/terms#Checksum    
        type: Property    
    compressionFormat:    
      description: This property refers to the format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    conformsTo:    
      description: This property refers to an established schema to which the described Distribution conforms    
      items:    
        description: Every rule o standard the distribution complies with    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    description:    
      description: This property contains a free-text account of the Distribution. This property can be repeated for parallel language versions of the description    
      items:    
        description: Every description of the distribution in a language    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    downloadURL:    
      description: This property contains a URL that is a direct link to a downloadable file in a given format    
      items:    
        description: Every URL available for downloading    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Property    
    format:    
      description: This property refers to the file format of the Distribution    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hasPolicy:    
      description: This property refers to the policy expressing the rights associated with the distribution if using the ODRL vocabulary    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/ns/odrl/2/hasPolicy    
        type: Property    
    issued:    
      description: This property contains the date of formal issuance (e.g., publication) of the Distribution    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    language:    
      description: This property refers to a language used in the Distribution. This property can be repeated if the metadata is provided in multiple languages    
      items:    
        description: Every language included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    license:    
      description: This property refers to a data service that gives access to the distribution of the dataset    
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
    mediaType:    
      description: This property refers to the media type of the Distribution as defined in the official register of media types managed by IANA    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    modified:    
      description: This property contains the most recent date on which the Distribution was changed or modified    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    packageFormat:    
      description: This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    packagingFormat:    
      description: This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA. Cardinality (0..1)    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    page:    
      description: This property refers to a page or document about this Distribution    
      items:    
        description: Every page providing information about the distribution    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/#term_Document    
        type: Property    
    rights:    
      description: This property refers to a statement that specifies rights associated with the Distribution    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    spatialResolutionInMeters:    
      description: This property refers to the minimum spatial separation resolvable in a distribution, measured in meters    
      items:    
        description: The minimum spatial separation resolvable in a dataset distribution, measured in meters.    
        type: number    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    status:    
      description: This property refers to the maturity of the Distribution. It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn    
      enum:    
        - Completed    
        - Deprecated    
        - Under Development    
        - Withdrawn    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#Concept    
        type: Property    
    temporalResolution:    
      description: 'This property refers to the minimum time period resolvable in the dataset. '    
      format: duration    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2001/XMLSchema#duration    
        type: Property    
    title:    
      description: This property contains a name given to the Distribution. This property can be repeated for parallel language versions of the description    
      items:    
        description: Every language description of the distribution title    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    type:    
      description: NGSI entity type. It has to be Distribution    
      enum:    
        - Distribution    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - accessURL    
    - id    
    - type    
  type: object    
  x-derived-from: https://github.com/SEMICeu/DCAT-AP/blob/master/releases/2.1.1/dcat-ap_2.1.1.pdf    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Distribution/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Distribution/schema.json    
  x-model-tags: INTERSTAT, WATERVERSE    
  x-version: 1.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### Distribution NGSI-v2 키-값 예시  
키-값 형식의 JSON-LD 형식 Distribution 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Distribution:id:NUZE:76215118",  
  "type": "Distribution",  
  "accessService": [  
    ""  
  ],  
  "accessURL": [  
    "https://datos.comunidad.madrid/catalogo/dataset/134210b4-3fbc-457d-8064-18d6d8cc785e/resource/fca9a0ef-60b3-44bc-8a69-c17d607b122d/download/alojamientos_turisticos.csv"  
  ],  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "24004",  
    "streetAddress": "Luxembourg platz 2"  
  },  
  "availability": "yes",  
  "byteSize": 43503,  
  "checksum": "H3FR.",  
  "compressionFormat": "",  
  "belongsToDataset": "urn:ngsi-ld:Dataset:items:CHIF:23645981",  
  "description": [  
    "Distribution of open data portals in csv"  
  ],  
  "page": [],  
  "downloadURL": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/WeatherObserved/examples/example.json"  
  ],  
  "format": " text/csv",  
  "hasPolicy": "Open data policy.",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "license": "CC-BY",  
  "conformsTo": ["https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/WeatherObserved/schema.json"],  
  "location": {  
    "coordinates": [  
      -67.057831,  
      67.968509  
    ],  
    "type": "Point"  
  },  
  "mediaType": "application/json",  
  "modified": "1986-03-28T19:56:43Z",  
  "packagingFormat": "zip",  
  "issued": "1997-05-06T05:04:10Z",  
  "rights": "copyleft",  
  "spatialResolutionInMeters": [  
    0.5,  
    0.5  
  ],  
  "status": "Withdrawn",  
  "temporalResolution": "PT15M",  
  "title": [  
    "Dataset base"  
  ]  
}  
```  
</details>  
#### Distribution NGSI-v2 정규화 예시  
정규화된 JSON-LD 형식의 Distribution 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Distribution:id:NUZE:76215118",  
  "type": "Distribution",  
  "description": {  
    "type": "StructuredValue",  
    "value": [  
      "Distribution of open data portals in csv"  
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
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Luxembourg platz 2",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "24004",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "accessURL": {  
    "type": "StructuredValue",  
    "value": [  
      "https://datos.comunidad.madrid/catalogo/dataset/134210b4-3fbc-457d-8064-18d6d8cc785e/resource/fca9a0ef-60b3-44bc-8a69-c17d607b122d/download/alojamientos_turisticos.csv"  
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
    "type": "StructuredValue",  
    "value": [  
      ""  
    ]  
  },  
  "byteSize": {  
    "type": "Number",  
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
  "belongsToDataset": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Dataset:items:CHIF:23645981"  
  },  
  "page": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "downloadURL": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "conformsTo": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "mediaType": {  
    "type": "Text",  
    "value": ""  
  },  
  "packagingFormat": {  
    "type": "Text",  
    "value": "zip"  
  },  
  "issued": {  
    "type": "DateTime",  
    "value": "1997-05-06T05:04:10Z"  
  },  
  "rights": {  
    "type": "Text",  
    "value": "copyleft"  
  },  
  "spatialResolutionInMeters": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "PT17S"  
  },  
  "title": {  
    "type": "StructuredValue",  
    "value": [  
      "Dataset base"  
    ]  
  },  
  "modified": {  
    "type": "DateTime",  
    "value": "1986-03-28T19:56:43Z"  
  }  
}  
```  
</details>  
#### Distribution NGSI-LD 키-값 예시  
키-값 형식의 JSON-LD 형식 Distribution 예시입니다. 이는 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Distribution:id:NUZE:76215118",  
  "type": "Distribution",  
  "accessService": [  
    ""  
  ],  
  "accessURL": [  
    "https://datos.comunidad.madrid/catalogo/dataset/134210b4-3fbc-457d-8064-18d6d8cc785e/resource/fca9a0ef-60b3-44bc-8a69-c17d607b122d/download/alojamientos_turisticos.csv"  
  ],  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "24004",  
    "streetAddress": "Luxembourg platz 2"  
  },  
  "availability": "yes",  
  "byteSize": 43503,  
  "checksum": "H3FR.",  
  "compressionFormat": "",  
  "belongsToDataset": "urn:ngsi-ld:Dataset:items:CHIF:23645981",  
  "description": [  
    "Distribution of open data portals in csv"  
  ],  
  "page": [],  
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
  "conformsTo": [],  
  "location": {  
    "coordinates": [  
      -67.057831,  
      67.968509  
    ],  
    "type": "Point"  
  },  
  "mediaType": "",  
  "modified": "1986-03-28T19:56:43Z",  
  "packagingFormat": "zip",  
  "issued": "1997-05-06T05:04:10Z",  
  "rights": "copyleft",  
  "spatialResolutionInMeters": [  
    0.5,  
    0.5  
  ],  
  "status": "Withdrawn",  
  "temporalResolution": "PT15S",  
  "title": [  
    "Dataset base"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Distribution NGSI-LD 정규화 예시  
정규화된 JSON-LD 형식의 Distribution 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Distribution:id:NUZE:76215118",  
  "type": "Distribution",  
  "accessService": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "accessURL": {  
    "type": "Property",  
    "value": [  
      "https://datos.comunidad.madrid/catalogo/dataset/134210b4-3fbc-457d-8064-18d6d8cc785e/resource/fca9a0ef-60b3-44bc-8a69-c17d607b122d/download/alojamientos_turisticos.csv"  
    ]  
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
  "availability": {  
    "type": "Property",  
    "value": "yes"  
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
  "belongsToDataset": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Dataset:items:CHIF:23645981"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Meloda.org"  
  },  
  "modified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-07-14T10:48:19Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": [  
      "Distribution of open data portals in csv"  
    ]  
  },  
  "documentation": {  
    "type": "Property",  
    "value": []  
  },  
  "downloadURL": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HVWX:12201868",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:ICPI:96947751"  
    ]  
  },  
  "format": {  
    "type": "Property",  
    "value": " text/csv"  
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
  "license": {  
    "type": "Property",  
    "value": "CC-BY"  
  },  
  "conformsTo": {  
    "type": "Property",  
    "value": []  
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
  "mediaType": {  
    "type": "Property",  
    "value": ""  
  },  
  "packagingFormat": {  
    "type": "Property",  
    "value": "zip"  
  },  
  "issued": {  
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
  "spatialResolutionInMeters": {  
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
