<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : DistributionDCAT-AP  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/DistributionDCAT-AP/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Il s'agit d'une distribution appartenant à un ensemble de données selon la norme DCAT-AP 2.0.1**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `accessService[array]`: Cette propriété fait référence à un service de données qui donne accès à la distribution de l'ensemble de données.  . Model: [https://schema.org/Text](https://schema.org/Text)- `accessUrl[array]`: Cette propriété contient une URL qui donne accès à une distribution de l'ensemble de données. La ressource de l'URL d'accès peut contenir des informations sur la façon d'obtenir l'ensemble de données.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: Cette propriété indique combien de temps il est prévu de garder la distribution de l'ensemble de données disponible.  . Model: [https://schema.org/Text](https://schema.org/Text)- `byteSize[number]`: Cette propriété contient la taille d'une distribution en octets.  . Model: [https://schema.org/Number](https://schema.org/Number)- `checksum[string]`: Cette propriété fournit un mécanisme qui peut être utilisé pour vérifier que le contenu d'une distribution n'a pas été modifié. La somme de contrôle est liée à la downloadURL.  . Model: [https://schema.org/Text](https://schema.org/Text)- `compressionFormat[string]`: Cette propriété fait référence au format du fichier dans lequel les données sont contenues sous une forme compressée, par exemple pour réduire la taille du fichier téléchargeable. Elle devrait être exprimée à l'aide d'un type de média tel que défini dans le registre officiel des types de médias géré par l'IANA.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `documentation[array]`: Cette propriété fait référence à une page ou un document concernant cette distribution.  . Model: [https://schema.org/Text](https://schema.org/Text)- `downloadURL[array]`: Cette propriété contient une URL qui est un lien direct vers un fichier téléchargeable dans un format donné.  . Model: [https://schema.org/Text](https://schema.org/Text)- `format[string]`: Cette propriété fait référence au format de fichier de la distribution.  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasPolicy[string]`: Cette propriété fait référence à la politique exprimant les droits associés à la distribution si le vocabulaire ODRL est utilisé.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `language[array]`: Cette propriété fait référence à une langue utilisée dans la distribution. Cette propriété peut être répétée si les métadonnées sont fournies dans plusieurs langues.  . Model: [https://schema.org/Text](https://schema.org/Text)- `license[string]`: Cette propriété fait référence à un service de données qui donne accès à la distribution de l'ensemble de données.  . Model: [https://schema.org/Text](https://schema.org/Text)- `linkedSchemas[array]`: Cette propriété fait référence à un schéma établi auquel la distribution décrite est conforme.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mediaType[string]`: Cette propriété fait référence au type de média de la distribution tel que défini dans le registre officiel des types de médias géré par l'IANA.  . Model: [https://schema.org/Text](https://schema.org/Text)- `modifiedDate[string]`: Cette propriété contient la date la plus récente à laquelle la distribution a été changée ou modifiée.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `packagingFormat[string]`: Cette propriété fait référence au format du fichier dans lequel un ou plusieurs fichiers de données sont regroupés, par exemple pour permettre de télécharger ensemble un ensemble de fichiers connexes. Elle DEVRAIT être exprimée à l'aide d'un type de média tel que défini dans le registre officiel des types de médias géré par l'IANA.  . Model: [https://schema.org/Text](https://schema.org/Text)- `releaseDate[string]`: Ce bien contient la date d'émission officielle (par exemple, la publication) de la distribution.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `rights[string]`: Cette propriété fait référence à une déclaration qui spécifie les droits associés à la distribution.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `spatialResolution[array]`: Cette propriété fait référence à la séparation spatiale minimale pouvant être résolue dans la distribution d'un ensemble de données, mesurée en mètres.  . Model: [https://schema.org/Text](https://schema.org/Text)- `status[string]`: Cette propriété fait référence à la maturité de la distribution. Elle DOIT prendre l'une des valeurs suivantes : Completed, Deprecated, Under Development, Withdrawn.  . Model: [https://schema.org/Text](https://schema.org/Text)- `temporalResolution[array]`: Cette propriété fait référence à la période minimale résoluble dans la distribution de l'ensemble de données.  . Model: [https://schema.org/Text](https://schema.org/Text)- `title[array]`: Cette propriété contient un nom donné à la distribution. Cette propriété peut être répétée pour les versions linguistiques parallèles de la description.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de DistributionDCAT-AP  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapted from [DCAT-AP version 2.0.1](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2020-06/e4823478-4458-4546-9a85-3609867ad089/DCAT_AP_2.0.1.pdf).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DistributionDCAT-AP:    
  description: 'this is a distribution belonging ot a dataset according to the DCAT-AP standard 2.0.1'    
  properties:    
    accessService:    
      description: 'This property refers to a data service that gives access to the distribution of the dataset'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    accessUrl:    
      description: 'This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset.'    
      items:    
        minitems: 1    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availability:    
      description: 'This property indicates how long it is planned to keep the Distribution of the Dataset available.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    byteSize:    
      description: 'This property contains the size of a Distribution in bytes.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    checksum:    
      description: 'This property provides a mechanism that can be used to verify that the contents of a distribution have not changed. The checksum is related to the downloadURL.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    compressionFormat:    
      description: 'This property refers to the format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    documentation:    
      description: 'This property refers to a page or document about this Distribution.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    downloadURL:    
      description: 'This property contains a URL that is a directlink to a downloadable file in a givenformat.'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    format:    
      description: 'This property refers to the file format of the Distribution.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hasPolicy:    
      description: 'This property refers to the policy expressing the rights associated with the distribution if using the ODRL vocabulary'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &distributiondcat-ap_-_properties_-_owner_-_items_-_anyof    
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
      description: 'This property refers to a language used in the Distribution. This property can be repeated if the metadata is provided in multiple languages.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    license:    
      description: 'This property refers to a data service that gives access to the distribution of the dataset'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    linkedSchemas:    
      description: 'This property refers to an established schema to which the described Distribution conforms.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    mediaType:    
      description: 'This property refers to the media type of the Distribution as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modifiedDate:    
      description: 'This property contains the most recent date on which the Distribution was changed or modified.'    
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
        anyOf: *distributiondcat-ap_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    packagingFormat:    
      description: 'This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    releaseDate:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Distribution.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    rights:    
      description: 'This property refers to a statement that specifies rights associated with the Distribution.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    spatialResolution:    
      description: 'This property refers to the minimum spatial separation resolvable in a dataset distribution, measured in meters'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
        units: Meters    
    status:    
      description: 'This property refers to the maturity of the Distribution. It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn'    
      enum:    
        - Completed    
        - Deprecated    
        - 'Under Development'    
        - Withdrawn    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    temporalResolution:    
      description: 'This property refers to the minimum time period resolvable in the dataset distribution'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    title:    
      description: 'This property contains a name given to the Distribution. This property can be repeated for parallel language versions of the description.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be DistributionDCAT-AP'    
      enum:    
        - DistributionDCAT-AP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DistributionDCAT-AP/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT_AP/DistributionDCAT-AP/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### DistributionDCAT-AP NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'un DistributionDCAT-AP au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "type": "DistributionDCAT-AP",  
  "accessService": [  
    ""  
  ],  
  "accessUrl": [  
    ""  
  ],  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "24004",  
    "streetAddress": "Luxembourg platz 2"  
  },  
  "alternateName": "csv",  
  "areaServed": "European Union.",  
  "availability": "yes",  
  "byteSize": 43503,  
  "checksum": "H3FR.",  
  "compressionFormat": "",  
  "dataProvider": "Meloda.org",  
  "dateCreated": "1993-08-16T05:35:56Z",  
  "dateModified": "1970-07-14T10:48:19Z",  
  "description": "Distribution of open data portals in csv",  
  "documentation": [],  
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
  "linkedSchemas": [],  
  "location": {  
    "coordinates": [  
      -67.057831,  
      67.968509  
    ],  
    "type": "Point"  
  },  
  "mediaType": "",  
  "modifiedDate": "1986-03-28T19:56:43Z",  
  "name": "csv portals distribution",  
  "owner": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
  ],  
  "packagingFormat": "zip",  
  "releaseDate": "1997-05-06T05:04:10Z",  
  "rights": "copyleft",  
  "seeAlso": [  
    "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
    "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
  ],  
  "source": "",  
  "spatialResolution": [  
    0.5,  
    0.5  
  ],  
  "status": "Withdrawn",  
  "temporalResolution": [  
    2,  
    10  
  ],  
  "title": [  
    "Dataset base"  
  ]  
}  
```  
</details>  
#### DistributionDCAT-AP NGSI-v2 normalisée Exemple  
Voici un exemple d'un DistributionDCAT-AP au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1993-08-16T05:35:56Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1970-07-14T10:48:19Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "csv portals distribution"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "csv"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Distribution of open data portals in csv"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Meloda.org"  
  },  
  "owner": {  
    "type": "Text",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
      "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
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
  "areaServed": {  
    "type": "Text",  
    "value": "European Union."  
  },  
  "accessUrl": {  
    "type": "array",  
    "value": [  
      ""  
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
  "documentation": {  
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
  "linkedSchemas": {  
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
  "releaseDate": {  
    "type": "DateTime",  
    "value": "1997-05-06T05:04:10Z"  
  },  
  "rights": {  
    "type": "Text",  
    "value": "copyleft"  
  },  
  "spatialResolution": {  
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
    "value": [  
      2,  
      10  
    ]  
  },  
  "title": {  
    "type": "array",  
    "value": [  
      "Dataset base"  
    ]  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "1986-03-28T19:56:43Z"  
  }  
}  
```  
</details>  
#### DistributionDCAT-AP NGSI-LD valeurs-clés Exemple  
Voici un exemple d'un DistributionDCAT-AP au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
    "type": "DistributionDCAT-AP",  
    "accessService": [  
        ""  
    ],  
    "accessUrl": [  
        ""  
    ],  
    "address": {  
        "addressCountry": "Luxembourg",  
        "addressLocality": "Luxembourg",  
        "addressRegion": "Luxembourg",  
        "postOfficeBoxNumber": "",  
        "postalCode": "24004",  
        "streetAddress": "Luxembourg platz 2"  
    },  
    "alternateName": "csv",  
    "areaServed": "European Union.",  
    "availability": "yes",  
    "byteSize": 43503,  
    "checksum": "H3FR.",  
    "compressionFormat": "",  
    "dataProvider": "Meloda.org",  
    "dateCreated": "1993-08-16T05:35:56Z",  
    "dateModified": "1970-07-14T10:48:19Z",  
    "description": "Distribution of open data portals in csv",  
    "documentation": [],  
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
    "linkedSchemas": [],  
    "location": {  
        "coordinates": [  
            -67.057831,  
            67.968509  
        ],  
        "type": "Point"  
    },  
    "mediaType": "",  
    "modifiedDate": "1986-03-28T19:56:43Z",  
    "name": "csv portals distribution",  
    "owner": [  
        "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
        "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
    ],  
    "packagingFormat": "zip",  
    "releaseDate": "1997-05-06T05:04:10Z",  
    "rights": "copyleft",  
    "seeAlso": [  
        "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
        "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
    ],  
    "source": "",  
    "spatialResolution": [  
        0.5,  
        0.5  
    ],  
    "status": "Withdrawn",  
    "temporalResolution": [  
        2,  
        10  
    ],  
    "title": [  
        "Dataset base"  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DistributionDCAT-AP NGSI-LD normalisée Exemple  
Voici un exemple d'un DistributionDCAT-AP au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DistributionDCAT-AP:id:NUZE:76215118",  
    "accessService": {  
        "type": "Property",  
        "value": [  
            ""  
        ]  
    },  
    "accessUrl": {  
        "type": "Property",  
        "value": [  
            ""  
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
    "alternateName": {  
        "type": "Property",  
        "value": "csv"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "European Union."  
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
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1993-08-16T05:35:56Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1970-07-14T10:48:19Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Distribution of open data portals in csv"  
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
    "linkedSchemas": {  
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
    "modifiedDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1986-03-28T19:56:43Z"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "csv portals distribution"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:DistributionDCAT-AP:items:HZAC:24935175",  
            "urn:ngsi-ld:DistributionDCAT-AP:items:AQGQ:50019342"  
        ]  
    },  
    "packagingFormat": {  
        "type": "Property",  
        "value": "zip"  
    },  
    "releaseDate": {  
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
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:DistributionDCAT-AP:items:TYQY:03354957",  
            "urn:ngsi-ld:DistributionDCAT-AP:items:VZQW:12690544"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "spatialResolution": {  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
