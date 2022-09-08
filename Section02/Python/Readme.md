## Proyectos GitHub que requieren Python
Keywords: `Python` `requirements` `GitHub`

Python es un potente lenguaje de programación interpretado con licencia de código abierto que soporta orientación a objetos y es comúnmente utilizado en el desarrollo de proyectos e investigación en ingeniería.

<div align="center">
<br><img alt="R.TeachingResearchGuide" src="Graph/Python.svg" width="50%"><br><br>
</div>


### Objetivos

* Instalar y configurar Python.
* Crear entornos virtuales en Python.
* Crear el archivo de requerimientos para la instalación de librerías.
* Ejecutar scripts en Python y generar archivos Markdown.


### Requerimientos

* Cuenta y repositorio [GitHub](https://github.com/). [:mortar_board:Aprender.](../../Section01/GitHubRepository)
* [PyCharm Community](https://www.jetbrains.com/pycharm/) instalado y configurado con repositorio clonado localmente. [:mortar_board:Aprender.](../Setup) 
* [Python 3.10](https://www.python.org/downloads/) o superior.


### Archivo de requerimientos Python

Existen diferentes alternativas para la instalación de librerías asociadas a un proyecto desarrollado en Python, desde instalar manualmente las librerías desde consola a través de gestores de paquetes o módulos como `pip`, instalación asistida desde entornos de desarrollo integrados (IDE) o a través de la creación del archivo de texto `requirements.txt`.

> Es recomendable crear el archivo de requerimientos en la raíz del repositorio antes de la asociación y creación del entorno virtual de Python. Esto permitirá que Python identifique los módulos o las librerías requeridas para el proyecto y permitirá realizar la instalación automática. 

1. En PyCharm Community, cree el archivo `requirements.txt` en la raíz del repositorio. Para ello, diríjase a la pestaña Proyect, de clic derecho en la raíz del repositorio `repotest`, seleccione la opción _New / File_

![R.TeachingResearchGuide](Screenshot/PyCharmNewFile.png)

2. Ingrese el nombre `requirements.txt` y de teclee <kbd>Enter</kbd>. Automáticamente se abre el archivo para su edición.

![R.TeachingResearchGuide](Screenshot/PyCharmNewFileEnter.png)

3. En la parte superior de la ventana podrá observar que aparecen dos mensajes indicando que el archivo de requerimientos se encuentra vacío y que para el procesamiento del archivo se requiere de un Plugin. De clic en el enlace _Install Plugins_.

![R.TeachingResearchGuide](Screenshot/PyCharmNewFileRequirementAlert.png)

Active la casilla de selección del plugin Requirements y de clic en el botón `Ok`

![R.TeachingResearchGuide](Screenshot/PyCharmRequirementPlugin.png)

De clic en el botón `Accept` en la ventana emergente que indica que este plugin ha sido desarrollado por un tercero y no directamente los por creadores de PyCharm.

![R.TeachingResearchGuide](Screenshot/PyCharmRequirementPluginAccept.png)

Para verificar la correcta instalación del Plugin, en el menu _File_, seleccione la opción _Settings_ u oprima la combinación de teclas <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>S</kbd>. En la pestaña Plugins, verifique que se encuentre instalado y activado _Requirements_.

![R.TeachingResearchGuide](Screenshot/PyCharmPlugins.png)

4. En el archivo de requerimiento, ingrese los nombre de las librerías requeridas, p. ej.: 

```
numpy
scipy
pandas
matplotlib
seaborn
```

![R.TeachingResearchGuide](Screenshot/PyCharmRequirementModules.png)

Al ingresar las librerías requerías, podrá observar que `seaborn` ha sido resaltado en color rojo indicando que no existe en la versión actual de Python instalada en el equipo. 

> Por defecto, cuando se clona localmente con PyCharm un repositorio de GitHub, se asocia el intérprete de Python instalado y registrado en el sistema operativo.

Al dar clic en el ícono rojo de alertas localizado en la parte superior derecha de la venta de edición del archivo de requerimientos, podrá visualizar en detalle la descripción de las librerías, si existen o no y si se encuentran actualizadas.

![R.TeachingResearchGuide](Screenshot/PyCharmRequirementModulesAlert.png)

> Debido a que realizaremos la instalación de una nueva versión de Python, no es necesario por ahora, verificar las versiones disponibles de las librerías encontradas en el entorno de Python sí este ya se encuentra instalado.


### Instalación personalizada de Python sobre Windows

1. Ingrese a www.python.org, de clic en _Downloads_ y seleccione la opción _Windows_ o seleccione su sistema operativo actual. Luego de clic en el botón de descarga, p. ej., `Python 3.10.7`

![R.TeachingResearchGuide](Screenshot/PythonDownload.png)

2. Desde la carpeta _Descargas_ de su equipo, de clic derecho sobre el instalador de Python descargado, seleccione la opción _Ejecutar como administrador._  

![R.TeachingResearchGuide](Screenshot/PythonInstallRunAsAdmin.png)

3. En la ventana de instalación, marque las casillas _Install launcher for all users_ y _Add Python 3.10 to PATH_ seleccione _Customize Installation_ para personalizar las opciones de instalación.

![R.TeachingResearchGuide](Screenshot/PythonInstallCustomize.png)

> _Install launcher for all users_ permitirá que cualquier usuario local ejecute la versión de Python instalada y _Add Python 3.10 to PATH_ creará la asociación de Python en las variables del sistema que facilitará su ejecución desde consola.

4. En Optional Features, marque todas las casillas disponibles para incluir: Documentación, gestor de paquetes, las opciones de creación de interfases gráficas con [tkinter](https://docs.python.org/3/library/tk.html), las librerías de prueba y el lanzador automático de scripts .py.

![R.TeachingResearchGuide](Screenshot/PythonInstallCustomizeOptionaFeatures.png)

5. En la ventana de opciones avanzadas, modifique la ruta de instalación de su usuario local, p. ej., `C:\Users\R\AppData\Local\Programs\Python\Python310` a `C:\Python310` y marque las casillas disponibles. Para finalizar, de clic en el botón `Install`.

![R.TeachingResearchGuide](Screenshot/PythonInstallCustomizeAdvanced.png)

En la ventana final, de clic en la opción _Disable path length limit_ que le permitirá utilizar rutas con más de 260 caracteres.

![R.TeachingResearchGuide](Screenshot/PythonInstallSuccessful.png)


### Verificación de Python por consola CMD de Windows

1. En Windows, oprima las teclas <kbd>Windows</kbd>+<kbd>R</kbd> para acceder a la ventana de ejecución. Ingrese el comando `cmd` y teclee <kbd>Enter</kbd> para acceder a la consola de comandos.

![R.TeachingResearchGuide](Screenshot/WindowsCMD.png)

2. En la consola, ingrese el comando `Python --version` y verifique que la versión instalada corresponde a la versión descargada. Para el ejemplo, corresponde a la versión 3.10.7.

![R.TeachingResearchGuide](Screenshot/WindowsCMDPtthonVersion.png)

> En el evento de que la versión devuelta no corresponda a la versión de Python instaladas, ingresar el comando `cd c:\Python310` y luego el comando `Python --version`.

![R.TeachingResearchGuide](Screenshot/WindowsCMDPtthonVersion1.png)


### Asociación local de Python en PyCharm Community

1. 






### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias a ser desarrolladas por el estudiante.

|  #  | Alcance |
|:---:|:--------|
|  1  | xxxx    |


### Preguntas y respuestas Q&A

| Pregunta | Respuesta |
|----------|-----------|
|          |           |

> Ayúdame desde este [hilo de discusión](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/9999) a crear y/o responder preguntas que otros usuarios necesiten conocer o experiencias relacionadas con esta actividad.


### Referencias

* https://www.python.org/
* 


### Control de versiones

| Versión    | Descripción      | Autor                                      | Horas |
|------------|:-----------------|--------------------------------------------|:-----:|
| 2022.08.22 | Versión inicial. | [rcfdtools](https://github.com/rcfdtools)  |  XX   |


_R.TeachingResearchGuide es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](../../LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](../GitHubRepository) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.TeachingResearchGuide/discussions/9999) | [Siguiente]() |
|---------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------|

[^1]: 