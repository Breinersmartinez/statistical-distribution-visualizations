# Encargo: Corrección de los defectos A–E del bloque de boxplots modernos (EVA 2019–2025)

## Encargo en una frase
Corregir el bloque `proyecto_boxplots/` de las cinco variaciones modernas del boxplot sobre EVA 2019–2025 resolviendo los defectos A–E definidos en el mensaje del usuario, editando el cuaderno, regenerando las 5 figuras HTML interactivas, los 5 PNG y `interpretaciones.json`, generando el informe HTML ejecutado y actualizando README, `requirements.txt`, la bitácora y los docs, sin tocar `presentation/` ni el CSV de `data/raw/`.

## Contexto
El repositorio `statistical-distribution-visualizations` contiene la actividad de "Técnicas de validación y simulación": cinco variaciones modernas del boxplot (Half-Eye, Ridge, Sinaplot, Boxenplot y Composite Stat-Boxplot) sobre el dataset EVA 2019–2025 (UPRA · datos.gov.co `uejq-wxrr`), en Python/Plotly. Una revisión independiente encontró defectos concretos (A–E) que esta ronda debe corregir. El destinatario es el propio Breiner y, en última instancia, la revisión del profesor: la decisión que depende del resultado es si la actividad queda entregable y verificable (figuras correctas, afirmaciones sostenibles, reproducibilidad sin Chrome, artefactos regenerados). Este tramo solo especifica; la corrección efectiva corresponde a los tramos de planear, ejecutar y validar.

## Lo que hay que responder o producir
1. **Cuaderno corregido** (`proyecto_boxplots/boxplots_modernos_EVA.ipynb`) con los defectos A–E resueltos uno a uno:
   - A: eje Y de la Figura 1 numérico (`tickvals=0..4`, `ticktext` = los 5 departamentos, rango fijo), `go.Box` con `y0=i`/`width`, sin `type="category"`; las 5 etiquetas `n=` en filas distintas.
   - B: Figura 5 reconstruida como boxplot estadístico integrado (violín + caja + puntos + media + `n` + Kruskal-Wallis H/gl/p + ε² + pares Mann-Whitney con Holm en tabla y hover, sin cajas letter-value), con la celda de concepto explicando qué agrega lo "estadístico".
   - C: cada afirmación insostenible de las Fig 1–5 corregida (texto y/o título), con cada cifra salida de una variable vía f-strings.
   - D: títulos de Fig 1 y 4 sin cortar (líneas ≤ ~85 caracteres, comprobado por código); etiquetas del eje X de Fig 3 sin solaparse.
   - E: exportación a PNG envuelta en try/except con aviso y lista final de PNG faltantes; requisitos fijados; informe HTML ejecutado; figuras y `interpretaciones.json` regenerados; README/bitácora/data-README/docs actualizados.
   El cuaderno se entrega **sin salidas** (0 `outputs`, 0 `execution_count`).
2. **Artefactos regenerados**: 5 HTML en `proyecto_boxplots/figuras_interactivas/`, 5 PNG en `proyecto_boxplots/figuras/` e `interpretaciones.json`, todos producidos desde el cuaderno corregido con Restart & Run All sin errores. Nombres de archivo y claves `fig1_halfeye`, `fig2_ridge`, `fig3_sinaplot`, `fig4_boxenplot`, `fig5_composite` **sin cambios**.
3. **Informe ejecutable** `proyecto_boxplots/boxplots_modernos_EVA.html` (nbconvert `--execute`) donde se ven las 5 figuras sin correr nada.
4. **Documentación actualizada**: `README.md` (tabla de hallazgos con los títulos corregidos y pasos de ejecución), `requirements.txt` (versiones mínimas), `data/raw/bitacora_descarga.json` (rutas relativas), `data/README.md` (hoy vacío) y `docs/dataset-sources.md` (explicación verificada de la discrepancia de `sha256`).
5. **Reporte de reproducción de los valores de referencia del mensaje**: tabla con, por figura, el valor declarado por el usuario y el valor que produce el cuaderno; si alguno no coincide, se **reporta la diferencia** (no se ajusta nada). Valores a reproducir: Fig 1 (medianas Antioquia 14, Nariño 15, Boyacá 16, Santander 18, Cundinamarca 20; N = 4.622; ancho del intervalo 95 % 22–37); Fig 2 (máximo 2021 = 25,0; media 2021 ≈ 7,55 y 2025 ≈ 8,46; medianas 7,0–7,57); Fig 3 (N por depto 187–247; máximos Valle 1,5 · Cauca 1,4 · Huila 0,88; ≈ 85 % múltiplos de 0,05; ≈ 43,8 % en 0,5 o 0,6); Fig 4 (p99 relativo tomate 4,82 · maíz 4,44 · frijol 3,23 · plátano 3,14 · yuca 2,50; máximos relativos maíz 15,6 · frijol 14,6 · yuca 9,0 · tomate 8,4 · plátano 4,3); Fig 5 (N = 2.562; medianas 0,95 Boyacá – 1,21 Antioquia; Kruskal-Wallis H ≈ 182,5, p ≈ 1,6e-37, ε² ≈ 0,069).
6. **Títulos nuevos escritos antes de redibujar** (en el tramo de plan, previo a cualquier ejecución) y luego **validados contra la tabla** de valores de referencia; ninguno retocado a posteriori para que "cuadre".
7. **Evidencia de las comprobaciones programáticas**: JSON/dict de la Figura 1 (eje Y no `category`, exactamente 5 `ticktext`, sin ticks decimales, 5 `Box` con `y0` distintos) y de la Figura 5 (componentes presentes, ausencia de letter-value, estadísticos y pares).

## Insumos que hace falta tener
| Insumo | Para qué se usa | Si no existe |
|---|---|---|
| `proyecto_boxplots/boxplots_modernos_EVA.ipynb` | Editar A–E y regenerar todos los artefactos. | Bloqueante: sin cuaderno no hay corrección; declararlo. |
| `proyecto_boxplots/interpretaciones.json` | Regenerar los textos con las claves fijas `fig1_halfeye`…`fig5_composite`. | Se crea desde el cuaderno; no inventar textos a mano. |
| `proyecto_boxplots/figuras/*.png` (5) y `figuras_interactivas/*.html` (5) | Sobrescribir con las versiones corregidas. | Se regeneran desde el cuaderno. |
| `data/raw/Evaluaciones_Agropecuarias_Municipales_EVA_2019_2025_agricola.csv` | Recalcular estadísticas y verificar el `sha256`. | El cuaderno lo descarga de la API (requiere internet); **no** editar el crudo. |
| `data/raw/bitacora_descarga.json` | Relativizar rutas y conservar campos de verificación. | Si falta, dejarlo anotado; no fabricar campos. |
| `README.md`, `requirements.txt`, `data/README.md`, `docs/dataset-sources.md`, `docs/statistical-methodology.md` | Actualizar según E. | Usar lo presente; no asumir versiones distintas. |
| Valores de referencia (mensaje del usuario) | Línea base de validación de A, B y C. | No deducibles del repo; ya vienen en el mensaje. |
| Entorno: `scipy`, `kaleido`, `nbconvert`, Chrome / `plotly_get_chrome` | B: Kruskal-Wallis/Mann-Whitney; D/E: PNG y HTML ejecutado. | Sin Chrome, PNG faltantes con aviso (no debe romper); declarar. |
| `AGENTS.md` (existe en local, en `.gitignore`) | Convenciones; decidir si se versiona o se quita su referencia del README. | No debe afectar la corrección; ver pregunta pendiente 1. |

## Criterio de aceptación
- **Forma esperada del resultado.** El cuaderno corregido y sin salidas; 5 HTML + 5 PNG + `interpretaciones.json` regenerados; el informe `proyecto_boxplots/boxplots_modernos_EVA.html`; README, `requirements.txt`, bitácora, `data/README.md` y docs actualizados; y un reporte de reproducción de valores de referencia por figura (valor declarado vs valor del cuaderno, con la diferencia si no coincide).
- **Condiciones verificables (textuales del mensaje):**
  1. Fig 1 pasa la comprobación programática de A, en el HTML y en el PNG.
  2. Fig 5 incluye violín + caja + puntos + media + n + Kruskal-Wallis + epsilon cuadrado + pares con Holm, y ya no usa cajas letter-value.
  3. Cada afirmación de C está corregida y cada cifra del texto sale de una variable (ninguna escrita a mano).
  4. Los 5 títulos se escriben antes de redibujar y se validan contra la tabla; ninguno retocado a posteriori.
  5. Títulos de Fig 1 y 4 sin cortar; etiquetas de Fig 3 sin solaparse (comprobado por código).
  6. El cuaderno corre de arriba a abajo sin errores, con y sin Chrome; el HTML ejecutado existe y muestra las 5 figuras.
  7. `data/raw/*.csv` con el mismo `sha256` que en la bitácora; `presentation/` sin cambios (`git diff` vacío en esa carpeta).
  8. Validación por figura con las cuatro preguntas del analista: ¿el número tiene sentido?, ¿la forma cuadra (misma escala, n visible, orden por mediana, densidad dentro del rango de los datos)?, ¿responde lo que pregunté?, ¿cambió algo frente al boxplot del mismo corte?
- **Sección E completa (textual del mensaje):**
  - `write_image` (Kaleido ≥ 1 requiere Chrome) no debe hacer fallar el cuaderno: envolver cada exportación PNG en try/except con aviso claro y una lista final de PNG que faltaron; documentar `plotly_get_chrome` en el README; el cuaderno completo debe correr sin errores incluso sin Chrome (con aviso).
  - `requirements.txt`: fijar versiones mínimas de lo ya listado (pandas, numpy, scipy, plotly, kaleido, requests, jupyter, ipykernel y las demás actuales); no eliminar entradas; añadir solo lo que se use (p. ej. nbconvert).
  - Generar y entregar `proyecto_boxplots/boxplots_modernos_EVA.html` (nbconvert `--execute`) donde se vean las 5 figuras sin correr nada; preferir figuras interactivas que abran sin internet; si el archivo supera ~40 MB, usar PNG incrustados y enlaces relativos a `figuras_interactivas/`, declarándolo en el README; el `.ipynb` sigue sin salidas.
  - Regenerar las 5 figuras HTML interactivas y los 5 PNG e `interpretaciones.json` desde el cuaderno corregido, con Restart & Run All sin errores.
  - `README.md`: actualizar la tabla de hallazgos con los títulos corregidos y los pasos de ejecución; eliminar la referencia a `AGENTS.md`; no modificar la sección sobre la presentación.
  - `data/raw/bitacora_descarga.json`: reemplazar las rutas absolutas locales (`/home/...`) por rutas relativas al repo; conservar todos los campos de verificación; comparar el CSV previo (mismo número de filas, `sha256` distinto) con el descargado y documentar en `docs/dataset-sources.md` la explicación verificada (p. ej. orden de columnas, codificación o formato numérico); si no se puede determinar, decirlo.
  - `data/README.md` está vacío: escribir una descripción breve (origen, enlace directo, cómo se descarga, qué es inmutable).
- **Límites razonables.** Se mantienen los cortes (papa × 5 deptos, plátano × años, cacao × 6 deptos, top 5 cultivos, café × 6 deptos) y los nombres de archivo/claves. Se admite cambiar un título si una validación lo obliga, nunca un corte. Las cifras de referencia pueden diferir del cuaderno (se reporta, no se ajusta).
- **Cómo se sabrá que responde.** (a) Fig 1 supera la comprobación programática en HTML y PNG; (b) Fig 5 tiene todos los componentes de B y cero letter-value; (c) ninguna cifra del texto está escrita a mano; (d) los 5 títulos están redactados antes de redibujar y coinciden con la tabla; (e) el cuaderno corre con y sin Chrome y el HTML ejecutado muestra 5 figuras; (f) `sha256` del CSV igual a la bitácora y `git diff -- presentation/` vacío; (g) existe el reporte de reproducción de valores de referencia.

## Lo que queda fuera
- Auditar el repo o confirmar/descartar defectos: los A–E ya están dados en el mensaje y esta ronda los corrige.
- Cambiar de dataset, de cortes o de nombres de archivo/claves (`fig1_halfeye`…`fig5_composite`).
- Tocar `presentation/` o modificar el CSV de `data/raw/` (su `sha256` debe quedar igual).
- Datos simulados o cifras de interpretación escritas a mano.
- Instalar dependencias sin declararlas en `requirements.txt`.
- Planificar pasos, ejecutar y validar: corresponde a los otros tramos del bucle.

## Riesgos del resultado
- **Valores de referencia no reproducidos:** si el cuaderno no da las cifras del mensaje, tomarlas como ciertas ocultaría un error de cálculo; se debe reportar la diferencia.
- **Título ajustado a posteriori:** retocar un título para que "cuadre" con la tabla rompe la regla del bucle; los títulos se escriben antes de dibujar.
- **Chrome ausente en el entorno de entrega:** sin el try/except, el cuaderno se rompe en la primera figura; con él, faltarían PNG y hay que declararlos.
- **Informe HTML sobredimensionado:** puede superar ~40 MB y volverse inmanejable; prever PNG incrustados + enlaces relativos.
- **Deriva de `presentation/` o del crudo:** cualquier edición en esas rutas invalida la entrega (condición 7).

## Preguntas pendientes
1. **`AGENTS.md` (versionado vs referencia).** El archivo existe en local pero está en `.gitignore` y no está versionado; el README lo referencia como fuente de reglas y comando. ¿Se **versiona** `AGENTS.md` (quitándolo de `.gitignore`) o se **elimina la referencia** a `AGENTS.md` del README (como pide E)?
2. **Criterio de "diferencias relevantes" en la Figura 5.** B pide mostrar en la figura "solo las diferencias relevantes" de los pares Mann-Whitney, sin definirlas. ¿Qué cuenta como relevante para dibujar (p. ej. solo pares con p de Holm < 0,05, un umbral de tamaño de efecto, o todas las de la tabla resumidas)? El resto de pares iría a la tabla del cuaderno y al hover.

## Decisiones tomadas
| Duda que apareció | Qué se decidió | Por qué |
|---|---|---|
| De dónde salen los defectos A–E. | Tomarlos **literalmente** de la sección "DEFECTOS A CORREGIR" del mensaje del usuario (A: Fig 1 rota; B: Fig 5 sin componente estadístico; C: afirmaciones insostenibles; D: legibilidad; E: reproducibilidad y entregables). No inferirlos de AGENTS.md. | El usuario corrigió que los defectos están en su mensaje, no en el repo. |
| Objetivo del encargo. | **Corregir** (editar cuaderno, regenerar figuras y JSON, generar informe, actualizar docs), no auditar. | Es la ronda de corrección; la auditoría anterior quedó descartada. |
| Qué cifras son línea base. | Los **valores de referencia del mensaje**, calculados de forma independiente; el cuaderno actual **no** lo es. | El usuario lo indicó explícitamente; si el cuaderno no los reproduce, se reporta. |
| Alcance de edición. | `proyecto_boxplots/`, `README.md`, `requirements.txt`, `data/README.md`, `data/raw/bitacora_descarga.json`, `docs/`. Prohibido `presentation/` y el CSV crudo. | Límite duro declarado por el usuario (condición 7). |
| Claves de `interpretaciones.json`. | Se conservan `fig1_halfeye`…`fig5_composite`. | Otros archivos (presentación y consumidores) las leen. |
| Salidas del cuaderno. | Se entrega **sin salidas** (0 `outputs`). El cuaderno ya está limpio hoy y debe seguir así. | Convención del repo y requisito de E. |
| Dónde se escriben los títulos nuevos. | Antes de redibujar (tramo de plan inmediato) y se validan contra la tabla; no se retocan después. | Regla del bucle (escribir el título antes de dibujar) repetida en C. |
| Comprobaciones "no dependan de verlo". | Se exige evidencia programática sobre el JSON/dict de las figuras (A y B). | El mensaje pide comprobación por código, no visual. |

Encargo listo. ¿Lo apruebas?
