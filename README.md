***TP1 Engenharia de Software***

**Grupo**:
- Ester Fiorillo
- Mateus Braga
- Pedro Wildemberg
- André Godoy

**Escopo**:
- Monitorador de gastos

**Requisitos funcionais**:
- Visualizar transações em gráficos por categorias (semana, mes, etc)
- projeções de gastos
- input de transações manualmente e por csv
- permitir mais de um usuário

**Tecnologia**:
- Front-end: Vue
- Back-end: Flask
- Banco de dados: SQLite
- Controle de versão: Git

**Histórias de usuários**:
- Como usuário, gostaria de criar uma conta (1);
- Como usuário, gostaria de salvar minhas transações (2);
  - Como usuário, gostaria de salvar minhas transações em formato csv
  - Como usuário, gostaria de salvar minhas transações manualmente
- Como usuário, gostaria de editar/apagar transações passadas (3);
- Como usuário, gostaria de visualizar minhas transações (4);
- Como usuário, gostaria de visualizar minhas transações em uma janela de tempo (visualizar ou por semana, ou por mês ou por ano) (5);
- Como usuário, gostaria de visualizar projeções das minhas finanças (6);
- Como usuário, gostaria de poder separar minhas transações em categorias (2,4);
- Como usuário, gostaria de criar um grupo de gastos com outros usuários (7).

**Backlog do Sprint**:

(2):

    Definir arquitetura do sistema (como integrar partes) (todos)
    Criar interface de salvar transação  (Pedro e André)
    Criar banco de dados com tabelas especificando as transações (Ester)
    Criar integração do banco dados com a interface (camada de acesso a dados) (Ester)
    Popular banco de dados com as transações (Ester)
    Tratar e filtrar os dados (Mateus)

(4):

    Definir  tipo de visualização de dados (André, Pedro)
    Implementar visualização por gráfico (Pedro)
    Implementar visualização por tabela (André)
    Integrar banco de dados com as transações ao gráfico de visualização de dados (Pedro e Mateus)
    Fazer queries para obter as transações a serem visualizadas (Ester)
    Testar se dados do banco estão consistentes com o gráfico (Mateus)
    
(3):

    Implementar interface de apagar (Pedro e André)
    Integrar front end com banco de dados com a transação a ser editada (Mateus)
    Fazer querie de edição do banco de dados (Ester)

(5):

    Definir e implementar interface para variar o tipo de visualização (Pedro e André)
    Criar queries específicas para cada tipo de visualização (Ester)
    Integrar dados com a visualização desejada (Mateus)
    Testar função de visualizar (Pedro e André)

Épico: 1, 6, 7

**Intruções Frontend:**

instale o vue,

```
npm install -g @vue/cli
```

prepare,

```
npm install
```

rode,

```
npm run serve
```

