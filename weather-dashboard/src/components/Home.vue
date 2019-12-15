<template>
  <div class="boxContainer" id="mainContainer">

    <header class="boxContainer" id="mainHeaderContainer">
        <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
    </header>

    <hr>

    <b-table></b-table>

  </div>
</template>

<script>
export default {
    name: 'MainView',
    props: {
    },
    data(){
      return{
        
        
        maxValues:{
          temp: 0
        },
        minValues:{
          temp: 0
        },
        currentValues:{
          temp: 0
        }
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

              // eslint-disable-next-line no-console
              console.log(JSON.stringify(dailydata));
              for(let i =0; i < dailydata.length; i++)
              {
                  timedataArr.push(dailydata[i].time.substring(0, 5));
                  tempdataArr.push(parseFloat(dailydata[i].temperature).toFixed(1));
              }
            
            this.maxValues.temp = Math.max(tempdataArr);

            }).catch(function(error){
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
	margin-top: 150px;
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