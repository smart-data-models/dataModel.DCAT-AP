<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)
<!-- 35-RequiredProperties -->

- `description`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

Catalogue:    
  description: Catalogue of datasets compliant with DCAT-AP specification version 2.1.1.    
  properties:    
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
        model: "http://www.w3.org/ns/dcat#Catalog"    
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
        model: "http://www.w3.org/ns/dcat#dataset"    
        type: Relationship    
    description:    
      description: 'This property contains a free-text account of the Catalogue. This property can be repeated for parallel language versions of the description. For further information on multilingual issues, please refer to section 8 of the pdf document https://codeload.github.com/SEMICeu/DCAT-AP/zip/refs/tags/v2.1.1'    
      items:    
        description: Catalogue description in different languages    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
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
        model: "http://www.w3.org/ns/dcat#Catalog"    
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
        type: Property    
    isPartOf:    
      description: This property refers to a related Catalogue in which the described Catalogue is physically or logically included    
      format: uri    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Catalog"    
        type: Relationship    
    issued:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Catalogue'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    language:    
      description: 'This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. This property can be repeated if the  metadata is provided in multiple languages'    
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
    modified:    
      description: This property contains the most recent date on which the Catalogue was modified    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    publisher:    
      description: This property refers to an entity (organisation) responsible for making the Catalogue available    
      type: string    
      x-ngsi:    
        model: "http://xmlns.com/foaf/0.1/#term_Agent"    
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
        model: "http://www.w3.org/ns/dcat#CatalogRecord"    
        type: Relationship    
    rights:    
      description: This property refers to a statement that specifies rights associated with the Catalogue    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    service:    
      description: 'This property refers to a site or end-point (Data Service) that is listed in the Catalogue. As empty Catalogues are usually indications of problems, this property should be combined with the previous property dataset to implement an empty Catalogue check'    
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
        model: "http://www.w3.org/ns/dcat#DataService"    
        type: Relationship    
    spatial:    
      description: This property refers to a geographical area covered by the Catalogue    
      items:    
        description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
        oneOf:    
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
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
        x-ngsi:    
          type: GeoProperty    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Location    
        type: GeoProperty    
    themeTaxonomy:    
      description: This property refers to a knowledge organization system used to classify the Catalogue's Datasets    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#ConceptScheme"    
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
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Catalogue/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Catalogue/schema.json    
  x-model-tags: ""    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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
  "creator": [""]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "description": {  
    "type": "array",  
    "value": ["Interesting art recently book girl yard represent book. Garden style wish blood your ground size."]  
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
      "postOfficeBoxNumber": "",  
      "areaServed": "European Union"  
    }  
  },  
  "dataset": {  
    "type": "array",  
    "value": ["urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"]  
  },  
  "publisher": {  
    "type": "Text",  
    "value": "spanish open data portal"  
  },  
  "title": {  
    "type": "Array",  
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
    "type": "array",  
    "value": [  
      "Town size computer way. Since challenge phone state listen south low.",  
      "Eight once single. Build every kid."  
    ]  
  },  
  "licence": {  
    "type": "Text",  
    "value": "Improve social simply court week debate bad. Structure ago cup head point. Above much can own course."  
  },  
  "issued": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
  },  
  "spatial": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.234944,  
        52.840273  
      ]  
    }  
  },  
  "themeTaxonomy": {  
    "type": "array",  
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
    "type": "array",  
    "value": ["urn:ngsi-ld:Catalogue:hasPart:GVZM:66676591"]  
  },  
  "isPartOf": {  
    "type": "Text",  
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
    "type": "Text",  
    "value": "Open source"  
  },  
  "catalog": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "array",  
    "value": ["Role fact sport shoulder blue direction probably order."]  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "Catalogue",  
  "address": {  
    "streetAddress": "2 Rue Mercier",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "addressCountry": "Luxembourg",  
    "postalCode": "2985 ",  
    "postOfficeBoxNumber": "",  
    "areaServed": "European Union"  
  },  
  "catalogue": [  
    "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
    "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
  ],  
  "creator": ["Role fact sport shoulder blue direction probably order."],  
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
  "licence": "Creative Commons 3.0 International",  
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


<details><summary><strong>show/hide example</strong></summary>    


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
      "postOfficeBoxNumber": "",  
      "areaServed": "European Union"  
    }  
  },  
  "catalog": {  
    "type": "Relationship",  
    "value": [  
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
    "value": [  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
