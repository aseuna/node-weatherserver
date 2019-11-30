<template>
  <div class="boxContainer" id="mainContainer">

    <header class="boxContainer" id="mainHeaderContainer">
        <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
    </header>

    <hr>

    <div class="boxContainer" id="tableContainer">
      <!-- tableContainer starts -->
      <table class="dailyInfoTable" id="dailyInfoTemp">
        <caption>
          <h2 class="headers infoHeaders" id="tempHeader">Lämpötila</h2>
        </caption>
        <tbody>
          <tr>
            <th>Viim</th>
            <th>Max</th>
            <th>Min</th>
          </tr>
          <tr>
            <td id="currentTemp"></td>
            <td id="maxTemp"></td>
            <td id="minTemp"></td>
          </tr>
        </tbody>
      </table>

      <table class="dailyInfoTable" id="dailyInfoHum">
        <caption>
          <h2 class="headers infoHeaders" id="humHeader">Ilmankosteus</h2>
        </caption>
        <tbody>
          <tr>
            <th>Viim</th>
            <th>Max</th>
            <th>Min</th>
          </tr>
          <tr>
            <td id="currentHum">27</td>
            <td id="maxHum">35</td>
            <td id="minHum">26</td>
          </tr>
        </tbody>
      </table>

      <table class="dailyInfoTable" id="dailyInfoPress">
        <caption>
          <h2 class="headers infoHeaders" id="pressHeader">Ilmanpaine</h2>
        </caption>
        <tbody>
          <tr>
            <th>Viim</th>
            <th>Max</th>
            <th>Min</th>
          </tr>
          <tr>
            <td id="currentPress">1,024</td>
            <td id="maxPress">1,026</td>
            <td id="minPress">1,013</td>
          </tr>
        </tbody>
      </table>
      <!-- tableContainer ends -->
    </div>

    <div class="boxContainer" id="plotContainer">
        <div class="plot" id="plotlydailyTempChart"></div>
        <div class="plot" id="plotlydailyHumChart"></div>
        <div class="plot" id="plotlydailyPressChart"></div>
    </div>
  </div>
</template>

<script>

export default {
    name: 'MainView',
    props: {
    },
    methods:{
        onLoad: function(){

            /*fetch('getdailyvalues.php').then(function(response) {
                return response.json();
            }).then(function(data) {
                console.log(JSON.stringify(data));

                let current = document.getElementById("currentTemp");
                current.innerHTML = parseFloat(data.current.temperature).toFixed(1) + "&deg;";

                let max= document.getElementById("maxTemp");
                max.innerHTML = parseFloat(data.max.temperature).toFixed(1) + "&deg;";

                let min = document.getElementById("minTemp");
                min.innerHTML = parseFloat(data.min.temperature).toFixed(1) + "&deg;";

            }).catch(function(error) {
                console.error(error);
            });*/

            /*fetch('getdailydata.php').then(function(response){
                return response.json();
            }).then(function(dailydata){
                let timedataArr = [];

                let temperaturedataArr = [];
                console.log(JSON.stringify(dailydata));

                for(let i =0; i < dailydata.length; i++)
                {
                    timedataArr.push(dailydata[i].time.substring(0, 5));
                    temperaturedataArr.push(parseFloat(dailydata[i].temperature).toFixed(1));
                }

                let tempData = [{
                    x: timedataArr,
                    y: temperaturedataArr
                    }];
                let tempLayout = {
                    title: { text: "Vuorokauden lämpötila" },
                    xaxis:{ title: "Kellonaika"},
                    yaxis: { title: "Lämpötila"},
                    margin: {
                        t: 25,
                        l: 35,
                        b: 60,
                        r: 0
                        }
                    };
                let plotlyTempConfigOptions = {
                    displayModeBar: false,
                    responsive: true
                };

                DAILYTEMPCHART = document.getElementById('plotlydailyTempChart');

                Plotly.plot( DAILYTEMPCHART,
                    tempData,
                    tempLayout,
                    plotlyTempConfigOptions
                );
            }).catch(function(error){
                console.log(error);
            });*/

        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
	margin: 0;
	padding: 0;
	border: none;
	font-family: 'Arial', 'Helvetica','sans-serif';
}

p {
	font-size: 40px;
	margin: 20px;
}

hr{
	color: black;
	border: solid;
	border-style: inset;
	border-width: 2px;
}

th, td{
	font-family: 'Quicksand', sans-serif;
}

th{
	border: none;
	height: 60px;
	width: 60px;
	text-align: center;
}

td{
	border: none;
	height: 60px;
	width: 60px;
	text-align: center;

}

.headers{
	font-family: 'Poiret One', cursive;
}

.dailyInfoTable{
}

.plot{
	width: 33.3333333333%;
}

#mainContainer{
	max-width: 1200px;
	width: auto;
	margin: auto;
	margin-top: 200px;
}

#mainHeader{
	text-align: center;
	font-size: 110px;
}

#tableContainer{
	display: flex;
	justify-content: space-around;
}

#plotContainer{
	display: flex;
	height: 300px;
}

#plotlyYearTempChart{
	width: inherit;
	height: inherit;
}
</style>
