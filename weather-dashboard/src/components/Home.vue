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
                :small="small"
                id="tempTable"
                >
                    <template v-slot:table-caption>
                        <h4 class="headers tableHeaders">Ilmanpaine</h4>
                    </template>
                </b-table>
            </div>
        </div>

        <div id="fullchartContainer">
            
        </div>

    </div>
</template>

<script>

var _ = require('lodash');

export default {
    name: 'MainView',
    components: {
    },
    props: {
    },
    data(){
        return{
            // misc
            subHeader: "",

            // table data
            fixed: true,
            small: true,
            tableFields: [
                { key: "max" },
                { key: "min" },
                { key: "latest" }
            ],
            tempTableItems: [
                { max: 0, min: 0, latest: 0 }
            ],
            humTableItems: [
                { max: 0, min: 0, latest: 0 }
            ],
            pressTableItems: [
                { max: 0, min: 0, latest: 0 }
            ],

            // chart data
            tempChartOption:{}

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
                this.tempTableItems[0].latest = tempdataArr[tempdataArr.length - 1];

                // config options for temperature chart
               
               
                // eslint-disable-next-line no-console
                console.log(tempdataArr);

            })
            .catch(function(error){
                // eslint-disable-next-line no-console
                console.log(error);
            });

        },
        buildSubHeader: function(){
            let subStr = new Date().toLocaleDateString();

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
	font-family: 'Poiret One', cursive;
    margin: 0;
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

#dailyTempChart{
    width: 33.33%;
    max-height: 300px;
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