<template>
    <div class="boxContainer" id="mainContainer">

        <header class="boxContainer" id="mainHeaderContainer">
            <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
        </header>

        <hr>

        <header class="boxContainer" id="subHeaderContainer">
            <h4 class="headers" id="subHeader">{{subHeader}}</h4>
        </header>

        <div id="fullTableContainer">
            <div id="tempTableContainer" class="boxContainer tableContainer">
                <b-table 
                caption-top 
                :items="tempTableItems" 
                :fields="tableFields" 
                :fixed="fixed"
                :small="small"
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders" id="tempTableHeader">Lämpötila (&deg;C)</h4>
                    </template>
                </b-table>
            </div>

            <div id="humTableContainer" class="boxContainer tableContainer">
                <b-table 
                caption-top  
                :items="humTableItems"
                :fields="tableFields" 
                :fixed="fixed"
                :small="small"
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders">Ilman kosteus (%)</h4>
                    </template>
                </b-table>
            </div>

            <div id="pressTableContainer" class="boxContainer tableContainer">
                <b-table 
                caption-top 
                :items="pressTableItems"
                :fields="tableFields" 
                :fixed="fixed"
                :small="small"
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders">Ilmanpaine</h4>
                    </template>
                </b-table>
            </div>
        </div>

        <div id="fullChartContainer">
            <div id="dailyTempChart" ref="dailyTempChart" class="chartContainer"></div>
            <div id="dailyHumChart" ref="dailyHumChart" class="chartContainer"></div>
            <div id="dailyPressChart" ref="dailyPressChart" class="chartContainer"></div>
        </div>

    </div>
</template>

<script>

var _ = require('lodash');
// var Plotly = require('plotly.js');
import Plotly from 'plotly.js/dist/plotly-basic.js';

export default {
    name: 'MainView',
    components: {
    },
    props: {
    },
    data(){
        return{
            // subheader for denoting the date
            subHeader: "",

            // table data
            fixed: true,
            small: true,
            tableFields: [
                { key: "max" },
                { key: "min" },
                { key: "viim" }
            ],
            tempTableItems: [
                { max: 0, min: 0, viim: 0 }
            ],
            humTableItems: [
                { max: 0, min: 0, viim: 0 }
            ],
            pressTableItems: [
                { max: 0, min: 0, viim: 0 }
            ],
        }
    },
    mounted(){
        this.buildSubHeader();
        this.fetchDailyData();
    },
    methods:{
        fetchDailyData: function(){
            fetch('http://localhost:3000/api/dailydata')
            .then(response => response.json())
            .then(dailydata => {
                let timedataArr = [];
                let tempdataArr = [];
                let humdataArr = [];
                let pressdataArr = [];

                // setting temperature and time datasets to own arrays while rounding temps to 1 decimal
                for(let i =0; i < dailydata.length; i++)
                {
                    timedataArr.push(dailydata[i].time.substring(0, 5));
                    tempdataArr.push(_.round(parseFloat(dailydata[i].temperature), 1));
                    humdataArr.push(_.round(parseFloat(dailydata[i].humidity), 1));
                    pressdataArr.push(_.round(parseFloat(dailydata[i].pressure), 1));
                }

                // setting peak and latest values to table variables from daily temp data
                this.tempTableItems[0].max = _.max(tempdataArr);
                this.tempTableItems[0].min = _.min(tempdataArr);
                this.tempTableItems[0].viim = tempdataArr[tempdataArr.length - 1];

                this.humTableItems[0].max = _.max(humdataArr);
                this.humTableItems[0].min = _.min(humdataArr);
                this.humTableItems[0].viim = humdataArr[humdataArr.length - 1];

                this.pressTableItems[0].max = _.max(pressdataArr);
                this.pressTableItems[0].min = _.min(pressdataArr);
                this.pressTableItems[0].viim = pressdataArr[pressdataArr.length - 1];

                // calling draw function to draw a line graph from fetched data
                this.drawLineGraph(tempdataArr, timedataArr, "temp", this.$refs.dailyTempChart);
                this.drawLineGraph(humdataArr, timedataArr, "hum", this.$refs.dailyHumChart);
                this.drawLineGraph(pressdataArr, timedataArr, "press", this.$refs.dailyPressChart);


                // eslint-disable-next-line no-console
                console.log(tempdataArr);

            })
            .catch(function(error){
                // eslint-disable-next-line no-console
                console.log(error);
            });

        },
        /**
         * function to draw a line graph from fetched data with plotly.js library
         */
        drawLineGraph: function(dataArr, timedataArr, type, chartElement){

            let graphTitle = {};
            let yaxisTitle = {};

            switch(type){
                case "temp":
                    graphTitle = {
                        text: "Vuorokauden lämpötila"
                    };
                    yaxisTitle = {
                        title: "Lämpötila (&deg;C)"
                    };
                    break;
                case "hum":
                    graphTitle = {
                        text: "Vuorokauden ilmankosteus"
                    };
                    yaxisTitle = {
                        title: "Ilmankosteus (%)"
                    };
                    break;
                case "press":
                    graphTitle = {
                        text: "Vuorokauden ilmanpaine"
                    };
                    yaxisTitle = {
                        title: "Ilmanpaine (mbar)"
                    };
                    break;
            }

            // temperature chart data options
            let data = [{
                x: timedataArr,
                y: dataArr
                }];
            // chart layout options
            let layout = {
                title: graphTitle,
                xaxis:{ title: "Kellonaika"},
                yaxis: yaxisTitle,
                margin: {
                    t: 25,
                    l: 35,
                    b: 60,
                    r: 10
                    }
                };
            // config options for chart
            let configOptions = {
                displayModeBar: false,
                responsive: true
            };

            // drawing a graph according to the config options
            Plotly.newPlot( chartElement,
                data,
                layout,
                configOptions
            );
        },
        /**
         * function for making a subheader for each day
         */
        buildSubHeader: function(){
            let subStr = new Date().toLocaleDateString("fi-FI");
            this.subHeader = "Vuorokauden " + subStr + " säätiedot";
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

.headers{
	/*font-family: 'Poiret One', cursive;*/
    margin: 0;
}

.tableHeaders{
    text-align: center;
    color: black;
}

.tableContainer{
    width: 33.33%;
}

.chartContainer{
    width: 33.33%;
    max-height: 300px;
}

#mainContainer{
	/*max-width: 1200px;*/
	width: auto;
	margin: auto;
}
#mainHeader{
	text-align: center;
}

#fullTableContainer{
    display: flex;
    flex-direction: row;
}

#fullChartContainer{
    display: flex;
    flex-direction: row;
}


@media screen and (max-width: 580px){
    .tableContainer{
        width: 100%;
    }

    .chartContainer{
        width: 100%;
    }

    #fullTableContainer{
        flex-direction: column;
    }
    
    #fullChartContainer{
        flex-direction: column;
    }
}
</style>