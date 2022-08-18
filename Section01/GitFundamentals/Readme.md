## Fundamentos de Git
Keywords: `Branch` `Commit` `Pull request` `Pull` `Fork`

Git es un software que permite rastrear y validar cambios en archivos de un proyecto o un repositorio.

<div align="center">
<br><img alt="R.TeachingResearchGuide" src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/Section01/GitFundamentals/Graph/GitFundamentals.svg" width="30%"><br>
</div>


### ¿Qué es Git?[^1]

Hoy en día, Git es, con diferencia, el sistema de control de versiones moderno más utilizado del mundo. Git es un proyecto de código abierto maduro y con un mantenimiento activo que desarrolló originalmente Linus Torvalds, el famoso creador del kernel del sistema operativo Linux, en 2005. Un asombroso número de proyectos de software dependen de Git para el control de versiones, incluidos proyectos comerciales y de código abierto. Los desarrolladores que han trabajado con Git cuentan con una buena representación en la base de talentos disponibles para el desarrollo de software, y este sistema funciona a la perfección en una amplia variedad de sistemas operativos e IDE (entornos de desarrollo integrados).

Git, que presenta una arquitectura distribuida, es un ejemplo de DVCS (sistema de control de versiones distribuido, por sus siglas en inglés). En lugar de tener un único espacio para todo el historial de versiones del software, como sucede de manera habitual en los sistemas de control de versiones antaño populares, como CVS o Subversion (también conocido como SVN), en Git, la copia de trabajo del código de cada desarrollador es también un repositorio que puede albergar el historial completo de todos los cambios.

Además de contar con una arquitectura distribuida, Git se ha diseñado teniendo en cuenta el rendimiento, la seguridad y la flexibilidad.


### Rendimiento[^1]

Las características básicas de rendimiento de Git son muy sólidas en comparación con muchas otras alternativas. La confirmación de nuevos cambios, la ramificación, la fusión y la comparación de versiones anteriores se han optimizado en favor del rendimiento. Los algoritmos implementados en Git aprovechan el profundo conocimiento sobre los atributos comunes de los auténticos árboles de archivos de código fuente, cómo suelen modificarse con el paso del tiempo y cuáles son los patrones de acceso.

A diferencia de algunos programas de software de control de versiones, Git no se deja engañar por los nombres de los archivos a la hora de determinar cuál debería ser el almacenamiento y el historial de versiones del árbol de archivos; en lugar de ello, se centra en el contenido del propio archivo. Al fin y al cabo, los archivos de código fuente se cambian de nombre, se dividen y se reorganizan con frecuencia. El formato de objeto de los archivos del repositorio de Git emplea una combinación de codificación delta (que almacena las diferencias de contenido) y compresión, y guarda explícitamente el contenido de los directorios y los objetos de metadatos de las versiones.

Su arquitectura distribuida también permite disfrutar de importantes ventajas en términos de rendimiento.


### Seguridad[^1]

Git se ha diseñado con la principal prioridad de conservar la integridad del código fuente gestionado. El contenido de los archivos y las verdaderas relaciones entre estos y los directorios, las versiones, las etiquetas y las confirmaciones, todos ellos objetos del repositorio de Git, están protegidos con un algoritmo de hash criptográficamente seguro llamado "SHA1". De este modo, se salvaguarda el código y el historial de cambios frente a las modificaciones accidentales y maliciosas, y se garantiza que el historial sea totalmente trazable.

Con Git, puedes tener la certeza de contar con un auténtico historial de contenido de tu código fuente.

Algunos otros sistemas de control de versiones carecen de protección contra las modificaciones ocultas realizadas con posterioridad, algo que puede suponer una grave vulnerabilidad de seguridad de la información para cualquier organización que se base en el desarrollo de software.


### Flexibilidad[^1]

Uno de los objetivos clave de Git en cuanto al diseño es la flexibilidad. Git es flexible en varios aspectos: en la capacidad para varios tipos de flujos de trabajo de desarrollo no lineal, en su eficiencia en proyectos tanto grandes como pequeños y en su compatibilidad con numerosos sistemas y protocolos.

Git se ha ideado para posibilitar la ramificación y el etiquetado como procesos de primera importancia (a diferencia de SVN) y las operaciones que afectan a las ramas y las etiquetas (como la fusión o la reversión) también se almacenan en el historial de cambios. No todos los sistemas de control de versiones ofrecen este nivel de seguimiento.


### Recursos para aprendizaje Git

* [Atlassian Bitbucket - Aprende Git](https://www.atlassian.com/es/git/tutorials/what-is-git): guía fundamental de Git.
* [freeCodeCamp - Git and GitHub Crash Course](https://www.freecodecamp.org/news/git-and-github-crash-course/): curso en video de conceptos generales de Git.
* [freeCodeCamp - Git for Professionals Tutorial - Tools & Concepts for Mastering Version Control with Git](https://www.youtube.com/watch?v=Uszj_k0DGsg): curso en video con herramientas y conceptos de Git.
* [edureka! - Git & GitHub Full Course in 5 Hours | Git GitHub Tutorial for Beginners | DevOps Training | Edureka](https://www.youtube.com/watch?v=KMOmw19ZCGs): curso completo de Git y Github para principantes.


### Ciclo de vida de repositorios en GitHub

Conceptos generales de Branch, Commit, Pull request, Pull, Fork.



### Preguntas y respuestas Q&A

| Pregunta                                                                                                              | Respuesta |
|-----------------------------------------------------------------------------------------------------------------------|-----------|
| ¿Para crear mi repositorio en GitHub requiero de conocimientos de programación?                                       |           |
| ¿Existen herramientas que realicen automáticamente la gestión de mis repositorios usando las funcionalidades de Git ? |           |

> Ayúdame a responder estas preguntas desde el [hilo de discusión](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/9999) de este microcontenido.
>
> Escribe o comparte en el [hilo de discusión](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/99999) de este microcontenido, que otras dudas, preguntas, contenidos y experiencias tienes relacionadas con desarrollo colaborativo para el enfoque en educación e investigación.


### Referencias

* https://www.atlassian.com/es/git/tutorials/what-is-git


### Control de versiones

| Versión    | Descripción         | Autor                                      | Horas |
|------------|:--------------------|--------------------------------------------|:-----:|
| 2022.08.13 | Versión preliminar. | [rcfdtools](https://github.com/rcfdtools)  |  1.5  |


_R.TeachingResearchGuide es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.TeachingResearchGuide/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.TeachingResearchGuide/tree/main/Section01/CollabTools) | [:house: Inicio](https://github.com/rcfdtools/R.TeachingResearchGuide/wiki) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/9999) | [Siguiente]() |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

[^1]: https://www.atlassian.com/es/git/tutorials/what-is-git