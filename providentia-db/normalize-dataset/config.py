# Does the dataset need to be normalized? If so, the locations need to be 
# specified too
NORMALIZE_DATASET = False
NORMALIZE_SETTINGS = {
    "NORMALIZE_BUS": True,
    "NORMALIZE_REV": True,
    "NORMALIZE_USE": True,
    "BUSINESS_FILE": "./business.json",
    "REVIEW_FILE": "./review.json",
    "USERS_FILE": "./user.json"
}

# Generate subset of data and clean user friends that aren't in table
GEN_SUBSET = False
SUBSET_SETTINGS = {
    "SUB_BUS": True,
    "SUB_REV": True,
    "SUB_USE": True,
    "PERC": 0.1
}

# The CSV format is used for TigerGraph's offline batch loader. The dataset
# needs to be normalized to use this option and will refer to the files in
# NORMALIZE_SETTINGS.
PREPARE_CSV = True
PREPARE_SETTINGS = {
    "PREPARE_BUS": True,
    "PREPARE_REV": True,
    "PREPARE_USE": True
}
