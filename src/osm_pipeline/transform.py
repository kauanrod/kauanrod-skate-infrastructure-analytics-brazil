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
                "nome": tags.get("name"),
                "cidade": tags.get("addr:city"),
                "estado": tags.get("addr:state"),
                "latitude": lat,
                "longitude": lon,
            }
        )

    df = pd.DataFrame(registros)

    df = df.drop_duplicates(subset="osm_id")

    return df
