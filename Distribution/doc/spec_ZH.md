<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：Distribution  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Distribution/LICENSE.md)  
[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**根据 DCAT-AP 标准 2.1.1，这是一个属于数据集的 Distribution**  
version: 1.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，则可能是因为它有多种类型或不同的格式/模式</sub></sup>  
- `accessService[array]`: 此属性指提供访问数据集 Distribution 的数据服务。  . Model: [http://www.w3.org/ns/dcat#DataService](http://www.w3.org/ns/dcat#DataService)- `accessURL[array]`: 此属性包含一个用于访问数据集 Distribution 的 URL。访问 URL 处的资源可能包含关于如何获取数据集的信息。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的城镇，该城镇位于该区域内  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 城镇所在的区域，该区域位于该国家内  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 区是一种行政区划类型，在某些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 邮政信箱地址的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定属性的编号    
- `areaServed[string]`: 提供服务或商品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: 此属性指示计划让数据集的 Distribution 保持可用多长时间。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `belongsToDataset[*]`: 它将 Distribution 连接到其父数据集。注意：此属性不属于当前版本的 DCAT-AP 2.1.1。  . Model: [https://www.w3.org/ns/dcat#Dataset](https://www.w3.org/ns/dcat#Dataset)- `byteSize[number]`: 此属性包含以字节为单位的 Distribution 大小。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `checksum[string]`: 此属性提供了一种可用于验证 Distribution 内容是否已更改的机制。校验和与 downloadURL 相关。  . Model: [http://spdx.org/rdf/terms#Checksum](http://spdx.org/rdf/terms#Checksum)- `compressionFormat[string]`: 此属性指数据以压缩形式包含的文件格式，例如为了减小可下载文件的大小。它应当使用由 IANA 管理的官方媒体类型注册表中定义的媒体类型来表示。  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `conformsTo[array]`: 此属性指所描述的 Distribution 所遵循的既定架构。  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `description[array]`: 此属性包含对 Distribution 的自由文本说明。对于描述的平行语言版本，此属性可以重复。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `downloadURL[array]`: 此属性包含一个指向给定格式的可下载文件的直接链接的 URL。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `format[string]`: 此属性指 Distribution 的文件格式。  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasPolicy[string]`: 如果使用 ODRL 词汇表，此属性指表达与 Distribution 相关权利的策略。  . Model: [http://www.w3.org/ns/odrl/2/hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy)- `issued[date-time]`: 此属性包含 Distribution 正式发布（例如，出版）的日期。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: 此属性指 Distribution 中使用的语言。如果以多种语言提供元数据，此属性可以重复。  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: 此属性指提供访问数据集 Distribution 的数据服务。  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: 项目的 Geojson 引用。它可以是 Point、LineString、Polygon、MultiPoint、MultiLineString 或 MultiPolygon  - `mediaType[string]`: 此属性指由 IANA 管理的官方媒体类型注册表中定义的 Distribution 媒体类型。  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `modified[date-time]`: 此属性包含 Distribution 最近一次更改或修改的日期。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `packageFormat[string]`: 此属性指将一个或多个数据文件组合在一起的文件格式，例如为了实现一组相关文件可以一起下载。它应当使用由 IANA 管理的官方媒体类型注册表中定义的媒体类型来表示。  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `packagingFormat[string]`: 此属性指将一个或多个数据文件组合在一起的文件格式，例如为了实现一组相关文件可以一起下载。它应当使用由 IANA 管理的官方媒体类型注册表中定义的媒体类型来表示。基数 (0..1)  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `page[array]`: 此属性指关于此 Distribution 的页面或文档。  . Model: [http://xmlns.com/foaf/0.1/#term_Document](http://xmlns.com/foaf/0.1/#term_Document)- `rights[string]`: 此属性指指定与 Distribution 相关权利的声明。  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `spatialResolutionInMeters[array]`: 此属性指 Distribution 中可分辨的最小空间间隔，以米为单位。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `status[string]`: 此属性指 Distribution 的成熟度。它必须取 Completed、Deprecated、Under Development、Withdrawn 中的一个值。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `temporalResolution[duration]`: 此属性指数据集中可分辨的最小时间周期。  . Model: [http://www.w3.org/2001/XMLSchema#duration](http://www.w3.org/2001/XMLSchema#duration)- `title[array]`: 此属性包含赋予 Distribution 的名称。对于描述的平行语言版本，此属性可以重复。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: NGSI 实体类型。它必须是 Distribution。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必填属性  
- `accessURL`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
改编自 [DCAT-AP 版本 2.1.1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211)。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（点击查看详情）  
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
## 示例载荷    
#### Distribution NGSI-v2 键值对示例  
这是一个键值对格式的 JSON-LD 格式的 Distribution 示例。在使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### Distribution NGSI-v2 归一化示例  
这是一个归一化格式的 JSON-LD 格式的 Distribution 示例。在不使用 options 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### Distribution NGSI-LD 键值对示例  
这是一个键值对格式的 JSON-LD 格式的 Distribution 示例。在使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### Distribution NGSI-LD 归一化示例  
这是一个归一化格式的 JSON-LD 格式的 Distribution 示例。在不使用 options 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [常见问题 10](https://smartdatamodels.org/index.php/faqs/)，了解如何处理数量单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
