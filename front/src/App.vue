<template>
  <div id="app">
    
    <div class = "container">
      <div class="logo-and-wordmark">
        <div class="logo">
          <img class="logo-img" :src="require('./assets/images/logo.png')"/>
        </div>
        <div class="wordmark">
          <span class="wordmark-text">LOGO</span>
        </div>
      </div>    

      <barra></barra>

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

import Barra from './components/Barra.vue'

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
    Barra,
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
  color: white;
}

.container {
  padding-top: 156px;
}

.logo-and-wordmark {
  justify-content: center;
  margin-bottom: 30px;
  display: flex;
}

.logo {
  display: flex;
  margin-right: 10px;
}

.logo-img {
  align-self: flex-end;
}

.wordmark { 
  align-self: flex-end;
  display: flex;
  justify-content: flex-end;
}

.wordmark-text {
  font-size: 75px;
  line-height: 52px;
  height: 52px;
  font-family: 'Roboto', sans-serif;
  color: white;
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
  color: var(white);;
}
.scorecard__header {
  margin-top: 0.4rem;
}
.scorecard__subheader {
  font-size: 0.8rem;
}


</style>