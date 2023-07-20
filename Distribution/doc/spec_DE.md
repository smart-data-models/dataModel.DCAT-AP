<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Vertrieb  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Distribution/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Dies ist eine Verteilung, die zu einem Datensatz nach dem DCAT-AP Standard 2.1.1** gehört  
Version: 1.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `accessService[array]`: Eigenschaft. Model:'http://www.w3.org/ns/dcat#DataService'. Diese Eigenschaft verweist auf einen Datendienst, der den Zugang zur Verteilung des Datensatzes ermöglicht  . Model: [http://www.w3.org/ns/dcat#DataService](http://www.w3.org/ns/dcat#DataService)- `accessUrl[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. Diese Eigenschaft enthält eine URL, die den Zugriff auf eine Verteilung des Datensatzes ermöglicht. Die Ressource unter der Zugriffs-URL kann Informationen darüber enthalten, wie man den Datensatz erhält.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: Eigenschaft. Model:'http://www.w3.org/2004/02/skos/core#Concept'. Diese Eigenschaft gibt an, wie lange das Distributio des Datensatzes verfügbar bleiben soll.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `byteSize[number]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält die Größe einer Verteilung in Bytes.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `checksum[string]`: Eigenschaft. Model:'http://spdx.org/rdf/terms#Checksum'. Diese Eigenschaft bietet einen Mechanismus, mit dem überprüft werden kann, ob sich der Inhalt einer Distribution nicht geändert hat. Die Prüfsumme bezieht sich auf die downloadURL.  . Model: [http://spdx.org/rdf/terms#Checksum](http://spdx.org/rdf/terms#Checksum)- `compressionFormat[string]`: Eigenschaft. Modell:'http://purl.org/dc/terms/MediaType'. Diese Eigenschaft bezieht sich auf das Format der Datei, in der die Daten in komprimierter Form enthalten sind, z. B. um die Größe der herunterladbaren Datei zu verringern. Sie SOLLTE durch einen Medientyp ausgedrückt werden, der im offiziellen, von der IANA verwalteten Register der Medientypen definiert ist  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `conformsTo[array]`: Eigenschaft. Model:'"http://purl.org/dc/terms/Standard". Diese Eigenschaft verweist auf ein etabliertes Schema, dem die beschriebene Verteilung entspricht.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `description[array]`: Eigenschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält eine Freitextbeschreibung der Verteilung. Diese Eigenschaft kann für parallele Sprachversionen der Beschreibung wiederholt werden.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `downloadURL[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. Diese Eigenschaft enthält eine URL, die einen direkten Link zu einer herunterladbaren Datei in einem bestimmten Format darstellt.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `format[string]`: Eigenschaft. Model:'https://schema.org/Text'. Diese Eigenschaft bezieht sich auf das Dateiformat der Verteilung.  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasPolicy[string]`: Eigenschaft. Modell:'http://www.w3.org/ns/odrl/2/hasPolicy'. Diese Eigenschaft bezieht sich auf die Richtlinie, die die mit der Verteilung verbundenen Rechte bei Verwendung des ODRL-Vokabulars ausdrückt  . Model: [http://www.w3.org/ns/odrl/2/hasPolicy](http://www.w3.org/ns/odrl/2/hasPolicy)- `issued[string]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält das Datum der offiziellen Ausgabe (z. B. Veröffentlichung) der Verteilung.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `language[array]`: Eigenschaft. Model:'http://purl.org/dc/terms/LinguisticSystem'. Diese Eigenschaft bezieht sich auf eine in der Verteilung verwendete Sprache. Diese Eigenschaft kann wiederholt werden, wenn die Metadaten in mehreren Sprachen bereitgestellt werden.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: Eigenschaft. Model:'http://purl.org/dc/terms/LicenseDocument'. Diese Eigenschaft verweist auf einen Datendienst, der den Zugang zur Verteilung des Datensatzes ermöglicht  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mediaType[string]`: Eigenschaft. Modell:'http://purl.org/dc/terms/MediaType'. Diese Eigenschaft bezieht sich auf den Medientyp der Verteilung, wie er im offiziellen, von der IANA verwalteten Register der Medientypen definiert ist  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `modified[string]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält das letzte Datum, an dem die Verteilung geändert oder modifiziert wurde.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `packageFormat[string]`: Eigenschaft. Model:'http://purl.org/dc/terms/MediaType'. Diese Eigenschaft bezieht sich auf das Dateiformat, in dem eine oder mehrere Datendateien gruppiert sind, z. B. um einen Satz zusammengehöriger Dateien gemeinsam herunterladen zu können. Sie SOLLTE durch einen Medientyp ausgedrückt werden, der im offiziellen, von der IANA verwalteten Register der Medientypen definiert ist  . Model: [http://purl.org/dc/terms/MediaType](http://purl.org/dc/terms/MediaType)- `page[array]`: Eigenschaft. Model:'https://schema.org/Text'. Diese Eigenschaft verweist auf eine Seite oder ein Dokument über diese Verteilung.  . Model: [https://schema.org/Text](https://schema.org/Text)- `rights[string]`: Eigenschaft. Modell:'http://purl.org/dc/terms/RightsStatement'. Diese Eigenschaft bezieht sich auf eine Erklärung, die die mit der Verteilung verbundenen Rechte angibt.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `spatialResolutionInMeters[array]`: Eigenschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft bezieht sich auf den minimalen räumlichen Abstand, der in einer Verteilung auflösbar ist, gemessen in Metern.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `status[string]`: Eigenschaft. Modell:'http://www.w3.org/2004/02/skos/core#Concept'. Diese Eigenschaft bezieht sich auf den Reifegrad der Verteilung. Sie MUSS einen der Werte Completed, Deprecated, Under Development, Withdrawn annehmen  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `temporalResolution[string]`: Eigenschaft. Model:'http://www.w3.org/2001/XMLSchema#duration'. Diese Eigenschaft bezieht sich auf den Mindestzeitraum, der im Datensatz auflösbar ist.  . Model: [http://www.w3.org/2001/XMLSchema#duration](http://www.w3.org/2001/XMLSchema#duration)- `title[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält einen Namen, der der Verteilung gegeben wird. Diese Eigenschaft kann für parallele Sprachversionen der Beschreibung wiederholt werden.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Eigenschaft. NGSI-Entitätstyp. Es muss Verteilung sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `accessURL`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Angepasst von [DCAT-AP Version 2.1.1] (https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Distribution:    
  description: This is a distribution belonging ot a dataset according to the DCAT-AP standard 2.1.1    
  properties:    
    accessService:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#DataService'. This property refers to a data service that gives access to the distribution of the dataset"    
      items:    
        description: Property. Every Data service providing access to the distribution    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#DataService"    
        type: Property    
    accessUrl:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset."    
      items:    
        minItems: 1    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Property    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      description: "Property. Model:'http://www.w3.org/2004/02/skos/core#Concept'. This property indicates how long it is planned to keep the Distributio of the Dataset available."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    byteSize:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the size of a Distribution in bytes."    
      type: number    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    checksum:    
      description: "Property. Model:'http://spdx.org/rdf/terms#Checksum'. This property provides a mechanism that can be used to verify that the contents of a distribution have not changed. The checksum is related to the downloadURL."    
      type: string    
      x-ngsi:    
        model: "http://spdx.org/rdf/terms#Checksum"    
        type: Property    
    compressionFormat:    
      description: 'Property. Model:''http://purl.org/dc/terms/MediaType''. This property refers to the format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    conformsTo:    
      description: 'Property. Model:''"http://purl.org/dc/terms/Standard''. This property refers to an established schema to which the described Distribution conforms.'    
      items:    
        description: Property. Every rule o standard the distribution complies with    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    description:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a free-text account of the Distribution. This property can be repeated for parallel language versions of the description."    
      items:    
        description: Property. Every description of the distribution in a language    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    downloadURL:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. This property contains a URL that is a direct link to a downloadable file in a given format."    
      items:    
        description: Property. Every URL available for downloading    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Property    
    format:    
      description: 'Property. Model:''https://schema.org/Text''. This property refers to the file format of the Distribution.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hasPolicy:    
      description: 'Property. Model:''http://www.w3.org/ns/odrl/2/hasPolicy''. This property refers to the policy expressing the rights associated with the distribution if using the ODRL vocabulary'    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/ns/odrl/2/hasPolicy    
        type: Property    
    issued:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the date of formal issuance (e.g., publication) of the Distribution."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    language:    
      description: 'Property. Model:''http://purl.org/dc/terms/LinguisticSystem''. This property refers to a language used in the Distribution. This property can be repeated if the metadata is provided in multiple languages.'    
      items:    
        description: Property. Every language included    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    license:    
      description: 'Property. Model:''http://purl.org/dc/terms/LicenseDocument''. This property refers to a data service that gives access to the distribution of the dataset'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/LicenseDocument    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    mediaType:    
      description: 'Property. Model:''http://purl.org/dc/terms/MediaType''. This property refers to the media type of the Distribution as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    modified:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the most recent date on which the Distribution was changed or modified."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    packageFormat:    
      description: 'Property. Model:''http://purl.org/dc/terms/MediaType''. This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/MediaType    
        type: Property    
    page:    
      description: 'Property. Model:''https://schema.org/Text''. This property refers to a page or document about this Distribution.'    
      items:    
        description: Property. Every page providing information about the distribution    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    rights:    
      description: 'Property. Model:''http://purl.org/dc/terms/RightsStatement''. This property refers to a statement that specifies rights associated with the Distribution.'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    spatialResolutionInMeters:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property refers to the minimum spatial separation resolvable in a distribution, measured in meters."    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    status:    
      description: "Property. Model:'http://www.w3.org/2004/02/skos/core#Concept'. This property refers to the maturity of the Distribution. It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn"    
      enum:    
        - Completed    
        - Deprecated    
        - Under Development    
        - Withdrawn    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    temporalResolution:    
      description: "Property. Model:'http://www.w3.org/2001/XMLSchema#duration'. This property refers to the minimum time period resolvable in the dataset. "    
      format: duration    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2001/XMLSchema#duration"    
        type: Property    
    title:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a name given to the Distribution. This property can be repeated for parallel language versions of the description."    
      items:    
        description: Property. Every language description of the distribution title    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    type:    
      description: Property. NGSI entity type. It has to be Distribution    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Distribution/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Distribution/schema.json    
  x-model-tags: ""    
  x-version: 1.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Verteilung NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Verteilung im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  "description": [  
    "Distribution of open data portals in csv"],  
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
  "temporalResolution":  
    "PT15M",  
  "title": [  
    "Dataset base"  
  ]  
}  
```  
</details>  
#### Verteilung NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine Verteilung im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Distribution:id:NUZE:76215118",  
  "type": "Distribution",  
  "description": {  
    "type": "Text",  
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
    "type": "PostalAddress",  
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
    "type": "array",  
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
    "type": "array",  
    "value": [  
      ""  
    ]  
  },  
  "byteSize": {  
    "type": "array",  
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
  "page": {  
    "type": "array",  
    "value": [  
    ]  
  },  
  "downloadURL": {  
    "type": "array",  
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
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "conformsTo": {  
    "type": "array",  
    "value": [  
    ]  
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
    "type": "array",  
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
    "type": "array",  
    "value": "PT17S"  
  },  
  "title": {  
    "type": "array",  
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
#### Verteilung NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Verteilung im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Verteilung NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine Verteilung im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
