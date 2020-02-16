<template>
    <div id="findContainer">
        <b-form
        @submit.prevent="onSubmitDate"
        inline
        >

            <b-form-group
            label="Aloitus pvm: "
            label-for="startDate"
            >
                <b-form-input
                id="startDate"
                required
                type="date"
                v-model="startDate"
                >
                </b-form-input>
            </b-form-group>

            <b-form-group
            label="Lopetus pvm: "
            label-for="endDate"
            >
                <b-form-input
                id="endDate"
                required
                type="date"
                v-model="endDate"
                >
                </b-form-input>
            </b-form-group>
        <b-button type="submit">Hae</b-button>
        </b-form>

        <div id="fullChartContainer">
            <div id="tempChart" ref="tempChart" class="chartContainer"></div>
            <div id="humChart" ref="humChart" class="chartContainer"></div>
            <div id="pressChart" ref="pressChart" class="chartContainer"></div>
        </div>
    </div>
</template>

<script>
var _ = require('lodash');
import Plotly from 'plotly.js/dist/plotly-basic.js';

export default {
    name: 'Find',
    data(){
        return{
            startDate: "",
            endDate: ""
        }
    },
    methods:{
        onSubmitDate: function(){

            let data = JSON.stringify(
                {
                    start: this.startDate,
                    end: this.endDate
                }
            );
            let config = {
                method: 'POST',
                headers: {
                    'content-type':'application/json'
                },
                body: data
            };
            fetch('http://localhost:3000/api/weatherdata', config)
            .then(response => response.json())
            .then(data => {
                // ZERO SERACH RESULTS
                let timedataArr = [];
                let tempdataArr = [];
                let humdataArr = [];
                let pressdataArr = [];

                // setting temperature and time datasets to own arrays while rounding temps to 1 decimal
                for(let i =0; i < data.length; i++)
                {
                    timedataArr.push(data[i].date.substring(0, 10) + ' ' + data[i].time.substring(0, 5));
                    tempdataArr.push(_.round(parseFloat(data[i].temperature), 1));
                    humdataArr.push(_.round(parseFloat(data[i].humidity), 1));
                    pressdataArr.push(_.round(parseFloat(data[i].pressure), 1));
                }


                // calling draw function to draw a line graph from fetched data
                this.drawLineGraph(tempdataArr, timedataArr, "temp", this.$refs.tempChart);
                this.drawLineGraph(humdataArr, timedataArr, "hum", this.$refs.humChart);
                this.drawLineGraph(pressdataArr, timedataArr, "press", this.$refs.pressChart);


                // eslint-disable-next-line no-console
                console.log(tempdataArr);

            })
            .catch(function(error){
                // eslint-disable-next-line no-console
                console.log(error);
            });
        },
        drawLineGraph: function(dataArr, timedataArr, type, chartElement){
            // ZERO SEARCH RESU*LTS
            let graphTitle = {};
            let yaxisTitle = {};

            switch(type){
                case "temp":
                    graphTitle = {
                        text: "Lämpötila"
                    };
                    yaxisTitle = {
                        title: "Lämpötila (&deg;C)"
                    };
                    break;
                case "hum":
                    graphTitle = {
                        text: "Ilmankosteus"
                    };
                    yaxisTitle = {
                        title: "Ilmankosteus (%)"
                    };
                    break;
                case "press":
                    graphTitle = {
                        text: "Ilmanpaine"
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
            Plotly.plot( chartElement,
                data,
                layout,
                configOptions
            );
        }
    },
    computed:{
    }
}
</script>

<style scoped>
.chartContainer{
    width: 33.33%;
    max-height: 300px;
}

#fullChartContainer{
    display: flex;
    flex-direction: row;
}

@media screen and (max-width: 580px){
    .chartContainer{
        width: 100%;
    }

    #fullChartContainer{
        flex-direction: column;
    }
}
</style>