<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: Katalog    
================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Catalogue/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Katalog der Datensätze, die mit der DCAT-AP-Spezifikation Version 2.1.1.** übereinstimmen    
Version: 1.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `catalog[array]`: Diese Eigenschaft verweist auf einen Katalog, dessen Inhalt im Zusammenhang mit diesem Katalog von Interesse ist  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `creator[array]`: Die für die Erstellung des Katalogs hauptverantwortlichen Stellen  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `dataset[array]`: Diese Eigenschaft verknüpft den Katalog mit einem Datensatz, der Teil des Katalogs ist  . Model: [http://www.w3.org/ns/dcat#dataset](http://www.w3.org/ns/dcat#dataset)- `description[array]`: Diese Eigenschaft enthält eine Freitextbeschreibung des Katalogs. Diese Eigenschaft kann für parallele Sprachversionen der Beschreibung wiederholt werden. Weitere Informationen zu mehrsprachigen Themen finden Sie in Abschnitt 8 des pdf-Dokuments https://codeload.github.com/SEMICeu/DCAT-AP/zip/refs/tags/v2.1.1  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `hasPart[array]`: Diese Eigenschaft verweist auf einen verwandten Katalog, der Teil des beschriebenen Katalogs ist  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `homepage[uri]`: Diese Eigenschaft verweist auf eine Webseite, die als Hauptseite für den Katalog dient  . Model: [http://xmlns.com/foaf/0.1/homepage](http://xmlns.com/foaf/0.1/homepage)- `id[*]`: Eindeutiger Bezeichner der Entität  - `isPartOf[uri]`: Diese Eigenschaft bezieht sich auf einen verwandten Katalog, in dem der beschriebene Katalog physisch oder logisch enthalten ist  . Model: [http://www.w3.org/ns/dcat#Catalog](http://www.w3.org/ns/dcat#Catalog)- `issued[date-time]`: Diese Eigenschaft enthält das Datum der förmlichen Herausgabe (z. B. der Veröffentlichung) des Katalogs  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: Diese Eigenschaft bezieht sich auf eine Sprache, die in den textlichen Metadaten verwendet wird, die Titel, Beschreibungen usw. der Datensätze im Katalog beschreiben. Diese Eigenschaft kann wiederholt werden, wenn die Metadaten in mehreren Sprachen bereitgestellt werden  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: Diese Eigenschaft bezieht sich auf die Lizenz, unter der der Katalog verwendet oder wiederverwendet werden kann  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `modified[date-time]`: Diese Eigenschaft enthält das letzte Datum, an dem der Katalog geändert wurde  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `publisher[string]`: Diese Eigenschaft bezieht sich auf eine Einrichtung (Organisation), die für die Bereitstellung des Katalogs verantwortlich ist  . Model: [http://xmlns.com/foaf/0.1/#term_Agent](http://xmlns.com/foaf/0.1/#term_Agent)- `record[array]`: Diese Eigenschaft bezieht sich auf einen Katalogsatz, der Teil des Katalogs ist  . Model: [http://www.w3.org/ns/dcat#CatalogRecord](http://www.w3.org/ns/dcat#CatalogRecord)- `rights[string]`: Diese Eigenschaft bezieht sich auf eine Erklärung, die die mit dem Katalog verbundenen Rechte angibt  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `service[array]`: Diese Eigenschaft bezieht sich auf einen Standort oder Endpunkt (Datendienst), der im Katalog aufgeführt ist. Da leere Kataloge in der Regel auf Probleme hinweisen, sollte diese Eigenschaft mit dem vorherigen Eigenschaftsdatensatz kombiniert werden, um eine Prüfung auf leere Kataloge zu implementieren  . Model: [http://www.w3.org/ns/dcat#DataService](http://www.w3.org/ns/dcat#DataService)- `spatial[array]`: Diese Eigenschaft bezieht sich auf ein geografisches Gebiet, das durch den Katalog abgedeckt wird  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `themeTaxonomy[array]`: Diese Eigenschaft bezieht sich auf ein Wissensorganisationssystem, das zur Klassifizierung der Datensätze des Katalogs verwendet wird  . Model: [http://www.w3.org/2004/02/skos/core#ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)- `title[array]`: Diese Eigenschaft enthält einen Namen, der dem Katalog gegeben wurde. Diese Eigenschaft kann für parallele Sprachversionen des Namens wiederholt werden  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Es muss ein Katalog sein  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `description`  - `id`  - `publisher`  - `title`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Datenmodell und andere des Themas DCAT-AP werden für ihre Verwendung angepasst und es wird empfohlen, dass zusätzlicher Kontext aufgenommen wird. [https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld" ](https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### Katalog NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für einen Katalog im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
  "creator": [  
    ""  
  ]  
}  
```  
</details>    
#### Katalog NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen Katalog im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
      "postOfficeBoxNumber": "",  
      "areaServed": "European Union"  
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
  "licence": {  
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
#### Katalog NGSI-LD-Schlüsselwerte Beispiel    
Hier ist ein Beispiel für einen Katalog im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
    "postOfficeBoxNumber": "",  
    "areaServed": "European Union"  
  },  
  "catalogue": [  
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
#### Katalog NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen Katalog im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
