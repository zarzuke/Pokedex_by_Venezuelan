from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer



def crear_reporte():
    # Datos de ejemplo (reemplaza con tus propios datos)
    nombre_usuario = "Ash Ketchum"
    pokemones = [
        {"ID": 1, "Nombre": "Pikachu", "Tipo": "Eléctrico", "Descripción": "Ratón eléctrico"},
        {"ID": 2, "Nombre": "Charizard", "Tipo": "Fuego/Volador", "Descripción": "Dragón de fuego"},
        # Agrega más Pokémon aquí según tus necesidades
    ]

    # Crear un archivo PDF
    doc = SimpleDocTemplate("Personal_Pokedex.pdf", pagesize=letter)

    # Estilos de texto
    styles = getSampleStyleSheet()
    titulo_style = ParagraphStyle("Titulo", parent=styles["Title"])
    titulo_style.alignment = 1  # Centrado

    # Contenido del PDF
    contenido = []
    contenido.append(Paragraph("Personal Pokédex System 1", titulo_style))
    contenido.append(Spacer(1, 20))  # Dos saltos de línea
    contenido.append(Paragraph(f"Pokémon favoritos de {nombre_usuario}", styles["Heading1"]))

    # Crear tabla con los campos ID, Nombre, Tipo y Descripción
    tabla_datos = [["ID", "Nombre", "Tipo", "Descripción"]]
    for pokemon in pokemones:
        tabla_datos.append([pokemon["ID"], pokemon["Nombre"], pokemon["Tipo"], pokemon["Descripción"]])

    tabla = Table(tabla_datos, colWidths=[40, 100, 80, 200])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), "#CCCCCC"),  # Fila de encabezado
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Centrar contenido
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Centrar verticalmente
        ("INNERGRID", (0, 0), (-1, -1), 0.25, "#000000"),  # Líneas internas
        ("BOX", (0, 0), (-1, -1), 0.5, "#000000"),  # Borde exterior
    ]))

    contenido.append(tabla)

    # Construir el PDF
    doc.build(contenido)
    print("PDF generado correctamente.")
