<template>
  <div class="boxContainer" id="mainContainer">

    <header class="boxContainer" id="mainHeaderContainer">
        <h1 class="headers" id="mainHeader">Seunalan sääasema</h1>
    </header>

    <hr>

    <b-table caption-top :items="tempTableItems">
      <template v-slot:table-caption>
        <h4 class="headers" id="tempTableHeader">
          Lämpötila
        </h4>
      </template>
    </b-table>

  </div>
</template>

<script>
export default {
    name: 'MainView',
    props: {
    },
    data(){
      return{
        tempTableItems: [
          {max: "", min: "", current: ""}
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

            // eslint-disable-next-line no-console
            console.log(JSON.stringify(dailydata));
            for(let i =0; i < dailydata.length; i++)
            {
                timedataArr.push(dailydata[i].time.substring(0, 5));
                tempdataArr.push(parseFloat(dailydata[i].temperature).toFixed(1));
            }

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

.headers{
	font-family: 'Poiret One', cursive;
}
#mainContainer{
	max-width: 1200px;
	width: auto;
	margin: auto;
	margin-top: 50px;
}
#mainHeader{
	text-align: center;
	font-size: 110px;
}

#tempTableHeader{
  text-align: center;
  color: black;
  font-weight: bold;
}
</style>