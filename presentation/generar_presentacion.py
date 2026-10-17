"""Genera la presentación de la actividad desde las figuras derivadas del cuaderno."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


RAIZ = Path(__file__).resolve().parents[1]
FIGURAS = RAIZ / "proyecto_boxplots" / "figuras"
SALIDA = Path(__file__).resolve().parent / "presentacion_boxplots_modernos.pptx"
URL_DATOS = "https://www.datos.gov.co/d/uejq-wxrr"

AZUL = RGBColor(11, 83, 148)
TINTA = RGBColor(32, 33, 36)
GRIS = RGBColor(90, 90, 90)
GRIS_CLARO = RGBColor(242, 242, 242)
ROJO = RGBColor(176, 58, 43)
BLANCO = RGBColor(255, 255, 255)


def cuadro_texto(slide, x, y, ancho, alto, texto, tam=18, color=TINTA,
                 negrita=False, alineacion=PP_ALIGN.LEFT):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(ancho), Inches(alto))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    for indice, linea in enumerate(texto.split("\n")):
        p = tf.paragraphs[0] if indice == 0 else tf.add_paragraph()
        p.text = linea
        p.alignment = alineacion
        p.space_after = Pt(4)
        for run in p.runs:
            run.font.name = "Aptos"
            run.font.size = Pt(tam)
            run.font.bold = negrita
            run.font.color.rgb = color
    return shape


def titulo(slide, texto, subtitulo=None):
    cuadro_texto(slide, 0.65, 0.32, 12.0, 0.55, texto, tam=25, color=AZUL, negrita=True)
    if subtitulo:
        cuadro_texto(slide, 0.68, 0.9, 12.0, 0.3, subtitulo, tam=11, color=GRIS)


def pie(slide, numero):
    cuadro_texto(slide, 0.65, 7.1, 8.0, 0.22, "Fuente: EVA 2019–2025 (UPRA) · datos.gov.co", tam=9, color=GRIS)
    enlace = cuadro_texto(slide, 8.7, 7.1, 3.7, 0.22, URL_DATOS, tam=9, color=AZUL,
                          alineacion=PP_ALIGN.RIGHT)
    enlace.text_frame.paragraphs[0].runs[0].hyperlink.address = URL_DATOS
    cuadro_texto(slide, 12.45, 7.1, 0.25, 0.22, str(numero), tam=9, color=GRIS,
                 alineacion=PP_ALIGN.RIGHT)


def caja(slide, x, y, ancho, alto, encabezado, contenido, acento=AZUL):
    fondo = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(ancho), Inches(alto))
    fondo.fill.solid()
    fondo.fill.fore_color.rgb = GRIS_CLARO
    fondo.line.color.rgb = acento
    fondo.line.width = Pt(1)
    cuadro_texto(slide, x + 0.2, y + 0.15, ancho - 0.4, 0.32, encabezado.upper(), tam=10, color=acento, negrita=True)
    cuadro_texto(slide, x + 0.2, y + 0.5, ancho - 0.4, alto - 0.62, contenido, tam=15, color=TINTA)


def diapositiva_concepto(prs, numero, nombre, concepto, limitacion, uso, muestra):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titulo(slide, f"{numero}. {nombre}", "Concepto, limitación que corrige y uso recomendado")
    caja(slide, 0.65, 1.45, 3.9, 4.95, "Concepto", concepto)
    caja(slide, 4.72, 1.45, 3.9, 4.95, "Qué no muestra la caja", limitacion, ROJO)
    caja(slide, 8.79, 1.45, 3.9, 4.95, "Úselo cuando", uso)
    cuadro_texto(slide, 0.7, 6.55, 12.0, 0.3, muestra, tam=12, color=GRIS, alineacion=PP_ALIGN.CENTER)
    pie(slide, 2 * numero + 1)


def diapositiva_figura(prs, numero, nombre_archivo, encabezado, interpretacion, demostracion):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titulo(slide, encabezado, "Captura de la visualización Plotly generada con datos reales EVA")
    ruta = FIGURAS / nombre_archivo
    slide.shapes.add_picture(str(ruta), Inches(0.5), Inches(1.2), width=Inches(12.33), height=Inches(4.85))
    cuadro_texto(slide, 0.7, 6.08, 11.95, 0.62, interpretacion, tam=11, color=TINTA)
    cuadro_texto(slide, 0.7, 6.72, 11.95, 0.22, demostracion, tam=9, color=GRIS, alineacion=PP_ALIGN.CENTER)
    pie(slide, 2 * numero + 2)


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Portada
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    cuadro_texto(slide, 0.8, 1.15, 11.8, 1.1, "Cinco variaciones modernas\ndel diagrama de caja y bigotes", tam=31, color=AZUL, negrita=True)
    cuadro_texto(slide, 0.85, 2.65, 10.8, 0.55, "Actividad de Técnicas de Validación y Simulación · Universidad Cooperativa de Colombia, campus Cali", tam=17, color=TINTA)
    cuadro_texto(slide, 0.85, 3.35, 9.8, 0.45, "Datos reales: rendimiento agrícola municipal EVA 2019–2025 (UPRA)", tam=18, color=ROJO)
    cuadro_texto(slide, 0.85, 5.3, 11.6, 0.7, "Pregunta conductora: ¿qué revela cada gráfico que el boxplot tradicional esconde?", tam=20, color=TINTA)
    pie(slide, 1)

    # Datos y entregables
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titulo(slide, "Datos, método y entregables", "Una misma fuente abierta; cinco preguntas y cinco visualizaciones interactivas")
    caja(slide, 0.65, 1.45, 3.85, 4.85, "Dataset real", "Evaluaciones Agropecuarias Municipales – EVA. 2019–2025, Base Agrícola (UPRA).\n\n166.732 registros; 32 departamentos; 1.103 municipios; 165 cultivos.\n\nCada punto representa municipio × cultivo × período.")
    caja(slide, 4.74, 1.45, 3.85, 4.85, "Reproducibilidad", "Cuaderno Python: proyecto_boxplots/boxplots_modernos_EVA.ipynb.\n\nGenera cinco HTML Plotly autónomos, cinco PNG y las interpretaciones.\n\nNo se usaron datos simulados.")
    caja(slide, 8.83, 1.45, 3.85, 4.85, "Cómo se demuestra", "En esta presentación: captura de cada gráfico interactivo.\n\nEn la entrega: abra los archivos HTML en proyecto_boxplots/figuras_interactivas/.\n\nLos títulos fueron contrastados contra las tablas del cuaderno.")
    pie(slide, 2)

    tecnicas = [
        ("Half-Eye Plot", "Una densidad KDE reflejada con mediana e intervalos empíricos; hace visible dónde se concentra la distribución.", "La caja no muestra forma, acumulaciones ni huecos dentro de los cuartiles.", "Variable continua y pocas o varias categorías con suficientes observaciones por grupo. Es útil si importa comparar forma, centro y colas.", "Corte: papa con rendimiento > 0 en cinco departamentos; N = 4.622.", "fig1_halfeye_papa.png", "Half-Eye · papa por departamento", "Cundinamarca (20,0 t/ha) y Boyacá superan a Antioquia (14,0) y Nariño en mediana. Los cinco departamentos presentan dispersión amplia; el intervalo central del 95 % mide entre 22,0 y 37,0 t/ha.", "Demostración: fig1_halfeye_papa.html · hover por municipio, período y rendimiento."),
        ("Ridge Plot (gráfico de crestas)", "Apila una densidad por grupo en un eje x común para comparar formas sin que una distribución tape a otra.", "El boxplot dificulta ver si la forma cambia entre muchos grupos ordenados, como una serie temporal.", "Muchas categorías ordenadas —años, tratamientos o sitios— con N suficiente en cada una. No conviene cuando hay pocas categorías.", "Corte: plátano con rendimiento > 0 por año, 2019–2025; N anual entre 784 y 824.", "fig2_ridge_platano.png", "Ridge · plátano por año", "La mediana se mantiene entre 7,0 y 7,6 t/ha y el IQR entre 4,2 y 5,0. El único movimiento visible es el leve repunte de 2025; persiste una cola alta en todos los años.", "Demostración: fig2_ridge_platano.html · hover por municipio, departamento, período y rendimiento."),
        ("Sinaplot", "Ubica cada observación y ensancha su desplazamiento horizontal según la densidad local; combina puntos y forma de distribución.", "La caja resume y oculta cuántas observaciones se apilan en cada valor.", "N moderado por categoría, cuando se necesitan ver todos los datos y su densidad. Con N masivo se satura; con muy pocos puntos el jitter pierde sentido.", "Corte: cacao con rendimiento > 0 en seis departamentos; N por grupo entre 187 y 247.", "fig3_sinaplot_cacao.png", "Sinaplot · cacao por departamento", "Las medianas son cercanas (0,50–0,60 t/ha), pero las colas distinguen a los departamentos: Valle del Cauca llega a 1,50 y Cauca a 1,40, mientras Huila alcanza 0,88 t/ha.", "Demostración: fig3_sinaplot_cacao.html · cada punto permite inspeccionar el registro real."),
        ("Boxenplot (Letter-Value Plot)", "Representa cuantiles anidados hasta las colas; cada banda añade detalle donde un boxplot solo muestra Q1, mediana y Q3.", "La caja tradicional pierde estructura de las colas, especialmente cuando N es grande y los cuantiles extremos se estiman con estabilidad.", "Miles de observaciones por grupo y preguntas sobre extremos o dispersión de cola. Para comparar unidades distintas, normalice primero.", "Corte: maíz, yuca, frijol, tomate y plátano; N total = 51.959. Rendimiento normalizado por mediana nacional.", "fig4_boxenplot_top5.png", "Boxenplot · top 5 de cultivos", "Todas las medianas relativas valen 1, pero las colas no: tomate tiene p99 = 4,8× y maíz 4,4×; yuca presenta la cola alta más corta, p99 = 2,5×. La escala logarítmica permite comparar esas razones.", "Demostración: fig4_boxenplot_top5.html · hover de cuantiles y muestra de registros."),
        ("Composite Stat-Boxplot", "Integra cajas letter-value, mediana, media y puntos en una sola vista para leer centro, dispersión y sesgo juntos.", "El boxplot no muestra la media ni revela de inmediato si el sesgo va hacia arriba o hacia abajo.", "Pocas o varias categorías cuando hay varias preguntas estadísticas a la vez y se necesita una lectura integrada. Evítelo si la audiencia requiere una vista muy simple.", "Corte: café con rendimiento > 0 en seis departamentos; N = 2.562.", "fig5_composite_cafe.png", "Composite Stat-Boxplot · café por departamento", "En los seis departamentos la media queda por debajo de la mediana, señal de cola baja. Antioquia lidera por mediana (1,21 t/ha) y Boyacá queda al final (0,95); el IQR máximo es 0,44 t/ha.", "Demostración: fig5_composite_cafe.html · hover de cuantiles, media, mediana y observaciones."),
    ]

    for indice, (nombre, concepto, limitacion, uso, muestra, png, encabezado, interpretacion, demostracion) in enumerate(tecnicas, start=1):
        diapositiva_concepto(prs, indice, nombre, concepto, limitacion, uso, muestra)
        diapositiva_figura(prs, indice, png, encabezado, interpretacion, demostracion)

    # Cierre
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titulo(slide, "Cierre: una técnica para cada pregunta", "El gráfico no se elige por apariencia: se deriva de lo que se necesita comparar")
    caja(slide, 0.65, 1.45, 3.85, 4.6, "Lo que se corrigió", "Forma y densidad: Half-Eye y Ridge.\n\nPilas de observaciones: Sinaplot.\n\nColas con N grande: Boxenplot.\n\nMedia, mediana y cuantiles juntos: Composite.")
    caja(slide, 4.74, 1.45, 3.85, 4.6, "Reglas de lectura", "Título conclusivo y verdadero.\n\nEjes con unidad y escala declarada.\n\nN visible por grupo.\n\nOrden por mediana; p99 para desempates.\n\nFuente y datos reales visibles.")
    caja(slide, 8.83, 1.45, 3.85, 4.6, "Entrega", "Presentación: este archivo.\n\nReproducible: boxplots_modernos_EVA.ipynb.\n\nInteractivos: cinco HTML Plotly.\n\nCapturas: cinco PNG.\n\nInterpretaciones: interpretaciones.json.")
    cuadro_texto(slide, 0.7, 6.35, 12.0, 0.35, "El boxplot clásico resume; estas cinco variaciones devuelven forma, densidad, colas y sesgo a la decisión.", tam=15, color=AZUL, negrita=True, alineacion=PP_ALIGN.CENTER)
    pie(slide, 13)

    prs.save(SALIDA)
    print(f"Presentación generada: {SALIDA}")


if __name__ == "__main__":
    main()
