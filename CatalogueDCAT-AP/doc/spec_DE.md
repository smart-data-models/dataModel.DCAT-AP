Entität: KatalogDCAT-AP  
=======================








- `dataset`  

<details><summary><strong>full yaml details</strong></summary>    

CatalogueDCAT-AP:    
  description: 'Catalogue of datasets compliant with DCAT-AP specification.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Relationship    
      x-ngsi:    
        model: dcat:catalog    
    creator:    
      description: 'This property refers to the entity primarily responsible for producing the catalogue'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
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
      type: Relationship    
      x-ngsi:    
        model: dcat:Dataset    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    hasPart:    
      description: 'This property refers to a related Catalogue that is part of the described Catalogue'    
      items:    
        format: uri    
        type: string    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    homepage:    
      description: 'This property refers to a web page that acts as the main page for the Catalogue.'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: foaf:homepage    
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
      type: Property    
    isPartOf:    
      description: 'This property refers to a related Catalogue in which the described Catalogue is physically or logically included.'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    language:    
      description: 'This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. This property can be repeated if the  metadata is provided in multiple languages.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: dct:language    
    licence:    
      description: 'This property refers to the licence under which the Catalogue can be used or reused.'    
      type: Property    
      x-ngsi:    
        model: dct:license    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_oneof    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    modificationDate:    
      description: 'This property contains the most recent date on which the Catalogue was modified.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *cataloguedcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    publisher:    
      description: 'This property refers to an entity (organisation) responsible for making the Catalogue available'    
      type: Property    
      x-ngsi:    
        model: dct:publisher    
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
      type: Relationship    
    releaseDate:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Catalogue.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    rights:    
      description: 'This property refers to a statement that specifies rights associated with the Catalogue.'    
      type: Property    
      x-ngsi:    
        model: dct:rights    
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
      type: Property    
    service:    
      description: 'This property refers to a site or end-point that is listed in the catalog'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: dcat:DataService    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    spatial_geographic:    
      description: 'This property refers to a geographical area covered by the Catalogue'    
      items:    
        $id: https://geojson.org/schema/Geometry.json    
        $schema: "http://json-schema.org/draft-07/schema#"    
        oneOf: *cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_oneof    
        title: 'GeoJSON Geometry'    
      type: Geoproperty    
      x-ngsi:    
        model: dct:spatial    
    themes:    
      description: 'This property refers to a knowledge organization system used to classify the Catalogue''s Datasets.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: dcat:themeTaxonomy    
    title:    
      description: 'This property contains a name given to the Catalogue. This property can be repeated for parallel language versions of the name'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: rdfs:Literal    
    type:    
      description: 'It has to be CatalogueDCAT-AP'    
      enum:    
        - CatalogueDCAT-AP    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "name": {  
    "type": "Property",  
    "value": [  
      "Catalogue"  
    ]  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": [  
      "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
    ]  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": [  
      "european open data portal"  
    ]  
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
    "type": "Property",  
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
    "value": [  
      "Five knowledge level character. Toward we billion number situation box film."  
    ]  
  },  
  "title": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "urn:ngsi-ld:Catalogue:homepage:ZFAW:13633782"  
  },  
  "language": {  
    "type": "Property",  
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
    "value": [  
      "Improve social simply court week debate bad. Structure ago cup head point. Above much can own course."  
    ]  
  },  
  "releaseDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2004-08-22T22:32:47Z"  
    }  
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
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1982-09-02T03:16:28Z"  
    }  
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
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:HLGA:73285516",  
      "urn:ngsi-ld:Catalogue:items:IHOB:85266800"  
    ]  
  },  
  "rights": {  
    "type": "Property",  
    "value": [  
      "Smile item their unit laugh reflect. Standard our worker coach threat present huge name. Reveal certainly director business sense."  
    ]  
  },  
  "catalogue": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "Property",  
    "value": [  
      "Role fact sport shoulder blue direction probably order."  
    ]  
  }  
}  
```  




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
  "@context": "https://smartdatamodels.org/context.jsonld"  
}  
```  




  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-03-03T10:01:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1987-12-04T10:44:40Z"  
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
    "value": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "european open data portal"  
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
    "type": "PostalAddress",  
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
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ]  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Five knowledge level character. Toward we billion number situation box film."  
  },  
  "title": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "Catalogue.homepage.ZFAW.13633782"  
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
    "value": "Role fact sport shoulder blue direction probably order."  
  }  
}  
```  