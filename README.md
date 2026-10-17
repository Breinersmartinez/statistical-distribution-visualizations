# Cinco variaciones modernas del diagrama de caja y bigotes

Exploración interactiva de cinco técnicas modernas de visualización de distribuciones sobre datos
abiertos colombianos reales. Cada figura responde una pregunta sobre el rendimiento agrícola
municipal y muestra algo que el boxplot clásico esconde.

## Qué es esto

El boxplot resume una distribución en cinco números y pierde la forma, las colas y la masa. Este
proyecto reproduce esa limitación y la corrige con cinco alternativas (Half-Eye, Ridge, Sinaplot,
Boxenplot y Composite Stat-Boxplot), cada una sobre un corte real de los datos y con su
interpretación validada contra la tabla.

## Dataset

- **Nombre:** Evaluaciones Agropecuarias Municipales - EVA. 2019 - 2025. Base Agrícola.
- **Fuente:** UPRA (Unidad de Planificación de Tierras Rurales), datos abiertos de Colombia.
- **Enlace:** <https://www.datos.gov.co/d/uejq-wxrr> · API: `https://www.datos.gov.co/resource/uejq-wxrr.json`
- **Tamaño:** 166 732 registros, 32 departamentos, 1 103 municipios, 165 cultivos (2019–2025).
- **Unidad de análisis:** un registro = municipio × desagregación de cultivo × periodo. Cada punto
  de las figuras es un registro municipal, no un promedio ponderado.
- **Crudo inmutable:** `data/raw/Evaluaciones_Agropecuarias_Municipales_EVA_2019_2025_agricola.csv`
  (descarga por la API, con `sha256` y conteos en `data/raw/bitacora_descarga.json`).
- Filtro transversal declarado en cada figura: se descartan los registros con `rendimiento = 0`.

## Las cinco figuras

| Figura | Técnica | Corte | Hallazgo |
|--------|---------|-------|----------|
| `fig1_halfeye_papa` | Half-Eye (densidad KDE + mediana + intervalos 66 % y 95 %) | Papa × Boyacá, Cundinamarca, Nariño, Antioquia, Santander | Medianas entre 14 y 20 t/ha; la amplitud del intervalo central del 95 % va de 22 a 37 t/ha |
| `fig2_ridge_platano` | Ridge (densidad KDE por año, eje x común) | Plátano × 2019–2025 | La forma es estable; mediana cerca de 7 t/ha y cola alta persistente, con leve repunte en 2025 |
| `fig3_sinaplot_cacao` | Sinaplot (jitter proporcional a la densidad) | Cacao × Huila, Tolima, Valle del Cauca, Cundinamarca, Cauca, Meta | Medianas casi iguales (0,5–0,6 t/ha) pero colas distintas: Valle del Cauca y Cauca llegan a 1,4–1,5 |
| `fig4_boxenplot_top5` | Boxenplot (letter-value, cuantiles anidados) | Cinco cultivos con más registros EVA positivos (maíz, yuca, frijol, tomate, plátano), rendimiento relativo | Mismo nivel (medianas = 1) pero colas distintas: tomate y maíz pesadas (p99 ≈ 4,4–4,8), yuca liviana (p99 ≈ 2,5) |
| `fig5_composite_cafe` | Composite (caja + mediana + media + puntos) | Café × Antioquia, Santander, Cundinamarca, Boyacá, Nariño, Valle del Cauca | La media es levemente menor que la mediana en los seis departamentos; las medianas van de 0,95 a 1,21 t/ha |

Salidas por figura: HTML interactivo en `proyecto_boxplots/figuras_interactivas/` y PNG en
`proyecto_boxplots/figuras/`. El texto de cada interpretación vive en
`proyecto_boxplots/interpretaciones.json`.

## Cómo se ejecuta

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/plotly_get_chrome -y  # una vez: necesario para exportar los PNG con Kaleido
.venv/bin/jupyter lab proyecto_boxplots/boxplots_modernos_EVA.ipynb
```

- El cuaderno declara el kernel `python3`; lánzalo desde `.venv/bin/` para que resuelva al entorno.
- En la primera corrida descarga el CSV de la API (necesita internet); después lo lee de `data/raw/`.
- El cuaderno se entrega **sin salidas**: cada figura se dibuja al ejecutar su celda y además se
  exporta a HTML y PNG.

**Portabilidad:** el cuaderno no usa rutas absolutas. Localiza la raíz del repositorio subiendo desde
el directorio actual hasta hallar la carpeta que contiene `proyecto_boxplots/` y `data/raw/`; también
acepta la variable de entorno `PROYECTO_RAIZ`. Así corre igual en cualquier máquina, siempre que el
repositorio mantenga esa estructura.

## Estructura del repositorio

```
proyecto_boxplots/       entregable: cuaderno, figuras (PNG/HTML) e interpretaciones.json
presentation/            presentacion_boxplots_modernos.pptx
data/raw/                fuente cruda inmutable + bitacora de descarga
docs/                    fuentes de datos y metodología estadística
requirements.txt         dependencias (pandas, numpy, scipy, plotly, kaleido, python-pptx)
.venv/                   interprete fijo del proyecto (Python 3.12.3)
```

## Presentación

`presentation/presentacion_boxplots_modernos.pptx` (14 diapositivas, orden contexto → hallazgo →
implicación → fuentes) reúne las cinco figuras y sus conclusiones.

## Método

Cada figura sigue el mismo ciclo reproducible: se escribe el título conclusivo antes de dibujar, se
arma la interpretación con f-strings desde las variables y se valida contra la tabla. El comando de
ejecución y las dependencias están documentados en este README.
