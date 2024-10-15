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


class Type6(Enum):
    CatalogueRecord = 'CatalogueRecord'


class CatalogueRecord(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    conformsTo: Optional[str] = Field(
        None,
        description="This property refers to an Application Profile that the Dataset's metadata conforms to",
    )
    description: Optional[List[str]] = Field(
        None,
        description='This property contains a free-text account of the record. This property can be repeated for parallel language versions of the description',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    issued: Optional[AwareDatetime] = Field(
        None,
        description='This property contains the date on which the description of the Dataset was included in the Catalogue',
    )
    language: Optional[List[str]] = Field(
        None,
        description='This property refers to a language used in the textual metadata describing titles, descriptions, etc. of the Dataset. This property can be repeated if the metadata is provided in multiple languages',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    modified: Optional[AwareDatetime] = Field(
        None,
        description='This property contains the most recent date on which the Catalogue entry was changed or modified',
    )
    primaryTopic: Optional[str] = Field(
        None,
        description='This property links the Catalogue Record to the Dataset, Data service or Catalog described in the record',
    )
    source: Optional[str] = Field(
        None,
        description='This property refers to the original metadata that was used in creating metadata for the Dataset',
    )
    status: Optional[str] = Field(
        None,
        description="This property refers to the type of the latest revision of a Dataset's entry in the Catalogue",
    )
    title: Optional[List[str]] = Field(
        None,
        description='This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be CatalogueRecord'
    )
