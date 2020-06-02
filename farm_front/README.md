# Agrosatelite - Frontend

## Requirements

- Node
- npm
- Angular 7

## Run

Install dependencies
```shell
npm install
```

Serve the project using the angular CLI
```shell
ng serve
```

or
```shell
npm run ng serve
```

## Fulfill the user stories bellow

1. Na página inicial do sistema eu posso clicar sobre a opção 'Cadastrar' para cadastrar uma nova fazenda;

    1.1 Ao clicar em 'Cadastrar', devo ser redirecionado para uma nova rota com o componente que me permitirá cadastrar uma nova fazenda.

2. Na página inicial do sistema eu posso ver o nome de todas as fazendas cadastradas.

3. Ao clicar sobre o nome de uma fazenda devo ser redirecionado para a rota '/details' para ver todas as informações associadas a ela (nome dos proprietários, município e estado);

    3.1. A rota /details deve receber como parâmetro o 'id' da fazenda;

    3.2. Se um 'id' inválido for passado como parâmetro, o roteador deve me encaminhar para a página inicial do sistema.

4. Na visualização dos detalhes da fazenda eu tenho a opção de editar e de excluir a fazenda atual;

    4.1. Ao clicar em 'Editar', serei redirecionado para a página de cadastro de fazendas com todos os campos preenchidos com o da fazenda atual;
    
    4.2. Ao finalizar a edição, a fazenda deverá ser atualizada com os novos valores;
    
    4.3. Ao clicar em 'Excluir', a fazenda deverá ser removida e o roteador deve me encaminhar para a página inicial do sistema.

5. (Opcional) Durante o cadastro de uma fazenda, eu posso desenhar polígonos que delimitam a área da fazenda. Use a opção 'Desenhar Círculo' que permite desenhar um círculo no mapa como base. Verifique os arquivos (farm.component.ts e draw.ts). A [documentação do openlayers](https://openlayers.org/en/latest/apidoc/) caso necessário.