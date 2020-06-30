<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/LogoE.png"
  align="left"
  width="85"
  height="90"
  alt="TerraWare HV">

<h1> TerraWare HV </h1>
<br/>
<p>Software developed by <a href="https://www.geotem.com.mx" title="Title">
Geotem Ingeniería</a> in Python 3.7.x to compute the spectral ratio (H/V) using seismic noise data and also to compute the inversion of the H/V using the Diffuse Field Assumption. The inversion uses the Particle Swarm Optimization Algorithm and an Occam inversion.</p>
<h2>Getting Started</h2>
The code is developed and tested on Windows and Ubuntu using
<a href="https://www.python.org/downloads/release/python-375" title="Title">
Python 3.7.x</a>
<h3>Prerequisites</h3>
<p>In addition to Python and setting it as a Path variable, you need to install the following packages using pip.</p>

```
pip install numpy==1.19.0
pip install matplotlib==3.2.2
pip install scipy==1.5.0
pip install pandas==1.0.5
pip install pyside2==5.15.0
```

<h3>Installation</h3>
<p>Download or clone this repository, then open main.py file with the python enviroment.</p>
<h2>Running the tests</h2>
<p>Once the main window is opened, load the files in the folder <em>"Ejemplos"</em> with <em>"Load V.A. file"</em> option and double click a sounding to work on it. Then change the parameters and process it.</p>
<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/Captura2.png"
  width="800"
  height="500">
<br/>
<p>The processing parameters are described in the next table:</p>
<p>To invert the results of the spectral ratio, click on the <em>"Inversion"</em> tab. You also need to modify the parameters on the <em>"Cargar Modelo Inicial"</em> and <em>"Parámetros de Inversión"</em> dialog boxes.</p>
<img src="https://github.com/sainosmichelle/TerraWare-HV/blob/master/Logos/Captura3.png"
  width="800"
  height="500">
<br/>
<p>Modify the parameters until you get the results you expect.</p>
<h2>Contributing</h2>
<p>Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.</p>
<h2>Authors</h2>
<ul>
<li> <b>Michelle Sainos Vizuett</b> <em>- Developer</it></em> </li>
<li> <b>Alfredo Sánchez Galindo</b> <em>- Chief Software Engineer </it></em> </li>
<li> <b>Francisco José Sánchez Sesma</b> <em>- External Consultant </it></em> </li>
</ul>
