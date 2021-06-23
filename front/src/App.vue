<template>
  <div id="app">
    <section class="dashboard">
      <section class="dashboard__summary">
        <valor-total :values="transacoes" :start="range.start" :end="range.end"/>
        <valor-total :values="transacoes" :start="range.start" :end="range.end"/>
        <valor-total :values="transacoes" :start="range.start" :end="range.end"/>
      </section>
      <div class="dashboard__row">
        <grafico-transacoes style="flex:2" :entries="transacoes" />
        <grafico-categoria-transacoes  :entries="transacoes" />
      </div>
      <div class="dashboard__row">
        <tabela-transacoes id="td-grid" :entries="transacoes" />
      </div>

    </section>
  </div>
</template>

<script>
import transacoes from './data/transacoes_teste.js';

import GraficoTransacoes from './components/GraficoTransacoes.vue';
import GraficoCategoriaTransacoes from './components/GraficoCategoriaTransacoes.vue';
import TabelaTransacoes from './components/TabelaTransacoes.vue';
import ValorTotal from './components/ValorTotal.vue';

export default {
  name: 'app',
  components: {

    GraficoTransacoes,
    GraficoCategoriaTransacoes,
    TabelaTransacoes,
    ValorTotal,
  },
  data() {
    return {
      transacoes,
      range: {
        start: new Date(2021, 5, 1), 
        end: new Date(2021, 6, 1) 
      }
    }
  },
  mounted() {
  }
}
</script>

<style>

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 2rem;
  --light-blue: #2196f3;
}

.dashboard {
  width: 100%;
}

.dashboard__summary {
  display: flex;
  justify-content: space-around;
  margin: 0.5rem 0;
}
.scorecard__value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--light-blue);;
}
.scorecard__header {
  margin-top: 0.4rem;
}
.scorecard__subheader {
  font-size: 0.8rem;
}


</style>