<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Datensatz  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Datensatzschema gemäß DCAT-AP 2.1.1 Spezifikation**  
Version: 2.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `Type[string]`: Eigenschaft. Model:'http://www.w3.org/2004/02/skos/core#Concept'. Diese Eigenschaft bezieht sich auf den Typ des Datasets. Vorgesehen ist ein empfohlener Datentyp des kontrollierten Vokabulars.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `accessRights[string]`: Eigenschaft. Model:'http://purl.org/dc/terms/RightsStatement'. Diese Eigenschaft bezieht sich auf Informationen, die angeben, ob es sich bei dem Datensatz um offene Daten handelt, ob es Zugangsbeschränkungen gibt oder ob er nicht öffentlich ist.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `accrualPeriodicity[string]`: Eigenschaft. Model:'http://purl.org/dc/terms/Frequency'. Diese Eigenschaft bezieht sich auf die Häufigkeit, mit der der Datensatz aktualisiert wird.  . Model: [http://purl.org/dc/terms/Frequency](http://purl.org/dc/terms/Frequency)- `conformsTo[array]`: Eigenschaft. Model:'http://purl.org/dc/terms/Standard'. Diese Eigenschaft bezieht sich auf eine Durchführungsvorschrift oder eine andere Spezifikation.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `contactPoint[array]`: Eigenschaft. Model:'http://www.w3.org/2006/vcard/ns#Kind'. Diese Eigenschaft enthält Kontaktinformationen, die für die Übermittlung von Kommentaren zu dem Datensatz verwendet werden können.  . Model: [http://www.w3.org/2006/vcard/ns#Kind](http://www.w3.org/2006/vcard/ns#Kind)- `creator[array]`: Eigenschaft. Modell:'http://xmlns.com/foaf/0.1/Agent'. Diese Eigenschaft bezieht sich auf die für die Erstellung des Datensatzes hauptverantwortliche Stelle.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `description[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält eine Freitextbeschreibung des Datensatzes. Diese Eigenschaft kann für parallele Sprachversionen der Beschreibung wiederholt werden.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `distribution[array]`: Verknüpfung. Diese Eigenschaft verknüpft das Dataset mit einer verfügbaren Verteilung. Modell:'http://www.w3.org/ns/dcat#Distribution'  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `hasVersion[array]`: Eigenschaft. Model:'http://www.w3.org/ns/dcat#Dataset'. Diese Eigenschaft bezieht sich auf einen verwandten Datensatz, der eine Version, Ausgabe oder Anpassung des beschriebenen Datensatzes ist.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `id[*]`: Eindeutiger Bezeichner der Entität  - `identifier[array]`: Eigenschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält den Hauptbezeichner für den Datensatz, z. B. den URI oder einen anderen eindeutigen Bezeichner im Kontext des Katalogs.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `isReferencedBy[array]`: Verwandtschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Resource'. Diese Eigenschaft bezieht sich auf eine verwandte Ressource, z. B. eine Veröffentlichung, die auf den Datensatz verweist, ihn zitiert oder anderweitig auf ihn verweist.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `isVersionOf[array]`: Eigenschaft. Model:'http://www.w3.org/ns/dcat#Dataset'. Diese Eigenschaft bezieht sich auf einen verwandten Datensatz, von dem der beschriebene Datensatz eine Version, Ausgabe oder Anpassung ist.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `issued[string]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält das Datum der offiziellen Ausgabe (z. B. Veröffentlichung) des Datensatzes.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `keyword[array]`: Eigenschaft. Diese Eigenschaft enthält ein Schlüsselwort oder Tag, das den Datensatz beschreibt. Modell:'http://www.w3.org/2000/01/rdf-schema#Literal'.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal.](http://www.w3.org/2000/01/rdf-schema#Literal.)- `landingPage[array]`: Eigenschaft. Modell:'http://xmlns.com/foaf/0.1/Document'. Diese Eigenschaft verweist auf eine Webseite, die Zugang zu dem Datensatz, seinen Verteilungen und/oder zusätzlichen Informationen bietet. Sie soll auf eine Landing Page beim ursprünglichen Datenanbieter verweisen, nicht auf eine Seite auf der Website eines Dritten, z. B. eines Aggregators.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `language[array]`: Eigenschaft. Model:'http://purl.org/dc/terms/LinguisticSystem'. Diese Eigenschaft bezieht sich auf eine Sprache des Datasets. Diese Eigenschaft kann wiederholt werden, wenn der Datensatz mehrere Sprachen enthält.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `modified[string]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält das jüngste Datum, an dem der Datensatz geändert oder modifiziert wurde.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `otherIdentifier[array]`: Eigenschaft. Modell:'http://www.w3.org/ns/adms#Identifier'. Diese Eigenschaft bezieht sich auf einen sekundären Identifikator des Datensatzes, wie MAST/ADS, DataCite, DOI, EZID oder W3ID.  . Model: [http://www.w3.org/ns/adms#Identifier](http://www.w3.org/ns/adms#Identifier)- `page[array]`: Eigenschaft. Model:'http://xmlns.com/foaf/0.1/Document'. Diese Eigenschaft verweist auf eine Seite oder ein Dokument über diesen Datensatz.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `provenance[array]`: Eigenschaft. Model:'http://purl.org/dc/terms/ProvenanceStatement'. Diese Eigenschaft enthält eine Aussage über die Abstammung eines Datasets.  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: Eigenschaft. Modell:'http://xmlns.com/foaf/0.1/Agent'. Diese Eigenschaft bezieht sich auf eine Einrichtung (Organisation), die für die Bereitstellung des Datensatzes verantwortlich ist.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `qualifiedAttribution[array]`: Eigenschaft. Modell:'http://www.w3.org/ns/dcat#Relationship'. Diese Eigenschaft verweist auf einen Link zu einem Agenten, der in irgendeiner Form für die Ressource verantwortlich ist  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `qualifiedRelation[array]`: Eigenschaft. Modell:'http://www.w3.org/ns/dcat#Relationship'. Diese Eigenschaft bietet einen Link zu einer Beschreibung einer Beziehung zu einer anderen Ressource.  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `relatedResource[array]`: Eigenschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Resource'. Diese Eigenschaft verweist auf eine verwandte Ressource.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `sample[array]`: Eigenschaft. Modell:'http://www.w3.org/ns/dcat#Distribution'. Diese Eigenschaft bezieht sich auf eine Stichprobenverteilung des Datensatzes.  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `source[array]`: Eigenschaft. Model:'http://www.w3.org/ns/dcat#Dataset'. Diese Eigenschaft verweist auf einen verwandten Datensatz, von dem der beschriebene Datensatz abgeleitet ist.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `spatial[array]`: GeoProperty. Model:'http://purl.org/dc/terms/Location'. Diese Eigenschaft bezieht sich auf eine geografische Region, die durch den Datensatz abgedeckt wird.  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `spatialResolutionInMeters[number]`: Eigenschaft. Modell:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft bezieht sich auf den minimalen räumlichen Abstand, der in einem Datensatz auflösbar ist, gemessen in Metern.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `temporal[array]`: Eigenschaft. Diese Eigenschaft bezieht sich auf einen zeitlichen Zeitraum, den der Datensatz abdeckt. Modell:'http://purl.org/dc/terms/PeriodOfTime'.  . Model: [http://purl.org/dc/terms/PeriodOfTime.](http://purl.org/dc/terms/PeriodOfTime.)- `temporalResolution[array]`: Eigenschaft. Model:'http://purl.org/dc/terms/PeriodOfTime'. Diese Eigenschaft bezieht sich auf den Mindestzeitraum, der im Datensatz auflösbar ist.  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `theme[array]`: Eigenschaft. Model:'http://www.w3.org/2004/02/skos/core#Concept'. Diese Eigenschaft bezieht sich auf eine Kategorie des Datasets. Ein Dataset kann mit mehreren Themen verknüpft sein.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält einen Namen für den Datensatz. Diese Eigenschaft kann für parallele Sprachversionen des Namens wiederholt werden.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Eigenschaft. NGSI-Typ. Es muss Dataset sein  - `version[string]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält eine Versionsnummer oder eine andere Versionsbezeichnung des Datasets.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `versionNotes[array]`: Eigenschaft. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. Diese Eigenschaft enthält eine Beschreibung der Unterschiede zwischen dieser Version und einer früheren Version des Datensatzes. Diese Eigenschaft kann für parallele Sprachversionen der Versionshinweise wiederholt werden.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `wasGeneratedBy[array]`: Eigenschaft. Model:'https://www.w3.org/ns/prov#Activity'. Diese Eigenschaft bezieht sich auf eine Aktivität, die die Erstellung des Datensatzes generiert hat oder den geschäftlichen Kontext für die Erstellung des Datensatzes liefert.  . Model: [https://www.w3.org/ns/prov#Activity](https://www.w3.org/ns/prov#Activity)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `description`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
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
Dataset:    
  description: Dataset Schema meeting DCAT-AP 2.1.1 specification    
  properties:    
    Type:    
      description: "Property. Model:'http://www.w3.org/2004/02/skos/core#Concept'. This property refers to the type of the Dataset. A recommended controlled vocabulary data-type is foreseen."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    accessRights:    
      description: 'Property. Model:''http://purl.org/dc/terms/RightsStatement''. This property refers to information that indicates whether the Dataset is open data, has access restrictions or is not public.'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    accrualPeriodicity:    
      description: 'Property. Model:''http://purl.org/dc/terms/Frequency''. This property refers to the frequency at which the Dataset is updated.'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/Frequency    
        type: Property    
    conformsTo:    
      description: 'Property. Model:''http://purl.org/dc/terms/Standard''. This property refers to an implementing rule or other specification. '    
      items:    
        description: Property. Every rule or specification applicable    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    contactPoint:    
      description: "Property. Model:'http://www.w3.org/2006/vcard/ns#Kind'. This property contains contact information that can be used for sending comments about the Dataset."    
      items:    
        description: Property. Every contact element    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2006/vcard/ns#Kind"    
        type: Property    
    creator:    
      description: 'Property. Model:''http://xmlns.com/foaf/0.1/Agent''. This property refers to the entity primarily responsible for producing the dataset.'    
      items:    
        description: Property. Every creator included    
        type: string    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    description:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a free-text account of the Dataset. This property can be repeated for parallel language versions of the description."    
      items:    
        description: Property. Every description in a language    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    distribution:    
      description: "Relationship. This property links the Dataset to an available Distribution. Model:'http://www.w3.org/ns/dcat#Distribution'"    
      items:    
        description: Property. Every link to a distribution    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Distribution"    
        type: Relationship    
    hasVersion:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Dataset'. This property refers to a related Dataset that is a version, edition, or adaptation of the described Dataset."    
      items:    
        description: Property. Every version of the related datasets    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    id:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    identifier:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue."    
      items:    
        description: Property. Every identifier of the dataset    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    isReferencedBy:    
      description: "Relationship. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. This property is about a related resource, such as a publication, that references, cites, or otherwise points to the dataset."    
      items:    
        description: Property. Every resource related to the dataset    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Relationship    
    isVersionOf:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Dataset'. This property refers to a related Dataset of which the described Dataset is a version, edition, or adaptation."    
      items:    
        description: Property. Every dataset that the current dataset is a version of it    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    issued:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the date of formal issuance (e.g., publication) of the Dataset."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    keyword:    
      description: "Property. This property contains a keyword or tag, describing the Dataset. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'."    
      items:    
        description: Property. Every keyword tag included    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal."    
        type: Property    
    landingPage:    
      description: 'Property. Model:''http://xmlns.com/foaf/0.1/Document''. This property refers to a web page that provides access to the Dataset, its Distributions and/or additional information. It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator.'    
      items:    
        description: Property. Every web page listed    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Property    
    language:    
      description: 'Property. Model:''http://purl.org/dc/terms/LinguisticSystem''. This property refers to a language of the Dataset. This property can be repeated if there are multiple languages in the Dataset.'    
      items:    
        description: Property. Every language included    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    modified:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains the most recent date on which the Dataset was changed or modified."    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    otherIdentifier:    
      description: "Property. Model:'http://www.w3.org/ns/adms#Identifier'. This property refers to a secondary identifier of the Dataset, such as MAST/ADS, DataCite, DOI, EZID or W3ID."    
      items:    
        description: Property. Every additional identifier included    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/adms#Identifier"    
        type: Property    
    page:    
      description: 'Property. Model:''http://xmlns.com/foaf/0.1/Document''. This property refers to a page or document about this Dataset. '    
      items:    
        description: Property. Every page or document    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Property    
    provenance:    
      description: 'Property. Model:''http://purl.org/dc/terms/ProvenanceStatement''. This property contains a statement about the lineage of a Dataset.'    
      items:    
        description: Property. Every lineage associated to the dataset    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/ProvenanceStatement    
        type: Property    
    publisher:    
      description: 'Property. Model:''http://xmlns.com/foaf/0.1/Agent''. This property refers to an entity (organisation) responsible for making the Dataset available.'    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    qualifiedAttribution:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Relationship'. This property refers to a link to an Agent having some form of responsibility for the resource"    
      items:    
        description: Property. Every attribution included    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Relationship"    
        type: Property    
    qualifiedRelation:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Relationship'. This property provides a link to a description of a relationship with another resource."    
      items:    
        description: Property. Every qualified relation included    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Relationship"    
        type: Property    
    relatedResource:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Resource'. This property refers to a related resource."    
      items:    
        description: Property. Every related resource included    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Property    
    sample:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Distribution'. This property refers to a sample distribution of the dataset."    
      items:    
        description: Property. Every sample included with the dataset    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Distribution"    
        type: Property    
    source:    
      description: "Property. Model:'http://www.w3.org/ns/dcat#Dataset'. This property refers to a related Dataset from which the described Dataset is derived."    
      items:    
        description: Property. Every dataset which is a source of the current dataset    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    spatial:    
      description: 'GeoProperty. Model:''http://purl.org/dc/terms/Location''. This property refers to a geographic region that is covered by the Dataset.'    
      items:    
        description: 'GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
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
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Location    
        type: GeoProperty    
    spatialResolutionInMeters:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property refers to the minimum spatial separation resolvable in a dataset, measured in meters."    
      type: number    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    temporal:    
      description: 'Property. This property refers to a temporal period that the Dataset covers. Model:''http://purl.org/dc/terms/PeriodOfTime''.'    
      items:    
        description: Property. Every temporal period included    
        format: date-time    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime.    
        type: Property    
    temporalResolution:    
      description: 'Property. Model:''http://purl.org/dc/terms/PeriodOfTime''. This property refers to the minimum time period resolvable in the dataset. '    
      items:    
        description: Property. Every temporal resolution included    
        format: duration    
        type: string    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime    
        type: Property    
    theme:    
      description: "Property. Model:'http://www.w3.org/2004/02/skos/core#Concept'. This property refers to a category of the Dataset. A Dataset may be associated with multiple themes."    
      items:    
        description: Property. Every theme included    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    title:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a name given to the Dataset. This property can be repeated for parallel language versions of the name."    
      items:    
        description: Property. Every title in a language    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    type:    
      description: Property. NGSI type. It has to be Dataset    
      enum:    
        - Dataset    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a version number or other version designation of the Dataset."    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    versionNotes:    
      description: "Property. Model:'http://www.w3.org/2000/01/rdf-schema#Literal'. This property contains a description of the differences between this version and a previous version of the Dataset. This property can be repeated for parallel language versions of the version notes."    
      items:    
        description: Property. Every language description of the version notes    
        type: string    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    wasGeneratedBy:    
      description: "Property. Model:'https://www.w3.org/ns/prov#Activity'. This property refers to an activity that generated, or provides the business context for, the creation of the dataset."    
      items:    
        description: Property. Every activity included    
        type: string    
      type: array    
      x-ngsi:    
        model: "https://www.w3.org/ns/prov#Activity"    
        type: Property    
  required:    
    - id    
    - type    
    - description    
    - title    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Dataset/schema.json    
  x-model-tags: INTERSTAT    
  x-version: 2.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Datensatz NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Datensatz im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:VESI:23278568",  
  "type": "Dataset",  
  "modified": "2015-07-13T03:09:32Z",  
  "source": [  
    "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  ],  
  "description": [  
    "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid."  
  ],  
  "title": [  
    "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid"  
  ],  
  "contactPoint": [  
    "https://datos.gob.es/es/comment/reply/145778."  
  ],  
  "distribution": [  
    "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
  ],  
  "keyword": [  
    "alojamiento",  
    "apartamento rural",  
    "apartamento turístico",  
    "campamento de turismo",  
    "camping",  
    "casa rural",  
    "casas de huéspedes",  
    "hostal",  
    "hostel",  
    "hosteria",  
    "hotel",  
    "hotel rural",  
    "hotel-apartamento",  
    "pension",  
    "vivienda de uso turistico"  
  ],  
  "publisher": "comunidad de madrid.",  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        9.922458,  
        109.478534  
      ]  
    }  
  ],  
  "temporal": [  
    "2023-04-03T02:35:57Z"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "accessRights": "https://creativecommons.org/licenses/by/4.0/legalcode.es",  
  "creator": [  
    "Comunidad de Madrid"  
  ],  
  "page": [  
    "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
    "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
  ],  
  "accrualPeriodicity": "weekly",  
  "hasVersion": [  
    "urn:ngsi-ld:Dataset:items:SQSB:90831182",  
    "urn:ngsi-ld:Dataset:items:FFVZ:69502935"  
  ],  
  "identifier": [  
    "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
    "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
  ],  
  "isReferencedBy": [  
    "urn:ngsi-ld:Dataset:items:YQRP:33454193",  
    "urn:ngsi-ld:Dataset:items:RBND:48628164"  
  ],  
  "isVersionOf": [  
    "urn:ngsi-ld:Dataset:items:AMAC:16896252",  
    "urn:ngsi-ld:Dataset:items:IPSO:04920226"  
  ],  
  "landingPage": [  
    "urn:ngsi-ld:Dataset:items:UMBA:72418275",  
    "urn:ngsi-ld:Dataset:items:GUKW:86586813"  
  ],  
  "language": [  
    "EN",  
    "SP"  
  ],  
  "otherIdentifier": [  
    "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
    "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "qualifiedAttribution": [  
    ""  
  ],  
  "qualifiedRelation": [  
    "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
    "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
  ],  
  "relatedResource": [  
    "urn:ngsi-ld:Dataset:items:FXEY:35067714",  
    "urn:ngsi-ld:Dataset:items:YYOL:47950545"  
  ],  
  "issued": "1983-07-16T12:51:26Z",  
  "sample": [  
    "urn:ngsi-ld:Dataset:items:QJPZ:50290394",  
    "urn:ngsi-ld:Dataset:items:ZSSA:73451152"  
  ],  
  "spatialResolutionInMeters": 0.6,  
  "temporalResolution": [  
    "PT15M"  
  ],  
  "Type": "",  
  "version": "",  
  "versionNotes": [  
  ],  
  "wasGeneratedBy": [  
    "datos.gob.es"  
  ]  
}  
```  
</details>  
#### Datensatz NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Datensatz im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:HUZY:68185655",  
  "type": "Dataset",  
  "modified": {  
    "type": "DateTime",  
    "value": "2021-07-01T10:27:59Z"  
  },  
  "source": {  
    "type": "Text",  
    "value":"urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  },  
  "description": {  
    "type": "Text",  
    "value": ["Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid."]  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid"  
    ]  
  },  
  "contactPoint": {  
    "type": "array",  
    "value": [  
       "https://datos.gob.es/es/comment/reply/145778."  
    ]  
  },  
  "distribution": {  
    "type": "array",  
    "value": [  
         "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
    ]  
  },  
  "keyword": {  
    "type": "array",  
    "value": [  
    "alojamiento",  
    "apartamento rural",  
    "apartamento turístico",  
    "campamento de turismo",  
    "camping",  
    "casa rural",  
    "casas de huéspedes",  
    "hostal",  
    "hostel",  
    "hosteria",  
    "hotel",  
    "hotel rural",  
    "hotel-apartamento",  
    "pension",  
    "vivienda de uso turistico"  
    ]  
  },  
  "publisher": {  
    "type": "Text",  
    "value": "comunidad de madrid"  
  },  
  "spatial": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        22.1394715,  
        -7.100602  
      ]  
    }  
  },  
  "temporal": {  
    "type": "array",  
    "value": [  
    "2023-04-03T02:35:57Z"  
    ]  
  },  
  "theme": {  
    "type": "array",  
    "value": [  
    "Economy",  
    "Tourism"  
    ]  
  },  
  "accessRights": {  
    "type": "Text",  
    "value": "https://creativecommons.org/licenses/by/4.0/legalcode.es"  
  },  
  "creator": {  
    "type": "Text",  
    "value":  "Comunidad de Madrid"  
  },  
  "page": {  
    "type": "array",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "accrualPeriodicity": {  
    "type": "array",  
    "value": "two years"  
  },  
  "hasVersion": {  
    "type": "Text",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "identifier": {  
    "type": "array",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "isReferencedBy": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:HJNK:88711880",  
      "urn:ngsi-ld:Dataset:items:MDEO:95193079"  
    ]  
  },  
  "isVersionOf": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:RBWE:31388012",  
      "urn:ngsi-ld:Dataset:items:GATZ:02632837"  
    ]  
  },  
  "landingPage": {  
    "type": "array",  
    "value": [  
      "htps://meloda.org"  
    ]  
  },  
  "language": {  
    "type": "array",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "otherIdentifier": {  
    "type": "array",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "provenance": {  
    "type": "array",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "qualifiedAttribution": {  
    "type": "array",  
    "value": [  
      ""  
    ]  
  },  
  "qualifiedRelation": {  
    "type": "array",  
    "value": [  
      ""  
    ]  
  },  
  "relatedResource": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:LGBY:74926949",  
      "urn:ngsi-ld:Dataset:items:ZAUC:79968579"  
    ]  
  },  
  "issued": {  
    "type": "DateTime",  
    "value": "2021-10-01T15:46:46Z"  
  },  
  "sample": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:MLHW:64299003",  
      "urn:ngsi-ld:Dataset:items:GNXL:59256807"  
    ]  
  },  
  "spatialResolutionInMeters": {  
    "type": "array",  
    "value": [  
      0.6  
    ]  
  },  
  "temporalResolution": {  
    "type": "array",  
    "value": [  
      "PT15M"  
    ]  
  },  
  "Type": {  
    "type": "Text",  
    "value": ""  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "versionNotes": {  
    "type": "array",  
    "value": [  
      "With temporal evolution"  
    ]  
  },  
  "wasGeneratedBy": {  
    "type": "Text",  
    "value": [  
      "meloda Team"  
    ]  
  }  
}  
```  
</details>  
#### Datensatz NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Datensatz im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:VESI:23278568",  
  "type": "Dataset",  
  "modified": "2015-07-13T03:09:32Z",  
  "source": [  
    "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  ],  
  "description": [  
    "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid."  
  ],  
  "title": [  
    "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid"  
  ],  
  "contactPoint": [  
    "https://datos.gob.es/es/comment/reply/145778."  
  ],  
  "distribution": [  
    "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
  ],  
  "keyword": [  
    "alojamiento",  
    "apartamento rural",  
    "apartamento turístico",  
    "campamento de turismo",  
    "camping",  
    "casa rural",  
    "casas de huéspedes",  
    "hostal",  
    "hostel",  
    "hosteria",  
    "hotel",  
    "hotel rural",  
    "hotel-apartamento",  
    "pension",  
    "vivienda de uso turistico"  
  ],  
  "publisher": "Statement which consumer product thought total. Nothing concern picture involve paper nor kid.",  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        9.922458,  
        109.478534  
      ]  
    }  
  ],  
  "temporal": [  
    "2023-04-03T02:35:57Z"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "accessRights": "https://creativecommons.org/licenses/by/4.0/legalcode.es",  
  "creator": [  
    "Comunidad de Madrid"  
  ],  
  "page": [  
    "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
    "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
  ],  
  "accrualPeriodicity": "weekly",  
  "hasVersion": [  
    "urn:ngsi-ld:Dataset:items:SQSB:90831182",  
    "urn:ngsi-ld:Dataset:items:FFVZ:69502935"  
  ],  
  "identifier": [  
    "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
    "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
  ],  
  "isReferencedBy": [  
    "urn:ngsi-ld:Dataset:items:YQRP:33454193",  
    "urn:ngsi-ld:Dataset:items:RBND:48628164"  
  ],  
  "isVersionOf": [  
    "urn:ngsi-ld:Dataset:items:AMAC:16896252",  
    "urn:ngsi-ld:Dataset:items:IPSO:04920226"  
  ],  
  "landingPage": [  
    "urn:ngsi-ld:Dataset:items:UMBA:72418275",  
    "urn:ngsi-ld:Dataset:items:GUKW:86586813"  
  ],  
  "language": [  
    "EN",  
    "SP"  
  ],  
  "otherIdentifier": [  
    "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
    "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "qualifiedAttribution": [  
    "Central born manage evidence data. Answer doctor visit ready physical fact. Quite allow however certain lose heart.",  
    "Home interesting range ever. Magazine the instead particularly. Late have collection."  
  ],  
  "qualifiedRelation": [  
    "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
    "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
  ],  
  "relatedResource": [  
    "urn:ngsi-ld:Dataset:items:FXEY:35067714",  
    "urn:ngsi-ld:Dataset:items:YYOL:47950545"  
  ],  
  "releaseDate": "1983-07-16T12:51:26Z",  
  "sample": [  
    "urn:ngsi-ld:Dataset:items:QJPZ:50290394",  
    "urn:ngsi-ld:Dataset:items:ZSSA:73451152"  
  ],  
  "spatialResolutionInMeters": 0.6,  
  "temporalResolution": [  
   "PT15M"  
  ],  
  "Type": "",  
  "version": "",  
  "versionNotes": [  
  ],  
  "wasGeneratedBy": [  
    "datos.gob.es"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Datensatz NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Datensatz im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:HUZY:68185655",  
  "type": "Dataset",  
  "modified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-01T10:27:59Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value":"urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  },  
  "description": {  
    "type": "Property",  
    "value": ["Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid."]  
  },  
  "title": {  
    "type": "Property",  
    "value": [  
      "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid"  
    ]  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": [  
       "https://datos.gob.es/es/comment/reply/145778."  
    ]  
  },  
  "distribution": {  
    "type": "Relationship",  
    "object": [  
         "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
    ]  
  },  
  "keyword": {  
    "type": "Property",  
    "value": [  
    "alojamiento",  
    "apartamento rural",  
    "apartamento turístico",  
    "campamento de turismo",  
    "camping",  
    "casa rural",  
    "casas de huéspedes",  
    "hostal",  
    "hostel",  
    "hosteria",  
    "hotel",  
    "hotel rural",  
    "hotel-apartamento",  
    "pension",  
    "vivienda de uso turistico"  
    ]  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Comunidad de madrid"  
  },  
  "spatial": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        22.1394715,  
        -7.100602  
      ]  
    }  
  },  
  "temporal": {  
    "type": "Property",  
    "value": [  
    "2023-04-03T02:35:57Z"  
    ]  
  },  
  "theme": {  
    "type": "Property",  
    "value": [  
    "Economy",  
    "Tourism"  
    ]  
  },  
  "accessRights": {  
    "type": "Property",  
    "value": "https://creativecommons.org/licenses/by/4.0/legalcode.es"  
  },  
  "creator": {  
    "type": "Property",  
    "value":  "Comunidad de Madrid"  
  },  
  "page": {  
    "type": "Property",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "accrualPeriodicity": {  
    "type": "Property",  
    "value": "two years"  
  },  
  "hasVersion": {  
    "type": "Property",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "identifier": {  
    "type": "Property",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "isReferencedBy": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:HJNK:88711880",  
      "urn:ngsi-ld:Dataset:items:MDEO:95193079"  
    ]  
  },  
  "isVersionOf": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:RBWE:31388012",  
      "urn:ngsi-ld:Dataset:items:GATZ:02632837"  
    ]  
  },  
  "landingPage": {  
    "type": "Property",  
    "value": [  
      "htps://meloda.org"  
    ]  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "otherIdentifier": {  
    "type": "Property",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "provenance": {  
    "type": "Property",  
    "value": [  
      "",  
      ""  
    ]  
  },  
  "qualifiedAttribution": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "qualifiedRelation": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "relatedResource": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:LGBY:74926949",  
      "urn:ngsi-ld:Dataset:items:ZAUC:79968579"  
    ]  
  },  
  "issued": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-10-01T15:46:46Z"  
    }  
  },  
  "sample": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:MLHW:64299003",  
      "urn:ngsi-ld:Dataset:items:GNXL:59256807"  
    ]  
  },  
  "spatialResolutionInMeters": {  
    "type": "Property",  
    "value": [  
      0.6  
    ]  
  },  
  "temporalResolution": {  
    "type": "Property",  
    "value": [  
      "PT15M"  
    ]  
  },  
  "Type": {  
    "type": "Property",  
    "value": ""  
  },  
  "version": {  
    "type": "Property",  
    "value": "3.0"  
  },  
  "versionNotes": {  
    "type": "Property",  
    "value": [  
      "With temporal evolution"  
    ]  
  },  
  "wasGeneratedBy": {  
    "type": "Property",  
    "value": [  
      "meloda Team"  
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
