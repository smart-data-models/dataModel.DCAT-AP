<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entité : CatalogueDCAT-AP  
=========================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/CatalogueDCAT-AP/LICENSE.md)  

[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Description globale : **Catalogue d'ensembles de données conformes à la spécification DCAT-AP**.  

version : 0.0.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste des propriétés  


<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)
- `alternateName[string]`: Un nom alternatif pour ce poste  
- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)
- `catalogue[array]`: Relation. Modèle : "dcat:catalog". Cette propriété fait référence à un catalogue dont le contenu présente un intérêt dans le contexte de ce catalogue.  . Model: [dcat:catalog](dcat:catalog)
- `creator[string]`: Propriété. Modèle : "https://schema.org/Text". Cette propriété fait référence à l'entité principalement responsable de la production du catalogue  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  
- `dataset[array]`: Relation. Cette propriété lie le Catalogue à un jeu de données qui fait partie du Catalogue. Modèle : 'dcat:Dataset'  . Model: [dcat:Dataset](dcat:Dataset)
- `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  
- `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  
- `description[string]`: Une description de l'article  
- `hasPart[array]`: Relation. Modèle : "https://schema.org/URL". Cette propriété fait référence à un catalogue apparenté qui fait partie du catalogue décrit.  . Model: [https://schema.org/URL](https://schema.org/URL)
- `homepage[string]`: Propriété. Modèle : "foaf:homepage". Cette propriété renvoie à une page web qui sert de page d'accueil pour le catalogue.  . Model: [foaf:homepage](foaf:homepage)
- `id[*]`: Identifiant unique de l'entité  
- `isPartOf[string]`: Relation. Modèle : "https://schema.org/URL". Cette propriété fait référence à un catalogue apparenté dans lequel le catalogue décrit est physiquement ou logiquement inclus.  . Model: [https://schema.org/URL](https://schema.org/URL)
- `language[array]`: Propriété. Modèle : "dct:language". Cette propriété fait référence à une langue utilisée dans les métadonnées textuelles décrivant les titres, les descriptions, etc. des ensembles de données du catalogue. Cette propriété peut être répétée si les métadonnées sont fournies dans plusieurs langues.  . Model: [dct:language](dct:language)
- `licence[string]`: Propriété. Modèle : "dct:license". Cette propriété fait référence à la licence sous laquelle le Catalogue peut être utilisé ou réutilisé.  . Model: [dct:license](dct:license)
- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  
- `modificationDate[string]`: Propriété. Modèle : "https://schema.org/DateTime". Cette propriété contient la date la plus récente à laquelle le catalogue a été modifié.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)
- `name[string]`: Le nom de cet élément.  
- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  
- `publisher[string]`: Propriété. Modèle : "https://schema.org/Text". Cette propriété fait référence à une entité (organisation) responsable de la mise à disposition du Catalogue. Modèle : 'dct:publisher'  . Model: [dct:publisher](dct:publisher)
- `record[array]`: Relation. Cette propriété fait référence à une fiche de catalogue qui fait partie du catalogue.  
- `releaseDate[string]`: Propriété. Modèle : "https://schema.org/DateTime". Cette propriété contient la date d'émission officielle (par exemple, la publication) du Catalogue.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)
- `rights[string]`: Propriété. Modèle : "dct:rights". Cette propriété renvoie à une déclaration qui précise les droits associés au catalogue.  . Model: [dct:rights](dct:rights)
- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  
- `service[array]`: Propriété. Cette propriété fait référence à un site ou à un point de terminaison répertorié dans le catalogue. Modèle : 'dcat:DataService'  . Model: [dcat:DataService](dcat:DataService)
- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  
- `spatial_geographic[array]`: Géopropriété. Cette propriété fait référence à une zone géographique couverte par le Catalogue. Modèle : 'dct:spatial'  . Model: [dct:spatial](dct:spatial)
- `themes[array]`: Propriété. Modèle : "dcat:themeTaxonomy". Cette propriété fait référence à un système d'organisation des connaissances utilisé pour classer les ensembles de données du catalogue.  . Model: [dcat:themeTaxonomy](dcat:themeTaxonomy)
- `title[array]`: Propriété. Modèle : "https://schema.org/URL". Cette propriété contient un nom donné au catalogue. Cette propriété peut être répétée pour les versions linguistiques parallèles du nom. Modèle : "rdfs:Literal  . Model: [rdfs:Literal](rdfs:Literal)
- `type[string]`: Propriété. Modèle : "https://schema.org/Text". Il doit s'agir du CatalogueDCAT-AP  . Model: [https://schema.org/Text](https://schema.org/Text)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Propriétés requises  
- `dataset`  
- `description`  
- `id`  
- `publisher`  
- `title`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  

Ce modèle de données et d'autres du sujet DCAT-AP sont en cours d'adaptation pour leur utilisation et il serait recommandé d'inclure un contexte supplémentaire. [https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld" ](https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld)  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Modèle de données description des propriétés  

Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
CatalogueDCAT-AP:    
  description: Catalogue of datasets compliant with DCAT-AP specification.    
  properties:    
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
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    catalogue:    
      description: 'Relationship. Model:''dcat:catalog''. This property refers to a catalog whose contents are of interest in the context of this catalog'    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: dcat:catalog    
        type: Relationship    
    creator:    
      description: 'Property. Model:''https://schema.org/Text''. This property refers to the entity primarily responsible for producing the catalogue'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dataset:    
      description: 'Relationship. This property links the Catalogue with a Dataset that is part of the Catalogue. Model:''dcat:Dataset'''    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: dcat:Dataset    
        type: Relationship    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    hasPart:    
      description: 'Relationship. Model:''https://schema.org/URL''. This property refers to a related Catalogue that is part of the described Catalogue'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    homepage:    
      description: 'Property. Model:''foaf:homepage''. This property refers to a web page that acts as the main page for the Catalogue.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: foaf:homepage    
        type: Property    
    id:    
      anyOf: &cataloguedcat-ap_-_properties_-_owner_-_items_-_anyof    
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
    isPartOf:    
      description: 'Relationship. Model:''https://schema.org/URL''. This property refers to a related Catalogue in which the described Catalogue is physically or logically included.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    language:    
      description: 'Property. Model:''dct:language''. This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. This property can be repeated if the  metadata is provided in multiple languages.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dct:language    
        type: Property    
    licence:    
      description: 'Property. Model:''dct:license''. This property refers to the licence under which the Catalogue can be used or reused.'    
      type: string    
      x-ngsi:    
        model: dct:license    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_oneof    
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
    modificationDate:    
      description: 'Property. Model:''https://schema.org/DateTime''. This property contains the most recent date on which the Catalogue was modified.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *cataloguedcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    publisher:    
      description: 'Property. Model:''https://schema.org/Text''. This property refers to an entity (organisation) responsible for making the Catalogue available. Model:''dct:publisher'''    
      type: string    
      x-ngsi:    
        model: dct:publisher    
        type: Property    
    record:    
      description: Relationship. This property refers to a Catalogue Record that is part of the Catalogue    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    releaseDate:    
      description: 'Property. Model:''https://schema.org/DateTime''. This property contains the date of formal issuance (e.g., publication) of the Catalogue.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    rights:    
      description: 'Property. Model:''dct:rights''. This property refers to a statement that specifies rights associated with the Catalogue.'    
      type: string    
      x-ngsi:    
        model: dct:rights    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    service:    
      description: 'Property. This property refers to a site or end-point that is listed in the catalog. Model:''dcat:DataService'''    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dcat:DataService    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    spatial_geographic:    
      description: 'GeoProperty. This property refers to a geographical area covered by the Catalogue. Model:''dct:spatial'''    
      items:    
        description: 'GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
        oneOf: *cataloguedcat-ap_-_properties_-_spatial_geographic_-_items_-_oneof    
      type: array    
      x-ngsi:    
        model: dct:spatial    
    themes:    
      description: 'Property. Model:''dcat:themeTaxonomy''. This property refers to a knowledge organization system used to classify the Catalogue''s Datasets.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: dcat:themeTaxonomy    
        type: Property    
    title:    
      description: 'Property. Model:''https://schema.org/URL''. This property contains a name given to the Catalogue. This property can be repeated for parallel language versions of the name. Model:''rdfs:Literal'''    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: rdfs:Literal    
        type: Property    
    type:    
      description: 'Property. Model:''https://schema.org/Text''. It has to be CatalogueDCAT-AP'    
      enum:    
        - CatalogueDCAT-AP    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - dataset    
    - description    
    - publisher    
    - title    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/CatalogueDCAT-AP/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/CatalogueDCAT-AP/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Exemples de charges utiles  

#### CatalogueDCAT-AP NGSI-v2 valeurs-clés Exemple  

Voici un exemple de CatalogueDCAT-AP au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
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
</details>  

#### CatalogueDCAT-AP NGSI-v2 normalisé Exemple  

Voici un exemple de CatalogueDCAT-AP au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
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
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Catalogue"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "european open data portal"  
  },  
  "owner": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
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
    "type": "object",  
    "value": "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
  },  
  "publisher": {  
    "type": "Property",  
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
    "type": "string",  
    "value": "urn:ngsi-ld:Catalogue:homepage:ZFAW:13633782"  
  },  
  "language": {  
    "type": "Array",  
    "value": [  
      "Town size computer way. Since challenge phone state listen south low.",  
      "Eight once single. Build every kid."  
    ]  
  },  
  "licence": {  
    "type": "Property",  
    "value": "Improve social simply court week debate bad. Structure ago cup head point. Above much can own course."  
  },  
  "releaseDate": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
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
    "type": "Array",  
    "value": [  
      "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
      "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
    ]  
  },  
  "modificationDate": {  
    "type": "DateTime",  
    "value": "1982-09-02T03:16:28Z"  
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
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:HLGA:73285516",  
      "urn:ngsi-ld:Catalogue:items:IHOB:85266800"  
    ]  
  },  
  "rights": {  
    "type": "Property",  
    "value": "Open source"  
  },  
  "catalogue": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
      "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ]  
  },  
  "creator": {  
    "type": "Text",  
    "value": "Role fact sport shoulder blue direction probably order."  
  }  
}  
```  
</details>  

#### CatalogueDCAT-AP NGSI-LD valeurs clés Exemple  

Voici un exemple de CatalogueDCAT-AP au format JSON-LD en tant que valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
    "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
    "type": "CatalogueDCAT-AP",  
    "address": {  
        "streetAddress": "2 Rue Mercier",  
        "addressLocality": "Luxembourg",  
        "addressRegion": "Luxembourg",  
        "addressCountry": "Luxembourg",  
        "postalCode": "2985 ",  
        "postOfficeBoxNumber": "",  
        "areaServed": "European Union"  
    },  
    "alternateName": "",  
    "catalogue": [  
        "urn:ngsi-ld:Catalogue:items:LZMQ:44249979",  
        "urn:ngsi-ld:Catalogue:items:PECX:02526105"  
    ],  
    "creator": "Role fact sport shoulder blue direction probably order.",  
    "dataProvider": "european open data portal",  
    "dataset": [  
        "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ],  
    "dateCreated": "1980-03-03T10:01:24Z",  
    "dateModified": "1987-12-04T10:44:40Z",  
    "description": "Interesting art recently book girl yard represent book. Garden style wish blood your ground size.",  
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
    "modificationDate": "1982-09-02T03:16:28Z",  
    "name": "Catalogue",  
    "owner": [  
        "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
    ],  
    "publisher": "Spanish data portal",  
    "record": [  
        "Catalogue.items.HLGA.73285516",  
        "Catalogue.items.IHOB.85266800"  
    ],  
    "releaseDate": "2004-08-22T22:32:47Z",  
    "rights": "",  
    "seeAlso": [  
        "urn:ngsi-ld:Catalogue:ILBA:60770941"  
    ],  
    "source": "",  
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
    "title": [  
        "title first",  
        "Secondary title."  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details>  

#### CatalogueDCAT-AP NGSI-LD normalisé Exemple  

Voici un exemple de CatalogueDCAT-AP au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Catalogue:id:LMVP:18269678",  
  "type": "CatalogueDCAT-AP",  
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
  "alternateName": {  
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
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "European open data portal"  
  },  
  "dataset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Catalogue:dataset:ZBCW:95668818"  
    ]  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-03T10:01:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-04T10:44:40Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": ""  
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
  "licence": {  
    "type": "Property",  
    "value": [  
      "Creative Commons 3.0 International"  
    ]  
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
  "modificationDate": {  
    "type": "DateTime",  
    "value": "1982-09-02T03:16:28Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Catalogue"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ZYKY:89462950"  
    ]  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Spain open data portal"  
  },  
  "record": {  
    "type": "Property",  
    "value": [  
      "Catalogue.items.HLGA.73285516",  
      "Catalogue.items.IHOB.85266800"  
    ]  
  },  
  "releaseDate": {  
    "type": "DateTime",  
    "value": "2004-08-22T22:32:47Z"  
  },  
  "rights": {  
    "type": "Property",  
    "value": ""  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Catalogue:ILBA:60770941"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "spatial_geographic": {  
    "type": "GeoProperty",  
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
      "Want couple him finally responsibility begin. Coach join down new major. Happy yard letter then return member.",  
      "Politics road two question offer white. Recognize fight keep blue person create be. Radio edge or improve less special future. Itself detail computer exist."  
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
    "https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/1.1/dcat-ap_1.1.jsonld",  
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
  
