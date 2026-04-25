import pandas as pd


def transform(data):
    registros = []

    for element in data["elements"]:
        tags = element.get("tags", {})
        lat = element.get("lat") or element.get("center", {}).get("lat")
        lon = element.get("lon") or element.get("center", {}).get("lon")

        registros.append(
            {
                "osm_id": element.get("id"),
                "name": tags.get("name"),
                "city": tags.get("addr:city"),
                "state": tags.get("addr:state"),
                "lat": lat,
                "lon": lon,
            }
        )

    df = pd.DataFrame(registros)

    df = df.drop_duplicates(subset="osm_id")

    return df
