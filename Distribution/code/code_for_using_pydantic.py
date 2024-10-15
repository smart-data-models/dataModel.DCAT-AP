from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Status(Enum):
    Completed = 'Completed'
    Deprecated = 'Deprecated'
    Under_Development = 'Under Development'
    Withdrawn = 'Withdrawn'


class Type6(Enum):
    Distribution = 'Distribution'


class Distribution(BaseModel):
    accessService: Optional[List[str]] = Field(
        None,
        description='This property refers to a data service that gives access to the distribution of the dataset',
    )
    accessURL: Optional[List[constr(min_items=1)]] = Field(
        None,
        description='This property contains a URL that gives access to a Distribution of the Dataset. The resource at the access URL may contain information about how to get the Dataset',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availability: Optional[str] = Field(
        None,
        description='This property indicates how long it is planned to keep the Distributio of the Dataset available',
    )
    belongsToDataset: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='It links the Distribution to its parent Dataset. Note: this attribute does not belong to the current version of DCAT-AP, 2.1.1',
    )
    byteSize: Optional[float] = Field(
        None, description='This property contains the size of a Distribution in bytes'
    )
    checksum: Optional[str] = Field(
        None,
        description='This property provides a mechanism that can be used to verify that the contents of a distribution have not changed. The checksum is related to the downloadURL',
    )
    compressFormat: Optional[str] = Field(
        None,
        description='This property refers to the format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA',
    )
    conformsTo: Optional[List[str]] = Field(
        None,
        description='This property refers to an established schema to which the described Distribution conforms',
    )
    description: Optional[List[str]] = Field(
        None,
        description='This property contains a free-text account of the Distribution. This property can be repeated for parallel language versions of the description',
    )
    downloadURL: Optional[List[AnyUrl]] = Field(
        None,
        description='This property contains a URL that is a direct link to a downloadable file in a given format',
    )
    format: Optional[str] = Field(
        None, description='This property refers to the file format of the Distribution'
    )
    hasPolicy: Optional[str] = Field(
        None,
        description='This property refers to the policy expressing the rights associated with the distribution if using the ODRL vocabulary',
    )
    issued: Optional[AwareDatetime] = Field(
        None,
        description='This property contains the date of formal issuance (e.g., publication) of the Distribution',
    )
    language: Optional[List[str]] = Field(
        None,
        description='This property refers to a language used in the Distribution. This property can be repeated if the metadata is provided in multiple languages',
    )
    license: Optional[str] = Field(
        None,
        description='This property refers to a data service that gives access to the distribution of the dataset',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mediaType: Optional[str] = Field(
        None,
        description='This property refers to the media type of the Distribution as defined in the official register of media types managed by IANA',
    )
    modified: Optional[AwareDatetime] = Field(
        None,
        description='This property contains the most recent date on which the Distribution was changed or modified',
    )
    packageFormat: Optional[str] = Field(
        None,
        description='This property refers to the format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA',
    )
    page: Optional[List[str]] = Field(
        None,
        description='This property refers to a page or document about this Distribution',
    )
    rights: Optional[str] = Field(
        None,
        description='This property refers to a statement that specifies rights associated with the Distribution',
    )
    spatialResolutionInMeters: Optional[List] = Field(
        None,
        description='This property refers to the minimum spatial separation resolvable in a distribution, measured in meters',
    )
    status: Optional[Status] = Field(
        None,
        description='This property refers to the maturity of the Distribution. It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn',
    )
    temporalResolution: Optional[str] = Field(
        None,
        description='This property refers to the minimum time period resolvable in the dataset. ',
    )
    title: Optional[List[str]] = Field(
        None,
        description='This property contains a name given to the Distribution. This property can be repeated for parallel language versions of the description',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be Distribution'
    )
