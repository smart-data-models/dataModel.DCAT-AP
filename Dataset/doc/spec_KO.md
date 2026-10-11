<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: Dataset  
============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Dataset/LICENSE.md)  
[자동으로 생성된 문서](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **DCAT-AP 3.0.0 사양에 기반한 데이터셋 스키마 정의.**  
version: 3.0.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 경우 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>  
- `Type[string]`: 이 속성은 데이터셋의 유형을 참조합니다. 권장되는 통제 어휘 데이터 유형이 예정되어 있습니다. 값은 DCMI Type 어휘(https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7), [ISO-19115-1] 범위 코드(https://standards.iso.org/iso/19115/resources/Codelists/gml/MD_ScopeCode.xml), Datacite 리소스 유형 [DataCite] (https://schema.datacite.org/meta/kernel-4.1/include/datacite-resourceType-v4.1.xsd), re3data.org에서 사용되는 PARSE.Insight 콘텐츠 유형 [RE3DATA-SCHEMA] (https://www.re3data.org/) (항목 15 contentType 참조), MARC 지적 리소스 유형(http://id.loc.gov/vocabulary/marcgt.html)과 같이 잘 관리되고 널리 인정되는 통제 어휘에서 가져와야 합니다(SHOULD). 이러한 통제 어휘의 일부 항목은 데이터셋이나 데이터 서비스에 엄격하게 적합하지 않을 수 있지만(예: DCMI Type Event, PhysicalObject; [ISO-19115-1](https://www.w3.org/TR/vocab-dcat-3/#bib-iso-19115-1) CollectionHardware, CollectionSession, Initiative, Sample, Repository), DCAT 프로필 또는 애플리케이션에서 정의된 다른 종류의 카탈로그 문맥에서는 사용될 수 있습니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `accessMechanism[string]`: MELODA5 메트릭의 3가지 수준에 따른 접근 수준입니다. 예상되는 값은 다음과 같습니다: * Level1AccessMechanism: 웹 접근 또는 데이터셋에 대한 고유 URL 매개변수. * Level2AccessMechanism: 단일 데이터에 대한 매개변수가 있는 고유 웹 접근. * Level3AccessMechanism: API 또는 쿼리 언어.  . Model: [https://schema.org/Text](https://schema.org/Text)- `accessRights[string]`: 이 속성은 데이터셋이 공개 데이터인지, 접근 제한이 있는지 또는 비공개인지 여부를 나타내는 정보를 나타냅니다.  . Model: [http://purl.org/dc/terms/RightsStatement](http://purl.org/dc/terms/RightsStatement)- `accuralPeriodicity[string]`: 이 속성은 데이터셋이 업데이트되는 빈도를 참조합니다.  . Model: [http://purl.org/dc/terms/Frequency](http://purl.org/dc/terms/Frequency)- `addressesAvailable[boolean]`: 데이터 스트림에 데이터셋 내의 요소를 식별하기 위한 우편 주소가 있는지 정의합니다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `applicableLegislation[array]`: 데이터셋의 생성 또는 관리를 의무화하는 법률. 카디널리티: 0..n.  . Model: [http://data.europa.eu/r5r/applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)- `belongsToCatalogue[*]`: 데이터셋을 상위 카탈로그에 연결합니다. 참고: 이 속성은 DCAT-AP 2.1.1의 현재 버전에 속하지 않습니다.  . Model: [https://www.w3.org/ns/dcat#Catalogue](https://www.w3.org/ns/dcat#Catalogue)- `conformsTo[array]`: 이 속성은 구현 규칙 또는 기타 사양을 참조합니다.  . Model: [http://purl.org/dc/terms/conformsTo](http://purl.org/dc/terms/conformsTo)- `contactPoint[array]`: 데이터셋에 대한 의견을 보내는 데 사용할 수 있는 연락처 정보. 카디널리티(Cardinality): 0..n.  . Model: [http://www.w3.org/ns/dcat#contactPoint](http://www.w3.org/ns/dcat#contactPoint)- `creator[array]`: 이 속성은 데이터셋 제작을 주도적으로 담당하는 엔티티를 참조합니다.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `description[*]`: LanguageProperty. 이 속성은 데이터셋에 대한 자유 형식의 텍스트 설명을 포함합니다. 이 속성은 설명의 병렬 언어 버전을 위해 반복될 수 있습니다.  . Model: [http://purl.org/dc/terms/description](http://purl.org/dc/terms/description)- `dissemination[string]`: MELODA5 커뮤니케이션 차원에 따른 배포(Dissemination) 수준: * Level1Dissemination: 체계적이지 않은 커뮤니케이션/배포. * Level2Dissemination: 업데이트에 대한 사용 가능한 리소스(예: RSS 피드). * Level3Dissemination: 선제적 배포/푸시 배포(자동적이고 적시적인 정보 제공).  . Model: [https://schema.org/Text](https://schema.org/Text)- `disseminationOrganization[string]`: 데이터셋과 관련된 배포 활동을 담당하는 조직의 URI입니다. 이는 MELODA5의 차원/커뮤니케이션(dimension/communication)과 일치합니다.  . Model: [https://schema.org/url](https://schema.org/url)- `distribution[array]`: 이 속성은 데이터셋을 사용 가능한 배포본에 연결합니다.  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `geolocation[boolean]`: 데이터 스트림이 해당 속성 중 하나라도 지리적 위치(좌표)를 가지고 있는지 정의합니다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasVersion[array]`: 이 속성은 설명된 데이터셋의 버전, 판(edition) 또는 개작(adaptation)인 관련 데이터셋을 참조합니다.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `id[*]`: 엔티티의 고유 식별자  - `identifier[array]`: 이 속성은 데이터셋의 기본 식별자(예: 카탈로그 문맥에서의 URI 또는 기타 고유 식별자)를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `inSeries[array]`: 이 속성은 데이터셋을 사용 가능한 배포본에 연결합니다.  . Model: [https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series)- `isReferencedBy[array]`: 이 속성은 데이터셋을 참조, 인용 또는 다른 방식으로 가리키는 출판물과 같은 관련 리소스에 관한 것입니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `isVersionOf[array]`: 이 속성은 설명된 데이터셋이 버전, 에디션 또는 각색본인 관련 데이터셋을 나타냅니다.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `issued[date-time]`: 이 속성은 데이터셋의 공식 발행(예: 출판) 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `keyword[array]`: 이 속성은 데이터셋을 설명하는 키워드 또는 태그를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `landingPage[array]`: 이 속성은 데이터셋, 데이터 배포(Distributions) 및/또는 추가 정보에 대한 액세스를 제공하는 웹 페이지를 참조합니다. 이는 어그리게이터와 같은 제3자 사이트의 페이지가 아니라, 원본 데이터 제공자의 랜딩 페이지를 가리키도록 의도되었습니다.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `language[array]`: 이 속성은 데이터셋의 언어를 참조합니다. 데이터셋에 여러 언어가 있는 경우 이 속성을 반복할 수 있습니다. 가능한 값은 미국 의회 도서관(Library of Congress)에 의해 정의됩니다(ISO 639-1: http://id.loc.gov/vocabulary/iso639-1.html, ISO 639-2: http://id.loc.gov/vocabulary/iso639-2.html).  . Model: [http://purl.org/dc/terms/LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)- `license[string]`: 이 속성은 데이터셋이 제공되는 라이선스를 나타냅니다. 열거된 값에 따른 라이선스 ID입니다. 이는 SPDX 표준(https://spdx.org/licenses)의 ID에서 추출됩니다.  . Model: [http://purl.org/dc/terms#LicenseDocument](http://purl.org/dc/terms#LicenseDocument)- `modified[date-time]`: 이 속성은 데이터셋이 변경되거나 수정된 가장 최근 날짜를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `otherIdentifier[array]`: 이 속성은 MAST/ADS, DataCite, DOI, EZID 또는 W3ID와 같은 데이터셋의 보조 식별자를 참조합니다.  . Model: [http://www.w3.org/ns/adms#Identifier](http://www.w3.org/ns/adms#Identifier)- `page[array]`: 이 속성은 이 데이터셋에 관한 페이지 또는 문서를 참조합니다.  . Model: [http://xmlns.com/foaf/0.1/Document](http://xmlns.com/foaf/0.1/Document)- `provenance[array]`: 이 속성은 데이터셋의 계보(lineage)에 관한 기술을 포함합니다.  . Model: [http://purl.org/dc/terms/ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)- `publisher[string]`: 이 속성은 데이터셋을 사용할 수 있도록 하는 데 책임이 있는 엔티티(조직)를 참조합니다.  . Model: [http://xmlns.com/foaf/0.1/Agent](http://xmlns.com/foaf/0.1/Agent)- `qualifiedAttribution[array]`: 이 속성은 해당 리소스에 대해 어떤 형태의 책임을 지는 에이전트(Agent)로의 링크를 참조합니다.  . Model: [https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)- `qualifiedRelation[array]`: 이 속성은 다른 리소스와의 관계에 대한 설명으로 연결되는 링크를 제공합니다.  . Model: [http://www.w3.org/ns/dcat#Relationship](http://www.w3.org/ns/dcat#Relationship)- `relation[array]`: 이 속성은 관련 리소스를 참조합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Resource](http://www.w3.org/2000/01/rdf-schema#Resource)- `reputation[string]`: MELODA5 평판 차원에 따른 평판 수준: * Level1Reputation: 데이터 소스의 평판에 대한 정보 없음. * Level2Reputation: 사용자 의견에 대해 발표된 통계 또는 보고서. * Level3Reputation: 데이터 소스의 평판에 대한 지표 또는 순위.  . Model: [https://schema.org/Text](https://schema.org/Text)- `reputationOrganization[string]`: 평판 측면에서 데이터셋의 발행을 담당하는 조직의 URI입니다. 이는 MELODA5의 평판(reputation) 차원과 일치하며, 순위에서 해당 조직의 명성(prestige)을 검색할 수 있게 합니다.  . Model: [https://schema.org/url](https://schema.org/url)- `sample[array]`: 이 속성은 데이터셋의 샘플 배포를 참조합니다.  . Model: [http://www.w3.org/ns/dcat#Distribution](http://www.w3.org/ns/dcat#Distribution)- `source[array]`: 이 속성은 설명된 데이터셋의 근거가 되는 관련 데이터셋을 참조합니다.  . Model: [http://www.w3.org/ns/dcat#Dataset](http://www.w3.org/ns/dcat#Dataset)- `spatial[array]`: 이 속성은 데이터셋이 다루는 지리적 영역을 참조합니다.  . Model: [http://purl.org/dc/terms/Location](http://purl.org/dc/terms/Location)- `spatialResolution[number]`: 이 속성은 미터 단위로 측정된 데이터셋에서 식별 가능한 최소 공간 분해능을 참조합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `standardization[string]`: 데이터셋이 따르는 데이터 모델 표준화 유형입니다. 이는 세(4) 가지 가능한 값을 가진 열거형입니다: * Level1Standardization: 문서 공개 없이 게시자가 표준화한 데이터 모델. * Level2Standardization: 문서 공개와 함께 게시자가 표준화한 데이터 모델. * Level3Standardization: 지역 표준(국가 또는 소규모 지역 범위)을 사용하는 데이터 모델. * Level4Standardization: 국제 표준을 사용하는 데이터 모델.  . Model: [https://schema.org/Text](https://schema.org/Text)- `standardizationSource[string]`: 속성 정의를 읽을 수 있는 소스의 URI입니다. 이는 표준화(standardization) 속성과 연관되어 있습니다. Level 1 및 Level 2의 경우 비어 있을 수 있으며, Level 3의 경우 기존 표준화 기구(예: DIN, UNE 등)로, Level 4의 경우(예: ISO, W3C 등)로 링크될 수 있습니다.  . Model: [https://schema.org/url](https://schema.org/url)- `temporal[array]`: 이 속성은 데이터셋이 다루는 시간적 기간을 참조합니다.  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `temporalResolution[array]`: 이 속성은 데이터셋에서 식별 가능한 최소 시간 간격을 참조합니다.  . Model: [http://purl.org/dc/terms/PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)- `theme[array]`: 이 속성은 데이터셋의 범주를 참조합니다. 데이터셋은 여러 테마와 연관될 수 있습니다.  . Model: [http://www.w3.org/2004/02/skos/core#Concept](http://www.w3.org/2004/02/skos/core#Concept)- `title[*]`: LanguageProperty. 이 속성은 데이터셋에 부여된 이름을 포함합니다. 이 속성은 이름의 병렬 언어 버전을 위해 반복될 수 있습니다.  . Model: [http://purl.org/dc/terms/title](http://purl.org/dc/terms/title)- `type[string]`: NGSI 유형. 'Dataset'이어야 합니다.  - `validationSchema[string]`: Smart Data Models 프로그램의 데이터셋용 기술 검증 스키마(JSON Schema) URL입니다.  . Model: [https://schema.org/url](https://schema.org/url)- `version[string]`: 이 속성은 데이터셋의 버전 번호 또는 기타 버전 지정 정보를 포함합니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `versionNotes[array]`: 이 속성은 이 버전과 데이터셋의 이전 버전 간의 차이점에 대한 설명을 포함합니다. 이 속성은 버전 노트의 병렬 언어 버전을 위해 반복될 수 있습니다.  . Model: [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)- `wasGeneratedBy[array]`: 이 속성은 데이터셋의 생성을 유발했거나, 생성에 대한 비즈니스 컨텍스트를 제공하는 활동을 나타냅니다.  . Model: [https://www.w3.org/ns/prov#Activity](https://www.w3.org/ns/prov#Activity)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `description`  - `id`  - `title`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
[DCAT-AP 버전 3.0.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/)에서 수정됨. FAIR 원칙 및 MELODA5 차원 속성 추가. accessMechanism: Meloda5 메트릭의 3단계에 따른 액세스 수준. 예상 값은 Level1AccessMechanism(웹 액세스 또는 데이터셋에 대한 고유 URL 매개변수), Level2AccessMechanism(단일 데이터에 대한 매개변수가 있는 고유 웹 액세스), Level3AccessMechanism(API 또는 쿼리 언어)입니다. addressAvailable: 데이터 스트림에 데이터셋 내의 요소를 식별하기 위한 우편 주소가 있는지 정의합니다. dissemination: Meloda5 커뮤니케이션 차원에 따른 배포 수준: Level1Dissemination(체계적이지 않은 커뮤니케이션/배포), Level2Dissemination(업데이트에 대한 사용 가능한 리소스, 즉 RSS 피드), Level3Dissemination(선제적 배포/푸시 배포, 자동적이고 적시적인 정보 제공). diseminationOrganization: 데이터셋과 관련된 배포 활동을 담당하는 조직의 URI입니다. 이는 Meloda5의 차원/커뮤니케이션과 일치합니다. geolocation: 데이터 스트림의 속성 중 하나에 지리적 위치(좌표)가 있는지 정의합니다. license: 이 속성은 데이터셋이 제공되는 라이선스를 참조합니다. 열거된 값에 따른 라이선스 ID입니다. 이는 SPDX 표준(https://spdx.org/licenses)의 id에서 추출됩니다. reputation: Meloda5 평판 차원에 따른 평판 수준: Level1Reputation(데이터 소스의 평판에 대한 정보 없음), Level2Reputation(사용자 의견에 대해 발표된 통계 또는 보고서), Level3Reputation(데이터 소스의 평판에 대한 지표 또는 순위). reputationOrganization: 평판 측면에서 데이터셋의 발행을 담당하는 조직의 URI입니다. 이는 Meloda5의 평판 차원과 일치하며, 순위에서 해당 조직의 명성을 검색할 수 있게 합니다. standardization: 데이터셋이 따르는 데이터 모델 표준화 유형입니다. 이는 네 가지 가능한 값을 가진 열거형입니다: Level1Standardization(문서를 공개하지 않고 발행자에 의해 표준화된 데이터 모델), Level2Standardization(문서를 공개하며 발행자에 의해 표준화된 데이터 모델), Level3Standardization(지역 표준, 국가 또는 더 작은 지역 범위를 사용하는 데이터 모델), Level4Standardization(국제 표준을 사용하는 데이터 모델). standardizationSource: 속성 정의를 읽을 수 있는 소스의 URI입니다. 이는 표준화 속성과 연관되어 있습니다. Level 1 및 Level 2의 경우 비어 있을 수 있으며, Level 3의 경우 기존 표준화 기구(예: DIN, UNE 등)로, Level 4의 경우(예: ISO, W3C 등)로 링크될 수 있습니다. validationSchema: Smart Data Models 프로그램의 데이터셋용 기술 검증 스키마(JSON Schema) URL입니다.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬됨 (자세한 내용은 클릭)  
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
## 페이로드 예시  
#### Dataset NGSI-v2 키-값 예시  
여기 키-값 형태의 JSON-LD 형식 데이터셋 예시가 있습니다. 이는 `options=keyValues`를 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### Dataset NGSI-v2 정규화된 예시  
여기 정규화된 형태의 JSON-LD 형식 데이터셋 예시가 있습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### 데이터셋 NGSI-LD 키-값 예시  
여기 키-값 형태의 JSON-LD 형식 데이터셋 예시가 있습니다. 이는 `options=keyValues`를 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### Dataset NGSI-LD 정규화된 예시  
여기 정규화된 형태의 JSON-LD 형식 데이터셋 예시가 있습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
변경 이력(CHANGELOG) DCAT-AP DCAT-AP::Dataset 2.1.1 -> 3.0.0 (schemaVersion "2.0.1" -> schemaVersion "3.0.0"). conformsTo가 모델을 'http://purl.org/dc/terms/Standard'에서 'http://purl.org/dc/terms/conformsTo'로 변경했습니다. title/description 속성은 문자열 배열로 표현되었으며, 배열의 각 항목은 특정 언어의 번역이었습니다. 이제 데이터셋 데이터의 다국어 지원을 제공하기 위해 ETSI NGSI-LD 사양에 정의된 LanguageProperty로 표현됩니다. hasVersion은 Property로 표현되었으나 Datasets의 Relationship으로 변경되었습니다. language의 경우, 가능한 값은 미국 의회 도서관 ISO 639-1 (http://id.loc.gov/vocabulary/iso639-1.html), ISO 639-2 (http://id.loc.gov/vocabulary/iso639-2.html)로 정의됩니다. source는 속성 설명에서 속성(Properties) 배열에서 관계(Relationships) 배열로 변경되었습니다. versionInfo는 DCAT v3 어휘 사양(https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version)의 정의에 따라 version으로 작성되어야 합니다.  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
크기 단위를 다루는 방법에 대한 답을 얻으려면 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하십시오.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
