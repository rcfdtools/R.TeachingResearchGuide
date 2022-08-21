## Creación y gestión en línea de repositorios en GitHub
Keywords: `Markdown` `HTML` `Repository` `.gitignore` `Readme.md`

En esta actividad aprenderá a crear y gestionar repositorios en GitHub directamente desde el navegador de Internet.

<div align="center">
<br><img alt="R.TeachingResearchGuide" src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Graph/GitHubRepository.svg" width="30%"><br><br>
</div>
                                                                                                                                                      

### Creación de usuario

1. Ingrese a https://github.com/ y de clic en la opción `Sign up`

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubSingUp.png)

2. En la ventana de registro, ingrese su dirección de correo electrónico, establezca una contraseña segura, defina su nombre de usuario, indique con `y/n` si desea recibir notificaciones por correo y de clic en el botón `Continue`. Para este ejemplo, crearé la cuenta de usuario `rcfdtoolstest`.

> En la ventana de creación aparecerán mensajes indicando si la cuenta de correo utilizada ya está siendo utilizada por otro usuario, password válido y nombre disponible para la creación del usuario GitHub.  
![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubEnterYourEmail.png)

> **Recomendación de correo asociado**: debido a que su cuenta de GitHub es personal y el ingreso de sesión y recuperación de contraseñas estará regido por su dirección de correo, se recomienda crear una cuenta de correo personal en Outlook o GMail y crear su cuenta GitHub utilizando esta dirección. Luego de generada la cuenta, podrá asociar su cuenta de correo corporativo desde la [configuración de cuenta de correo](https://github.com/settings/emails).
> 
> **Recomendación para nombre de usuario**: utilice un nombre corto que describa su identidad profesional o su especialidad, p. ej. si ud es experto en proyectos relacionados con física cuántica, su nombre de usuario podrá ser algo como `quantumphysicsprj`, siempre y cuando este nombre no haya sido tomado por otro usuario. Por privacidad y para dar un carácter más profesional a su espacio colaborativo en  GitHub, **No es recomendable usar su nombre** o información personal. Si es propietario de una empresa, no use este nombre para crear su perfil, cree un espacio compartido colaborativo a través de una Organización de GitHub.  

3. Para terminar con la creación de cuenta, verifique la creación de su cuenta seleccionando o solucionando el rompecabezas que aparece en pantalla y de clic en el botón `Create account`. Será enviado un código de verificación a su cuenta de correo.

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubVerifyAccount.png)
![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubCreateAccount.png)

4. Ingrese el código de verificación recibido en su cuenta de correo, automáticamente será dirigido a la raíz de su espacio GitHub.

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubEmailCode.png)
![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubEnterCode.png)
![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubMain.png)

5. Para visualizar su espacio personal y los repositorios creados asociados, ingrese su nombre de usuario después del nombre de dominio `https://github.com/rcfdtoolstest`

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubHome.png)


### Creación de mi primer repositorio

1. En la parte superior derecha de su ventana de GitHub, de clic en el botón `+` y seleccione la opción `New repository`.

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubNewRepository.png)

2. En la ventana de creación de repositorio nuevo, ingrese el nombre del repositorio, p. ej. `repotest` e ingrese una descripción general de su propósito.

Defina su el repositorio será de uso Público o Privado, si es público, cualquier usuario de Internet podrá visualizar, clonar o descargar la información contenida dentro del respositorio; si es privado, usted podrá decidir quien o quienes pueden acceder al respositorio.

> Para los dos tipos de repositorio, el creador podrá decidir si integra o no las modificaciones que los usuarios propongan a través de commit's.

Para inicializar un repositorio, uste puede decidir si quiere incluir el primer archivo de documentación `Readme.md` en formato Markdown sobre la raíz. También podrá incluir el archivo de exclusiones `.gitignore` que le permitirá realizar exclusiones de archivos y directorios que no hacen parte de la información pública que se sincronizará desde unidades locales cuando la gestión del repositorio se realiza con una herramienta externa directamente desde su equipo. Para este ejemplo incluiremos estas dos opciones sin definir una plantilla prototipo para .gitignore.

> En caso de que no cree el archivo Readme.md y .gitingore, estos podrán ser creados manualmente.
> 
> Github dispone de múltiples plantillas que contiene los archivos que no deben ser sincronizados y publicados en su proyecto, p. ej. para proyectos creados en Python en los cuales se han creado ambientes virtuales, no se debe sincronizar la carpeta `.venv` ni los archivos precompilados `.pyc` de librerías propias contenidas en `__pycache__`. Para la gestión desde Desktop, p. ej. a través de PyCharm o de Visual Studio Code`, no se incluyen la carpeta `.idea` y demás archivos de gestión utilizados por los administradores de contenido o herramientas de gestión Git.

Opcionalmente, podrá seleccionar el tipo de licencia a utilizar entre diferentes licencias disponibles orientadas a desarrollo de software o a producción de contenido audiovisual. Generalmente, los usuarios seleccionan la [Licencia MIT](https://opensource.org/licenses/MIT) debido a que confiere uso abierto completo pero sin ningún tipo de garantía o responsabilidad.

> Para este ejemplo no especificaremos una licencia debido a que utilizaremos una licencia derivada que será documentada desde el centro de documentación wiki de este ejemplo.

Para finalizar la creación del repositorio, de clic en el botón `Create repository`

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubCreateRepository.png)

[Ejemplo de licencia MIT](https://opensource.org/licenses/MIT)

```
Copyright <YEAR> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

[Ejemplo de licencia embebida en R.TeachingResearchGuide.](https://github.com/rcfdtools/R.TeachingResearchGuide/wiki/License)

3. Luego de creado el repositorio, será dirigido automáticamente `repotest` y podrá visualizar el contenido del Archivo `Readme.md`

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRepoTest.png)

> Recuerde que la documentación del proyecto principalmente se realiza a través de archivos Markdown en formato .md, y GitHub puede interpretar y mostrar en pantalla el contenido del archivo con su traducción a HTML para su visualización.

En la dirección de su navegador podrá observar el nombre de su cuenta de usuario y el nombre del repositorio creado `https://github.com/rcfdtoolstest/repotest`. Desde este momento, el repositorio se encuentra visible en Internet y puede ser consultado por cualquier usuario debido a que es público.

Para clonar o descargar el repositorio, en el botón `Code` encontrará opciones para generar una URL de clonación, [GitHub command line - CLI](https://cli.github.com/), apertura y sincronización desde GitHub Desktop y descarga en formato .zip. Para este proyecto, la URL de clonación es `https://github.com/rcfdtoolstest/repotest.git` que corresponde al nombre que aparece en la barra del navegador más la terminación `.git`

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRepoTestCode.png)

Al encontrarse su sesión de usuario abierta en el navegador, ingresando https://github.com/, podrá observar que en el panel izquierdo aparece su repositorio en recientes.

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRecent.png)


### Opciones predeterminadas disponibles para repositorios nuevos

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRepoTestCodeSections.png)

En la parte superior de la ventana del repositorio, podrá encontrar las siguientes secciones:

| Sección      | Utilidad                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <> Code      | Ventana principal del repositorio donde se encuentran los archivos y carpetas del proyecto, investigación, e-book. Por defecto, todos los archivos se encuentran en el `main` del repositorio y pueden existir múltiples ramas o `branch`.                                                                                                                                                                                           |
| Issues       | Los Issues son utilizados para elementos del repositorio, reportar errores que necesitan ser ajustados en nuevas versiones, solicitar nuevas funcionalidades, referenciar otras fuentes o métodos y en general se convierten en la lista de tareas pendientes que se deben ir solucionando. Issues permite la creación de plantillas para facilitar el reporte por parte de los usuarios.                                            |
| Pull request | Cuando un usuario o un colaborador clona el repositorio y realiza ajustes, correcciones, actualizaciones, nuevas implementaciones; estas pueden ser incorporadas a través de peticiones de incorporación o Pull request. Una vez el propietario o colaborador directo revisa los cambios, estos pueden ser incorporados al main del proyecto y quedan documentados a través de Commit's.                                             |
| Actions      | GitHub actions permite crear, probar y depurar el código creado a través de flujos de procesos. Durante las acciones se pueden documentar las revisiones, administrar las diferentes ramas de prueba y clasificar los problemas encontrados para colocarlos en la lista de pendientes de Issues.                                                                                                                                     |
| Projects     | Esta herramienta permite crear una especie de libro electrónico donde se crean actividades y se designan equipos y responsables, que permiten realizar un seguimiento a los avances del proyecto. Se pueden filtrar, ordenar y agrupar por diferentes criterios.                                                                                                                                                                     |
| Wiki         | Wikis es el lugar donde se crea la documentación general del repositorio, permite incluir múltiples archivos Markdown para generar, p. ej. el índice general de contenidos, referencias generales, licencia de uso y un listado de abreviaturas.                                                                                                                                                                                     |
| Security     | Desde esta pestaña se establecen las políticas generales y recomendaciones de seguridad, además de la configuración de herramientas para detectar vulnerabilidades.                                                                                                                                                                                                                                                                  |
| Insights     | Esta pestaña permite monitorear todo lo que sucede en el repositorio, p. ej. el total de incorporaciones realizadas, las incorporaciones pendientes, los problemas identificados y resueltos, las acciones realizadas, los contribuidores, el tráfico hacia el repositorio como el número de veces que ha sido clonado o visitado, la frecuencia con la que se trabaja en el repositorio, gráficas de dependencia y linea de tiempo. |
| Settings     | Configuración general del repositorio, definición de colaboradores, opciones de moderación, administración de ramas, definición de etiquetas, acciones, ambientes, páginas, integraciones y otros.                                                                                                                                                                                                                                   |

> Por defecto, en las opciones disponibles para el repositorio no se encuentran las Discusiones, cuyo funcionamiento es similar al de un foro de ayuda y soporte y es el mejor canal de comunicación entre los creadores y los usuarios. Su activación se realiza desde las opciones de configuración o Settings a través del grupo de opciones General.

En la parte derecha encontrará la sección acerca de o `About` que presenta un resumen general del repositorio, su descripción, usuarios que han marcado el repositorio como favorito, usuarios que se encueran visualizando, número de clonaciones y secciones con la liberación de nuevas versiones (cuando se trata de un software) y paquetes liberados. Desde el ícono de configuración localizado en la parte superior derecha, podrá actualizar los detalles generales, tales como el texto resumen, las palabras clave y desactivar los Releases, Packages & Environments.

<div align="center">

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRepoTestRightSidePanel.png)

</div>

De clic en las opciones de configuración, podrá observar que también puede asociar un Website creado a través de [GitHub Pages](https://pages.github.com/). Realice los siguientes ajustes:

* Actualice la descripción del repositorio a "Repositorio de prueba - Guía para enseñanza e investigación colaborativa - https://github.com/rcfdtools/R.TeachingResearchGuide."
* Topics: research teaching guide guidelines rcfdtools (ingresar en minúscula y separados por un espacio)
* Desactive: Releases, Packages & Environments

> Para su propio repositorio, ingrese una descripción que resuma su alcance y propósito. Ingrese las palabras clave más representativas de todas las actividades, clases o herramientas contenidas en el repositorio. En caso de que su repositorio corresponda a un proyecto de investigación a través del cual se van a crear scripts, herramientas, módulos, paquetes; mantenga activas las opciones Releases, Packages & Environments.

<div align="center">

![R.TeachingResearchGuide](https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitHubRepository/Screenshot/GitHubRepoTestRightSidePanel1.png)

</div>


### Estructura genérica de un curso, una investigación, un e-book o un repositorio orientado a desarrollo de software

Las estructuras de directorios de un repositorio en GitHub, dependen del tipo de proyecto a realizar, p. ej.:

| Tipo de proyecto                                | Descripción                                                                                                                                                                                                                                                                                                    |
|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repositorio orientado al desarrollo de software | Su estructura depende de los requerimientos y entornos de desarrollo propios de cada lenguaje de programación.                                                                                                                                                                                                 |
| Libro electrónico o e-Book                      | Su estructura general se puede definir a través de capítulos y sub-capítulos más directorios comunes para referencias, iconografía y gráficos.                                                                                                                                                                 |
| Investigación / Profundización                  | Se puede utilizar una combinación entre la estructura general de un libro electrónico y desarrollo de software, cuando la investigación incluye la creación de scripts, herramientas, módulos, paquetes. Son requeridas carpetas complementarias para almacenamiento de conjuntos de datos y archivos comunes. |
| Curso teórico                                   | Su estructura general se puede definir a través de secciones o temas y clases, más directorios comunes para referencias, iconografía y gráficos.                                                                                                                                                               |
| Curso práctico                                  | Su estructura general se puede definir a través de secciones y actividades, más directorios comunes para conjuntos datos, referencias, iconografía y gráficos.                                                                                                                                                 |
| Curso teórico / práctico                        | Su estructura general se puede definir a través de secciones y actividades, más directorios comunes para conjuntos datos, referencias, iconografía y gráficos.                                                                                                                                                 |

Para la estructura general de los cursos, es recomendable utilizar únicamente dos niveles para facilitar la navegabilidad entre los contenidos y la administración de los directorios o carpetas asociadas. 

| Tipología                      | Jerarquía interna         | Caso de estudio / Aplicabilidad                                                    |
|:-------------------------------|:--------------------------|:-----------------------------------------------------------------------------------|
| Curso teórico                  | Temas y clases            | Ejemplos teóricos                                                                  |
| Curso teórico y práctico       | Secciones y actividades   | Caso de estudio general y/o casos de estudios particulares por sección o actividad |
| Investigación / Profundización | Capítulos y sub-capítulos | Caso de estudio único                                                              |
| e-book                         | Capítulos y sub-capítulos | Ejemplos teóricos y prácticos                                                      |

Estructura ejemplo para un curso teórico y práctico:  

* Sección 1
  * Actividad A
  * Actividad B
  * Actividad C
* Sección 2
  * Actividad A
  * Actividad B
  * Actividad C
* Sección 3
  * Actividad A
  * Actividad B
  * Actividad C

> Dentro de la estructura de carpetas se nombran y numeran las secciones de forma consecutiva debido a que enmarcan contenidos y actividades que se relacionan entre ellas. Respecto a las actividades, estás no se numeran, indexan o se ordenan de manera sucesiva debido a que su estructura interna y ordenamiento puede modificarse o ajustarse por inclusión de nuevas actividades intermedias, actividades complementarias o el retiro de actividades que dentro de la gestión del curso se consideran obsoletas o han sido reemplazadas por una nueva actividad con contenidos actualizados.  
>
> Tenga en cuenta que las actividades de un curso o una investigación pueden ser utilizadas o citadas transversalmente en otros cursos o investigaciones y que al ser incluida numeración consecutiva, esta no coincidirá con la establecida. Por tal motivo no se recomienda numerar las actividades. 
> 
> Respecto al nombre de las secciones y actividades, se recomienda utilizar un nombre corto que no incluya espacios, tildes, eñes, apóstrofes ni caracteres especiales como #$&*/|\{}[]. 


### Carpetas de archivos comunes

Para la gestión de los recursos compartidos del repositorio, es necesario crear diferentes carpetas en el directorio principal que faciliten su llamado. Las carpetas en la raíz del repositorio utilizarán como prefijo un punto, se escriben en minúscula y utilizan nombres cortos, excepto aquellas que correspondan al nombre genérico de una herramienta específica, por ejemplo HECGeoHMS.

Ejemplo:

| Carpeta   | Descripción                                                                                             | Formatos ejemplo                                                                                  |
|-----------|:--------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| .datasets | Contiene datos base que puedan ser convertidos en tablas, series o bases de datos.                      | .xls, xlsx, .txt, .dbf, .asc, .csv, .db, .mdbno espacial, .accdb no espacial, .sqlite no espacial |
| .gdb      | Bases de datos espaciales                                                                               | Esri .gdb, .mdb .spatialite                                                                       |
| .github   | Almacenamiento de plantillas Issue del repositorio                                                      | .md                                                                                               |
| .icons    | Iconografía general                                                                                     | .ico, .png, .svg (recomendado)                                                                    |
| .refs     | Archivos de referencias bibliográficas de uso libre recopiladas                                         | .pdf, .md, .doc, .docx, .epub                                                                     |
| .src      | Scripts de uso común                                                                                    | .py, .bas, .sh                                                                                    |
| .temp     | Carpeta para volcado de archivos temporales de aplicaciones. Archivos de prueba. Versiones preliminares | Cualquier formato                                                                                 |

> Todos los directorios contendrán un archivo Readme.md en formato Markdown con las especificaciones detalladas de los contenidos de las carpetas.

Dentro de una sección, una actividad o clase, pueden existir carpetas específicas para gestión de datos, p. ej. la carpeta `.datasets` con archivos particulares que únicamente se utilizan en esa sección o actividad. Dentro de cada sección es necesario incluir las siguientes carpetas:

| Carpeta    | Descripción                                                                                                                 | Formatos ejemplo  |
|------------|:----------------------------------------------------------------------------------------------------------------------------|:------------------|
| Graph      | Gráficos generados o exportados, diagramas, esquemas, ilustraciones y archivos fuente de diseño gráfico                     | .cdr, .svg, .vsdx |
| Screenshot | Capturas y recortes de pantalla que son utilizados como ejemplo en el desarrollo de la actividad, subtema, clase o lección. | .png              |





### Preguntas y respuestas Q&A

| Pregunta | Respuesta |
|----------|-----------|
|          |           |


> Ayúdame a crear y/o responder preguntas que otros usuarios necesiten conocer desde el [hilo de discusión](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/7) de este microcontenido.
>
> Escribe o comparte en el [hilo de discusión](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/9999) de este microcontenido, que otras dudas, preguntas, contenidos y experiencias tienes relacionadas con desarrollo colaborativo para el enfoque en educación e investigación.


### Referencias

* https://opensource.org/licenses/MIT
* https://pages.github.com/


### Control de versiones

| Versión    | Descripción      | Autor                                      | Horas |
|------------|:-----------------|--------------------------------------------|:-----:|
| 2022.08.18 | Versión inicial. | [rcfdtools](https://github.com/rcfdtools)  |   3   |


_R.TeachingResearchGuide es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.TeachingResearchGuide/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.TeachingResearchGuide/tree/main/Section01/Markdown)  | [:house: Inicio](https://github.com/rcfdtools/R.TeachingResearchGuide/wiki) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/7) | [Siguiente]() |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------|

[^1]: 