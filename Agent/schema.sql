/* (Beta) Export of data model Agent of the subject dataModel.DCAT-AP for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Agent_type AS ENUM ('Agent');
CREATE TABLE Agent (Type TEXT, address JSON, areaServed TEXT, id TEXT PRIMARY KEY, location JSON, name JSON, type Agent_type);