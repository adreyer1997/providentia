# Does the dataset need to be normalized? If so, the locations need to be 
# specified too
NORMALIZE_DATASET = True
NORMALIZE_SETTINGS = {
    "NORMALIZE_BUS": True,
    "NORMALIZE_REV": True,
    "NORMALIZE_USE": True,
    "NORMALIZE_SIM": True,
    "NORMALIZE_PHOTOS": True,
    "BUSINESS_FILE": "../yelp/yelp_dataset/business.json",
    "REVIEW_FILE": "../yelp/yelp_dataset/review.json",
    "USERS_FILE": "../yelp/yelp_dataset/user.json",
    "PHOTOS_FILE": "../yelp/yelp_photos/photo.json",
    "SIM_FILE": "./out/alarms.csv"
}

# Generate subset of data and clean user friends that aren't in table
GEN_SUBSET = True
SUBSET_SETTINGS = {
    "SUB_BUS": True,
    "SUB_REV": True,
    "SUB_USE": True,
    "SUB_PHOTOS": True,
    "PERC": 0.01
}

# The CSV format is used for TigerGraph's offline batch loader. The dataset
# needs to be normalized to use this option and will refer to the files in
# NORMALIZE_SETTINGS.
PREPARE_CSV = True
PREPARE_SETTINGS = {
    "PREPARE_BUS": True,
    "PREPARE_REV": True,
    "PREPARE_USE": True,
    "PREPARE_SIM": True,
    "PREPARE_PHOTOS": True
}
