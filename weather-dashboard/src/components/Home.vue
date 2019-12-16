<template>
    <div class="boxContainer" id="mainContainer">

        <header class="boxContainer" id="mainHeaderContainer">
            <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
        </header>

        <hr>

        <div id="fullTableContainer">
            <div id="tempTableContainer" class="boxContainer tableContainer">
                <b-table 
                caption-top 
                :items="tempTableItems" 
                :fields="tableFields" 
                :fixed="fixed"
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
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders">Ilman suht. kosteus</h4>
                    </template>
                </b-table>
            </div>

            <div id="pressTableContainer" class="boxContainer tableContainer">
                <b-table 
                caption-top 
                :items="pressTableItems"
                :fields="tableFields" 
                :fixed="fixed"
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders">Ilmanpaine</h4>
                    </template>
                </b-table>
            </div>
        </div>

        <div id="fullchartContainer">
            <v-chart :options="tempChartOption" id="dailyTempChart"/>
        </div>

    </div>
</template>

<script>

import ECharts from 'vue-echarts';
import 'echarts/lib/chart/line';

var _ = require('lodash');

export default {
    name: 'MainView',
    components: {
        "v-chart": ECharts
    },
    props: {
    },
    data(){
        return{
            fixed: true,
            tableFields: [
                { key: "max" },
                { key: "min" },
                { key: "current" }
            ],
            tempTableItems: [
                { max: 0, min: 0, current: 0 }
            ],
            humTableItems: [
                { max: 0, min: 0, current: 0 }
            ],
            pressTableItems: [
                { max: 0, min: 0, current: 0 }
            ],
            tempChartOption:{}

        }
    },
    mounted(){
        this.init();
    },
    methods:{
        init: function(){
            fetch('http://localhost:3000/api/dailydata')
            .then(response => response.json())
            .then(dailydata => {
                let timedataArr = [];
                let tempdataArr = [];

                // setting temperature and time datasets to own arrays while rounding temps to 1 decimal
                for(let i =0; i < dailydata.length; i++)
                {
                    timedataArr.push(dailydata[i].time.substring(0, 5));
                    tempdataArr.push(_.round(parseFloat(dailydata[i].temperature), 1));
                }
                // setting data sets to chart data arrays


                // setting peak and latest values to table variables from daily temp data
                this.tempTableItems[0].max = _.max(tempdataArr);
                this.tempTableItems[0].min = _.min(tempdataArr);
                this.tempTableItems[0].current = tempdataArr[tempdataArr.length - 1];

                // config options for temperature chart
                this.tempChartOption = {
                    xAxis: {
                        type: 'category',
                        data: timedataArr
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: tempdataArr,
                        type: 'line'
                    }]
                }
                // eslint-disable-next-line no-console
                console.log(tempdataArr);

            })
            .catch(function(error){
                // eslint-disable-next-line no-console
                console.log(error);
            });

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
	font-family: 'Poiret One', cursive;
}

.tableHeaders{
    text-align: center;
    color: black;
    font-weight: bold;
}

.tableContainer{
    width: 33.33%;
}

#mainContainer{
	max-width: 1200px;
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

#dailyTempChart{
    width: 33.33%;
}

@media screen and (max-width: 580px){
    .tableContainer{
        width: 100%;
    }

    #fullTableContainer{
        flex-direction: column;
    }
}
</style>