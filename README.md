<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/LogoE.png"
  align="left"
  width="85"
  height="90"
  alt="TerraWare HV">

<h1> TerraWare HV </h1>
<br/>
<p>Software developed by <a href="http://www.geotem.com.mx" title="Title">
Geotem Ingeniería</a> in Python 3.7.x to compute the spectral ratio (H/V) using seismic noise data and also to compute the inversion of the H/V using the Diffuse Field Assumption. The inversion uses the Particle Swarm Optimization Algorithm (PSO) and an Occam gradient to smooth velocity variations between layers. The results the software provide are the shear and compressional velocity profiles estimated.</p>
<p>The processing of ambient noise vibrations is made with the stacking and the mean of the selected windows considering the diffuse field assumption.</p>
<p>The inversion of the H/V runs an external C++ executable file. The modeler of the H/V phenomena used in the inversion algorithm is the one described in <a href="https://academic.oup.com/gji/article/186/1/221/2102268" title="Title">
Sánchez-Sesma, et al. 2011.</a></p>
<h2>Getting Started</h2>
The code is developed and tested on Windows and Ubuntu using
<a href="https://www.python.org/downloads/release/python-375" title="Title">
Python 3.7.x</a>. You have two options of installation, through the creation of an Anaconda enviroment or using the pip method.
<h4>a) Anaconda enviroment installation</h4>
<p>First we need to create an enviroment in the Anaconda prompt with the following specifications:</p>

```
conda create -n terrawarehv python=3.7 numpy matplotlib=3.2.2 scipy=1.5.0 pandas=1.0.5 pyside2
```

<p>Then we need to activate the enviroment</p>

```
conda activate terrawarehv
```

<h4>b) Pip installation</h4>
<p>In addition to Python and setting it as a Path variable, you need to install the following packages using pip.</p>

```
pip install numpy==1.19.0
pip install matplotlib==3.2.2
pip install scipy==1.5.0
pip install pandas==1.0.5
pip install pyside2==5.15.0
```

<h3>Installation</h3>
<p>Download or clone this repository, then open main.py file. For the anaconda option we need to activate the "terrawarehv" enviroment and run the file in it.</p>

```
python main.py
```
<h2>Running the tests</h2>
<p>Once the main window is opened, load the files in the folder <em>"Ejemplos"</em> with <em>"Load V.A. file"</em> option and double click a sounding to work on it. Then change the parameters and process it.</p>
<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/Captura2.png"
  width="800"
  height="500">
<br/>
<p>The processing parameters are described in the next table:</p>

| Processing Parameters        | Description          |
| ------------- |:-------------:|
|<b>Normalización</b> | Type of normalization in frequencies |
|<b>Window</b> | Type of tappered window |
|<b>Traslape</b>| Overlap percentage|
|<b>Factor de Taper</b>| Taper factor if the window is Tukey type|
|<b>OneBit</b> | Applies a OneBit normalization in time |
|<b>Quitar tendencia</b> | Remove mean trend of the signal |
|<b>Muestreo tiempo</b> | Time sampling rate. Takes the signal default sampling rate|
|<b>Muestreo frecuencia</b> | Frecuency sampling rate for the spectral ratio. |
|<b>Segundos de ventana</b> | Window length in seconds|
|<b>Konno-Ohmachi</b> | Konno-Ohmachi filter factor that goes from 0 to 90, being 90 the raw ratio and 0 the most smoothed ratio.|
|<b>Frecuencias para H/V</b>| Range of frequencies to visualize the spectral ratio|
|<b>Filtro de Butterworth</b>| Cut-off frequencies to apply a Butterworth filter if needed|
|<b>H/V direccionales</b> | Spectral ratio of the N-S and E-W components|
|<b>Espectros</b>| Amplitude spectrum of the raw signal|

<p>To invert the results of the spectral ratio, click on the <em>"Inversion"</em> tab. You also need to modify the parameters on the <em>"Cargar Modelo Inicial"</em> and <em>"Parámetros de Inversión"</em> dialog boxes. Make sure to select the Particle Swarm Optimization as the inversion method. Normally, the default PSO parameters work fine for near surface results.</p>

| PSO Parameters        | Description          |
| ------------- |:-------------:|
|<b>Iteraciones</b> | Number of iterations of the Swarm (external loop)|
|<b>Partículas</b> | Number of elements of the Swarm (internal loop)|
|<b>Factor de inercia inicial</b> | Initial value of the inertia factor, normally ranges between 1 to 2. |
|<b>Amortiguamiento</b> | Damping factor for the inertial term. Normally ranges between 0.5 (higher perturbation of the parameter space) to 0.9999+ (lower perturbation of the parameter space).|
|<b>Coeficiente cognitivo</b> | Cognitive factor, controls the term that depends on the particle trajectory. Ranges between 1-2.|
|<b>Coeficiente social</b> | Social factor, controls the term that depends on the swarm best result. Ranges between 1-2. |
|<b>Factor de Velocidad</b> | Perturbation of the parameter space step factor|
|<b>Gradiente de VP</b> | Poisson ratio gradient factor, the smaller the quantity the less smoothed the resulting Poisson ratio you'll get. |
|<b>Gradiente de VS</b> | Shear velocity gradient factor, the smaller the quantity the less smoothed the resulting VS profile.|
|<b>Gradiente de Densidad</b> | Density gradient factor, the smaller the quantity the less smoothed the resulting density profile.|

<p>The initial model parameters depend on the results you are expecting:</p>
<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/Captura3.png"
  width="800"
  height="500">


| Initial Model Parameters        | Description          |
| ------------- |:-------------:|
|<b>Espesor de la primera capa</b> | Since the thickness of the resulting layers are computed logarithmically we need to provide the first layer thickness in meters|
|<b>Número de capas</b> | Number of expected layers. Suggested ranges are between 8 to 36. Remember that the more layers the algorithm takes more time to compute the results|
|<b>Profundidad</b> | Expected depth of the results|
|<b>Coef. de Poisson mínimo</b> | Minimum value of the Poisson ratio. (Poisson ratio normally ranges between 0.15 to 0.4999+ for geosciences)|
|<b>Coef. de Poisson máximo</b> | Maximum value of the Poisson ratio. (Poisson ratio normally ranges between 0.15 to 0.4999+ for geosciences)|
|<b>VS mínima</b> | Minimum value of the Shear velocity expected. (Shear velocity normally ranges between 100 to 3000 [m/s] for near surface applications)|
|<b>VS máxima</b> | Maximum value of the Shear velocity expected. (Shear velocity normally ranges between 100 to 3000 [m/s] for near surface applications)|
|<b>Densidad mínima</b> | Minimum value of the density expected. (Shear velocity normally ranges between 1000 to 3000 [kg/m3] for near surface applications)|
|<b>Densidad máxima</b> | Minimum value of the density expected. (Shear velocity normally ranges between 1000 to 3000 [kg/m3] for near surface applications|
|<b>Basamento</b> | If selected, forces the last layer to have the maximum value.|

<p>Modify the parameters until you get the results you expect.</p>
<h2>Contributing</h2>
<p>Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.</p>
<h2>Authors</h2>
<ul>
<li> <b>Michelle Sainos Vizuett</b> <em>- Developer</it></em> </li>
<li> <b>Juan Carlos Colchado Casas</b> <em>- Developer</it></em> </li>
<li> <b>Alfredo Sánchez Galindo</b> <em>- Chief Software Manager </it></em> </li>
<li> <b>Francisco José Sánchez Sesma</b> <em>- External Consultant </it></em> </li>
</ul>
