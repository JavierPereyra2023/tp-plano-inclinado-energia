# Carrera de energia: pelotitas, rampas y rozamiento

Proyecto HTML imprimible para un trabajo practico experimental de Fisica de 4.º ano de secundaria.

## Contenido

- `index.html`: guia completa del trabajo practico.
- `styles.css`: estilos visuales y reglas de impresion.
- `graficos.py`: script con datos ficticios editables para generar graficos.
- `assets/`: imagenes realistas PNG, respaldos SVG editables y graficos PNG.

## Como abrir el trabajo

Abrir `index.html` con cualquier navegador moderno. No requiere servidor web.

## Como generar los graficos con Python

Desde esta carpeta ejecutar:

```bash
python graficos.py
```

El script genera:

- `assets/grafico_velocidad_media.png`
- `assets/grafico_energia_mecanica.png`
- `assets/grafico_perdida_energia.png`
- `assets/grafico_tiempo_superficie.png`

Para usar datos reales, modificar la tabla `datos` dentro de `graficos.py`.

## Como exportar a PDF

1. Abrir `index.html` en el navegador.
2. Presionar `Ctrl + P`.
3. Elegir `Guardar como PDF`.
4. Activar fondos o graficos de fondo si el navegador lo permite, para conservar los colores.

## Archivos que se pueden modificar

- `index.html`: textos, consignas, tablas y prompts.
- `styles.css`: colores, tipografias y espaciados.
- `graficos.py`: datos experimentales y estilo de graficos.
- `assets/`: reemplazar imagenes SVG por imagenes generadas.

## Imagenes realistas

El documento ya usa imagenes realistas generadas y guardadas en `assets/`:

- `hero-laboratorio-plano-inclinado.png`
- `diagrama-realista-plano-inclinado.png`
- `superficies-realistas-rozamiento.png`
- `mockup-planilla-realista.png`
- `mockup-documento-realista.png`

Los archivos SVG quedan como respaldo editable, pero `index.html` usa las versiones PNG.

## Como reemplazar imagenes por OpenAI Images

En `index.html` hay una seccion con prompts en castellano. Generar cada imagen con esos prompts y guardar los archivos resultantes en `assets/`.

Se recomienda reemplazar:

- `assets/portada-plano-inclinado.svg`
- `assets/diagrama-plano-inclinado.svg`
- `assets/superficies-rozamiento.svg`
- `assets/mockup-google-sheets.svg`
- `assets/boceto-google-docs.svg`

Mantener el mismo nombre de archivo, o actualizar la ruta correspondiente en `index.html`.
