TRAIN_DATA = [
    
  ("INCIDENT REPORT\n\nCase #: 2024-06234\nDate: June 22, 2024\nLocation: 315 Maple Ave, Willowville\n\nCRIME DETAILS:\nCrime Type: Burglary and Assault\nModes of Accessing Victim: The suspects gained entry to the victim's residence by breaking a basement window using a crowbar. Once inside, they proceeded upstairs and encountered the victim in the kitchen.\n\nCommon Tools Used: Crowbar\n\nType of Force Used: The suspects used physical force and violence against the victim.\n\nWeapons Used in the Crime: None reported\n\nNARRATIVE:\nOn June 22nd at approximately 11:00 PM, the victim (Emily Johnson, 27) was in her kitchen preparing dinner when she heard the sound of glass breaking from the basement. Moments later, two masked individuals entered the kitchen through the hallway. One suspect was carrying a crowbar.\n\nThe suspects immediately grabbed Ms. Johnson, demanding valuables and money. When she resisted, one suspect struck her in the back with the crowbar, causing her to fall to the floor. The other suspect then proceeded to ransack the kitchen, searching for valuables.\n\nMs. Johnson managed to activate the panic alarm on her home security system, prompting the suspects to flee the scene through the front door. Responding officers arrived within minutes and found Ms. Johnson injured but conscious. Emergency medical services were summoned to treat her for a fractured rib and lacerations on her back.\n\nInvestigating officers discovered the broken basement window and evidence of forced entry. They collected the crowbar left behind by the suspects for forensic analysis. The investigation is ongoing, and efforts are being made to identify and apprehend the perpetrators involved in this violent burglary.",
  
  {"entities": [
    (25, 35, "CASE_NUMBER"),
    (42,  55, "DATE"),
    (66,  92,  "LOCATION"),
    ( 169,  347,  "METHOD"),
    ( 1402,  1570,  "EVIDENCE"),
    ( 121,  141,  "CRIME"),
  ]
})
,
    ("POLICE INCIDENT REPORT\n\nCase No. 2024-03291\n\nCrime Type: Theft and Vandalism\n\nDate/Time of Incident: June 15, 2024 - Between 9 PM - 5 AM\n\nLocation: 721 Maple Avenue, Cedar Falls, Illinois\n\nVictim(s): Emily and Daniel Thompson\n\nOn the morning of June 15th, Cedar Falls Police Department responded to a call from Mrs. Emily Thompson reporting a break-in and theft at her residence on Maple Avenue. Officers arrived at the scene at approximately 5:30 AM.\n\nUpon arrival, officers observed that the front door of the residence had been forcefully kicked in, splintering the door frame and damaging the lock mechanism. It was evident that considerable force had been used to gain entry.\n\nInside the house, rooms were in disarray. Furniture was overturned, cabinets were open, and personal belongings were strewn across the floors. The thieves targeted electronics, jewelry, and sentimental items.\n\nThe perpetrators broke into the family's home office, where a safe was hidden behind a false panel in the wall. Despite the concealment, the safe was forcibly opened, with marks suggesting the use of a heavy-duty drill and pry bars. It was emptied of cash, important documents, and irreplaceable family heirlooms.\n\nSecurity camera footage retrieved from the home's DVR system revealed two individuals wearing hooded jackets and gloves arriving around 11:00 PM the previous night. They were seen carrying large backpacks and appeared to be equipped with tools including a drill and bolt cutters.\n\nThe suspects disabled outdoor motion lights and cameras before gaining entry through the front door. They spent nearly four hours inside, methodically searching rooms and bypassing a secondary alarm system.\n\nThe forensic team processed the scene for evidence, collecting potential DNA samples from discarded gloves and fingerprints from surfaces throughout the house. Footwear impressions were also lifted from the scene for comparison.\n\nThe estimated value of stolen items totals approximately $120,000, including antique jewelry, high-end electronics, and cash. Detectives are actively investigating leads and analyzing evidence to identify the perpetrators involved in this brazen burglary.\n\nPrepared by Officer Michael Reynolds, Badge #5218, Cedar Falls Police Department.", {
        'entities': [
            (33, 43, "CASE_NUMBER"),
            (101,  136, "DATE"),
            (148,  187,  "LOCATION"),
            ( 892,  1003,  "METHOD"),
            ( 1207,  1731,  "EVIDENCE"),
            ( 1926,  2051,  "STOLEN"),
            ( 57,  76,  "CRIME")
        ]
    }),
    ("POLICE INCIDENT REPORT\n\nCase #2024-06251\n\nCrime Type: Home Invasion Robbery\nDate/Time of Incident: June 23, 2024 - Between 11:30 PM - 1:45 AM\nLocation: 601 Willow Lane, Pinecrest, Montana\n\nOn the night of June 23rd, between 11:30 PM and 1:45 AM, Pinecrest Police Department responded to a 911 call reporting a home invasion robbery at 601 Willow Lane. Officers arrived on scene swiftly and secured the area.\n\nEntry into Victim's Territory:\nInvestigation revealed that the perpetrators gained entry by forcibly breaking a ground-floor window on the west side of the residence. The window frame was damaged, suggesting the use of a heavy blunt object such as a crowbar or hammer.\n\nDescription of Tools Used:\nUpon gaining entry, the suspects proceeded to ransack multiple rooms within the residence. They employed tools including a crowbar found at the scene, which was likely used to force open locked drawers and cabinets. Evidence of the tool's use was apparent through visible pry marks on furniture and doors.\n\nUtilization of Strength:\nThe level of violence exhibited by the intruders was substantial, as evidenced by the extensive property damage and personal disruption. Multiple items of personal value were tossed around, including several electronics and jewelry.\n\nIdentification of Thieves:\nSurveillance footage from the home's security system captured two individuals dressed in dark clothing and ski masks arriving at approximately 11:45 PM. They were observed carrying bags of items, and tools resembling the crowbar found at the scene were visible in their possession.\n\nStrategic Response to Valuables:\nThe thieves departed the premises by the same broken window, carrying a significant amount of stolen goods including jewelry, electronics, and a small safe containing personal documents and a large amount of cash. This modus operandi was well prepared and professional.\n\nForensic Examination:\nCrime scene investigators collected evidence including fingerprints, DNA samples, and tool marks from the broken window and damaged furniture. The collected items are being meticulously examined for potential identification of the criminals.\n\nFinancial Value Stolen:\nThe estimated value of the stolen items is approximately $90,000, including sentimental valuables and electronics. This incident has left the family shaken, and they are now in the process of assessing their security measures.\n\nThe investigation into this home invasion robbery is ongoing, with detectives actively pursuing leads and analyzing the gathered evidence. Anyone with information pertinent to this case is urged to contact the Pinecrest Police Department immediately.\n\nPrepared by Detective L. Rodriguez #4783, Pinecrest Police Department."
, {
        'entities': [
            (30, 40, "CASE_NUMBER"),
            (99,  141, "DATE"),
            (152,  187,  "LOCATION"),
            (726,  921,  "METHOD"),
            (1299,  1451,  "EVIDENCE"),
            (2175,  2289,  "STOLEN"),
            (54,  75,  "CRIME")
        ]
    }),

(
    "POLICE INCIDENT REPORT\n\nCase #: 2024-06252\n\nCrime Type: Armed Robbery\n\nOn the night of April 24th, 2024, a daring and organized group of criminals executed a meticulously planned heist at the Pinecrest Jewelry Exchange. The perpetrators gained access to the building by disabling the alarm system and cutting through the reinforced steel door using high-powered cutting tools, likely diamond-tipped drill bits and oxy-acetylene torches - tools commonly used to breach secure locations.\n\nOnce inside, the assailants proceeded with extreme force, physically assaulting and restraining two security guards who were on duty. Eyewitness accounts describe the suspects as wearing tactical gear and ski masks, armed with handguns to subdue their victims.\n\nThe thieves then swiftly emptied multiple display cases, seizing a vast array of jewelry and luxury watches valued at an estimated $3.8 million.\n\nWeapons Used: Handguns (likely 9mm semi-automatic pistols based on shell casings recovered)\n\nDuring their escape, a confrontation ensued with responding law enforcement officers, resulting in an exchange of gunfire. One officer sustained a minor injury before the suspects fled the scene in a stolen van.\n\nRecovered evidence includes spent ammunition, tools used in the heist, and trace evidence such as shoe prints and fabric fibers. Security footage from the jewelry store and surrounding area is being reviewed, and investigative leads are actively pursued, although the suspects remain unidentified at this time.\n\nThis audacious crime exhibited a high level of aggression, meticulous planning, and a callous disregard for public safety. Law enforcement agencies are collaborating extensively to apprehend these dangerous individuals and bring them to justice. Anyone with pertinent information is urged to contact the Pinecrest Police Department immediately.\n\nPrepared by Detective M. Ramirez #6214, Pinecrest Police Department.", {
        'entities': [
            (32, 42, "CASE_NUMBER"),
            (87,  103, "DATE"),
            (192,  218,  "LOCATION"),
            (220,  375,  "METHOD"),
            (1201,  1409,  "EVIDENCE"),
            (816,  892,  "STOLEN"),
            (56,  69,  "CRIME")
        ]
    }),

("POLICE INCIDENT REPORT\n\nCase #2024-06253\n\nDate of Incident: October 25th, 2024\nTime of Incident: Approximately 10:15 PM\nLocation: 707 Elm Street, Springfield\n\nINCIDENT SUMMARY:\nOn the night of October 25th, a tragic homicide occurred in the residential area of Springfield. The victim, identified as Mr. Samuel Thompson, was found deceased in his home at 707 Elm Street. Initial investigations indicate Mr. Thompson suffered multiple stab wounds to the chest and back.\n\nWitnesses reported hearing loud arguments coming from the residence earlier that evening, followed by sounds of a struggle and breaking glass. Subsequent police arrival revealed signs of forced entry through a rear window, with shattered glass and pry marks present.\n\nVICTIM INFORMATION:\nVictim: Samuel Thompson, 45 years old\n\nSUSPECT INFORMATION:\nCurrently unidentified\n- Description unavailable pending further investigation\n\nEVIDENCE RECOVERED:\n- Broken glass and pry marks from forced entry\n- Multiple blood stains found throughout the residence\n- Recovered knife believed to be the murder weapon\n\nACTIONS TAKEN:\n- Secured the crime scene and initiated forensic processing\n- Interviewed witnesses in the neighborhood\n- Issued BOLO (Be On the Lookout) for potential suspects\n- Requested assistance from homicide investigators and crime scene technicians\n\nThe investigation into this tragic homicide is actively underway. Anyone with information regarding this incident or potential suspects is urged to contact the Springfield Police Department immediately.\n\nPrepared by Detective A. Reynolds #7351, Springfield Police Department.", {
        'entities': [
            (30, 40, "CASE_NUMBER"),
            (60,  78, "DATE"),
            (130,  157,  "LOCATION"),
            (403,  467,  "METHOD"),
            (920,  1070,  "EVIDENCE"),
            (216,  224,  "CRIME")
        ]
    }
),
(
    "POLICE INCIDENT REPORT\nCase No. 2024-06254\n\nNature of Incident: Homicide\n\nDate/Time of Incident: December 8, 2024 / 9:15 PM\n\nLocation of Incident: 600 block of Pine Avenue\n\nVictim:\nEmily Johnson, 28-year-old female\n\nSuspect(s):\nUnknown - Description: Short male, approximately 5'6\", wearing a black cap\n\nDetails:\nOn the evening of December 8th, the victim, Emily Johnson, was discovered deceased in her apartment on Pine Avenue. Initial investigations indicate Ms. Johnson suffered multiple stab wounds to the chest and neck.\n\nNeighbors reported hearing raised voices and commotion coming from the victim's apartment earlier that evening. Concerned for her safety, one neighbor attempted to check on Ms. Johnson but found the door locked. Upon hearing no response, the neighbor alerted the building superintendent who subsequently contacted emergency services.\n\nUpon arrival, emergency responders forced entry into the apartment and discovered Ms. Johnson's lifeless body in the living room. The scene revealed signs of a struggle, with overturned furniture and blood spatter present.\n\nVictim Information:\nVictim: Emily Johnson, 28 years old\n\nSuspect Information:\nCurrently unidentified\n- Description: Short male, approximately 5'6\", wearing a black cap\n\nEvidence Recovered:\n- Multiple blood stains found at the scene\n- Recovered knife believed to be the murder weapon\n\nActions Taken:\n- Secured the crime scene and initiated forensic processing\n- Interviewed neighbors and potential witnesses\n- Issued BOLO (Be On the Lookout) for potential suspects\n- Requested assistance from homicide investigators and crime scene technicians\n\nThe investigation into this tragic homicide is actively underway. Anyone with information regarding this incident or potential suspects is urged to contact the local police department immediately.\n\nReporting Officer: Det. M. Anderson, Badge #7892", {
        'entities': [
            (32, 42, "CASE_NUMBER"),
            (97,  123, "DATE"),
            (147,  171,  "LOCATION"),
            (461,  525,  "METHOD"),
            (1275,  1368,  "EVIDENCE"),
            (251,  302,  "SUSPECT"),
            (64,  72,  "CRIME")
        ]
    }
),
(
    """
POLICE REPORT

Case #: 2024-06292  
Crime: Kidnapping

On September 15th, 2024, officers from the 7th Precinct responded to a reported kidnapping incident involving Ms. Emily Johnson, a 32-year-old resident of 210 Apple Avenue. Ms. Johnson's spouse reported that she failed to return home from work and was unreachable by phone, which prompted a welfare check by concerned family members.

Initial inquiries revealed that Ms. Johnson had last been seen leaving her workplace at 5:30 PM, where she worked as a financial analyst. Surveillance footage from the vicinity showed Ms. Johnson entering the parking garage alone, but no footage captured her departure or any suspicious activity involving other individuals.

Further investigation into Ms. Johnson's background and recent activities did not uncover any known enemies or conflicts that might suggest a motive for abduction. Her personal belongings, including her purse and mobile phone, were discovered abandoned in her unlocked vehicle parked in the garage.

Witness interviews conducted at Ms. Johnson's workplace yielded no leads or suspicious sightings. A review of nearby CCTV cameras is currently underway to ascertain if any vehicle or person was observed following Ms. Johnson upon her departure from work.

As of this report, Ms. Johnson's whereabouts remain unknown, and there have been no ransom demands or communication from any potential suspects. The circumstances surrounding her disappearance are being treated with utmost urgency, and the investigation has been escalated to include assistance from the Major Crimes Division and federal agencies.

Family members have been briefed on the ongoing investigation and are cooperating with law enforcement efforts. They have provided additional background information that may assist in locating Ms. Johnson.

This case is currently designated as an active kidnapping investigation. Any person with information regarding Ms. Johnson's disappearance is urged to contact Detective A. Thompson at 555-1234 or submit tips anonymously through the police department's mobile app.

Reporting Officer: Officer M. Ramirez, Badge #5147
""", {
        'entities': [
            (24, 34, "CASE_NUMBER"),
            (59,  79, "DATE"),
            (211,  227,  "LOCATION"),
            (529,  715,  "EVIDENCE"),
            (44,  54,  "CRIME")
        ]
    }
),

("""
POLICE REPORT

Case No: 2024-0807-FRAUD

Crime Type: Fraud

On August 7th, 2024, the Financial Crimes Unit received a report from Mr. David Smith, a 55-year-old resident of 415 Elm Street, regarding a complex fraud scheme targeting his retirement savings accounts.

The Incident:
Mr. Smith reported that he discovered unauthorized transactions and withdrawals totaling over $100,000 from his retirement accounts over the past month. The transactions included wire transfers to offshore accounts, purchases of luxury items, and investments in cryptocurrency, none of which were authorized by Mr. Smith.

Initial Investigation:
Upon initial investigation, it was determined that Mr. Smith's personal information, including account details and passwords, may have been compromised through a sophisticated phishing attack. Analysis of Mr. Smith's computer revealed traces of malware designed to capture sensitive login information and financial data.

Modus Operandi:
The perpetrator(s) likely utilized advanced cyber techniques to gain unauthorized access to Mr. Smith's retirement accounts and bypassed security protocols to execute fraudulent transactions. This crime was committed entirely through digital means, with no evidence of physical intrusion or coercion.

Estimated Losses:
The total financial loss incurred by Mr. Smith is estimated to exceed $100,000. Efforts are ongoing to assess the full extent of the fraudulent activities and to determine if additional financial accounts or personal information were compromised.

Investigative Steps:
The Financial Crimes Unit, in collaboration with cybersecurity experts and financial institutions, has initiated a comprehensive forensic investigation to identify the perpetrator(s) and trace the flow of the stolen funds. Legal subpoenas have been issued to financial institutions involved in the fraudulent transactions.

Next Steps:
Mr. Smith has been advised to secure his financial accounts, place fraud alerts on his credit files, and monitor all financial statements for any further suspicious activity. The Financial Crimes Unit will continue to provide support and updates to Mr. Smith throughout the investigation.

This case remains active and ongoing. Anyone with information related to this fraud incident is urged to contact Detective B. Johnson at 555-5678 or submit tips anonymously through the police department's online portal.

Reporting Officer: Officer L. Anderson, Badge #7890 """,{
    'entities': [
            (25, 40, "CASE_NUMBER"),
            (64,  80, "DATE"),
            (174,  188,  "LOCATION"),
            (969,  1120,  "METHOD"),
            (820,  946,  "EVIDENCE"),
            (361,  557,  "STOLEN"),
            (54,  59,  "CRIME")
        ]
}),

("""
    INCIDENT REPORT

Case Number: 2024-02195
Crime: Identity Theft
Date/Time: February 19, 2024
Location: 325 Elm Street, Apartment 5C, Rivertown

VICTIM:
Emily Turner
Female, 45 years old

NARRATIVE:
On February 19th, 2024, officers responded to a report of identity theft at 325 Elm Street, Apartment 5C in the Rivertown neighborhood. Upon arrival, officers met with the victim, Emily Turner, who reported unauthorized activity on her financial accounts.

Turner stated that she discovered multiple unauthorized transactions totaling over $50,000 on her credit card statements and bank accounts. The transactions included purchases of high-end electronics, luxury items, and international wire transfers, none of which were authorized by Turner.

Further investigation revealed that Turner's personal information, including her social security number and banking details, may have been compromised through a phishing email she received several weeks prior. The email purported to be from her bank and requested updated account information.

Turner unwittingly provided her login credentials and other sensitive information, which enabled the perpetrator(s) to gain access to her accounts and carry out the fraudulent transactions. The crime appears to have been committed through sophisticated cyber means, with no physical intrusion or coercion.

Evidence:
- Statements from the victim
- Copies of unauthorized transaction records
- Forensic analysis of phishing email and compromised accounts

The investigation into this identity theft is ongoing, with efforts focused on tracing the financial transactions and identifying the perpetrator(s) responsible for the fraudulent activities. Turner has been advised to monitor her credit report closely and place fraud alerts on her accounts.

This case remains active, and anyone with information related to this identity theft incident is urged to contact Detective E. Sanchez at 555-6789 or submit tips anonymously through the police department's online portal.

Reporting Officer: Officer K. Thompson, Badge #4321

""", {
    'entities': [
            (31, 41, "CASE_NUMBER"),
            (201,  220, "DATE"),
            (103,  142,  "LOCATION"),
            (1137,  1229,  "METHOD"),
            (1357,  1493,  "EVIDENCE"),
            (49,  63,  "CRIME")
        ]
}),

("""
INCIDENT REPORT

Case Number: 2024-11230
Date of Incident: November 15, 2024
Location: 410 Pine Avenue, Apartment 2D, Lakeside

SUMMARY OF INCIDENT:
On the evening of November 15th, 2024, officers responded to a report of a homicide at 410 Pine Avenue, Apartment 2D, in the Lakeside neighborhood. Upon arrival, officers discovered the victim, Jane Smith (35), deceased in the living room of her apartment.

According to initial findings, Ms. Smith sustained multiple stab wounds to her chest and abdomen, indicating a violent and targeted attack. There were signs of a struggle in the apartment, with furniture overturned and bloodstains throughout the living area.

Neighbors reported hearing raised voices and loud noises coming from Ms. Smith's apartment around 10:00 PM the previous night. However, no one witnessed the actual incident or saw anyone entering or leaving the apartment around the time of the murder.

EVIDENCE COLLECTED:
- Crime scene photographs
- Blood samples for DNA analysis
- Potential murder weapon recovered (a kitchen knife found near the victim)

SUSPECT INFORMATION:
- No specific suspect identified at this time
- Investigators are exploring possible motives and persons of interest based on Ms. Smith's personal and professional relationships

STATUS OF INVESTIGATION:
- Active investigation underway
- Interviewing neighbors and acquaintances of Ms. Smith
- Analyzing forensic evidence for further leads
- Seeking additional witnesses and surveillance footage from the area

This case is being treated as a homicide, and the Lakeside Police Department is dedicated to bringing the perpetrator(s) to justice. Anyone with information regarding this incident is urged to contact Detective J. Martinez at 555-7890 or submit tips anonymously through the police department's website.

Reporting Officer: Officer M. Ramirez, Badge #5147

""",{
'entities': [
            (31, 41, "CASE_NUMBER"),
            (60,  77, "DATE"),
            (88,  127,  "LOCATION"),
            (439,  547,  "METHOD"),
            (941,  1075,  "EVIDENCE"),
            (1100,  1143,  "SUSPECT"),
            (225,  233,  "CRIME")
        ]
})

]