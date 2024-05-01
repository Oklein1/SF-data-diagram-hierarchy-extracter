import pandas as pd


def hierarchy_builder(filename):
    
    df = pd.read_csv(filename)
    
    ################
    #### PART I ####
    ################
    
    #main dfs
    source_df = df[["Id", "Name", "Line Source", "Line Destination", "Text Area 1","Source Arrow"]]
    sf_entities = source_df[source_df["Name"] == "Collapsed card"][["Id", "Text Area 1"]].rename(columns={"Text Area 1":"SF_Entities"})
    hierarchy = source_df[source_df["Name"] == "Line"][["Id", "Line Source", "Line Destination", "Source Arrow"]].rename(columns={"Line Source":"Child",
                                                                                                                  "Line Destination": "Parent"})
    # parent and child cols in hierarchy df are loaded as floats => making them into ints.
    
    hierarchy["Parent"] = hierarchy["Parent"].dropna().astype(int)
    hierarchy["Child"] = hierarchy["Child"].dropna().astype(int)
    
    #merging dfs
    parent_hierarchy = pd.merge(sf_entities,hierarchy,how='inner',left_on='Id',right_on='Parent').rename(columns={"SF_Entities": "SF_Entities(Parent)",
                                                                                                             "Id_x":"id"})
    parent_hierarchy_cleaned = parent_hierarchy[["id","SF_Entities(Parent)","Parent","Child","Source Arrow"]]
    sales_cloud_hierarchy = pd.merge(parent_hierarchy_cleaned,sf_entities,how='inner',left_on='Child',right_on='Id')
    
    
    #format SF hierarchy df
    sales_cloud_hierarchy_source = sales_cloud_hierarchy.rename(columns={"SF_Entities":"SF_Entities(Child)",
                                                                        "Parent":"Parent(ID)",
                                                                        "Child":"Child(ID)"})[["SF_Entities(Parent)","Parent(ID)","SF_Entities(Child)","Child(ID)","Source Arrow"]]
    
    
    #################
    #### PART II ####
    #################
    
    # Cleaning up SF hierarchy data (Parent & Child) - achtung: assumption here
    sales_cloud_hierarchy_source["SF_Entities(Parent)_clean"] = sales_cloud_hierarchy_source["SF_Entities(Parent)"].str.split("\u2028",expand=False).str[0] #ACHTUNG: this line and below assumes broken encoding may not be in all lucid charts
    sales_cloud_hierarchy_source["SF_Entities(Child)_clean"] = sales_cloud_hierarchy_source["SF_Entities(Child)"].str.split("\u2028",expand=False).str[0]
    sales_cloud_hierarchy_final = sales_cloud_hierarchy_source[["SF_Entities(Parent)_clean","Parent(ID)","SF_Entities(Child)_clean","Child(ID)","Source Arrow"]].rename(columns={"SF_Entities(Parent)_clean":"SF_Entities(Parent)",
                                                                                                                                                            "SF_Entities(Child)_clean": "SF_Entities(Child)",
                                                                                                                                                            "Source Arrow":"Parent-Child(Relationship)"})
    
    ################
    ### PART III ###
    ################
    
    return sales_cloud_hierarchy_final