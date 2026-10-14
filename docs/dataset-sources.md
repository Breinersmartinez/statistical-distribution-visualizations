# Fuentes de datos

## Origen

| Campo | Valor |
|-------|-------|
| Nombre | Evaluaciones Agropecuarias Municipales - EVA. 2019 - 2025. Base Agrícola |
| Entidad | UPRA (Unidad de Planificación de Tierras Rurales) |
| Portal | <https://www.datos.gov.co/d/uejq-wxrr> |
| API (Socrata) | `https://www.datos.gov.co/resource/uejq-wxrr.json` |
| Identificador | `uejq-wxrr` |
| Periodo | 2019–2025 |

Datos publicados como datos abiertos del Estado colombiano. La descarga la hace el propio cuaderno
(`descargar_si_falta`); si el CSV ya está en `data/raw/` no se re-descarga.

## Mecánica de descarga

- Paginación Socrata: `$limit = 50000`, `$offset` incremental, `$order = :id`, pausa de 0.3 s.
- 4 páginas descargadas; `count(*)` de la API = 166 732 = filas escritas (coincide).
- Archivo: `data/raw/Evaluaciones_Agropecuarias_Municipales_EVA_2019_2025_agricola.csv`.
- SHA-256: `b0eee1cff5102e1e9dd2efcddfcf173c42d5a6fc7808fa588e534ba2cc69d3ca`.
- Fecha de descarga (UTC): `2026-10-14T15:20:21Z`.
- Metadatos completos en `data/raw/bitacora_descarga.json`.

## Columnas (crudas → renombradas)

La API entrega los encabezados degradados (la vocal acentuada se volvió `_`), de modo que el cuaderno
los renombra al cargar (`REN`).

| Crudo | Renombrado | Contenido |
|-------|-----------|-----------|
| `c_digo_dane_departamento` | `codigo_dane_departamento` | Código DANE departamento |
| `departamento` | `departamento` | Nombre del departamento |
| `c_digo_dane_municipio` | `codigo_dane_municipio` | Código DANE municipio |
| `municipio` | `municipio` | Nombre del municipio |
| `grupo_cultivo` | `grupo_cultivo` | Agrupación de cultivos |
| `subgrupo` | `subgrupo` | Subagrupación |
| `cultivo` | `cultivo` | Nombre del cultivo |
| `desagregaci_n_cultivo` | `desagregacion_cultivo` | Desagregación (tipo/variedad) |
| `a_o` | `anio` | Año |
| `periodo` | `periodo` | Periodo, p. ej. `2019A` |
| `rea_sembrada` | `area_sembrada` | Área sembrada (ha) |
| `rea_cosechada` | `area_cosechada` | Área cosechada (ha) |
| `producci_n` | `produccion` | Producción (t) |
| `rendimiento` | `rendimiento` | Rendimiento (t/ha) |
| `ciclo_del_cultivo` | `ciclo_del_cultivo` | Transitorio / Permanente |
| `estado_f_sico_del_cultivo` | `estado_fisico_del_cultivo` | Estado físico reportado |
| `c_digo_del_cultivo` | `codigo_cultivo` | Código del cultivo |
| `nombre_cient_fico_del_cultivo` | `nombre_cientifico_cultivo` | Nombre científico |

## Cobertura

- 166 732 filas; 32 departamentos; 1 103 municipios; 165 cultivos; años 2019–2025.
- 21 valores distintos de `periodo`; por tipo: `anual` 65 286, `A` 53 065, `B` 48 381.

## Calidad y advertencias

- **Sin nulos**: 0 valores faltantes en las 18 columnas crudas.
- **Rendimiento cero**: 7 116 registros (4.27 %) con `rendimiento = 0`; coinciden exactamente con los
  que tienen `area_cosechada = 0` (no hubo cosecha). Se descartan en todas las figuras.
- **Área sembrada cero**: 3 007 registros (algunos con producción reportada).
- **Granularidad**: 0 duplicados con la llave `municipio × desagregacion_cultivo × periodo`; 17 058
  duplicados si se ignora `desagregacion_cultivo` (varias desagregaciones por cultivo y periodo).
- **Precisión del dato**: 66.41 % de los rendimientos positivos son enteros y 26.63 % son múltiplos
  de 5 → el rendimiento es en buena parte una cifra estimada/redondeada, no medida al decimal.
- **Cola extrema**: máximo global 253 t/ha (muy por encima de la mediana 6); se trata dentro de cada
  figura, no se elimina.
- **Ciclo vs. periodo**: hay ruido en la convención — 311 registros de cultivos Transitorios vienen
  con `periodo` anual y 81 registros de Permanentes vienen con `A`/`B`. No se corrige; se respeta el
  campo `ciclo_del_cultivo`.
- **CSV de la web ≠ CSV de la API**: el archivo que publica el portal (descarga web) y el export de la
  API tienen el mismo número de filas pero distinto SHA-256 (`mismo_contenido_sha256: false`). Este
  proyecto trabaja siempre con el export de la API, registrado en la bitácora.
