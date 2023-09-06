<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティデータセット  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**DCAT-AP 2.1.1仕様を満たすデータセットスキーマ**。  
バージョン: 2.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `Type[string]`: このプロパティは、データセットのタイプを示す。推奨される統制語彙データ型は以下のとおりです。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `accessRights[string]`: このプロパティは、データセットがオープンデータであるか、アクセス制限があるか、公開されていないかを示す情報を指す。  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `accrualPeriodicity[string]`: このプロパティは、データセットが更新される頻度を示す。  . Model: [http://purl.org/dc/terms/Frequency](http://purl.org/dc/terms/Frequency)- `belongsToCatalogue[*]`: この属性は、データセットをその親カタログにリンクします。注：この属性は、DCAT-APの現在のバージョン2.1.1にはありません。  . Model: [https://www.w3.org/ns/dcat#Catalogue](https://www.w3.org/ns/dcat#Catalogue)- `conformsTo[array]`: このプロパティは、実装規則またはその他の仕様を指す。  . Model: [http://purl.org/dc/terms/Standard](http://purl.org/dc/terms/Standard)- `contactPoint[array]`: このプロパティは、データセットに関するコメントを送信するために使用できる連絡先情報を含みます。  . Model: [http://www.w3.org/2006/vcard/ns#Kind](http://www.w3.org/2006/vcard/ns#Kind)- `creator[array]`: このプロパティは、データセットの作成を主に担当するエンティティを指す。  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `description[array]`: このプロパティには、データセットに関するフリーテキストの説明が含まれる。このプロパティは、並列言語版の説明のために繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `distribution[array]`: このプロパティは、データセットを利用可能なディストリビューションにリンクします。  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `hasVersion[array]`: このプロパティは、記述されたデータセットのバージョン、エディション、または翻案である関連データセットを指す。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `id[*]`: エンティティの一意識別子  - `identifier[array]`: このプロパティには、データセットの主な識別子（例えば、カタログのコンテキストにおけるURIまたはその他の一意の識別子）が含まれます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `isReferencedBy[array]`: このプロパティは、データセットを参照、引用、またはその他の形で指し示す出版物などの関連リソースに関するものである。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `isVersionOf[array]`: このプロパティは、説明されているデータセットがバージョン、エディション、または適応である関連データセットを指します。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `issued[date-time]`: このプロパティには、データセットの正式発行日（発行日など）が含まれる。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `keyword[array]`: このプロパティには、データセットを説明するキーワードまたはタグが含まれます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `landingPage[array]`: このプロパティは、データセット、そのディストリビューション、および追加情報へのアクセスを提供するウェブページを指します。このプロパティは、アグリゲータのような第三者のサイト上のページではなく、元のデータ提供者のランディング・ページを指すことを意図しています。  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `language[array]`: このプロパティは、データセットの言語を参照します。データセットに複数の言語がある場合は、このプロパティを繰り返すことができます。  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `modified[date-time]`: このプロパティには、データセットが変更または修正された最新の日付が含まれます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `otherIdentifier[array]`: このプロパティは、MAST/ADS、DataCite、DOI、EZID、W3IDなど、データセットの二次識別子を指します。  . Model: [http://www.w3.org/ns/adms#Identifier](http://www.w3.org/ns/adms#Identifier)- `page[array]`: このプロパティは、このデータセットに関するページまたはドキュメントを参照します。  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `provenance[array]`: このプロパティには、データセットの系統に関する記述が含まれています。  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: このプロパティは、データセットを利用可能にする責任を負うエンティティ（組織）を指す。  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `qualifiedAttribution[array]`: このプロパティは、リソースに対して何らかの責任を持つエージェントへのリンクを指す。  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `qualifiedRelation[array]`: このプロパティは、他のリソースとの関係の記述へのリンクを提供する。  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `relation[array]`: このプロパティは関連リソースを参照する  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `sample[array]`: このプロパティは、データセットのサンプル分布を指す。  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `source[array]`: このプロパティは、記述されたデータセットが派生する関連データセットを参照する。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `spatial[array]`: このプロパティは、データセットがカバーする地理的な領域を指します。  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `spatialResolutionInMeters[number]`: このプロパティは、データセットで解決可能な最小空間分離を指し、メートル単位で測定される。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `temporal[array]`: このプロパティは、データセットがカバーする時間的期間を指す。  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `temporalResolution[array]`: このプロパティは、データセットで解決可能な最小期間を指す。  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `theme[array]`: このプロパティは、データセットのカテゴリを参照します。データセットは複数のテーマに関連付けることができます。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[array]`: このプロパティには、データセットに付けられた名前が格納されます。このプロパティは、並列言語版の名前のために繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `type[string]`: NGSIタイプ。データセット  - `versionInfo[string]`: このプロパティには、データセットのバージョン番号またはその他のバージョン指定が含まれます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `versionNotes[array]`: このプロパティには、このバージョンと以前のバージョンのデータセットとの相違点の説明が含まれます。このプロパティは、バージョン・ノートの並行言語バージョンに対して繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `wasGeneratedBy[array]`: このプロパティは、データセットを生成した、あるいはデータセット生成のためのビジネスコンテキストを提供したアクティビティを指す。  . Model: [https://www.w3.org/ns/prov#Activity](https://www.w3.org/ns/prov#Activity)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `description`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
DCAT-APバージョン2.1.1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211)より引用。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Dataset:    
  description: Dataset Schema meeting DCAT-AP 2.1.1 specification    
  properties:    
    Type:    
      description: This property refers to the type of the Dataset. A recommended controlled vocabulary data-type is foreseen    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    accessRights:    
      description: 'This property refers to information that indicates whether the Dataset is open data, has access restrictions or is not public'    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    accrualPeriodicity:    
      description: This property refers to the frequency at which the Dataset is updated    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/Frequency    
        type: Property    
    belongsToCatalogue:    
      anyOf:    
        - description: Link to the catalogue    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Link to the catalogue    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'It links the Dataset to its parent Catalogue. Note: this attribute does not belong to the current version of DCAT-AP, 2.1.1'    
      x-ngsi:    
        model: "https://www.w3.org/ns/dcat#Catalogue"    
        type: Relationship    
    conformsTo:    
      description: 'This property refers to an implementing rule or other specification. '    
      items:    
        description: Every rule or specification applicable    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Standard    
        type: Property    
    contactPoint:    
      description: This property contains contact information that can be used for sending comments about the Dataset    
      items:    
        description: Every contact element    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2006/vcard/ns#Kind"    
        type: Property    
    creator:    
      description: This property refers to the entity primarily responsible for producing the dataset    
      items:    
        description: Every creator included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    description:    
      description: This property contains a free-text account of the Dataset. This property can be repeated for parallel language versions of the description    
      items:    
        description: Every description in a language    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    distribution:    
      description: This property links the Dataset to an available Distribution    
      items:    
        anyOf:    
          - description: Every link to a distribution    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Every link to a distribution    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Distribution"    
        type: Relationship    
    hasVersion:    
      description: 'This property refers to a related Dataset that is a version, edition, or adaptation of the described Dataset'    
      items:    
        description: Every version of the related datasets    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
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
    identifier:    
      description: 'This property contains the main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue'    
      items:    
        description: Every identifier of the dataset    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    isReferencedBy:    
      description: 'This property is about a related resource, such as a publication, that references, cites, or otherwise points to the dataset'    
      items:    
        description: Every resource related to the dataset    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Relationship    
    isVersionOf:    
      description: 'This property refers to a related Dataset of which the described Dataset is a version, edition, or adaptation'    
      items:    
        description: Every dataset that the current dataset is a version of it    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    issued:    
      description: 'This property contains the date of formal issuance (e.g., publication) of the Dataset'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    keyword:    
      description: 'This property contains a keyword or tag, describing the Dataset'    
      items:    
        description: Every keyword tag included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    landingPage:    
      description: 'This property refers to a web page that provides access to the Dataset, its Distributions and/or additional information. It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator'    
      items:    
        description: Every web page listed    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Property    
    language:    
      description: This property refers to a language of the Dataset. This property can be repeated if there are multiple languages in the Dataset    
      items:    
        description: Every language included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    modified:    
      description: This property contains the most recent date on which the Dataset was changed or modified    
      format: date-time    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    otherIdentifier:    
      description: 'This property refers to a secondary identifier of the Dataset, such as MAST/ADS, DataCite, DOI, EZID or W3ID'    
      items:    
        description: Every additional identifier included    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/adms#Identifier"    
        type: Property    
    page:    
      description: 'This property refers to a page or document about this Dataset. '    
      items:    
        description: Every page or document    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Property    
    provenance:    
      description: This property contains a statement about the lineage of a Dataset    
      items:    
        description: Every lineage associated to the dataset    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/ProvenanceStatement    
        type: Property    
    publisher:    
      description: This property refers to an entity (organisation) responsible for making the Dataset available    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    qualifiedAttribution:    
      description: This property refers to a link to an Agent having some form of responsibility for the resource    
      items:    
        description: Every attribution included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Relationship"    
        type: Property    
    qualifiedRelation:    
      description: This property provides a link to a description of a relationship with another resource    
      items:    
        description: Every qualified relation included    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Relationship"    
        type: Property    
    relation:    
      description: This property refers to a related resource    
      items:    
        description: Every related resource included    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Resource"    
        type: Property    
    sample:    
      description: This property refers to a sample distribution of the dataset    
      items:    
        description: Every sample included with the dataset    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Distribution"    
        type: Property    
    source:    
      description: This property refers to a related Dataset from which the described Dataset is derived    
      items:    
        description: Every dataset which is a source of the current dataset    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/ns/dcat#Dataset"    
        type: Property    
    spatial:    
      description: This property refers to a geographic region that is covered by the Dataset    
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
    spatialResolutionInMeters:    
      description: 'This property refers to the minimum spatial separation resolvable in a dataset, measured in meters'    
      type: number    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    temporal:    
      description: This property refers to a temporal period that the Dataset covers    
      items:    
        description: Every temporal period included    
        format: date-time    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime    
        type: Property    
    temporalResolution:    
      description: 'This property refers to the minimum time period resolvable in the dataset. '    
      items:    
        description: Every temporal resolution included    
        format: duration    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime    
        type: Property    
    theme:    
      description: This property refers to a category of the Dataset. A Dataset may be associated with multiple themes    
      items:    
        description: Every theme included    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2004/02/skos/core#Concept"    
        type: Property    
    title:    
      description: This property contains a name given to the Dataset. This property can be repeated for parallel language versions of the name    
      items:    
        description: Every title in a language    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    type:    
      description: NGSI type. It has to be Dataset    
      enum:    
        - Dataset    
      type: string    
      x-ngsi:    
        type: Property    
    versionInfo:    
      description: This property contains a version number or other version designation of the Dataset    
      type: string    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    versionNotes:    
      description: This property contains a description of the differences between this version and a previous version of the Dataset. This property can be repeated for parallel language versions of the version notes    
      items:    
        description: Every language description of the version notes    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: "http://www.w3.org/2000/01/rdf-schema#Literal"    
        type: Property    
    wasGeneratedBy:    
      description: 'This property refers to an activity that generated, or provides the business context for, the creation of the dataset'    
      items:    
        description: Every activity included    
        type: string    
        x-ngsi:    
          type: Property    
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
## ペイロードの例  
#### データセット NGSI-v2 キー値の例  
以下は、JSON-LD形式のデータセットをkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
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
  "belongsToCatalogue": "urn:ngsi-ld:Catalogue:items:MWVK:61846917",  
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
#### データセット NGSI-v2 正規化 例  
以下は、正規化されたJSON-LD形式のデータセットの例です。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
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
  "belongsToCatalogue": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Catalogue:items:MWVK:61846917"  
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
#### データセット NGSI-LD キー値の例  
JSON-LD形式のデータセットをkey-valuesとした例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
  "belongsToCatalogue": "urn:ngsi-ld:Catalogue:items:MWVK:61846917",  
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
#### データセット NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のデータセットの例です。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "belongsToCatalogue": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Catalogue:items:MWVK:61846917"  
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
  "relation": {  
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
  "versionInfo": {  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
