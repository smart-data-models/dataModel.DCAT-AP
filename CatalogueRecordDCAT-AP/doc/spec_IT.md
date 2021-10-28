Entità: CatalogueRecordDCAT-AP  
==============================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/CatalogueRecordDCAT-AP/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questo è un record di catalogo appartenente a un set di dati secondo lo standard DCAT-AP 2.0.1**  
versione: 0.0.1  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `applicationProfile`: Questa proprietà si riferisce a un profilo di applicazione a cui i metadati del dataset sono conformi  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `changeType`: Questa proprietà si riferisce al tipo dell'ultima revisione della voce di un dataset nel catalogo.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `language`: Questa proprietà si riferisce a una lingua usata nei metadati testuali che descrivono titoli, descrizioni, ecc. del dataset. Questa proprietà può essere ripetuta se i metadati sono forniti in più lingue  - `listingDate`: Questa proprietà contiene la data in cui la descrizione del dataset è stata inclusa nel catalogo.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `modificationDate`: Questa proprietà contiene la data più recente in cui la voce del catalogo è stata cambiata o modificata.  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `primaryTopic`: Questa proprietà collega il record del catalogo al dataset, al servizio dati o al catalogo descritto nel record.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `sourceMetadata`: Questa proprietà si riferisce ai metadati originali che sono stati usati nella creazione dei metadati per il dataset.  - `title`: Questa proprietà contiene un nome dato al record del catalogo. Questa proprietà può essere ripetuta per le versioni in lingue parallele del nome.  - `type`: Tipo di entità NGSI. Deve essere CatalogueRecordDCAT-AP    
Proprietà richieste  
- `id`  - `modificationDate`  - `primaryTopic`  - `type`    
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf).  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CatalogueRecordDCAT-AP:    
  description: 'This is a Catalogue Record belonging to a dataset according to the DCAT-AP standard 2.0.1'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    applicationProfile:    
      description: 'This property refers to an Application Profile that the Dataset’s metadata conforms to'    
      type: string    
      x-ngsi:    
        model: dct:conformsTo    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    changeType:    
      description: 'This property refers to the type of the latest revision of a Dataset''s entry in the Catalogue.'    
      type: string    
      x-ngsi:    
        model: adms:status    
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
    id:    
      anyOf: &cataloguerecorddcat-ap_-_properties_-_owner_-_items_-_anyof    
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
      description: 'This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Dataset. This property can be repeated if the metadata is provided in multiple languages'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dct:language    
        type: Property    
    listingDate:    
      description: 'This property contains the date on which the description of the Dataset was included in the Catalogue.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: dct:issued    
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
    modificationDate:    
      description: 'This property contains the most recent date on which the Catalogue entry was changed or modified..'    
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
        anyOf: *cataloguerecorddcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    primaryTopic:    
      description: 'This property links the Catalogue Record to the Dataset, Data service or Catalog described in the record.'    
      type: string    
      x-ngsi:    
        model: foaf:primaryTopic    
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
    sourceMetadata:    
      description: 'This property refers to the original metadata that was used in creating metadata for the Dataset.'    
      type: string    
      x-ngsi:    
        model: dct:source    
        type: Property    
    title:    
      description: 'This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be CatalogueRecordDCAT-AP'    
      enum:    
        - CatalogueRecordDCAT-AP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - primaryTopic    
    - modificationDate    
  type: object    
  version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### CatalogueRecordDCAT-AP NGSI-v2 valori chiave Esempio  
Ecco un esempio di un CatalogueRecordDCAT-AP in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": "2020-11-02T21:25:54Z",  
  "dateModified": "2021-07-02T18:37:55Z",  
  "source": "",  
  "name": "",  
  "alternateName": "",  
  "description": "Catalogue record of the solar system open data portal",  
  "dataProvider": "european open data portal",  
  "owner": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
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
  "modificationDate": "2021-07-02T18:37:55Z",  
  "applicationProfile": "DCAT Application profile for data portals in Europe",  
  "changeType": "First version",  
  "listingDate": "2021-07-02T18:37:55Z",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "sourceMetadata": "",  
  "title": [  
    "Example of catalogue record",  
    "Ejemplo de registro de catálogo"  
  ]  
}  
```  
#### CatalogueRecordDCAT-AP NGSI-v2 normalizzato Esempio  
Ecco un esempio di un CatalogueRecordDCAT-AP in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-11-02T21:25:54Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Catalogue record of the solar system open data portal"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "european open data portal"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
    ]  
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
    "type": "PostalAdress",  
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
  "modificationDate": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "applicationProfile": {  
    "type": "Text",  
    "value": "DCAT Application profile for data portals in Europe"  
  },  
  "changeType": {  
    "type": "Text",  
    "value": "First version"  
  },  
  "listingDate": {  
    "type": "DateTime",  
    "value": "2021-07-02T18:37:55Z"  
  },  
  "language": {  
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "sourceMetadata": {  
    "type": "Text",  
    "value": ""  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Example of catalogue record",  
      "Ejemplo de registro de catálogo"  
    ]  
  }  
}  
```  
#### CatalogueRecordDCAT-AP NGSI-LD valori chiave Esempio  
Ecco un esempio di un CatalogueRecordDCAT-AP in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": "2020-11-02T21:25:54Z",  
  "dateModified": "2021-07-02T18:37:55Z",  
  "source": "",  
  "name": "",  
  "alternateName": "",  
  "description": "Catalogue record of the solar system open data portal",  
  "dataProvider": "european open data portal",  
  "owner": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
    "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
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
  "modificationDate": "2021-07-02T18:37:55Z",  
  "applicationProfile": "DCAT Application profile for data portals in Europe",  
  "changeType": "First version",  
  "listingDate": "2021-07-02T18:37:55Z",  
  "language": [  
    "EN",  
    "ES"  
  ],  
  "sourceMetadata": "",  
  "title": [  
    "Example of catalogue record",  
    "Ejemplo de registro de catÃ¡logo"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### CatalogueRecordDCAT-AP NGSI-LD normalizzato Esempio  
Ecco un esempio di un CatalogueRecordDCAT-AP in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:CatalogueRecordDCAT-AP:id:KFTL:88140679",  
  "type": "CatalogueRecordDCAT-AP",  
  "dateCreated": {  
    "type": {  
      "@type": "Property",  
      "@value": "2020-11-02T21:25:54Z"  
    }  
  },  
  "dateModified": {  
    "type": {  
      "@type": "Property",  
      "@value": "2021-07-02T18:37:55Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Catalogue record of the solar system open data portal"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "european open data portal"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:ISXP:07320625",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:BQMW:23610768"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:FVCU:03753474",  
      "urn:ngsi-ld:CatalogueRecordDCAT-AP:items:AIEC:73224831"  
    ]  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        36.633152,  
        -85.183315  
      ]  
    }  
  },  
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
  "areaServed": {  
    "type": "Property",  
    "value": "European Union and beyond"  
  },  
  "primaryTopic": {  
    "type": "Property",  
    "value": "Public administration"  
  },  
  "modificationDate": {  
    "type": {  
      "@type": "Property",  
      "@value": "2021-07-02T18:37:55Z"  
    }  
  },  
  "applicationProfile": {  
    "type": "Property",  
    "value": "DCAT Application profile for data portals in Europe"  
  },  
  "changeType": {  
    "type": "Property",  
    "value": "First version"  
  },  
  "listingDate": {  
    "type": {  
      "@type": "Property",  
      "@value": "2021-07-02T18:37:55Z"  
    }  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "sourceMetadata": {  
    "type": "Property",  
    "value": ""  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "Example of catalogue record",  
      "Ejemplo de registro de catÃ¡logo"  
    ]  
  }  
}  
```  
