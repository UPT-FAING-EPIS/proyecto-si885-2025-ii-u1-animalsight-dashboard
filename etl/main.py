from etl.scraper import SECTIONS, get_links, extract_text
from etl.transform import transformar_noticia
from etl.load import guardar_csv

def run_etl():
    rows = []
    for medio, url in SECTIONS.items():
        print(f"--- Buscando en {medio} ---")
        links = get_links(url)
        for link in links:
            texto = extract_text(link)
            resultados = transformar_noticia(medio, link, texto)
            rows.extend(resultados)

    df = guardar_csv(rows)
    print("ETL terminado. Registros:", len(df))

if __name__ == "__main__":
    run_etl()
