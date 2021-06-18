<template>
  <zing-grid
    ref="myGrid"
    caption="Detalhes das Transações"
    layout="row"
    pager
    page-size="5"
    page-size-options="5,10,20"
    control-bar="false"
    style="width: 100%;"
    height="240px"
    theme="default"
    :data.prop="entries"
  >
    <zg-colgroup>
      <zg-column index="timestamp" header="Data" type="date"></zg-column>
      <zg-column index="descricao" header="Descrição" type="text"></zg-column>
      <zg-column index="valor" header="Valor" type="currency" type-currency="BRL"></zg-column>
      <zg-column index="categoria" header="Categoria" type="text"></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>
export default {
  props: ['entries'],
  mounted() {
  }
}
</script>
<style>

zg-head-cell {
  background: white;
  color: #5d7d9a;
  font-size: 1rem;
}

zg-control-bar {
  display: none;
}
zg-caption {
color: #5d7d9a;
font-family: "Avenir", Helvetica, Arial, sans-serif;
font-weight: bold;
background: white;
padding-left: 0;
font-size: 1.4rem;
height: 54px;
text-align: left;

}
zing-grid {
  border: 0px;
}

zing-grid input[type="text"], zing-grid input[type="number"]{
  border-radius: 5px;
}

</style>