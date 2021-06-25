<template>
  <div id="app">
    
    <div class = "container">
      <div class="logo-and-wordmark">
        <div class="logo">
          <img :src="require('./assets/images/logo.png')"/>
        </div>
        <div class="wordmark">
          LOGO
        </div>
      </div>    

      <div class = "search-form">

      </div>

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
  display: flex;
  background-color: #5abbbd;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  --light-blue: #2196f3;
}

.container {
  padding-top: 156px;
}

.logo-and-wordmark {
  align-items: center;
  justify-content: center;
  margin-bottom: 48px;
  display: flex;
}

.wordmark { /* TODO: Alinhar texto à parte de baixo da div*/
  font-size: 85px;
  font-family: 'Roboto', sans-serif;
  color: white;
  margin: 10px;
}

.search-form {
  background-color: #fff;
  margin: 0 auto;
  border-radius: 2px;
  position: relative;
  width: 624px;
}

.dashboard {
  padding-bottom: 38px;
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