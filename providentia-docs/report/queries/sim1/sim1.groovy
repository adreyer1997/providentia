g.V().hasLabel("Priority")
    .has("priority_id", "1")
	.in("RESPONSE_PRIORITY").hasLabel("Response")
	.has("destination", geoWithin(
	    Geoshape.circle(63.67, 19.11, 0.5))
	).fold().aggregate("avg_ttas")
		.by(unfold()
		    .values("time_to_ambulance_starts")
		    .mean())
    .unfold().out("RESPONSE_TRANSFER")
	.fold().aggregate("avg_tth")
		.by(unfold()
		    .values("travel_time_hospital")
		    .mean())
	.select("avg_ttas", "avg_tth")