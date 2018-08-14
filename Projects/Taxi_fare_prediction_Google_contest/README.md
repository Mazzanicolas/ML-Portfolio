# NYC Taxi Fare Prediction

![alt text](http://www.taximac.com.ar/img/relojmuestra.jpg)

## Description

Data analysis for the [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). In this analysis we're only going to use 10,000 rows from the original dataset (~55,000,000 rows).

## Dataset

![alt text](http://i1376.photobucket.com/albums/ah11/mazzanicolas/Screen%20Shot%202018-08-14%20at%2010.20.58%20AM_zpsejfsp9ed.png?t=1534168182)

**fare_amount** - `float` dollar amount of the cost of the taxi ride.

**pickup_datetime**   - `timestamp` value indicating when the taxi ride started.

**pickup_longitude**  - `float` for longitude coordinate of where the taxi ride started.

**pickup_latitude**   - `float` for latitude coordinate of where the taxi ride started.

**dropoff_longitude** - `float` for longitude coordinate of where the taxi ride ended.

**dropoff_latitude**  - `float` for latitude coordinate of where the taxi ride ended.

**passenger_count**   - `integer` indicating the number of passengers in the taxi ride.

## Removing unuseful columns

The **key** (unique identifier) column doesn't have any significant value so we're going to remove it. 

## Transforming data

### Pickup: Longitude, Latitude & Dropoff: Logitude, Latitude to distance

My first idea was to use Manhattan distance ([taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry))

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;d_{1}(\mathbf&space;{p}&space;,\mathbf&space;{q}&space;)=\|\mathbf&space;{p}&space;-\mathbf&space;{q}&space;\|_{1}=\sum&space;_{i=1}^{n}|p_{i}-q_{i}|,}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;d_{1}(\mathbf&space;{p}&space;,\mathbf&space;{q}&space;)=\|\mathbf&space;{p}&space;-\mathbf&space;{q}&space;\|_{1}=\sum&space;_{i=1}^{n}|p_{i}-q_{i}|,}" title="{\displaystyle d_{1}(\mathbf {p} ,\mathbf {q} )=\|\mathbf {p} -\mathbf {q} \|_{1}=\sum _{i=1}^{n}|p_{i}-q_{i}|,}" /></a>

but comparing short distances with long distances it might not be representative.**(expand and explain)**

Then i switch to [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) to get the linear distance in a sphere.

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;2r\arcsin&space;\left({\sqrt&space;{\sin&space;^{2}\left({\frac&space;{\varphi&space;_{2}-\varphi&space;_{1}}{2}}\right)&plus;\cos(\varphi&space;_{1})\cos(\varphi&space;_{2})\sin&space;^{2}\left({\frac&space;{\lambda&space;_{2}-\lambda&space;_{1}}{2}}\right)}}\right)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;2r\arcsin&space;\left({\sqrt&space;{\sin&space;^{2}\left({\frac&space;{\varphi&space;_{2}-\varphi&space;_{1}}{2}}\right)&plus;\cos(\varphi&space;_{1})\cos(\varphi&space;_{2})\sin&space;^{2}\left({\frac&space;{\lambda&space;_{2}-\lambda&space;_{1}}{2}}\right)}}\right)}" title="{\displaystyle 2r\arcsin \left({\sqrt {\sin ^{2}\left({\frac {\varphi _{2}-\varphi _{1}}{2}}\right)+\cos(\varphi _{1})\cos(\varphi _{2})\sin ^{2}\left({\frac {\lambda _{2}-\lambda _{1}}{2}}\right)}}\right)}" /></a>

### Pickup timestamp


## Outlier data

Checking the diferent values for outlier rows.

