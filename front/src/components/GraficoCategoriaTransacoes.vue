<template>
   <zingchart :data="chartConfig" :theme="theme" :height="'100%'"/> 
</template>

<script>
import theme from '../theme/theme.js';

export default {
  props: ['entries'],
  data() {
    return {
    theme
    };
  },
  computed: {
    acquisitionBreakdown() {
      const categories = this.entries.reduce((acc, transaction) => {
        if (transaction.categoria in acc){
          acc[transaction.categoria] += parseFloat(transaction.valor);
        }
        else {
          acc[transaction.categoria] = parseFloat(transaction.valor);
        }

        return acc;
      }, {});
      return categories;
    },
    chartConfig() {
      const colors = [
        {
          backgroundColor: '#0080ab',
          hoverState: {
            backgroundColor: '#0080ab'
          }
        },
        {
          backgroundColor: '#00afd3',
          hoverState: {
            backgroundColor: '#00afd3'
          }
        },
        {
          backgroundColor: '#25c3ff',
          hoverState: {
            backgroundColor: '#25c3ff'
          }
        },
        {
          backgroundColor: '#099ad9',
          hoverState: {
            backgroundColor: '#099ad9'
          }
        },
        {
          backgroundColor: '#0080ab',
          hoverState: {
            backgroundColor: '#0080ab'
          }
        },
        {
          backgroundColor: '#00afd3',
          hoverState: {
            backgroundColor: '#00afd3'
          }
        },
        {
          backgroundColor: '#25c3ff',
          hoverState: {
            backgroundColor: '#25c3ff'
          }
        },
        {
          backgroundColor: '#099ad9',
          hoverState: {
            backgroundColor: '#099ad9'
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
          },
          animation: {
            effect: 3,
            speed: 1,
            method: 4,
            sequence: 2,
          },
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