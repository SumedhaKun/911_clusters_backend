#run clustering algorithm and return cluster information
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import dbconnection
import matplotlib as plt
import parseCrimeReportsData

conn= dbconnection.open_connection_to_db("rds!cluster-37ab34ae-e03e-4681-ad30-a7dfb19f2520")
cur=conn.cursor
#run clustering algorithm and return cluster information




#get analytics on a specific case in the DB when provided with the caseNumber

def get_analytics(caseNumber):
    analysis=""
    query="SELECT * FROM CaseRecords WHERE caseNum NOT IN (SELECT caseNum FROM your_table WHERE %(caseNumber)d)"
    df = pd.read_sql_query(query, conn)
    print(df)
    num_clusters = 3
    features = ['compromiseMethod', 'tools', 'evidence']  
    # Fit KMeans clustering model
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(df[features])
    cluster_assignment = kmeans.predict(pd.read_sql_query("SELECT * FROM CaseRecords WHERE caseNum = %(caseNumber)d"))

    if cluster_assignment in kmeans.labels_:
        analysis+="The row belongs to a cluster."
    else:
        analysis+="The row does not belong to any cluster."
    analysis+="This row belongs to "+cluster_assignment+" based on the features: "+features
    conn.close()
    return analysis








#
