<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Ensemble de données  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Dataset Schema conforme à la spécification DCAT-AP 2.1.1**  
version : 2.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `Type[string]`: Propriété. Modèle : "http://www.w3.org/2004/02/skos/core#Concept". Cette propriété fait référence au type de l'ensemble de données. Un vocabulaire contrôlé recommandé est prévu pour le type de données.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `accessRights[string]`: Propriété. Modèle : "http://purl.org/dc/terms/RightsStatement". Cette propriété fait référence à l'information qui indique si le jeu de données est une donnée ouverte, s'il a des restrictions d'accès ou s'il n'est pas public.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `accrualPeriodicity[string]`: Propriété. Modèle : "http://purl.org/dc/terms/Frequency". Cette propriété fait référence à la fréquence de mise à jour de l'ensemble de données.  . Model: [http://purl.org/dc/terms/Frequency](http://purl.org/dc/terms/Frequency)- `conformsTo[array]`: Propriété. Modèle : "http://purl.org/dc/terms/Standard". Cette propriété fait référence à une règle de mise en œuvre ou à une autre spécification.  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `contactPoint[array]`: Propriété. Modèle : "http://www.w3.org/2006/vcard/ns#Kind". Cette propriété contient des informations de contact qui peuvent être utilisées pour envoyer des commentaires sur le jeu de données.  . Model: [http://www.w3.org/2006/vcard/ns#Kind](http://www.w3.org/2006/vcard/ns#Kind)- `creator[array]`: Propriété. Modèle : "http://xmlns.com/foaf/0.1/Agent". Cette propriété fait référence à l'entité principalement responsable de la production de l'ensemble de données.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `description[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient une description en texte libre de l'ensemble de données. Cette propriété peut être répétée pour les versions en langues parallèles de la description.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `distribution[array]`: Relation. Cette propriété lie l'ensemble de données à une distribution disponible. Modèle : "http://www.w3.org/ns/dcat#Distribution  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `hasVersion[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Dataset". Cette propriété fait référence à un jeu de données apparenté qui est une version, une édition ou une adaptation du jeu de données décrit.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `id[*]`: Identifiant unique de l'entité  - `identifier[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient l'identifiant principal de l'ensemble de données, par exemple l'URI ou un autre identifiant unique dans le contexte du catalogue.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `isReferencedBy[array]`: Relation. Modèle : "http://www.w3.org/2000/01/rdf-schema#Resource". Cette propriété concerne une ressource connexe, telle qu'une publication, qui fait référence à l'ensemble de données, le cite ou le signale d'une autre manière.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `isVersionOf[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Dataset". Cette propriété fait référence à un jeu de données apparenté dont le jeu de données décrit est une version, une édition ou une adaptation.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `issued[string]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient la date d'émission officielle (par exemple, la publication) de l'ensemble de données.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `keyword[array]`: Propriété. Cette propriété contient un mot-clé ou une étiquette décrivant l'ensemble de données. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal".  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal.](http://www.w3.org/2000/01/rdf-schema#Literal.)- `landingPage[array]`: Propriété. Modèle : "http://xmlns.com/foaf/0.1/Document". Cette propriété renvoie à une page web qui permet d'accéder à l'ensemble de données, à ses distributions et/ou à des informations supplémentaires. Elle est destinée à pointer vers une page d'atterrissage du fournisseur de données d'origine, et non vers une page sur le site d'un tiers, tel qu'un agrégateur.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `language[array]`: Propriété. Modèle : "http://purl.org/dc/terms/LinguisticSystem". Cette propriété fait référence à une langue de l'ensemble de données. Cette propriété peut être répétée si l'ensemble de données comporte plusieurs langues.  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `modified[string]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient la date la plus récente à laquelle le jeu de données a été changé ou modifié.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `otherIdentifier[array]`: Propriété. Modèle : "http://www.w3.org/ns/adms#Identifier". Cette propriété fait référence à un identifiant secondaire de l'ensemble de données, tel que MAST/ADS, DataCite, DOI, EZID ou W3ID.  . Model: [http://www.w3.org/ns/adms#Identifier](http://www.w3.org/ns/adms#Identifier)- `page[array]`: Propriété. Modèle : "http://xmlns.com/foaf/0.1/Document". Cette propriété renvoie à une page ou à un document sur cet ensemble de données.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `provenance[array]`: Propriété. Modèle : "http://purl.org/dc/terms/ProvenanceStatement". Cette propriété contient une déclaration sur la lignée d'un jeu de données.  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: Propriété. Modèle : "http://xmlns.com/foaf/0.1/Agent". Cette propriété fait référence à une entité (organisation) responsable de la mise à disposition du jeu de données.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `qualifiedAttribution[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Relationship". Cette propriété renvoie à un lien vers un agent ayant une certaine responsabilité à l'égard de la ressource.  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `qualifiedRelation[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Relationship". Cette propriété fournit un lien vers la description d'une relation avec une autre ressource.  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `relatedResource[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Resource". Cette propriété fait référence à une ressource connexe.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `sample[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Distribution". Cette propriété fait référence à un échantillon de distribution de l'ensemble de données.  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `source[array]`: Propriété. Modèle : "http://www.w3.org/ns/dcat#Dataset". Cette propriété fait référence à un ensemble de données apparenté dont l'ensemble de données décrit est dérivé.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `spatial[array]`: GeoProperty. Modèle : "http://purl.org/dc/terms/Location". Cette propriété fait référence à une région géographique couverte par le jeu de données.  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `spatialResolutionInMeters[number]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété fait référence à la séparation spatiale minimale pouvant être résolue dans un ensemble de données, mesurée en mètres.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `temporal[array]`: Propriété. Cette propriété fait référence à une période temporelle couverte par le Dataset. Modèle : "http://purl.org/dc/terms/PeriodOfTime".  . Model: [http://purl.org/dc/terms/PeriodOfTime.](http://purl.org/dc/terms/PeriodOfTime.)- `temporalResolution[array]`: Propriété. Modèle : "http://purl.org/dc/terms/PeriodOfTime". Cette propriété fait référence à la période minimale pouvant être résolue dans l'ensemble de données.  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `theme[array]`: Propriété. Modèle : "http://www.w3.org/2004/02/skos/core#Concept". Cette propriété fait référence à une catégorie du Dataset. Un Dataset peut être associé à plusieurs thèmes.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient un nom donné à l'ensemble de données. Cette propriété peut être répétée pour les versions linguistiques parallèles du nom.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: Propriété. Type NGSI. Il doit s'agir d'un jeu de données  - `version[string]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient un numéro de version ou une autre désignation de version du jeu de données.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `versionNotes[array]`: Propriété. Modèle : "http://www.w3.org/2000/01/rdf-schema#Literal". Cette propriété contient une description des différences entre cette version et une version précédente de l'ensemble de données. Cette propriété peut être répétée pour les versions en langues parallèles des notes de version.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `wasGeneratedBy[array]`: Propriété. Modèle : "https://www.w3.org/ns/prov#Activity". Cette propriété fait référence à une activité qui a généré la création de l'ensemble de données ou qui en fournit le contexte.  . Model: [https://www.w3.org/ns/prov#Activity](https://www.w3.org/ns/prov#Activity)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `description`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de [DCAT-AP version 2.1.1] (https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Ensemble de données NGSI-v2 Valeurs clés Exemple  
Voici un exemple de jeu de données au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Ensemble de données NGSI-v2 normalisé Exemple  
Voici un exemple d'un jeu de données au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Ensemble de données Valeurs clés NGSI-LD Exemple  
Voici un exemple d'ensemble de données au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Ensemble de données NGSI-LD normalisé Exemple  
Voici un exemple de jeu de données au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsque les options ne sont pas utilisées et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
