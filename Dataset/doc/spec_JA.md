<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：データセット  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md)  
[自動生成されたドキュメント](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全体的な説明：**DCAT-AP 3.0.0仕様に基づくデータセットスキーマ定義。**  
version: 3.0.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティリスト  

<sup><sub>[*] 属性に型がない場合、それは複数の型または異なる形式/パターンを持つ可能性があるためです。</sub></sup>  
- `Type[string]`: このプロパティはデータセットのタイプを参照します。推奨される制御語彙データタイプが想定されています。値は、DCMI Type vocabulary (https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7)、[ISO-19115-1] scope codes (https://standards.iso.org/iso/19115/resources/Codelists/gml/MD_ScopeCode.xml)、Datacite resource types [DataCite] (https://schema.datacite.org/meta/kernel-4.1/include/datacite-resourceType-v4.1.xsd)、re3data.org [RE3DATA-SCHEMA] (https://www.re3data.org/) で使用されている PARSE.Insight content-types (項目15 contentTypeを参照)、MARC 知的リソースタイプ (http://id.loc.gov/vocabulary/marcgt.html) など、適切に管理され、広く認識されている制御語彙から取得する必要があります。これらの制御語彙の一部は、データセットやデータサービスに厳密には適していませんが（例：DCMI TypeのEvent、PhysicalObject、[ISO-19115-1](https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19115-1)のCollectionHardware、CollectionSession、Initiative、Sample、Repository）、DCATプロファイルまたはアプリケーションで定義された他の種類のカタログのコンテキストで使用される場合があります。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `accessMechanism[string]`: MELODA5指標の3つのレベルに基づくアクセスレベルです。期待される値は以下の通りです：* Level1AccessMechanism: データセットへのウェブアクセスまたは一意のURLパラメータ。* Level2AccessMechanism: 単一データへのパラメータを伴う一意のウェブアクセス。* Level3AccessMechanism: APIまたはクエリ言語。  . Model: [https://schema.org/Text](https://schema.org/Text)- `accessRights[string]`: このプロパティは、データセットがオープンデータであるか、アクセス制限があるか、または非公開であるかを示す情報を指します。  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `accuralPeriodicity[string]`: このプロパティは、データセットが更新される頻度を参照します。  . Model: [http://purl.org/dc/terms/Frequency](http://purl.org/dc/terms/Frequency)- `addressesAvailable[boolean]`: データストリームが、データセット内の要素を識別するための郵便住所を持っているかどうかを定義します。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `applicableLegislation[array]`: データセットの作成または管理を義務付ける法律。カーディナリティ：0..n。  . Model: [http://data.europa.eu/r5r/applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)- `belongsToCatalogue[*]`: データセットをその親カタログにリンクします。注：この属性はDCAT-APの現在のバージョン2.1.1には含まれていません。  . Model: [https://www.w3.org/ns/dcat#Catalogue](https://www.w3.org/ns/dcat#Catalogue)- `conformsTo[array]`: このプロパティは、実施規則またはその他の仕様を参照します。  . Model: [http://purl.org/dc/terms/conformsTo](http://purl.org/dc/terms/conformsTo)- `contactPoint[array]`: データセットに関するコメントを送信するために使用できる連絡先情報。カーディナリティ：0..n。  . Model: [http://www.w3.org/ns/dcat#contactPoint](http://www.w3.org/ns/dcat#contactPoint)- `creator[array]`: このプロパティは、データセットの作成に主に責任を持つエンティティを参照します。  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `description[*]`: LanguageProperty。このプロパティは、データセットの自由形式の記述を含みます。このプロパティは、説明の並列言語バージョンに対して繰り返すことができます。  . Model: [http://purl.org/dc/terms/description](http://purl.org/dc/terms/description)- `dissemination[string]`: MELODA5のコミュニケーション次元に基づく普及レベル： * Level1Dissemination：コミュニケーション/普及が体系的ではない。 * Level2Dissemination：更新に関する利用可能なリソース（例：RSSフィード）。 * Level3Dissemination：プロアクティブな普及/プッシュ型普及（自動的かつタイムリーな情報提供）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `disseminationOrganization[string]`: データセットに関連する普及活動に責任を持つ組織へのURI。これはMELODA5の次元/コミュニケーションに一致します。  . Model: [https://schema.org/url](https://schema.org/url)- `distribution[array]`: このプロパティは、データセットを利用可能なディストリビューションにリンクします。  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `geolocation[boolean]`: データストリームのいずれかの属性に地理位置情報（座標）が含まれているかどうかを定義します。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasVersion[array]`: このプロパティは、記述されたデータセットのバージョン、版、または適応である関連データセットを参照します。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `id[*]`: エンティティの一意な識別子  - `identifier[array]`: このプロパティは、カタログのコンテキストにおけるURIやその他のユニーク識別子など、データセットのメイン識別子を含みます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `inSeries[array]`: このプロパティは、データセットを利用可能なディストリビューションにリンクします。  . Model: [https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series)- `isReferencedBy[array]`: このプロパティは、データセットを参照、引用、またはその他の方法で指し示す出版物などの関連リソースに関するものです。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `isVersionOf[array]`: このプロパティは、記述されたデータセットがバージョン、版、または適応版である関連するデータセットを指します。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `issued[date-time]`: このプロパティは、データセットの正式な発行日（例：公開日）を含みます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `keyword[array]`: このプロパティは、データセットを記述するキーワードまたはタグを含みます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `landingPage[array]`: このプロパティは、データセット、その配布物、および/または追加情報へのアクセスを提供するウェブページを参照します。これは、アグリゲーターなどの第三者のサイトのページではなく、元のデータ提供者のランディングページを指すことを意図しています。  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `language[array]`: このプロパティは、データセットの言語を参照します。データセットに複数の言語がある場合は、このプロパティを繰り返すことができます。可能な値は、米国議会図書館（ISO 639-1: http://id.loc.gov/vocabulary/iso639-1.html、ISO 639-2: http://id.loc.gov/vocabulary/iso639-2.html）によって定義されています。  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: このプロパティは、データセットが提供される際のライセンスを指します。列挙値に基づくライセンスのIDです。これはSPDX標準（https://spdx.org/licenses）のIDから抽出されます。  . Model: [http://purl.org/dc/terms#LicenseDocument](http://purl.org/dc/terms#LicenseDocument)- `modified[date-time]`: このプロパティは、データセットが変更または修正された最新の日付を含みます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `otherIdentifier[array]`: このプロパティは、MAST/ADS、DataCite、DOI、EZID、W3IDなどのデータセットの二次識別子を参照します。  . Model: [http://www.w3.org/ns/adms#Identifier](http://www.w3.org/ns/adms#Identifier)- `page[array]`: このプロパティは、このデータセットに関するページまたはドキュメントを参照します。  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `provenance[array]`: このプロパティは、データセットのリネージ（系譜）に関する記述を含みます。  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: このプロパティは、データセットを利用可能にする責任を持つエンティティ（組織）を参照します。  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `qualifiedAttribution[array]`: このプロパティは、リソースに対して何らかの責任を持つエージェントへのリンクを参照します。  . Model: [https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)- `qualifiedRelation[array]`: このプロパティは、他のリソースとの関係に関する説明へのリンクを提供します。  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `relation[array]`: このプロパティは、関連リソースを参照します。  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `reputation[string]`: MELODA5のレピュテーション次元に基づくレピュテーションレベル： * Level1Reputation：データソースのレピュテーションに関する情報なし。 * Level2Reputation：ユーザーの意見について公開された統計またはレポート。 * Level3Reputation：データソースのレピュテーションに関する指標またはランキング。  . Model: [https://schema.org/Text](https://schema.org/Text)- `reputationOrganization[string]`: レピュテーションの観点からデータセットの公開に責任を持つ組織へのURI。これはMELODA5のレピュテーション次元に一致し、ランキングからその威信（プレステージ）を取得することを可能にします。  . Model: [https://schema.org/url](https://schema.org/url)- `sample[array]`: このプロパティは、データセットのサンプル分布を参照します。  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `source[array]`: このプロパティは、記述されたデータセットの派生元である関連データセットを参照します。  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `spatial[array]`: このプロパティは、データセットがカバーする地理的領域を参照します。  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `spatialResolution[number]`: このプロパティは、データセットで分解可能な最小の空間的分離（メートル単位）を参照します。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `standardization[string]`: データセットが従っているデータモデル標準化のタイプです。これは、次の3つ（4つ）の可能な値を持つ列挙型です：* Level1Standardization: ドキュメントを公開せずに発行元によって標準化されたデータモデル。* Level2Standardization: ドキュメントを公開して発行元によって標準化されたデータモデル。* Level3Standardization: ローカル標準（国内またはより狭い地域範囲）を使用するデータモデル。* Level4Standardization: 国際標準を使用するデータモデル。  . Model: [https://schema.org/Text](https://schema.org/Text)- `standardizationSource[string]`: 属性の定義を読み取ることができるソースへのURI。これは標準化プロパティに関連付けられています。レベル1およびレベル2の場合は空になる場合があり、レベル3の場合は既存の標準化団体（例：DIN、UNEなど）、レベル4の場合は（例：ISO、W3Cなど）へのリンクになります。  . Model: [https://schema.org/url](https://schema.org/url)- `temporal[array]`: このプロパティは、データセットがカバーする時間的期間を参照します。  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `temporalResolution[array]`: このプロパティは、データセットで分解可能な最小の時間期間を参照します。  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `theme[array]`: このプロパティは、データセットのカテゴリを参照します。データセットは複数のテーマに関連付けられる場合があります。  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[*]`: LanguageProperty。このプロパティは、データセットに与えられた名前を含みます。このプロパティは、名前の並列言語バージョンに対して繰り返すことができます。  . Model: [http://purl.org/dc/terms/title](http://purl.org/dc/terms/title)- `type[string]`: NGSIタイプ。Datasetである必要があります。  - `validationSchema[string]`: Smart Data Models プログラムにおけるデータセットの技術的なバリデーションスキーマ（JSONスキーマ）へのURL。  . Model: [https://schema.org/url](https://schema.org/url)- `version[string]`: このプロパティは、データセットのバージョン番号またはその他のバージョン指定を含みます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `versionNotes[array]`: このプロパティは、このバージョンとデータセットの以前のバージョンとの違いに関する説明を含みます。このプロパティは、バージョンノートの並列言語バージョンに対して繰り返すことができます。  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `wasGeneratedBy[array]`: このプロパティは、データセットの作成を生成した、または作成に関するビジネスコンテキストを提供するアクティビティを指します。  . Model: [https://www.w3.org/ns/prov#Activity](https://www.w3.org/ns/prov#Activity)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `description`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
[DCAT-AP version 3.0.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/) より適応。FAIR原則およびMELODA5次元プロパティを追加。accessMechanism：Meloda5メトリクスの3レベルに基づくアクセスレベル。想定される値は、Level1AccessMechanism（WebアクセスまたはデータセットへのユニークなURLパラメータ）、Level2AccessMechanism（単一データへのパラメータ付きユニークWebアクセス）、Level3AccessMechanism（APIまたはクエリ言語）です。addressAvailable：データストリームが、データセット内の要素を識別するための郵便住所を持っているかどうかを定義します。dissemination：Meloda5コミュニケーション次元に基づく普及レベル：Level1Dissemination（コミュニケーション/普及が体系的ではない）、Level2Dissemination（更新に関する利用可能なリソース、例：RSSフィード）、Level3Dissemination（プロアクティブな普及/プッシュ型普及、自動的かつタイムリーな情報提供）。diseminationOrganization：データセットに関連する普及活動に責任を持つ組織へのURI。Meloda5の次元/コミュニケーションに一致します。geolocation：データストリームのいずれかの属性に地理位置情報（座標）があるかどうかを定義します。license：このプロパティは、データセットが提供されるライセンスを参照します。列挙された値に基づくライセンスID。SPDX標準 (https://spdx.org/licenses) のIDから抽出されます。reputation：Meloda5レピュテーション次元に基づくレピュテーションレベル：Level1Reputation（データソースのレピュテーションに関する情報なし）、Level2Reputation（ユーザーの意見について公開された統計またはレポート）、Level3Reputation（データソースのレピュテーションに関する指標またはランキング）。reputationOrganization：レピュテーションの観点からデータセットの公開に責任を持つ組織へのURI。Meloda5のレピュテーション次元に一致し、ランキングからその威信を取得することを可能にします。standardization：データセットが準拠しているデータモデル標準化のタイプ。以下の4つの可能な値を持つ列挙型です：Level1Standardization（ドキュメントを公開せずに発行者が標準化したデータモデル）、Level2Standardization（ドキュメントを公開して発行者が標準化したデータモデル）、Level3Standardization（ローカル標準、国内または小規模な地域範囲の標準を使用したデータモデル）、Level4Standardization（国際標準を使用したデータモデル）。standardizationSource：属性の定義を読み取ることができるソースへのURI。標準化プロパティに関連付けられています。レベル1およびレベル2の場合は空になる場合があり、レベル3の場合は既存の標準化団体（例：DIN、UNEなど）、レベル4の場合は（例：ISO、W3Cなど）へのリンクになります。validationSchema：Smart Data Models プログラムにおけるデータセットの技術的なバリデーションスキーマ（JSONスキーマ）へのURL。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順にソートされています（詳細はこちらをクリック）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Dataset:    
  description: Dataset Schema definition based on DCAT-AP 3.0.0 specification.    
  properties:    
    Type:    
      description: This property refers to the type of the Dataset. A recommended controlled vocabulary data-type is foreseen. The value SHOULD be taken from a well governed and broadly recognised controlled vocabulary, such as DCMI Type vocabulary (https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7), [ISO-19115-1] scope codes (https://standards.iso.org/iso/19115/resources/Codelists/gml/MD_ScopeCode.xml), Datacite resource types [DataCite] (https://schema.datacite.org/meta/kernel-4.1/include/datacite-resourceType-v4.1.xsd), PARSE.Insight content-types used by re3data.org [RE3DATA-SCHEMA] (https://www.re3data.org/) (see item 15 contentType), MARC intellectual resource types (http://id.loc.gov/vocabulary/marcgt.html). Some members of these controlled vocabularies are not strictly suitable for datasets or data services (e.g., DCMI Type Event, PhysicalObject; [ISO-19115-1](https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19115-1) CollectionHardware, CollectionSession, Initiative, Sample, Repository), but might be used in the context of other kinds of catalogs defined in DCAT profiles or applications.    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2004/02/skos/core#Concept    
        type: Property    
    accessMechanism:    
      description: 'Access level according to the 3 levels of MELODA5 metric. The expected values are: * Level1AccessMechanism: Web access or unique URL parameters to dataset. * Level2AccessMechanism: Web Access unique with parameters to single data. * Level3AccessMechanism: API or query language.'    
      enum:    
        - Level1AccessMechanism    
        - Level2AccessMechanism    
        - Level3AccessMechanism    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    accessRights:    
      description: This property refers to information that indicates whether the Dataset is open data, has access restrictions or is not public.    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/RightsStatement    
        type: Property    
    accuralPeriodicity:    
      description: This property refers to the frequency at which the Dataset is updated.    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/terms/Frequency    
        type: Property    
    addressesAvailable:    
      description: Defines if the data stream has postal addresses to identify the elements in the dataset.    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    applicableLegislation:    
      description: 'The legislation that mandates the creation or management of the Dataset. Cardinality: 0..n.'    
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
    belongsToCatalogue:    
      anyOf:    
        - description: Link to the catalogue.    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Link to the catalogue.    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'It links the Dataset to its parent Catalogue. Note: this attribute does not belong to the current version of DCAT-AP, 2.1.1.'    
      x-ngsi:    
        model: https://www.w3.org/ns/dcat#Catalogue    
        type: Relationship    
    conformsTo:    
      description: This property refers to an implementing rule or other specification.    
      items:    
        description: Every rule or specification applicable.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/conformsTo    
        type: Property    
    contactPoint:    
      description: 'Contact information that can be used for sending comments about the Dataset. Cardinality: 0..n.'    
      items:    
        description: Every contact element    
        properties:    
          email:    
            description: Email as defined by the 'Mailbox' ABNF rule in RFC 5321, section 4.1.2 (https://datatracker.ietf.org/doc/html/rfc5321#section-4.1.2).    
            format: email    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#contactPoint    
        type: Property    
    creator:    
      description: This property refers to the entity primarily responsible for producing the dataset.    
      items:    
        description: Every creator included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    description:    
      description: LanguageProperty. This property contains a free-text account of the Dataset. This property can be repeated for parallel language versions of the description.    
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
    dissemination:    
      description: 'Dissemination level according to MELODA5 communication dimension: * Level1Dissemination: communication/dissemination not systematic. * Level2Dissemination: available resources on updates (i.e., RSS feed). * Level3Dissemination: proactive dissemination/push dissemination (information automatic and timely).'    
      enum:    
        - Level1Dissemination    
        - Level2Dissemination    
        - Level3Dissemination    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    disseminationOrganization:    
      description: URI to the organization which is responsible for dissemination activities related to the dataset. It matches the dimension/communication of MELODA5.    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
    distribution:    
      description: This property links the Dataset to an available Distribution.    
      items:    
        anyOf:    
          - description: Every link to a distribution.    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Every link to a distribution.    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: This property provides a list of distributions in the format of either URI or NGSI-LD Identifier.    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Distribution    
        type: Relationship    
    geolocation:    
      description: Defines if the data stream has geolocation (coordinates) in any of its attributes.    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    hasVersion:    
      description: This property refers to a related Dataset that is a version, edition, or adaptation of the described Dataset.    
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
        description: Every version of the related datasets.    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Dataset    
        type: Relationship    
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
    identifier:    
      description: This property contains the main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.    
      items:    
        description: Every identifier of the dataset.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Relationship    
    inSeries:    
      description: This property links the Dataset to an available Distribution.    
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
        description: A dataset series of which the dataset is part.    
        x-ngsi:    
          model: http://www.w3.org/ns/dcat#Dataset    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series    
        type: Relationship    
    isReferencedBy:    
      description: This property is about a related resource, such as a publication, that references, cites, or otherwise points to the dataset.    
      items:    
        description: Every resource related to the dataset.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Relationship    
    isVersionOf:    
      description: This property refers to a related Dataset of which the described Dataset is a version, edition, or adaptation.    
      items:    
        description: Every dataset that the current dataset is a version of it.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Dataset    
        type: Relationship    
    issued:    
      description: This property contains the date of formal issuance (e.g., publication) of the Dataset.    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    keyword:    
      description: This property contains a keyword or tag, describing the Dataset.    
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
      description: This property refers to a web page that provides access to the Dataset, its Distributions and/or additional information. It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator.    
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
    language:    
      description: 'This property refers to a language of the Dataset. This property can be repeated if there are multiple languages in the Dataset. The possible values are defined by the Library of Congress (ISO 639-1: http://id.loc.gov/vocabulary/iso639-1.html, ISO 639-2: http://id.loc.gov/vocabulary/iso639-2.html).'    
      items:    
        description: Every language included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/LinguisticSystem    
        type: Property    
    license:    
      description: This property refers to the license under which the Dataset is made available. Id of the license according to the enumerated values. It is extracted from the id of the SPDX standard (https://spdx.org/licenses).    
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
        model: http://purl.org/dc/terms#LicenseDocument    
        type: Property    
    modified:    
      description: This property contains the most recent date on which the Dataset was changed or modified.    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    otherIdentifier:    
      description: This property refers to a secondary identifier of the Dataset, such as MAST/ADS, DataCite, DOI, EZID or W3ID.    
      items:    
        description: Every additional identifier included.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/adms#Identifier    
        type: Relationship    
    page:    
      description: This property refers to a page or document about this Dataset.    
      items:    
        description: Every page or document.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Document    
        type: Relationship    
    provenance:    
      description: This property contains a statement about the lineage of a Dataset.    
      items:    
        description: Every lineage associated to the dataset.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/ProvenanceStatement    
        type: Property    
    publisher:    
      description: This property refers to an entity (organisation) responsible for making the Dataset available.    
      type: string    
      x-ngsi:    
        model: http://xmlns.com/foaf/0.1/Agent    
        type: Property    
    qualifiedAttribution:    
      description: This property refers to a link to an Agent having some form of responsibility for the resource.    
      items:    
        description: Every attribution included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution    
        type: Relationship    
    qualifiedRelation:    
      description: This property provides a link to a description of a relationship with another resource.    
      items:    
        description: Every qualified relation included.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Relationship    
        type: Relationship    
    relation:    
      description: This property refers to a related resource.    
      items:    
        description: Every related resource included.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Resource    
        type: Relationship    
    reputation:    
      description: 'Reputation level according to MELODA5 reputation dimension: * Level1Reputation: no information about the reputation of the data source. * Level2Reputation: statistics or reports published on user’s opinions. * Level3Reputation: Indicators or rankings on reputation of the data source.'    
      enum:    
        - Level1Reputation    
        - Level2Reputation    
        - Level3Reputation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    reputationOrganization:    
      description: URI to the organization which is responsible for the publication of the dataset in terms of reputation. It matches the dimension reputation of MELODA5 and it allows to retrieve their prestige from the ranking.    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
    sample:    
      description: This property refers to a sample distribution of the dataset.    
      items:    
        description: Every sample included with the dataset.    
        format: uri    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Distribution    
        type: Relationship    
    source:    
      description: This property refers to a related Dataset from which the described Dataset is derived.    
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
        description: Every version of the related datasets.    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/ns/dcat#Dataset    
        type: Relationship    
    spatial:    
      description: This property refers to a geographic region that is covered by the Dataset.    
      items:    
        description: Every location included.    
        oneOf:    
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
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
          - bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items: {}    
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
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/Location    
        type: GeoProperty    
    spatialResolution:    
      description: This property refers to the minimum spatial separation resolvable in a dataset, measured in meters.    
      type: number    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    standardization:    
      description: 'The type of data model standardization followed by the dataset. This is an enumeration with three (4) possible values: * Level1Standardization: data model standardized by the publisher without releasing the documentation. * Level2Standardization: data model standardized by the published releasing the documentation. * Level3Standardization: data model using a local standard (national or smaller regional scope). * Level4Standardization: data model using an international standard.'    
      enum:    
        - Level1Standardization    
        - Level2Standardization    
        - Level3Standardization    
        - Level4Standardization    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    standardizationSource:    
      description: URI to the source where the definitions of the attributes can be read. It is associated with the standardization property. It can be empty in case of Level1 and Level2 or link to an existing standardization body (e.g., DIN, UNE, etc.) for Level3 or (e.g., ISO, W3C, etc.) for Level4.    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
    temporal:    
      description: This property refers to a temporal period that the Dataset covers.    
      items:    
        description: Every temporal period included.    
        format: date-time    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime    
        type: Property    
    temporalResolution:    
      description: This property refers to the minimum time period resolvable in the dataset.    
      items:    
        description: Every temporal resolution included.    
        format: duration    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://purl.org/dc/terms/PeriodOfTime    
        type: Property    
    theme:    
      description: This property refers to a category of the Dataset. A Dataset may be associated with multiple themes.    
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
      description: LanguageProperty. This property contains a name given to the Dataset. This property can be repeated for parallel language versions of the name.    
      oneOf:    
        - properties:    
            languageMap:    
              description: A JSON object consisting of a series of key-value pairs where the keys shall be JSON strings representing IETF RFC 5646 (https://www.rfc-editor.org/info/rfc5646) language codes.    
              properties:    
                de:    
                  description: The title written in German.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                el:    
                  description: The title written in Modern Greek.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                en:    
                  description: The title written in English.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                es:    
                  description: The title written in Spanish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fi:    
                  description: The title written in Finnish.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                fr:    
                  description: The title written in French.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                it:    
                  description: The title written in Italian.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ja:    
                  description: The title written in Japanese.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                ko:    
                  description: The title written in Korean.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                nl:    
                  description: The title written in Dutch.    
                  type: string    
                  x-ngsi:    
                    model: http://www.w3.org/2000/01/rdf-schema#Literal    
                    type: Property    
                zh:    
                  description: The title written in Chinese.    
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
      description: NGSI type. It has to be Dataset.    
      enum:    
        - Dataset    
      type: string    
      x-ngsi:    
        type: Property    
    validationSchema:    
      description: URL to the technical validation schema for the dataset (JSON Schema) in the Smart Data Models program.    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
    version:    
      description: This property contains a version number or other version designation of the Dataset.    
      type: string    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    versionNotes:    
      description: This property contains a description of the differences between this version and a previous version of the Dataset. This property can be repeated for parallel language versions of the version notes.    
      items:    
        description: Every language description of the version notes.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: http://www.w3.org/2000/01/rdf-schema#Literal    
        type: Property    
    wasGeneratedBy:    
      description: This property refers to an activity that generated, or provides the business context for, the creation of the dataset.    
      items:    
        description: Every activity included.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://www.w3.org/ns/prov#Activity    
        type: Property    
  required:    
    - id    
    - type    
    - description    
    - title    
  type: object    
  x-derived-from: https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DCAT-AP/Dataset/schema.json    
  x-model-tags: INTERSTAT, WATERVERSE    
  x-version: 3.0.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 例のペイロード  
#### データセット NGSI-v2 キー・バリュー例  
以下は、キー・バリュー形式のJSON-LDフォーマットによるデータセットの例です。これは `options=keyValues` を使用する場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:VESI:23278568",  
  "type": "Dataset",  
  "accessMechanism": "Level3AccessMechanism",  
  "accessRights": "https://creativecommons.org/licenses/by/4.0/legalcode.es",  
  "accuralPeriodicity": "weekly",  
  "addressesAvailable": true,  
  "applicableLegislation": [  
    "Regulation 883/2004",  
    "Regulation 465/2012"  
  ],  
  "belongsToCatalogue": "urn:ngsi-ld:Catalogue:items:MWVK:61846917",  
  "conformsTo": [  
    "http://www.opengis.net/def/crs/EPSG/0/28992",  
    "http://data.europa.eu/eli/reg/2014/1312/oj"  
  ],  
  "contactPoint": [  
    {  
      "email": "wheatfarm@email.com"  
    },  
    {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  ],  
  "creator": [  
    "Comunidad de Madrid"  
  ],  
  "description": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
  },  
  "dissemination": "Level2Dissemination",  
  "disseminationOrganization": "https://url_to_organization.org",  
  "distribution": [  
    "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
  ],  
  "geolocation": true,  
  "hasVersion": [  
    "urn:ngsi-ld:Dataset:items:SQSB:90831182",  
    "urn:ngsi-ld:Dataset:items:FFVZ:69502935"  
  ],  
  "identifier": [  
    "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
    "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
  ],  
  "inSeries": [  
    "urn:ngsi-ld:Dataset:id:HUZY:681332655",  
    "urn:ngsi-ld:Dataset:id:HUZY:681970245"  
  ],  
  "isReferencedBy": [  
    "urn:ngsi-ld:Dataset:items:YQRP:33454193",  
    "urn:ngsi-ld:Dataset:items:RBND:48628164"  
  ],  
  "isVersionOf": [  
    "urn:ngsi-ld:Dataset:items:AMAC:16896252",  
    "urn:ngsi-ld:Dataset:items:IPSO:04920226"  
  ],  
  "issued": "1983-07-16T12:51:26Z",  
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
    "vivienda de uso turístico"  
  ],  
  "landingPage": [  
    "urn:ngsi-ld:Dataset:items:UMBA:72418275",  
    "urn:ngsi-ld:Dataset:items:GUKW:86586813"  
  ],  
  "language": [  
    "EN",  
    "SP"  
  ],  
  "license": "AGPL-3.0",  
  "modified": "2015-07-13T03:09:32Z",  
  "otherIdentifier": [  
    "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
    "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
  ],  
  "page": [  
    "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
    "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "publisher": "Comunidad de madrid",  
  "qualifiedAttribution": [  
    "urn:ngsi-ld:Agent:2567369057",  
    "urn:ngsi-ld:Agent:6457369057"  
  ],  
  "qualifiedRelation": [  
    "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
    "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
  ],  
  "relation": [  
    "urn:ngsi-ld:Dataset:items:FXEY:35067714",  
    "urn:ngsi-ld:Dataset:items:YYOL:47950545"  
  ],  
  "reputation": "Level2Reputation",  
  "reputationOrganization": "https://url_to_organization.org",  
  "sample": [  
    "urn:ngsi-ld:Dataset:items:QJPZ:50290394",  
    "urn:ngsi-ld:Dataset:items:ZSSA:73451152"  
  ],  
  "source": [  
    "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  ],  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        9.922458,  
        109.478534  
      ]  
    }  
  ],  
  "spatialResolution": 0.6,  
  "standardization": "Level4Standardization",  
  "standardizationSource": "https://www.w3.org/",  
  "temporal": [  
    "2023-04-03T02:35:57Z"  
  ],  
  "temporalResolution": [  
    "PT15M"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "title": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
  },  
  "Type": "service",  
  "validationSchema": "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/refs/heads/master/Dataset/schema.json",  
  "version": "3.0",  
  "versionNotes": [  
    "With temporal evolution"  
  ],  
  "wasGeneratedBy": [  
    "datos.gob.es"  
  ]  
}  
```  
</details>  
#### データセット NGSI-v2 正規化例  
以下は、正規化されたJSON-LDフォーマットによるデータセットの例です。これはオプションを使用しない場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:HUZY:68185655",  
  "type": "Dataset",  
  "accessMechanism": {  
    "type": "Text",  
    "value": "Level3AccessMechanism"  
  },  
  "accessRights": {  
    "type": "Text",  
    "value": "https://creativecommons.org/licenses/by/4.0/legalcode.es"  
  },  
  "accuralPeriodicity": {  
    "type": "Text",  
    "value": "two years"  
  },  
  "addressesAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "applicableLegislation": {  
    "type": "StructuredValue",  
    "value": [  
      "Regulation 883/2004",  
      "Regulation 465/2012"  
    ]  
  },  
  "belongsToCatalogue": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Catalogue:items:MWVK:61846917"  
  },  
  "conformsTo": {  
    "type": "StructuredValue",  
    "value": [  
      "http://www.opengis.net/def/crs/EPSG/0/28992",  
      "http://data.europa.eu/eli/reg/2014/1312/oj"  
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
  "creator": {  
    "type": "StructuredValue",  
    "value":  [  
      "Comunidad de Madrid"  
    ]  
  },  
  "description": {  
    "type": "StructuredValue",  
    "value": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "dissemination": {  
    "type": "Text",  
    "value": "Level2Dissemination"  
  },  
  "disseminationOrganization": {  
    "type": "Text",  
    "value": "https://url_to_organization.org"  
  },  
  "distribution": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
      "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
    ]  
  },  
  "geolocation": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasVersion": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:id:ASDF:68185655",  
      "urn:ngsi-ld:Dataset:id:ASDF:78185655"  
    ]  
  },  
  "identifier": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
      "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
    ]  
  },  
  "inSeries": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:id:HUZY:681332655",  
      "urn:ngsi-ld:Dataset:id:HUZY:681970245"  
    ]  
  },  
  "isReferencedBy": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:HJNK:88711880",  
      "urn:ngsi-ld:Dataset:items:MDEO:95193079"  
    ]  
  },  
  "isVersionOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:RBWE:31388012",  
      "urn:ngsi-ld:Dataset:items:GATZ:02632837"  
    ]  
  },  
  "issued": {  
    "type": "StructuredValue",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-10-01T15:46:46Z"  
    }  
  },  
  "keyword": {  
    "type": "StructuredValue",  
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
    "vivienda de uso turístico"  
    ]  
  },  
  "landingPage": {  
    "type": "StructuredValue",  
    "value": [  
      "htps://meloda.org"  
    ]  
  },  
  "language": {  
    "type": "StructuredValue",  
    "value": [  
      "EN",  
      "ES"  
    ]  
  },  
  "license": {  
    "type": "Text",  
    "value": "AGPL-3.0"  
  },  
  "modified": {  
    "type": "StructuredValue",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-01T10:27:59Z"  
    }  
  },  
  "otherIdentifier": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
      "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
      ]  
  },  
  "page": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
      "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
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
  "qualifiedAttribution": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Agent:2567369057",  
      "urn:ngsi-ld:Agent:6457369057"  
    ]  
  },  
  "qualifiedRelation": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
      "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
    ]  
  },  
  "relation": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:LGBY:74926949",  
      "urn:ngsi-ld:Dataset:items:ZAUC:79968579"  
    ]  
  },  
  "reputation": {  
    "type": "Text",  
    "value": "Level2Reputation"  
  },  
  "reputationOrganization": {  
    "type": "Text",  
    "value": "https://url_to_organization.org"  
  },  
  "sample": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:MLHW:64299003",  
      "urn:ngsi-ld:Dataset:items:GNXL:59256807"  
    ]  
  },  
  "source": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
    ]  
  },  
  "spatial": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        22.1394715,  
        -7.100602  
      ]  
    }  
  },  
  "spatialResolution": {  
    "type": "Number",  
    "value": 0.6  
  },  
  "standardization": {  
    "type": "Text",  
    "value": "Level4Standardization"  
  },  
  "standardizationSource": {  
    "type": "Text",  
    "value": "https://www.w3.org/"  
  },  
  "temporal": {  
    "type": "StructuredValue",  
    "value": [  
    "2023-04-03T02:35:57Z"  
    ]  
  },  
  "temporalResolution": {  
    "type": "StructuredValue",  
    "value": [  
      "PT15M"  
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
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "Type": {  
    "type": "Text",  
    "value": "service"  
  },  
  "validationSchema": {  
    "type": "Text",  
    "value": "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/refs/heads/master/Dataset/schema.json"  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "versionNotes": {  
    "type": "StructuredValue",  
    "value": [  
      "With temporal evolution"  
    ]  
  },  
  "wasGeneratedBy": {  
    "type": "StructuredValue",  
    "value": [  
      "meloda Team"  
    ]  
  }  
}  
```  
</details>  
#### データセット NGSI-LD キー値の例  
以下は、キー・バリュー形式のJSON-LDフォーマットによるデータセットの例です。これは `options=keyValues` を使用する場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:VESI:23278568",  
  "type": "Dataset",  
  "accessMechanism": "Level3AccessMechanism",  
  "accessRights": "https://creativecommons.org/licenses/by/4.0/legalcode.es",  
  "accuralPeriodicity": "weekly",  
  "addressesAvailable": true,  
  "applicableLegislation": [  
    "Regulation 883/2004",  
    "Regulation 465/2012"  
  ],  
  "belongsToCatalogue": "urn:ngsi-ld:Catalogue:items:MWVK:61846917",  
  "conformsTo": [  
    "http://www.opengis.net/def/crs/EPSG/0/28992",  
    "http://data.europa.eu/eli/reg/2014/1312/oj"  
  ],  
  "contactPoint": [  
    {  
      "email": "wheatfarm@email.com"  
    },  
    {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  ],  
  "creator": [  
    "Comunidad de Madrid"  
  ],  
  "description": {  
    "languageMap": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "dissemination": "Level2Dissemination",  
  "disseminationOrganization": "https://url_to_organization.org",  
  "distribution": [  
    "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
    "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
  ],  
  "geolocation": true,  
  "hasVersion": [  
    "urn:ngsi-ld:Dataset:items:SQSB:90831182",  
    "urn:ngsi-ld:Dataset:items:FFVZ:69502935"  
  ],  
  "identifier": [  
    "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
    "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
  ],  
  "inSeries": [  
    "urn:ngsi-ld:Dataset:id:HUZY:681332655",  
    "urn:ngsi-ld:Dataset:id:HUZY:681970245"  
  ],  
  "isReferencedBy": [  
    "urn:ngsi-ld:Dataset:items:YQRP:33454193",  
    "urn:ngsi-ld:Dataset:items:RBND:48628164"  
  ],  
  "isVersionOf": [  
    "urn:ngsi-ld:Dataset:items:AMAC:16896252",  
    "urn:ngsi-ld:Dataset:items:IPSO:04920226"  
  ],  
  "issued": "1983-07-16T12:51:26Z",  
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
    "vivienda de uso turístico"  
  ],  
  "landingPage": [  
    "urn:ngsi-ld:Dataset:items:UMBA:72418275",  
    "urn:ngsi-ld:Dataset:items:GUKW:86586813"  
  ],  
  "language": [  
    "EN",  
    "SP"  
  ],  
  "license": "AGPL-3.0",  
  "modified": "2015-07-13T03:09:32Z",  
  "otherIdentifier": [  
    "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
    "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
  ],  
  "page": [  
    "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
    "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
  ],  
  "provenance": [  
    "1",  
    "2"  
  ],  
  "publisher": "Comunidad de madrid",  
  "qualifiedAttribution": [  
    "urn:ngsi-ld:Agent:2567369057",  
    "urn:ngsi-ld:Agent:6457369057"  
  ],  
  "qualifiedRelation": [  
    "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
    "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
  ],  
  "relation": [  
    "urn:ngsi-ld:Dataset:items:FXEY:35067714",  
    "urn:ngsi-ld:Dataset:items:YYOL:47950545"  
  ],  
  "reputation": "Level2Reputation",  
  "reputationOrganization": "https://url_to_organization.org",  
  "sample": [  
    "urn:ngsi-ld:Dataset:items:QJPZ:50290394",  
    "urn:ngsi-ld:Dataset:items:ZSSA:73451152"  
  ],  
  "source": [  
    "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
  ],  
  "spatial": [  
    {  
      "type": "Point",  
      "coordinates": [  
        9.922458,  
        109.478534  
      ]  
    }  
  ],  
  "spatialResolution": 0.6,  
  "standardization": "Level4Standardization",  
  "standardizationSource": "https://www.w3.org/",  
  "temporal": [  
    "2023-04-03T02:35:57Z"  
  ],  
  "temporalResolution": [  
    "PT15M"  
  ],  
  "theme": [  
    "Economy",  
    "Tourism"  
  ],  
  "title": {  
    "languageMap": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "Type": "service",  
  "validationSchema": "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/refs/heads/master/Dataset/schema.json",  
  "version": "3.0",  
  "versionNotes": [  
    "With temporal evolution"  
  ],  
  "wasGeneratedBy": [  
    "datos.gob.es"  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.DCAT-AP/context.jsonld"  
  ]  
}  
```  
</details>  
#### データセット NGSI-LD 正規化例  
以下は、正規化されたJSON-LDフォーマットによるデータセットの例です。これはオプションを使用しない場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Dataset:id:HUZY:68185655",  
  "type": "Dataset",  
  "accessMechanism": {  
    "type": "Property",  
    "value": "Level3AccessMechanism"  
  },  
  "accessRights": {  
    "type": "Property",  
    "value": "https://creativecommons.org/licenses/by/4.0/legalcode.es"  
  },  
  "accuralPeriodicity": {  
    "type": "Property",  
    "value": "two years"  
  },  
  "addressesAvailable": {  
    "type": "Property",  
    "value": true  
  },  
  "applicableLegislation": {  
    "type": "Property",  
    "value": [  
      "Regulation 883/2004",  
      "Regulation 465/2012"  
    ]  
  },  
  "belongsToCatalogue": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Catalogue:items:MWVK:61846917"  
  },  
  "conformsTo": {  
    "type": "Property",  
    "value": [  
      "http://www.opengis.net/def/crs/EPSG/0/28992",  
      "http://data.europa.eu/eli/reg/2014/1312/oj"  
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
  "creator": {  
    "type": "Property",  
    "value":  [  
      "Comunidad de Madrid"  
    ]  
  },  
  "description": {  
    "type": "LanguageProperty",  
    "languageMap": {  
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "dissemination": {  
    "type": "Property",  
    "value": "Level2Dissemination"  
  },  
  "disseminationOrganization": {  
    "type": "Property",  
    "value": "https://url_to_organization.org"  
  },  
  "distribution": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Distribution:items:KJVK:30944451",  
      "urn:ngsi-ld:Distribution:items:MMWU:84196227"  
    ]  
  },  
  "geolocation": {  
    "type": "Property",  
    "value": true  
  },  
  "hasVersion": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:id:ASDF:68185655",  
      "urn:ngsi-ld:Dataset:id:ASDF:78185655"  
    ]  
  },  
  "identifier": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:MBNQ:57176010",  
      "urn:ngsi-ld:Dataset:items:DDDJ:93242038"  
    ]  
  },  
  "inSeries": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:id:HUZY:681332655",  
      "urn:ngsi-ld:Dataset:id:HUZY:681970245"  
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
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:RBWE:31388012",  
      "urn:ngsi-ld:Dataset:items:GATZ:02632837"  
    ]  
  },  
  "issued": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-10-01T15:46:46Z"  
    }  
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
      "vivienda de uso turístico"  
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
  "license": {  
    "type": "Property",  
    "value": "AGPL-3.0"  
  },  
  "modified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-01T10:27:59Z"  
    }  
  },  
  "otherIdentifier": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:ZNYR:18053145",  
      "urn:ngsi-ld:Dataset:items:ICBO:96194869"  
    ]  
  },  
  "page": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:EDTJ:28919577",  
      "urn:ngsi-ld:Dataset:items:GKJO:30040605"  
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
  "qualifiedAttribution": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Agent:2567369057",  
      "urn:ngsi-ld:Agent:6457369057"  
    ]  
  },  
  "qualifiedRelation": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:ITFK:67369057",  
      "urn:ngsi-ld:Dataset:items:ZJWX:10596189"  
    ]  
  },  
  "relation": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:LGBY:74926949",  
      "urn:ngsi-ld:Dataset:items:ZAUC:79968579"  
    ]  
  },  
  "reputation": {  
    "type": "Property",  
    "value": "Level2Reputation"  
  },  
  "reputationOrganization": {  
    "type": "Property",  
    "value": "https://url_to_organization.org"  
  },  
  "sample": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:MLHW:64299003",  
      "urn:ngsi-ld:Dataset:items:GNXL:59256807"  
    ]  
  },  
  "source": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Dataset:items:YSWN:41266715"  
    ]  
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
  "spatialResolution": {  
    "type": "Property",  
    "value": 0.6  
  },  
  "standardization": {  
    "type": "Property",  
    "value": "Level4Standardization"  
  },  
  "standardizationSource": {  
    "type": "Property",  
    "value": "https://www.w3.org/"  
  },  
  "temporal": {  
    "type": "Property",  
    "value": [  
      "2023-04-03T02:35:57Z"  
    ]  
  },  
  "temporalResolution": {  
    "type": "Property",  
    "value": [  
      "PT15M"  
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
      "en": "Tourist accommodation in its different types and categories in the Community of Madrid.",  
      "de": "Touristische Unterkünfte in ihren verschiedenen Arten und Kategorien in der Gemeinschaft Madrid.",  
      "es": "Alojamientos turísticos en sus diferentes modalidades y categorias de la Comunidad de Madrid.",  
      "fr": "L'hébergement touristique dans ses différents types et catégories dans la Communauté de Madrid.",  
      "it": "Gli alloggi turistici nelle loro diverse tipologie e categorie nella Comunità di Madrid.",  
      "ja": "マドリッド州内の様々なタイプやカテゴリーの観光宿泊施設。",  
      "ko": "마드리드 커뮤니티의 다양한 유형과 카테고리의 관광 숙박 시설.",  
      "zh": "马德里大区不同类型和类别的旅游住宿。",  
      "el": "Τουριστικά καταλύματα σε διάφορους τύπους και κατηγορίες στην Κοινότητα της Μαδρίτης.",  
      "nl": "Toeristische accommodatie in de verschillende soorten en categorieën in de gemeente Madrid.",  
      "fi": "Matkailijoiden majoitustyypit ja -luokat Madridin alueella."  
    }  
  },  
  "Type": {  
    "type": "Property",  
    "value": "service"  
  },  
  "validationSchema": {  
    "type": "Property",  
    "value": "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/refs/heads/master/Dataset/schema.json"  
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
    "https://smart-data-models.github.io/dataModel.DCAT-AP/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
変更履歴 DCAT-AP DCAT-AP::Dataset 2.1.1 -> 3.0.0 (schemaVersion "2.0.1" -> schemaVersion "3.0.0")。conformsToのモデルを 'http://purl.org/dc/terms/Standard' から 'http://purl.org/dc/terms/conformsTo' に変更。title/descriptionプロパティは文字列の配列として表現され、配列の各エントリが特定言語の翻訳となっていましたが、現在はデータセットデータの多言語サポートを提供するために ETSI NGSI-LD 仕様で定義された LanguageProperty として表現されています。hasVersionはプロパティとして表現されていましたが、データセット間のリレーションシップに変更されました。languageについて、可能な値が米国議会図書館の ISO 639-1 (http://id.loc.gov/vocabulary/iso639-1.html)、ISO 639-2 (http://id.loc.gov/vocabulary/iso639-2.html) で定義されていることを明記しました。sourceは、プロパティの説明においてプロパティの配列からリレーションシップの配列に変更されました。versionInfoは、DCAT v3 語彙仕様 (https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version) の定義に従い、versionと記述されるべきです。  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
規模単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
