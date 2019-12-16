<template>
    <div class="boxContainer" id="mainContainer">

        <header class="boxContainer" id="mainHeaderContainer">
            <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
        </header>

        <hr>

        <b-table 
        caption-top 
        :items="tempTableItems" 
        :fields="tableFields" 
        :fixed=true
        id="tempTable"
        >
            <template v-slot:table-caption>
                <h4 class="headers" id="tempTableHeader">Lämpötila (&deg;C)</h4>
            </template>
        </b-table>

    </div>
</template>

<script>
var _ = require('lodash');

export default {
    name: 'MainView',
    props: {
    },
    data(){
        return{
            tableFields: [
                {
                    key: "max"
                },
                {
                    key: "min"
                },
                {
                    key: "current"
                }
            ],
            tempTableItems: [
                {
                    max: 0,
                    min: 0,
                    current: 0
                }
            ],
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

                // setting peak and latest values to table variables from daily temp data
                this.tempTableItems[0].max = _.max(tempdataArr);
                this.tempTableItems[0].min = _.min(tempdataArr);
                this.tempTableItems[0].current = tempdataArr[tempdataArr.length - 1];


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

.headers{
	font-family: 'Poiret One', cursive;
}
#mainContainer{
	max-width: 1000px;
	width: auto;
	margin: auto;
}
#mainHeader{
	text-align: center;
}

#tempTableHeader{
  text-align: center;
  color: black;
  font-weight: bold;
}

@media screen and (max-width: 480px){
    #mainHeader{
    }
}
</style>