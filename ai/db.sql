pubrec=> CREATE EXTENSION vector;


CREATE TABLE CaseRecords (
    caseNum CHARVAR(255) PRIMARY KEY COLLATE pg_catalog."default",
    crimeType VECTOR(1536),
    date DATE,
    time TIME,
    location VECTOR(1536),
    victimName VECTOR(1536)',
    victimAge INT,
    victimRelation VECTOR(1536),
    eventSequence VECTOR(1536),
    compromiseMethod VECTOR(1536),
    suspectSex BOOLEAN,
    suspectRace VECTOR(1536),
    suspectHeight FLOAT DEFAULT,
    suspectBuild VECTOR(1536),
    suspectClothes VECTOR(1536),
    tools VECTOR(1536),
    forceUsed VECTOR(1536),
    weapon VECTOR(1536),
    victimHarm VECTOR(1536),
    itemsStolen VECTOR(1536),
    fundsStolen FLOAT DEFAULT 0,
    evidence VECTOR(1536),
    suspectTechniques VECTOR(1536),
    status BOOLEAN DEFAULT TRUE,
    notes VECTOR(1536)
);
