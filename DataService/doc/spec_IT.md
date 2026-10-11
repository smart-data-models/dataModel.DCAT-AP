<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: DataService  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataService/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Data Service adattato dalla specifica DCAT-AP 3.0.0, ma esteso con proprietà aggiuntive e compatibile con lo standard NGSI**  
version: 1.0.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/pattern</sub></sup>  
- `accessRights[string]`: Questa proprietà PUÒ includere informazioni riguardanti l'accesso o le restrizioni basate sulla privacy, la sicurezza o altre policy.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo civico  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `applicableLegislation[array]`: La legislazione che impone la creazione o la gestione del Data Service. Cardinalità: 0..n.  . Model: [http://data.europa.eu/r5r/applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)- `conformsTo[array]`: Uno standard (tecnico) stabilito a cui il Data Service si conforma. Gli standard qui citati DOVREBBERO descrivere il Data Service e non i dati che serve. Questi ultimi sono forniti dal dataset con cui questo Data Service è collegato. Ad esempio, il servizio dati aderisce allo standard OGC WFS API, mentre il dataset associato aderisce al modello di dati Address di INSPIRE (https://knowledge-base.inspire.ec.europa.eu/index_en). Cardinalità: 0..n.  . Model: [http://purl.org/dc/terms/conformsTo](http://purl.org/dc/terms/conformsTo)- `contactPoint[array]`: Informazioni di contatto che possono essere utilizzate per inviare commenti sul Data Service. Cardinalità: 0..n.  . Model: [http://www.w3.org/ns/dcat#contactPoint](http://www.w3.org/ns/dcat#contactPoint)- `description[*]`: LanguageProperty. Una descrizione in testo libero del Data Service.  . Model: [http://purl.org/dc/terms/description](http://purl.org/dc/terms/description)- `endpointDescription[array]`: Questa proprietà contiene una descrizione dei servizi disponibili tramite gli endpoint, incluse le loro operazioni, i parametri, ecc. La proprietà fornisce dettagli specifici sulle istanze effettive dell'endpoint, mentre dct:conformsTo è usato per indicare lo standard o la specifica generale che gli endpoint implementano.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `endpointURL[array]`: La posizione radice o l'endpoint principale del servizio (un IRI)  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `format[array]`: La struttura che può essere restituita interrogando l'endpointURL. Cardinalità: 0..n.  . Model: [http://purl.org/dc/terms/format](http://purl.org/dc/terms/format)- `id[*]`: Identificatore unico dell'entità  - `keyword[array]`: Questa proprietà contiene una parola chiave o un tag, che descrive il Data Service.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `landingPage[array]`: Questa proprietà si riferisce a una pagina web che fornisce l'accesso al Data Service e/o informazioni aggiuntive. È destinata a puntare a una landing page del fornitore originale del servizio dati, non a una pagina di un sito di terze parti, come un aggregatore.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `lastUpdated[date-time]`: Ultima volta in cui il servizio dati è stato aggiornato in modo tale da cambiarne il comportamento.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `license[string]`: Questa proprietà contiene la licenza sotto la quale il Data Service è reso disponibile.  . Model: [http://purl.org/dc/terms/LicenseDocument](http://purl.org/dc/terms/LicenseDocument)- `location[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `operationSpace[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `page[array]`: Una pagina o un documento riguardante questo Data Service. Cardinalità: 0..n.  . Model: [http://xmlns.com/foaf/0.1/page](http://xmlns.com/foaf/0.1/page)- `provenance[array]`: Elenco delle librerie e degli strumenti utilizzati nello sviluppo e nell'esecuzione del servizio.  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: Questa proprietà si riferisce a un'entità (organizzazione) responsabile della messa a disposizione del Data Service.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `servesDataset[array]`: Questa proprietà si riferisce a una collezione di dati che questo servizio dati può distribuire.  . Model: [https://www.w3.org/ns/dcat#servesDataset](https://www.w3.org/ns/dcat#servesDataset)- `theme[array]`: Questa proprietà si riferisce a una categoria del Data Service. Un Dataset può essere associato a più temi.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[*]`: LanguageProperty. Questa proprietà contiene un nome assegnato al Data Service. Questa proprietà può essere ripetuta per versioni linguistiche parallele del nome.  . Model: [http://purl.org/dc/terms/title](http://purl.org/dc/terms/title)- `type[string]`: Tipo di entità NGSI. Deve essere DataService.  - `validationSchema[string]`: URL dello schema di validazione tecnica per il DataService (JSON Schema) nel programma Smart Data Models.  . Model: [https://schema.org/url](https://schema.org/url)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `endpointURL`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Adattato da [DCAT-AP versione 3.0.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/). Alcune proprietà sono state rinominate per evitare conflitti con altre proprietà esistenti. Inoltre, sono state aggiunte altre proprietà per mantenere la compatibilità con lo standard NGSI e altri modelli di dati. Aggiunta delle proprietà relative ai principi FAIR e alle dimensioni MELODA5: provenance, elenco delle librerie e degli strumenti utilizzati nello sviluppo e nell'esecuzione del servizio. lastUpdated, l'ultima volta in cui il servizio dati è stato aggiornato in modo tale da cambiarne il comportamento. operationSpace, riferimento Geojson al Data Service, può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon. address, l'indirizzo postale o l'organizzazione che fornisce il Data Service. validationSchema, URL dello schema di validazione tecnica per il Data Service (JSON Schema) nel programma Smart Data Models. license, questa proprietà contiene la licenza sotto la quale il Data service è reso disponibile.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descrizione delle proprietà del modello di dati  
Ordinato alfabeticamente (clicca per dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataService:    
  description: Data Service adapted from DCAT-AP 3.0.0 specification, but extended with additional properties and compatible with NGSI standard    
  properties:    
    accessRights:    
      description: This property MAY include information regarding access or restrictions based on privacy, security, or other policies.    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
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
    applicableLegislation:    
      description: 'The legislation that mandates the creation or management of the Data Service. Cardinality: 0..n.'    
      items:    
        description: This class represents the legislation, policy or policies that lie behind the Rules that govern the service. The definition and properties of the Legal Resource class are aligned with the ontology included in Council conclusions inviting the introduction of the European Legislation Identifier (ELI - https://eur-lex.europa.eu/eli-register/about.html). For describing the attributes of a Legal Resource (labels, preferred labels, alternative labels, definition, etc.) we refer to the (ELI - https://op.europa.eu/en/web/eu-vocabularies/eli) ontology. In this data specification the use is restricted to instances of this class that follow the (ELI - https://op.europa.eu/en/web/eu-vocabularies/eli) URI guidelines.    
        type: string    
        x-ngsi:    
          model: http://data.europa.eu/eli/ontology#LegalResource    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://data.europa.eu/r5r/applicableLegislation    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    conformsTo:    
      description: 'An established (technical) standard to which the Data Service conforms. The standards referred here SHOULD describe the Data Service and not the data it serves. The latter is provided by the dataset with which this Data Service is connected. For instance the data service adheres to the OGC WFS API standard, while the associated dataset adheres to the INSPIRE (https://knowledge-base.inspire.ec.europa.eu/index_en) Address data model. Cardinality: 0..n.'    
      items:    
        description: A standard or other specification to which a resource conforms. This specification does not impose any additional requirements to properties for this entity.    
        type: string    
        x-ngsi:    
          model: https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/conformsTo    
        type: Property    
    contactPoint:    
      description: 'Contact information that can be used for sending comments about the Data Service. Cardinality: 0..n.'    
      items:    
        description: Every contact element    
        properties:    
          email:    
            description: To specify the electronic mail address for communication with the object the DataService represents.    
            format: email    
            type: string    
            x-ngsi:    
              model: https://www.w3.org/2006/vcard/ns#Email    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#contactPoint    
        type: Property    
    description:    
      description: LanguageProperty. A free-text account of the Data Service.    
      oneOf:    
        - properties:    
            languageMap:    
              description: ' A JSON object consisting of a series of key-value pairs where the keys shall be JSON strings representing IETF RFC 5646 (https://www.rfc-editor.org/info/rfc5646) language codes.'    
              properties:    
                de:    
                  description: The description written in German.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                el:    
                  description: The description written in Modern Greek.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                en:    
                  description: The description written in English.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                es:    
                  description: The description written in Spanish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fi:    
                  description: The description written in Finnish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fr:    
                  description: The description written in French.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                it:    
                  description: The description written in Italian.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ja:    
                  description: The description written in Japanese.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ko:    
                  description: The description written in Korean.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                nl:    
                  description: The description written in Dutch.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                zh:    
                  description: The description written in Chinese.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
              type: object    
              x-ngsi:    
                model: http://www.w3.org/2000/01/rdf-schema#Literal    
                type: Property    
          type: object    
        - description: The description written in a specific language.    
          type: string    
          x-ngsi:    
            model: http://www.w3.org/2000/01/rdf-schema#Literal    
            type: Property    
      x-ngsi:    
        model: http://purl.org/dc/terms/description    
    endpointDescription:    
      description: This property contains a description of the services available via the end-points, including their operations, parameters etc. The property gives specific details of the actual endpoint instances, while dct:conformsTo is used to indicate the general standard or specification that the endpoints implement.    
      items:    
        description: Every service available at an end-point.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Relationship    
    endpointURL:    
      description: The root location or primary endpoint of the service (an IRI)    
      items:    
        description: Every root location    
        format: uri    
        minItems: 1    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Property    
    format:    
      description: 'The structure that can be returned by querying the endpointURL. Cardinality: 0..n.'    
      items:    
        description: A media type or extent. This specification does not impose any additional requirements to properties for this entity.    
        type: string    
        x-ngsi:    
          model: http://purl.org/dc/terms/MediaTypeOrExtent    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/format    
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
        type: Relationship    
    keyword:    
      description: This property contains a keyword or tag, describing the Data Service.    
      items:    
        description: Every keyword tag included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    landingPage:    
      description: This property refers to a web page that provides access to the Data Service and/or additional information. It is intended to point to a landing page at the original data service provider, not to a page on a site of a third party, such as an aggregator.    
      items:    
        description: Every web page listed.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Property    
    lastUpdated:    
      description: Last time at which the data service has been updated in a way that changes its behavior.    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    license:    
      description: This property contains the license under which the Data Service is made available.    
      enum:    
        - 0BSD    
        - AAL    
        - Abstyles    
        - AdaCore-doc    
        - Adobe-2006    
        - Adobe-Glyph    
        - ADSL    
        - AFL-1.1    
        - AFL-1.2    
        - AFL-2.0    
        - AFL-2.1    
        - AFL-3.0    
        - Afmparse    
        - AGPL-1.0    
        - AGPL-1.0-only    
        - AGPL-1.0-or-later    
        - AGPL-3.0    
        - AGPL-3.0-only    
        - AGPL-3.0-or-later    
        - Aladdin    
        - AMDPLPA    
        - AML    
        - AMPAS    
        - ANTLR-PD    
        - ANTLR-PD-fallback    
        - Apache-1.0    
        - Apache-1.1    
        - Apache-2.0    
        - APAFML    
        - APL-1.0    
        - App-s2p    
        - APSL-1.0    
        - APSL-1.1    
        - APSL-1.2    
        - APSL-2.0    
        - Arphic-1999    
        - Artistic-1.0    
        - Artistic-1.0-cl8    
        - Artistic-1.0-Perl    
        - Artistic-2.0    
        - ASWF-Digital-Assets-1.0    
        - ASWF-Digital-Assets-1.1    
        - Baekmuk    
        - Bahyph    
        - Barr    
        - Beerware    
        - Bitstream-Charter    
        - Bitstream-Vera    
        - BitTorrent-1.0    
        - BitTorrent-1.1    
        - blessing    
        - BlueOak-1.0.0    
        - Boehm-GC    
        - Borceux    
        - Brian-Gladman-3-Clause    
        - BSD-1-Clause    
        - BSD-2-Clause    
        - BSD-2-Clause-FreeBSD    
        - BSD-2-Clause-NetBSD    
        - BSD-2-Clause-Patent    
        - BSD-2-Clause-Views    
        - BSD-3-Clause    
        - BSD-3-Clause-Attribution    
        - BSD-3-Clause-Clear    
        - BSD-3-Clause-LBNL    
        - BSD-3-Clause-Modification    
        - BSD-3-Clause-No-Military-License    
        - BSD-3-Clause-No-Nuclear-License    
        - BSD-3-Clause-No-Nuclear-License-2014    
        - BSD-3-Clause-No-Nuclear-Warranty    
        - BSD-3-Clause-Open-MPI    
        - BSD-4-Clause    
        - BSD-4-Clause-Shortened    
        - BSD-4-Clause-UC    
        - BSD-4.3RENO    
        - BSD-4.3TAHOE    
        - BSD-Advertising-Acknowledgement    
        - BSD-Attribution-HPND-disclaimer    
        - BSD-Protection    
        - BSD-Source-Code    
        - BSL-1.0    
        - BUSL-1.1    
        - bzip2-1.0.5    
        - bzip2-1.0.6    
        - C-UDA-1.0    
        - CAL-1.0    
        - CAL-1.0-Combined-Work-Exception    
        - Caldera    
        - CATOSL-1.1    
        - CC-BY-1.0    
        - CC-BY-2.0    
        - CC-BY-2.5    
        - CC-BY-2.5-AU    
        - CC-BY-3.0    
        - CC-BY-3.0-AT    
        - CC-BY-3.0-DE    
        - CC-BY-3.0-IGO    
        - CC-BY-3.0-NL    
        - CC-BY-3.0-US    
        - CC-BY-4.0    
        - CC-BY-NC-1.0    
        - CC-BY-NC-2.0    
        - CC-BY-NC-2.5    
        - CC-BY-NC-3.0    
        - CC-BY-NC-3.0-DE    
        - CC-BY-NC-4.0    
        - CC-BY-NC-ND-1.0    
        - CC-BY-NC-ND-2.0    
        - CC-BY-NC-ND-2.5    
        - CC-BY-NC-ND-3.0    
        - CC-BY-NC-ND-3.0-DE    
        - CC-BY-NC-ND-3.0-IGO    
        - CC-BY-NC-ND-4.0    
        - CC-BY-NC-SA-1.0    
        - CC-BY-NC-SA-2.0    
        - CC-BY-NC-SA-2.0-DE    
        - CC-BY-NC-SA-2.0-FR    
        - CC-BY-NC-SA-2.0-UK    
        - CC-BY-NC-SA-2.5    
        - CC-BY-NC-SA-3.0    
        - CC-BY-NC-SA-3.0-DE    
        - CC-BY-NC-SA-3.0-IGO    
        - CC-BY-NC-SA-4.0    
        - CC-BY-ND-1.0    
        - CC-BY-ND-2.0    
        - CC-BY-ND-2.5    
        - CC-BY-ND-3.0    
        - CC-BY-ND-3.0-DE    
        - CC-BY-ND-4.0    
        - CC-BY-SA-1.0    
        - CC-BY-SA-2.0    
        - CC-BY-SA-2.0-UK    
        - CC-BY-SA-2.1-JP    
        - CC-BY-SA-2.5    
        - CC-BY-SA-3.0    
        - CC-BY-SA-3.0-AT    
        - CC-BY-SA-3.0-DE    
        - CC-BY-SA-3.0-IGO    
        - CC-BY-SA-4.0    
        - CC-PDDC    
        - CC0-1.0    
        - CDDL-1.0    
        - CDDL-1.1    
        - CDL-1.0    
        - CDLA-Permissive-1.0    
        - CDLA-Permissive-2.0    
        - CDLA-Sharing-1.0    
        - CECILL-1.0    
        - CECILL-1.1    
        - CECILL-2.0    
        - CECILL-2.1    
        - CECILL-B    
        - CECILL-C    
        - CERN-OHL-1.1    
        - CERN-OHL-1.2    
        - CERN-OHL-P-2.0    
        - CERN-OHL-S-2.0    
        - CERN-OHL-W-2.0    
        - CFITSIO    
        - check-cvs    
        - checkmk    
        - ClArtistic    
        - Clips    
        - CMU-Mach    
        - CNRI-Jython    
        - CNRI-Python    
        - CNRI-Python-GPL-Compatible    
        - COIL-1.0    
        - Community-Spec-1.0    
        - Condor-1.1    
        - copyleft-next-0.3.0    
        - copyleft-next-0.3.1    
        - Cornell-Lossless-JPEG    
        - CPAL-1.0    
        - CPL-1.0    
        - CPOL-1.02    
        - Crossword    
        - CrystalStacker    
        - CUA-OPL-1.0    
        - Cube    
        - curl    
        - D-FSL-1.0    
        - diffmark    
        - DL-DE-BY-2.0    
        - DL-DE-ZERO-2.0    
        - DOC    
        - Dotseqn    
        - DRL-1.0    
        - DSDP    
        - dtoa    
        - dvipdfm    
        - ECL-1.0    
        - ECL-2.0    
        - eCos-2.0    
        - EFL-1.0    
        - EFL-2.0    
        - eGenix    
        - Elastic-2.0    
        - Entessa    
        - EPICS    
        - EPL-1.0    
        - EPL-2.0    
        - ErlPL-1.1    
        - etalab-2.0    
        - EUDatagrid    
        - EUPL-1.0    
        - EUPL-1.1    
        - EUPL-1.2    
        - Eurosym    
        - Fair    
        - FDK-AAC    
        - Frameworx-1.0    
        - FreeBSD-DOC    
        - FreeImage    
        - FSFAP    
        - FSFUL    
        - FSFULLR    
        - FSFULLRWD    
        - FTL    
        - GD    
        - GFDL-1.1    
        - GFDL-1.1-invariants-only    
        - GFDL-1.1-invariants-or-later    
        - GFDL-1.1-no-invariants-only    
        - GFDL-1.1-no-invariants-or-later    
        - GFDL-1.1-only    
        - GFDL-1.1-or-later    
        - GFDL-1.2    
        - GFDL-1.2-invariants-only    
        - GFDL-1.2-invariants-or-later    
        - GFDL-1.2-no-invariants-only    
        - GFDL-1.2-no-invariants-or-later    
        - GFDL-1.2-only    
        - GFDL-1.2-or-later    
        - GFDL-1.3    
        - GFDL-1.3-invariants-only    
        - GFDL-1.3-invariants-or-later    
        - GFDL-1.3-no-invariants-only    
        - GFDL-1.3-no-invariants-or-later    
        - GFDL-1.3-only    
        - GFDL-1.3-or-later    
        - Giftware    
        - GL2PS    
        - Glide    
        - Glulxe    
        - GLWTPL    
        - GNU-compiler-exception    
        - gnuplot    
        - GPL-1.0    
        - GPL-1.0+    
        - GPL-1.0-only    
        - GPL-1.0-or-later    
        - GPL-2.0    
        - GPL-2.0+    
        - GPL-2.0-only    
        - GPL-2.0-or-later    
        - GPL-2.0-with-autoconf-exception    
        - GPL-2.0-with-bison-exception    
        - GPL-2.0-with-classpath-exception    
        - GPL-2.0-with-font-exception    
        - GPL-2.0-with-GCC-exception    
        - GPL-3.0    
        - GPL-3.0+    
        - GPL-3.0-only    
        - GPL-3.0-or-later    
        - GPL-3.0-with-autoconf-exception    
        - GPL-3.0-with-GCC-exception    
        - Graphics-Gems    
        - gSOAP-1.3b    
        - HaskellReport    
        - Hippocratic-2.1    
        - HP-1986    
        - HP-1989    
        - HPND    
        - HPND-export-US    
        - HPND-Markus-Kuhn    
        - HPND-sell-variant    
        - HPND-sell-variant-MIT-disclaimer    
        - HTMLTIDY    
        - IBM-pibs    
        - ICU    
        - IEC-Code-Components-EULA    
        - IJG    
        - IJG-short    
        - ImageMagick    
        - iMatix    
        - Imlib2    
        - Info-ZIP    
        - Inner-Net-2.0    
        - Intel    
        - Intel-ACPI    
        - Interbase-1.0    
        - IPA    
        - IPL-1.0    
        - ISC    
        - Jam    
        - JasPer-2.0    
        - JPL-image    
        - JPNIC    
        - JSON    
        - Kazlib    
        - Knuth-CTAN    
        - LAL-1.2    
        - LAL-1.3    
        - Latex2e    
        - Latex2e-translated-notice    
        - Leptonica    
        - LGPL-2.0    
        - LGPL-2.0+    
        - LGPL-2.0-only    
        - LGPL-2.0-or-later    
        - LGPL-2.1    
        - LGPL-2.1+    
        - LGPL-2.1-only    
        - LGPL-2.1-or-later    
        - LGPL-3.0    
        - LGPL-3.0+    
        - LGPL-3.0-only    
        - LGPL-3.0-or-later    
        - LGPLLR    
        - Libpng    
        - libpng-2.0    
        - libselinux-1.0    
        - libtiff    
        - libutil-David-Nugent    
        - LiLiQ-P-1.1    
        - LiLiQ-R-1.1    
        - LiLiQ-Rplus-1.1    
        - Linux-man-pages-1-para    
        - Linux-man-pages-copyleft    
        - Linux-man-pages-copyleft-2-para    
        - Linux-man-pages-copyleft-var    
        - Linux-OpenIB    
        - LOOP    
        - LPL-1.0    
        - LPL-1.02    
        - LPPL-1.0    
        - LPPL-1.1    
        - LPPL-1.2    
        - LPPL-1.3a    
        - LPPL-1.3c    
        - LZMA-SDK-9.11-to-9.20    
        - LZMA-SDK-9.22    
        - MakeIndex    
        - Martin-Birgmeier    
        - metamail    
        - Minpack    
        - MirOS    
        - MIT    
        - MIT-0    
        - MIT-advertising    
        - MIT-CMU    
        - MIT-enna    
        - MIT-feh    
        - MIT-Festival    
        - MIT-Modern-Variant    
        - MIT-open-group    
        - MIT-testregex    
        - MIT-Wu    
        - MITNFA    
        - MMIXware    
        - Motosoto    
        - MPEG-Software-Simulation    
        - mpi-permissive    
        - mpich2    
        - MPL-1.0    
        - MPL-1.1    
        - MPL-2.0    
        - MPL-2.0-no-copyleft-exception    
        - mplus    
        - MS-LPL    
        - MS-PL    
        - MS-RL    
        - MTLL    
        - MulanPSL-1.0    
        - MulanPSL-2.0    
        - Multics    
        - Mup    
        - NAIST-2003    
        - NASA-1.3    
        - Naumen    
        - NBPL-1.0    
        - NCGL-UK-2.0    
        - NCSA    
        - Net-SNMP    
        - NetCDF    
        - Newsletr    
        - NGPL    
        - NICTA-1.0    
        - NIST-PD    
        - NIST-PD-fallback    
        - NIST-Software    
        - NLOD-1.0    
        - NLOD-2.0    
        - NLPL    
        - Nokia    
        - NOSL    
        - Noweb    
        - NPL-1.0    
        - NPL-1.1    
        - NPOSL-3.0    
        - NRL    
        - NTP    
        - NTP-0    
        - Nunit    
        - O-UDA-1.0    
        - OCCT-PL    
        - OCLC-2.0    
        - ODbL-1.0    
        - ODC-By-1.0    
        - OFFIS    
        - OFL-1.0    
        - OFL-1.0-no-RFN    
        - OFL-1.0-RFN    
        - OFL-1.1    
        - OFL-1.1-no-RFN    
        - OFL-1.1-RFN    
        - OGC-1.0    
        - OGDL-Taiwan-1.0    
        - OGL-Canada-2.0    
        - OGL-UK-1.0    
        - OGL-UK-2.0    
        - OGL-UK-3.0    
        - OGTSL    
        - OLDAP-1.1    
        - OLDAP-1.2    
        - OLDAP-1.3    
        - OLDAP-1.4    
        - OLDAP-2.0    
        - OLDAP-2.0.1    
        - OLDAP-2.1    
        - OLDAP-2.2    
        - OLDAP-2.2.1    
        - OLDAP-2.2.2    
        - OLDAP-2.3    
        - OLDAP-2.4    
        - OLDAP-2.5    
        - OLDAP-2.6    
        - OLDAP-2.7    
        - OLDAP-2.8    
        - OLFL-1.3    
        - OML    
        - OpenPBS-2.3    
        - OpenSSL    
        - OPL-1.0    
        - OPL-UK-3.0    
        - OPUBL-1.0    
        - OSET-PL-2.1    
        - OSL-1.0    
        - OSL-1.1    
        - OSL-2.0    
        - OSL-2.1    
        - OSL-3.0    
        - Parity-6.0.0    
        - Parity-7.0.0    
        - PDDL-1.0    
        - PHP-3.0    
        - PHP-3.01    
        - Plexus    
        - pnmstitch    
        - PolyForm-Noncommercial-1.0.0    
        - PolyForm-Small-Business-1.0.0    
        - PostgreSQL    
        - PSF-2.0    
        - psfrag    
        - psutils    
        - Python-2.0    
        - Python-2.0.1    
        - Qhull    
        - QPL-1.0    
        - QPL-1.0-INRIA-2004    
        - Rdisc    
        - RHeCos-1.1    
        - RPL-1.1    
        - RPL-1.5    
        - RPSL-1.0    
        - RSA-MD    
        - RSCPL    
        - Ruby    
        - SANE-exception    
        - SAX-PD    
        - Saxpath    
        - SCEA    
        - SchemeReport    
        - Sendmail    
        - Sendmail-8.23    
        - SGI-B-1.0    
        - SGI-B-1.1    
        - SGI-B-2.0    
        - SGP4    
        - SHL-0.5    
        - SHL-0.51    
        - SimPL-2.0    
        - SISSL    
        - SISSL-1.2    
        - SL    
        - Sleepycat    
        - SMLNJ    
        - SMPPL    
        - SNIA    
        - snprintf    
        - Soundex    
        - Spencer-86    
        - Spencer-94    
        - Spencer-99    
        - SPL-1.0    
        - SSH-OpenSSH    
        - SSH-short    
        - SSPL-1.0    
        - StandardML-NJ    
        - stunnel-exception    
        - SugarCRM-1.1.3    
        - SunPro    
        - SWL    
        - Symlinks    
        - TAPR-OHL-1.0    
        - TCL    
        - TCP-wrappers    
        - TermReadKey    
        - Texinfo-exception    
        - TMate    
        - TORQUE-1.1    
        - TOSL    
        - TPDL    
        - TPL-1.0    
        - TTWL    
        - TTYP0    
        - TU-Berlin-1.0    
        - TU-Berlin-2.0    
        - UCAR    
        - UCL-1.0    
        - Unicode-DFS-2015    
        - Unicode-DFS-2016    
        - Unicode-TOU    
        - UnixCrypt    
        - Unlicense    
        - UPL-1.0    
        - URT-RLE    
        - Vim    
        - VOSTROM    
        - VSL-1.0    
        - W3C    
        - W3C-19980720    
        - W3C-20150513    
        - w3m    
        - Watcom-1.0    
        - Widget-Workshop    
        - Wsuipa    
        - WTFPL    
        - wxWindows    
        - X11    
        - X11-distribute-modifications-variant    
        - Xdebug-1.03    
        - Xerox    
        - Xfig    
        - XFree86-1.1    
        - xinetd    
        - xlock    
        - Xnet    
        - xpp    
        - XSkat    
        - YPL-1.0    
        - YPL-1.1    
        - Zed    
        - Zeeff    
        - Zend-2.0    
        - Zimbra-1.3    
        - Zimbra-1.4    
        - Zlib    
        - zlib-acknowledgement    
        - ZPL-1.1    
        - ZPL-2.0    
        - ZPL-2.1    
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
    operationSpace:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon.    
      oneOf:    
        - description: Geojson reference to the item. Point.    
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
        - description: Geojson reference to the item. LineString.    
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
        - description: Geojson reference to the item. Polygon.    
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
        - description: Geojson reference to the item. MultiPoint.    
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
        - description: Geojson reference to the item. MultiLineString.    
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
        - description: Geojson reference to the item. MultiLineString.    
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
    page:    
      description: 'A page or document about this Data Service. Cardinality: 0..n.'    
      items:    
        description: A textual resource intended for human consumption that contains information, e.g. a web page about a Dataset. This specification does not impose any additional requirements to properties for this entity.    
        type: string    
        x-ngsi:    
          model: https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/page    
        type: Property    
    provenance:    
      description: List of libraries and tools used in the development and execution of the service.    
      items:    
        description: Every lineage associated to the data service.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/ProvenanceStatement    
        type: Property    
    publisher:    
      description: This property refers to an entity (organisation) responsible for making the Data Service available.    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    servesDataset:    
      description: This property refers to a collection of data that this data service can distribute.    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity.    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity.    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: This property refers to a collection of data that this data service can distribute.    
        x-ngsi:    
          model: http://www.w3.org/ns/dcat#Dataset    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://www.w3.org/ns/dcat#servesDataset    
        type: Relationship    
    theme:    
      description: This property refers to a category of the Data Service. A Dataset may be associated with multiple themes.    
      items:    
        description: Every theme included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#Concept    
        type: Property    
    title:    
      description: LanguageProperty. This property contains a name given to the Data Service. This property can be repeated for parallel language versions of the name.    
      oneOf:    
        - properties:    
            languageMap:    
              description: ' A JSON object consisting of a series of key-value pairs where the keys shall be JSON strings representing IETF RFC 5646 (https://www.rfc-editor.org/info/rfc5646) language codes.'    
              properties:    
                de:    
                  description: The description written in German.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                el:    
                  description: The description written in Modern Greek.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                en:    
                  description: The description written in English.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                es:    
                  description: The description written in Spanish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fi:    
                  description: The description written in Finnish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fr:    
                  description: The description written in French.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                it:    
                  description: The description written in Italian.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ja:    
                  description: The description written in Japanese.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ko:    
                  description: The description written in Korean.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                nl:    
                  description: The description written in Dutch.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                zh:    
                  description: The description written in Chinese.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
              type: object    
              x-ngsi:    
                model: https://www.w3.org/2000/01/rdf-schema#Literal    
                type: Property    
          type: object    
        - description: The title written in a specific language.    
          type: string    
          x-ngsi:    
            model: http://www.w3.org/2000/01/rdf-schema#Literal    
            type: Property    
      x-ngsi:    
        model: http://purl.org/dc/terms/title    
    type:    
      description: NGSI Entity type. It has to be DataService.    
      enum:    
        - DataService    
      type: string    
      x-ngsi:    
        type: Property    
    validationSchema:    
      description: URL to the technical validation schema for the DataService (JSON Schema) in the Smart Data Models program.    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
  required:    
    - endpointURL    
    - id    
    - title    
    - type    
  type: object    
  x-derived-from: https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/DataService/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json    
  x-model-tags: WATERVERSE    
  x-version: 1.0.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Alcune proprietà sono state aggiunte per consentire una gamma più ampia di utilizzi. Nello specifico assetProvider e configuration.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload    
#### Esempio di chiave-valore DataService NGSI-v2    
Ecco un esempio di un DataService in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "applicableLegislation": [  
    "Regulation 883/2004",  
    "Regulation 465/2012"  
  ],  
  "areaServed": "European Union and beyond",  
  "conformsTo": [  
    "OGC WFS API"  
  ],  
  "contactPoint": [  
    {  
      "email": "wheatfarm@email.com"  
    },  
    {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  ],  
  "description": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
  },  
  "endpointDescription": [  
    "SPARQL end point without authentication",  
    "API compliant with CKAN specification"  
  ],  
  "endpointURL": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
  ],  
  "format": [  
    "CSV",  
    "JSON"  
  ],  
  "keyword": [  
    "Data Service",  
    "CKAN"  
  ],  
  "landingPage": [  
    "https://dataservice.data",  
    "https://otherservice.data"  
  ],  
  "lastUpdated": "2021-07-01T10:27:59Z",  
  "license": "GPL-1.0",  
  "operationSpace": {  
    "coordinates": [  
      72.564509,  
      11.125289  
    ],  
    "type": "Point"  
  },  
  "page": [  
    "http://foo.org/how-to"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "publisher": "Comunidad de madrid",  
  "servesDataset": [  
    "urn:ngsi-ld:Dataset:id:HUZY:41266715",  
    "urn:ngsi-ld:Dataset:id:HUZY:41266716"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "title": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
  },  
  "validationSchema": "https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json"  
}  
```  
</details>  
#### Esempio di DataService NGSI-v2 normalizzato    
Ecco un esempio di un DataService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": {  
    "type": "Text",  
    "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "2, rue Mercier",  
      "addressLocality": "Luxembourg",  
      "addressRegion": "Luxembourg",  
      "addressCountry": "Luxembourg",  
      "postalCode": "2985",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "applicableLegislation": {  
    "type": "StructuredValue",  
    "value": [  
      "Regulation 883/2004",  
      "Regulation 465/2012"  
    ]  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "European Union and beyond"  
  },  
  "conformsTo": {  
    "type": "StructuredValue",  
    "value": [  
      "OGC WFS API"  
    ]  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "type": "Text",  
        "email": "wheatfarm@email.com"  
      },  
      {  
        "type": "Text",  
        "email": "vehiculoelectrico@ava.es"  
      }  
    ]  
  },  
  "description": {  
    "type": "StructuredValue",  
    "value": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "endpointDescription": {  
    "type": "StructuredValue",  
    "value": [  
      "SPARQL end point without authentication",  
      "API compliant with CKAN specification"  
    ]  
  },  
  "endpointURL": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
    ]  
  },  
  "format": {  
    "type": "StructuredValue",  
    "value": [  
      "CSV",  
      "JSON"  
    ]  
  },  
  "keyword": {  
    "type": "StructuredValue",  
    "value": [  
      "Data Service",  
      "CKAN"  
    ]  
  },  
  "landingPage": {  
    "type": "StructuredValue",  
    "value": [  
      "https://dataservice.data",  
      "https://otherservice.data"  
    ]  
  },  
  "lastUpdated": {  
    "type": "StructuredValue",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-01T10:27:59Z"  
    }  
  },  
  "license": {  
    "type": "Text",  
    "value": "GPL-1.0"  
  },  
  "operationSpace": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        72.564509,  
        11.125289  
      ]  
    }  
  },  
  "page": {  
    "type": "StructuredValue",  
    "value": [  
      "http://foo.org/how-to"  
    ]  
  },  
  "provenance": {  
    "type": "StructuredValue",  
    "value": [  
      "1",  
      "2"  
    ]  
  },  
  "publisher": {  
    "type": "Text",  
    "value": "Comunidad de madrid"  
  },  
  "servesDataset": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:id:HUZY:41266715",  
      "urn:ngsi-ld:Dataset:id:HUZY:41266716"  
    ]  
  },  
  "theme": {  
    "type": "StructuredValue",  
    "value": [  
      "Economy",  
      "Tourism"  
    ]  
  },  
  "title": {  
    "type": "StructuredValue",  
    "value": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "validationSchema": {  
    "type": "Text",  
    "value": "https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json"  
  }  
}  
```  
</details>  
#### Esempio di chiave-valore DataService NGSI-LD    
Ecco un esempio di un DataService in formato JSON-LD come chiave-valore. Questo è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": "No restrictions to access the data but APi requests limit, 5000 requests per hour",  
  "address": {  
    "addressCountry": "Luxembourg",  
    "addressLocality": "Luxembourg",  
    "addressRegion": "Luxembourg",  
    "postOfficeBoxNumber": "",  
    "postalCode": "2985",  
    "streetAddress": "2, rue Mercier"  
  },  
  "applicableLegislation": [  
    "Regulation 883/2004",  
    "Regulation 465/2012"  
  ],  
  "areaServed": "European Union and beyond",  
  "conformsTo": [  
    "OGC WFS API"  
  ],  
  "contactPoint": [  
    {  
      "email": "wheatfarm@email.com"  
    },  
    {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  ],  
  "description": {  
    "languageMap": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "endpointDescription": [  
    "SPARQL end point without authentication",  
    "API compliant with CKAN specification"  
  ],  
  "endpointURL": [  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
    "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
  ],  
  "format": [  
    "CSV",  
    "JSON"  
  ],  
  "keyword": [  
    "Data Service",  
    "CKAN"  
  ],  
  "landingPage": [  
    "https://dataservice.data",  
    "https://otherservice.data"  
  ],  
  "lastUpdated": "2021-07-01T10:27:59Z",  
  "license": "GPL-1.0",  
  "operationSpace": {  
    "coordinates": [  
      72.564509,  
      11.125289  
    ],  
    "type": "Point"  
  },  
  "page": [  
    "http://foo.org/how-to"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "publisher": "Comunidad de madrid",  
  "servesDataset": [  
    "urn:ngsi-ld:Dataset:id:HUZY:41266715",  
    "urn:ngsi-ld:Dataset:id:HUZY:41266716"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "title": {  
    "languageMap": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "validationSchema": "https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.DCAT-AP/context.jsonld"  
  ]  
}  
```  
</details>  
#### Esempio di DataService NGSI-LD normalizzato    
Ecco un esempio di un DataService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DataService:id:JBDJ:56257192",  
  "type": "DataService",  
  "accessRights": {  
    "type": "Property",  
    "value": "No restrictions to access the data but APi requests limit, 5000 requests per hour"  
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
  "applicableLegislation": {  
    "type": "Property",  
    "value": [  
      "Regulation 883/2004",  
      "Regulation 465/2012"  
    ]  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "European Union and beyond"  
  },  
  "conformsTo": {  
    "type": "Property",  
    "value": [  
      "OGC WFS API"  
    ]  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": [  
      {  
        "email": "wheatfarm@email.com"  
      },  
      {  
        "email": "vehiculoelectrico@ava.es"  
      }  
    ]  
  },  
  "description": {  
    "type": "LanguageProperty",  
    "languageMap": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "endpointDescription": {  
    "type": "Property",  
    "value": [  
      "SPARQL end point without authentication",  
      "API compliant with CKAN specification"  
    ]  
  },  
  "endpointURL": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:AFGI:79071729",  
      "urn:ngsi-ld:DataServiceDCAT-AP:items:JAZP:97999812"  
    ]  
  },  
  "format": {  
    "type": "Property",  
    "value": [  
      "CSV",  
      "JSON"  
    ]  
  },  
  "keyword": {  
    "type": "Property",  
    "value": [  
      "Data Service",  
      "CKAN"  
    ]  
  },  
  "landingPage": {  
    "type": "Property",  
    "value": [  
      "https://dataservice.data",  
      "https://otherservice.data"  
    ]  
  },  
  "lastUpdated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-01T10:27:59Z"  
    }  
  },  
  "license": {  
    "type": "Property",  
    "value": "GPL-1.0"  
  },  
  "operationSpace": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        72.564509,  
        11.125289  
      ]  
    }  
  },  
  "page": {  
    "type": "Property",  
    "value": [  
      "http://foo.org/how-to"  
    ]  
  },  
  "provenance": {  
    "type": "Property",  
    "value": [  
      "1",  
      "2"  
    ]  
  },  
  "publisher": {  
    "type": "Property",  
    "value": "Comunidad de madrid"  
  },  
  "servesDataset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:id:HUZY:41266715",  
      "urn:ngsi-ld:Dataset:id:HUZY:41266716"  
    ]  
  },  
  "theme": {  
    "type": "Property",  
    "value": [  
      "Economy",  
      "Tourism"  
    ]  
  },  
  "title": {  
    "type": "LanguageProperty",  
    "languageMap": {  
      "en": "Data service of the european open data portal",  
      "de": "Datendienst des Europäischen Portals für offene Daten",  
      "es": "Data service del portal europeo de datos abiertos",  
      "fr": "Service de données du portail européen de données ouvertes",  
      "it": "Servizio dati del Portale europeo dei dati aperti",  
      "ja": "欧州オープンデータ・ポータルのデータサービス",  
      "ko": "유럽 오픈 데이터 포털의 데이터 서비스",  
      "zh": "欧洲开放数据门户的数据服务",  
      "el": "Υπηρεσία δεδομένων της Ευρωπαϊκής Πύλης Ανοικτών Δεδομένων",  
      "nl": "Dataservice van het Europese open dataportaal",  
      "fi": "Euroopan avoimen datan portaalin tietopalvelu"  
    }  
  },  
  "validationSchema": {  
    "type": "Property",  
    "value": "https://smart-data-models.github.io/dataModel.DCAT-AP/DataService/schema.json"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.DCAT-AP/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
CHANGELOG DCAT-AP DCAT-AP::DataService 2.1.1 -> 3.0.0 (schemaVersion "0.0.2" -> schemaVersion "1.0.0") contactPoint, nuova proprietà in DCAT-AP 3.0.0, array di informazioni di contatto che possono essere utilizzate per inviare commenti sul Data Service. format, nuova proprietà in DCAT-AP 3.0.0, la struttura che può essere restituita interrogando l'endpointURL. keyword, nuova proprietà in DCAT-AP 3.0.0, contiene un elenco di parole chiave o tag, che descrivono il Data Service. landingPage, nuova proprietà in DCAT-AP 3.0.0, questa proprietà si riferisce a una pagina web che fornisce l'accesso al Data Service e/o informazioni aggiuntive. publisher, nuova proprietà in DCAT-AP 3.0.0, questa proprietà si riferisce a una collezione di dati che questo servizio dati può distribuire. theme, nuova proprietà in DCAT-AP 3.0.0, questa proprietà si riferisce a una categoria del Data Service. endPointURL è tradotto in endpointURL. endPointDescription è tradotto in endpointDescription. la descrizione serverDataset è stata modificata da Property a Relationship of Datasets. le proprietà title/description erano rappresentate come un array di stringhe, con ogni voce dell'array che era una traduzione in una lingua specifica. Ora sono rappresentate come LanguageProperty definite nella specifica ETSI NGSI-LD per offrire il supporto multilingue dei dati del Data Service.  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedi [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di misura  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
