<template>
   <zingchart :data="chartConfig"  :height="'100%'"/> 
</template>

<script>
export default {
  props: ['entries'],
  data() {
    return {
    };
  },
  computed: {
    acquisitionBreakdown() {
      const categories = this.entries.reduce((acc, transaction) => {
        if (transaction.categoria in acc){
          // arrumar isto
          // funcionando errado
          acc[transaction.categoria] ++
        }
        else {
          acc[transaction.categoria] = transaction.valor;
        }

        return acc;
      }, {});
      return categories;
    },
    chartConfig() {
      const colors = [
        {
          backgroundColor: '#04A3F5',
          hoverState: {
            backgroundColor: '#45D6C4'
          }
        },
        {
          backgroundColor: '#98D1EE',
          hoverState: {
            backgroundColor: '#45D6C4'
          }
        },
                {
          backgroundColor: '#295A73',
          hoverState: {
            backgroundColor: '#45D6C4'
          }
        },
      ]
      const config ={
        type: 'pie',
        tooltip: {
          text: '%npv%'
        },
        plotarea: {
          margin: '5'
        },
        plot: {
          valueBox: {
            fontSize: 10,
            text: '%t'
          },
          hoverState: {
         	  borderWidth: 2,
          }
        },
        series: Object.keys(this.acquisitionBreakdown).map((type, index) => {
          return Object.assign(
            { values: [this.acquisitionBreakdown[type]], text: type},
            colors[index],
          );
        })
      };
      return config;
    },
  }
}
</script>