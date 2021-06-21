<template>
    <zingchart :data="chartConfig" :theme="theme" :height="'100%'"/>
</template>
<script>
import theme from '../theme/theme.js';

export default {
  props: ['entries'],
  data() {
    return {
      theme,
    };
  },
  computed: {
    values() {
      return this.entries.map(o => {
          return [o.timestamp, parseFloat(o.valor)]
       });
    },
    chartConfig() {
      // TODO: Add a series object
      return {
        type: 'line',
        title: {
          adjustLayout: true,
          align: 'left',
          margin: 0,
          fontColor: '#5d7d9a'
        },
        plot: {
          aspect: 'spline',
          marker: {
            visible: false,
          },

        },
        crosshairX:{
          plotLabel :{
            negation: "currency",
            text: 'R$%v',
            'thousands-separator': ","
          },
          marker: {
            visible: false,
          }
        },
        tooltip: { 
          visible: false,

        },
        plotarea: {
          margin: '35 35 60 60'

        },
        scaleX: {
          transform: {
            type: 'date',
            all: '%M %d',
          }
        },
        scaleY: {
          label: {
            text: 'Valor em Reais',
          },
          short:false,
        },
        series: [
          {
            values: this.values,
            text: 'Sales'
          }
        ],
      };
    }
  },
}
</script>