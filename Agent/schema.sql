/* (Beta) Export of data model Agent of the subject dataModel.DCAT-AP for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Agent_type AS ENUM ('Agent');
CREATE TABLE Agent (Type text, address json, areaServed text, id text, location json, name json, type Agent_type);