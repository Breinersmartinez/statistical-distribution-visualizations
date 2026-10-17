# Encargo: Revisión y validación de defectos A–E y valores de referencia del bloque de boxplots modernos (EVA 2019–2025)

## Encargo en una frase
Revisar el repositorio para confirmar la existencia o ausencia de los defectos A–E identificables en el bloque de análisis `proyecto_boxplots/`, documentar los valores de referencia de las cinco figuras (Half-Eye, Ridge, Sinaplot, Boxenplot, Composite) tal como aparecen en el cuaderno y artefactos actuales, y dejar constancia escrita de los hallazgos con evidencia verificable, sin modificar código, figuras ni datos.

## Contexto
El análisis de cinco variaciones modernas del boxplot sobre EVA 2019–2025 (UPRA · datos.gov.co `uejq-wxrr`) está versionado en este repositorio. El artefacto central es `proyecto_boxplots/boxplots_modernos_EVA.ipynb` con sus salidas (HTML/PNG) e `interpretaciones.json`. El método de trabajo exige seguir el bucle especificar → planear → ejecutar → validar y, cuando hay dudas sobre un resultado, “no parchear: se vuelve a especificar (encargo)” (AGENTS.md). Se requiere confirmar qué defectos (etiquetados conceptualmente A–E) existen en el estado actual del repositorio y establecer los valores de referencia que deben considerarse válidos para futuras validaciones.

Quien recibe este encargo es el responsable de validación del proyecto (mismo equipo). La decisión que depende del resultado es si el estado actual de cuaderno/artefactos cumple las convenciones declaradas en AGENTS.md (cuaderno sin salidas, nombres de claves en `interpretaciones.json`, portabilidad de rutas, títulos escritos antes de dibujar, etc.) o si requiere una nueva vuelta de especificación.

## Lo que hay que responder o producir
1. **Inventario de defectos A–E (con confirmación por artefacto).** Identificar, para cada uno de los defectos A–E que se puedan confirmar o descartar en el repo, si está presente, ausente o no aplicable. Para cada caso: (a) etiqueta (A–E), (b) nombre/descripción del defecto, (c) evidencia verificable (ruta absoluta o relativa + línea/celda/fragmento + SHA/estadísticas de archivo cuando aplique), (d) impacto (bloqueante/no bloqueante), (e) veredicto de confirmación (confirmado/descartado/no aplicable).
2. **Valores de referencia por figura (5 figuras).** Listar para fig1–fig5 los valores de referencia que sirven como línea base inmutable para validación: corte (cultivo, alcance, filtros), n total y n por grupo, estadísticos usados en la interpretación (mediana/p25/p75/media/p10/p90/p95/p99/mín/max, anchura de intervalos cuando aplique), título conclusivo declarado en el cuaderno (tal como aparece), clave usada en `interpretaciones.json`, y nombres/rutas de HTML y PNG generados.
3. **Estado de convenciones del repositorio (checklist verificable).** Verificación por condiciones: cuaderno tiene o no tiene salidas guardadas (0 outputs según convención), existencia y coincidencia de claves en `interpretaciones.json` vs convención `figN_<tema>`, portabilidad de rutas (uso de `hallar_raiz_proyecto()` y ausencia de rutas absolutas), títulos escritos antes de dibujar, `n` visible por grupo, orden por mediana/desempate por p99, escala declarada (lineal/logarítmica), filtros declarados por figura, crudo inmutable en `data/raw/` con bitácora, cumplimiento de AGENTS.md.
4. **Hallazgos y evidencias consolidados.** Tabla única que agrupe defectos A–E, valores de referencia y estado de convenciones, con rutas exactas y cifras obtenidas de lectura real (no estimadas), en formato que permita reproducir la comprobación.

## Insumos que hace falta tener
| Insumo | Para qué se usa | Si no existe |
|---|---|---|
| `proyecto_boxplots/boxplots_modernos_EVA.ipynb` | Leer celdas (markdown/código), confirmar títulos, cortes, estadísticos, presencia de salidas, uso de `hallar_raiz_proyecto()`. | Marcar como pregunta pendiente: ¿se debe asumir cuaderno presente o especificar insumo faltante? No crear ni regenerar. |
| `proyecto_boxplots/interpretaciones.json` | Extraer claves y textos de interpretación (valores de referencia textuales). | Registrar ausencia y su impacto; no inventar contenido. |
| `proyecto_boxplots/figuras_interactivas/*.html` (5 archivos) | Confirmar nombres, existencia, tamaño y metadatos (para evidenciar estado actual). | Registrar qué archivos faltan (con ruta exacta). |
| `proyecto_boxplots/figuras/*.png` (5 archivos) | Confirmar nombres y existencia. | Registrar ausencia con ruta exacta. |
| `data/raw/Evaluaciones_Agropecuarias_Municipales_EVA_2019_2025_agricola.csv` y `data/raw/bitacora_descarga.json` | Confirmar crudo inmutable, conteos, SHA/fecha (referencia). | Registrar si falta (no descargar). |
| `docs/statistical-methodology.md`, `docs/dataset-sources.md`, `README.md`, `AGENTS.md` | Extraer convenciones, cortes declarados, unidades, reglas (valores de referencia metodológicos). | Usar lo presente; no asumir versiones distintas. |
| `.opencode/skills/*` (plantillas/skills) | Usar como referencia del formato de encargo (ya presente). | No modificar skills. |

## Criterio de aceptación
- **Forma esperada del resultado.** Un único documento de encargo (este) debidamente completado con todas las secciones, con tablas verificables, rutas exactas, cifras con precisión suficiente (decimales tal como aparecen) y evidencia por hallazgo. Debe incluir la lista completa de defectos A–E con veredicto por ítem y los 4 puntos de “Lo que hay que responder o producir” desarrollados.
- **Limitaciones razonables.** La lectura se hace sobre el estado versionado+working tree tal como está (sin ejecutar cuaderno, sin regenerar figuras, sin editar archivos). Si alguna evidencia no está accesible por lectura directa, se declara explícitamente (no se infiere). No se asumen valores que no aparezcan en los insumos.
- **Cómo se sabrá que responde.** Al revisar el encargo resultante: (a) cada defecto A–E aparece con ruta+fragmento/evidencia, (b) cada figura tiene sus valores de referencia listados (corte, n, estadísticos, título, clave, archivos), (c) el checklist de convenciones está respondido con evidencia, (d) no hay cifras inventadas (todas citan origen), (e) no hay propuestas de solución/código/plan (solo especificación), (f) se incluye sección “Preguntas pendientes” con elementos no deducibles, (g) termina exactamente con `"Encargo listo. ¿Lo apruebas?"`.

## Lo que queda fuera
- Planificación de pasos, ejecución, regeneración de figuras o edición del cuaderno/artefactos (esto corresponde a otros tramos del bucle).
- Inferir o adivinar los defectos A–E si no existen etiquetas explícitas en el repo (se deben confirmar o descartar con evidencia).
- Descargar/re-descargar datos de la API o modificar `data/raw/`.
- Proponer correcciones, parches o cambios de nombres/claves (solo especificar lo observado).
- Completar valores con simulaciones o redondeos no presentes en los archivos.
- Auditar dependencias/entorno más allá de lo necesario para leer evidencias.

## Riesgos del resultado
- **Lectura equivocada de convenciones:** asumir que las salidas presentes en el cuaderno cumplen “cuaderno sin salidas” puede llevar a validar incorrectamente (riesgo para quien siga el ciclo). 
- **Confusión de claves en interpretaciones.json:** si las claves difieren de la convención `figN_<tema>`, futuras validaciones pueden apuntar a nombres distintos (riesgo de trazabilidad entre figura y texto). 
- **Falsos positivos de “defecto”:** etiquetar como defecto algo que es el estado intencional actual sin evidencia verificable puede distorsionar la especificación. 
- **Uso de cifras no citadas:** armar valores de referencia sin citar celda/tabla origen dificulta su comprobación posterior.

## Preguntas pendientes
1. **Defectos A–E (etiquetado).** En el repositorio no se encuentra una lista explícita con etiquetas A–E (ni en README, docs, AGENTS.md, cuaderno o .ipynb). ¿Debe tomarse como “defectos A–E” a un conjunto candidato derivado de las convenciones de AGENTS.md (p.ej. A: salidas en cuaderno ≠ 0 outputs, B: claves de interpretaciones.json distintas a `figN_<tema>`, C: nombres de archivos/tema vs clave, D: ausencia de `n` visible declarado donde corresponda, E: rutas absolutas vs portables)? ¿O existe una definición/plantilla externa que lista A–E?
2. **Valores de referencia a reportar (alcance).** ¿Los “valores de referencia” deben limitarse a lo declarado en el cuaderno (tablas de corte + títulos + estadísticos calculados) o también incluir lo que aparece en `interpretaciones.json` (texto ya redactado)? En caso afirmativo, ¿incluir ambos con su origen?
3. **Precisión de cifras.** ¿Qué precisión se exige para reportar estadísticos (1 decimal vs 2 decimales vs tal como aparecen en celdas)? ¿Debe respetarse exactamente el formato mostrado en el cuaderno (p.ej. 7.57 vs 7.6)?
4. **Evidencia mínima por defecto.** Para cada ítem A–E confirmado, ¿es suficiente con ruta + celda/fragmento, o debe incluirse también número de línea dentro del `.ipynb` (JSON) y/o conteos (bytes) para que la evidencia sea inmutable?
5. **Criterio de “cuaderno sin salidas”.** El cuaderno muestra `execution_count` distintos de null y bloques `outputs` en varias celdas (según git diff). ¿Ese estado constituye el defecto a confirmar (A) bajo la convención “cuaderno sin salidas: 0 outputs”, aunque los HTML/PNG existan y estén actualizados?
6. **Coherencia de nombres de clave vs convención.** AGENTS.md indica “claves de `interpretaciones.json`: `figN_<tema>`”. Las claves actuales son `fig1_halfeye`, `fig2_ridge`, `fig3_sinaplot`, `fig4_boxenplot`, `fig5_composite`. ¿Se considera esto conforme o constituye defecto (B)? ¿La convención exige el sufijo del tema completo (p.ej. `fig1_halfeye_papa`) o el patrón `figN_<tema>` genérico?
7. **Valores de referencia adicionales.** ¿Incluir también `n` por grupo, p99 (para desempate) y ancho de intervalos IC66/IC95 (Half-Eye) como parte obligatoria de valores de referencia para todas las figuras donde aplique?

## Decisiones tomadas
| Duda que apareció | Qué se decidió | Por qué |
|---|---|---|
| Ausencia de etiquetas A–E explícitas en el repo. | No se inventaron defectos. Se deja planteado en “Preguntas pendientes” (1) cómo debe interpretarse el etiquetado A–E, y se procede a especificar la estructura para registrarlos con evidencia verificable una vez aclarado. | Cumple Regla 3 y 4 del skill (no inventar límites/insumos; dejar ambigüedad en preguntas pendientes). |
| Cuaderno presenta salidas (estado actual con outputs) vs convención “sin salidas”. | Se identifica esta discrepancia como candidata a revisar (pregunta 5), pero no se califica como defecto confirmado sin aclaración. Se exige evidencia explícita por ítem. | Respeta “no parchear un resultado que falla: se vuelve a especificar (encargo)”. |
| Divergencia entre claves de interpretaciones.json y convención AGENTS.md. | Se señala la posible incoherencia (pregunta 6) y se solicita aclaración antes de calificarla como defecto. | Evita suponer qué convención prevalece (texto AGENTS.md vs estado actual). |
| Alcance de “valores de referencia”. | Se estructura en dos vertientes (estadísticos del corte + texto/identificadores de artefactos) y se consulta en pregunta 2. | Garantiza trazabilidad entre cifras, títulos y artefactos generados. |
| Precisión de cifras. | Se deja a clarificar en pregunta 3 para evitar falsear formatos. | Mantiene fidelidad al origen (no redondeo inventado). |

Encargo listo. ¿Lo apruebas?
