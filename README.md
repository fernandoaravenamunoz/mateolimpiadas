# Olimpiadas de Matemáticas · Middle School

Plataforma para conducir las Olimpiadas de Matemáticas de 3° a 6° básico del
**George Chaytor English College**, pensada para proyectar en la sala.

👉 **Ver la plataforma:** https://USUARIO.github.io/REPOSITORIO/
*(reemplaza `USUARIO` y `REPOSITORIO` cuando publiques el sitio)*

## Qué incluye

- **Torneo por nivel:** rondas de 2 a 4 jugadores, ronda final entre los ganadores y pantalla de campeón.
- **Seis juegos:** cálculo mental contra reloj, cadena mental, cuadrado mágico, recta numérica, kakoomas y problemas.
  La dificultad depende del nivel y los ejercicios se generan sin repetirse entre rondas.
- **Banco de 240 problemas** (45 por nivel más 15 de desempate), alineados a los Aprendizajes Basales
  de la Actualización de la Priorización Curricular del MINEDUC.
- **Desempates** con problema sorpresa y botón de ausencia.
- **Configuración por nivel:** qué juegos se juegan en las rondas y en la final, tiempos, puntajes,
  cantidades y los jugadores de cada ronda.
- **PDF para imprimir:** el banco de problemas con sus soluciones y la pauta de cálculo mental del conductor.

## Cómo publicarlo en GitHub Pages

1. Crea un repositorio y sube `index.html` (y este `README.md`) a la rama `main`.
2. Entra a **Settings → Pages**.
3. En **Source** elige `Deploy from a branch`, rama `main` y carpeta `/ (root)`.
4. Guarda y espera un par de minutos: el sitio queda en `https://USUARIO.github.io/REPOSITORIO/`.

Para publicarlo dentro de un sitio que ya tengas, copia `index.html` en una carpeta
(por ejemplo `olimpiadas/`) de ese repositorio; quedará en `.../olimpiadas/`.

## Cómo funciona

Es **una sola página**: todo el código, los estilos, las imágenes y el banco de problemas van
dentro de `index.html`. No necesita servidor, base de datos ni instalación.

- La configuración, los jugadores y los resultados se guardan en el navegador del computador
  que se use (`localStorage`). Si vas a conducir desde otro equipo, usa **Exportar** e **Importar**
  desde la pantalla de Configuración.
- Para generar los PDF se necesita conexión a internet (la librería jsPDF se carga desde un CDN).
- También funciona abriendo el archivo directamente con doble clic, sin publicarlo.

## Uso rápido

1. En la portada, el ícono ⚙ abre la configuración: elige los juegos de cada nivel y escribe los
   jugadores de cada ronda.
2. Presiona la insignia para entrar y elige el nivel.
3. Cada juego parte con una diapositiva de título, una explicación con ejemplo y el tema de cada
   pregunta; el tiempo comienza cuando aparece la pregunta.
4. Al terminar las rondas, la plataforma muestra los clasificados y da paso a la final.

**Atajos:** `Espacio` pausa el cronómetro · `R` muestra la respuesta · `B` campanilla ·
`←` `→` navegar · `1`–`6` dar el punto a un jugador · en cálculo mental, `C` correcta y `X` incorrecta.
