g.V().has("User", "user_id", "qUL3CdRRF1vedNvaq06rIA")
        .as("kate")
    .outE("REVIEWS")
        .has("stars", gt(3))
    .inV().in("REVIEWS")
        .where(neq("kate")).as("users")
    .out("REVIEWS").out("IN_CATEGORY")
        .has("name", "Restaurants")
    .select("users").dedup()
    .values("user_id").fold()