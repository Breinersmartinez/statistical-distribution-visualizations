# Metodología estadística

## Unidad de análisis

Un registro = `municipio × desagregacion_cultivo × periodo` (0 duplicados con esa llave). Cada punto
de las figuras es un registro municipal, **no** un promedio ponderado por área ni producción. Cuando
se dice "la mediana del departamento" es la mediana de sus registros municipales, no la del
departamento como total.

## Convención de periodo por ciclo

- Cultivos **Transitorios** (papa, yuca, maíz, cacao de ciclo corto, etc.): dos periodos por año, `A`
  y `B`.
- Cultivos **Permanentes** (café, plátano, cacao): un periodo `anual`.
- El cuaderno deriva `tipo_periodo` con la expresión regular `(\d{4})([AB]?)$` → `A`, `B` o `anual`.
- Hay ruido declarado en el campo (ver `dataset-sources.md`): 311 Transitorios anuales y 81
  Permanentes con `A`/`B`. No se corrige.

## Limpieza

1. Áreas, producción y rendimiento se convierten a numérico con `errors="coerce"`; `anio` a entero.
2. Todas las figuras descartan los registros con `rendimiento = 0` (no hubo cosecha). El filtro se
   reporta en voz alta: cuántas filas quita antes de seguir.

## Cortes por figura

| Figura | Cultivo | Alcance | Filtros |
|--------|---------|---------|---------|
| fig1 · Half-Eye | Papa | Boyacá, Cundinamarca, Nariño, Antioquia, Santander | `rendimiento > 0` (n = 4 622) |
| fig2 · Ridge | Plátano | 2019–2025 | `rendimiento > 0`, por año |
| fig3 · Sinaplot | Cacao | Huila, Tolima, Valle del Cauca, Cundinamarca, Cauca, Meta | `rendimiento > 0` |
| fig4 · Boxenplot | Top 5 (maíz, yuca, frijol, tomate, plátano) | todos los municipios | `rendimiento > 0`, normalizado por mediana nacional |
| fig5 · Composite | Café | Antioquia, Santander, Cundinamarca, Boyacá, Nariño, Valle del Cauca | `rendimiento > 0` (n = 2 562) |

## Las cinco técnicas: qué estima cada una

- **Half-Eye** (fig1): densidad **KDE** (`scipy.stats.gaussian_kde`, ancho de banda por defecto de
  Scott), evaluada **solo dentro del rango observado** (sin extrapolar) y reflejada en el eje;
  mediana marcada; bandas de intervalo del 66 % (`np.quantile(v,[0.17,0.83])`) y del 95 %
  (`np.quantile(v,[0.025,0.975])`). Contrasta con un `go.Box` del mismo corte.
- **Ridge** (fig2): una KDE por año sobre un **eje x común** ([0, 30] t/ha), apiladas sin
  extrapolación. Compara **formas**, no solo centros.
- **Sinaplot** (fig3): cada observación se dibuja y se desplaza en horizontal en proporción a su
  **densidad local** (`dens = gaussian_kde(v)(v)`). Muestra todos los puntos, además de la forma.
- **Boxenplot** (fig4): **cuantiles anidados** de `np.quantile(v,[qlo,qhi])` desde `(0.25,0.75)`
  hasta `(0.0156,0.9844)`, cada banda proporcional al número de observaciones que resume. Como la
  variable es un **cociente** (rendimiento ÷ mediana nacional del cultivo), se usa **escala
  logarítmica** y una referencia en 1.
- **Composite** (fig5): superpone la caja letter-value, la **mediana**, la **media** (rombo, distinta
  de la mediana) y una capa de puntos. Panel derecho: `go.Box` clásico del mismo corte.

En fig4 y fig5 la capa de puntos del hover es una **muestra** por grupo (se declara); no son todos los
registros.

## Cuantiles y estadística descriptiva

- Los cuantiles se calculan con `numpy.quantile` / `pandas.Series.quantile` (interpolación **lineal**,
  la de por defecto).
- Se usan p01, p10, p17, p25, p50 (mediana), p75, p83, p90, p95, p99, media, mínimo y máximo según la
  figura, siempre sobre el corte ya filtrado.

## Regla de atípicos

La regla convencional del boxplot marca atípicos fuera de `[Q1 − 1.5·IQR, Q3 + 1.5·IQR]`
(`((s < q1-1.5*iqr) | (s > q3+1.5*iqr)).mean()`). Sirve de **contraejemplo**, no de criterio: cuando
la distribución tiene la cola larga **abajo** (café), la regla se dispara en el lado alto y esconde
precisamente la cola baja que importa; y cultivos con la cola alta más pesada (tomate) resultan entre
los que **menos** puntos marcan. Por eso las figuras muestran la forma, no solo los atípicos.

## Reglas de orden (por qué las categorías van en ese orden)

1. Orden natural cuando existe (años en el Ridge; escala ordinal), y se **rotula** el eje.
2. En lo demás, **orden por mediana ascendente**.
3. **Desempate**: si las medianas empatan, se desempata por el **cuantil de cola p99** ascendente
   (fig4, con medianas relativas = 1; fig5, Santander/Nariño con mediana 1,09). Se **declara en el eje**.

## Reglas de lectura y validación

- El **título conclusivo se escribe antes de dibujar** y luego se valida contra la tabla del corte.
- La interpretación se arma con **f-strings** desde las variables: ninguna cifra se escribe a mano.
- En cada figura se declara: `n` visible por grupo, tipo de escala (lineal/logarítmica) y el filtro
  aplicado.
- Cada figura se valida contra su especificación; si algo no cuadra, se **re-especifica** en vez de
  parchear.

## Limitaciones

- Todo el análisis es **descriptivo**: no se atribuye causalidad a ninguna diferencia entre
  departamentos, años o cultivos.
- La KDE depende del ancho de banda; con colas largas y datos redondeados, la densidad es una
  **estimación suave**, no la distribución exacta.
- El rendimiento es en buena parte una cifra **redondeada** (66.41 % enteros), lo que infla los
  empates y afecta la forma de la densidad.
- El letter-value plot asume que hay observaciones suficientes para estimar cuantiles extremos; con
  N pequeño, las bandas de cola son poco fiables.
