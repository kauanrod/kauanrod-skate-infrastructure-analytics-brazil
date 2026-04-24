from extract import extract, save_raw
from transform import transform
from load import load

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    logging.info("Extraindo dados...")
    raw_data = extract()

    logging.info("Salvando raw...")
    save_raw(raw_data)

    logging.info("Transformando...")
    df = transform(raw_data)

    logging.info("Carregando...")
    load(df)

    logging.info("Pipeline concluída.")


if __name__ == "__main__":
    run_pipeline()
